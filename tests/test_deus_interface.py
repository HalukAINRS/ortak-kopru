"""Local CLI/HTTP workflows, exact text, stale results and surface boundaries."""

from contextlib import redirect_stdout
import http.client
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest import mock
from urllib.parse import parse_qs, quote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru.server import MAX_BODY_BYTES, create_server, runtime_status  # noqa: E402


class LocalHTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-http-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        ui = self.root / "ui"
        ui.mkdir()
        (ui / "index.html").write_text('<p>Başlatma bağlantısıyla giriş yapın.</p>', encoding="utf-8")
        (ui / "app.js").write_text("'use strict';", encoding="utf-8")
        (ui / "styles.css").write_text("body { color: black; }", encoding="utf-8")
        self.server = create_server(self.root / "private", backend="portable", port=0, ui_dir=ui)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.close)
        self.port = self.server.server_address[1]
        self.origin = f"http://127.0.0.1:{self.port}"

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=3)

    def request(self, method, path, value=None, *, headers=None, raw=None, token=True):
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        try:
            actual = {"X-Deus-Token": self.server.token} if token else {}
            if method == "POST":
                actual.update({"Origin": self.origin, "Content-Type": "application/json"})
            if headers:
                actual.update(headers)
                actual = {k: v for k, v in actual.items() if v is not None}
            body = raw if raw is not None else (json.dumps(value, ensure_ascii=False).encode("utf-8") if value is not None else None)
            connection.request(method, path, body=body, headers=actual)
            response = connection.getresponse()
            data = response.read()
            if response.getheader("Content-Type", "").startswith("application/json"):
                data = json.loads(data)
            return response.status, data, dict(response.getheaders())
        finally:
            connection.close()

    def task(self):
        body = {"original_words": "Özgün söz\r\n  Son satır.\n",
                "authority": {"actor": "Haluk", "source": "Bu yerel test girdisi", "scope": "Yalnız sentetik dosya"},
                "criteria": [{"id": "exact", "description": "Çıktı özgün sözü korur"}],
                "request_key": "create-exact"}
        status, task, _ = self.request("POST", "/api/tasks", body)
        self.assertEqual(200, status, task)
        return body, task

    def test_local_surface_token_and_cross_site_boundaries(self):
        status, html, headers = self.request("GET", "/", token=False)
        self.assertEqual(200, status)
        self.assertNotIn(self.server.token.encode(), html)
        self.assertNotIn(b"__DEUS_TOKEN__", html)
        self.assertEqual("no-store", headers["Cache-Control"])
        self.assertIn("frame-ancestors 'none'", headers["Content-Security-Policy"])
        self.assertNotIn("Access-Control-Allow-Origin", headers)
        self.assertEqual(403, self.request("GET", "/api/tasks", token=False)[0])
        self.assertEqual(403, self.request("GET", "/api/tasks", headers={"Host": f"attacker.invalid:{self.port}"})[0])
        self.assertEqual(403, self.request("GET", "/", headers={"Sec-Fetch-Site": "cross-site"})[0])
        self.assertEqual(403, self.request("POST", "/api/tasks", {}, headers={"Origin": None})[0])
        self.assertEqual(403, self.request("POST", "/api/tasks", {}, headers={"Origin": "https://other.invalid"})[0])
        self.assertEqual(403, self.request("POST", "/api/tasks", {}, headers={"X-Deus-Token": "wrong"})[0])
        self.assertEqual(403, self.request("GET", "/api/tasks", headers={"X-Deus-Token": "\u00b5"})[0])
        self.assertEqual(404, self.request("GET", "/../../private/bridge.sqlite3")[0])

    def test_only_private_startup_fragment_supplies_api_credential(self):
        from ortak_kopru.cli import main
        for path in ("/", "/index.html", "/app.js", "/styles.css"):
            status, data, headers = self.request("GET", path, token=False)
            self.assertEqual(200, status, path)
            self.assertNotIn(self.server.token.encode(), data)
            self.assertNotIn(self.server.token, str(headers))
        for path in ("/api/runtime", "/api/tasks"):
            status, data, headers = self.request("GET", path, token=False)
            self.assertEqual(403, status, path)
            self.assertNotIn(self.server.token, json.dumps(data))
            self.assertNotIn(self.server.token, str(headers))

        output = io.StringIO()
        with mock.patch("ortak_kopru.cli.create_server", return_value=self.server), \
                mock.patch.object(self.server, "serve_forever"), \
                mock.patch.object(self.server, "server_close"), redirect_stdout(output):
            code = main(["--backend", "portable", "--state-dir", str(self.root / "private"), "serve"])
        self.assertEqual(0, code)
        startup = json.loads(output.getvalue())
        launch = startup.pop("launch_url")
        token = parse_qs(urlsplit(launch).fragment)["token"][0]
        self.assertEqual(self.server.token, token)
        self.assertEqual(self.origin + "/", launch.split("#", 1)[0])
        self.assertNotIn(token, json.dumps(startup))
        self.assertEqual(1, output.getvalue().count(token))
        status, data, _ = self.request("GET", "/api/tasks", token=False, headers={"X-Deus-Token": token})
        self.assertEqual(200, status)
        self.assertEqual([], data["tasks"])
        status, runtime, _ = self.request("GET", "/api/runtime", token=False, headers={"X-Deus-Token": token})
        self.assertEqual(200, status)
        self.assertNotIn(token, json.dumps(runtime))
        # HTTP query strings are not a second credential bootstrap channel.
        status, data, _ = self.request("GET", "/?token=" + token, token=False)
        self.assertEqual(400, status)
        self.assertNotIn(token, json.dumps(data))

    def test_body_validation_has_no_partial_effect(self):
        self.assertEqual(400, self.request("POST", "/api/tasks", raw=b'{"request_key":"a","request_key":"b"}')[0])
        self.assertEqual(400, self.request("POST", "/api/tasks", raw=b'[]')[0])
        self.assertEqual(400, self.request("POST", "/api/tasks", raw=b'{"value":NaN}')[0])
        self.assertEqual(400, self.request("POST", "/api/tasks", {}, headers={"Content-Length": str(MAX_BODY_BYTES + 1)})[0])
        self.assertEqual(400, self.request("POST", "/api/tasks", {}, headers={"Content-Type": "text/plain"})[0])
        self.assertEqual([], self.request("GET", "/api/tasks")[1]["tasks"])

    def test_session_inbox_is_private_read_only_and_accepts_encoded_session_id(self):
        _, task = self.task()
        session = "Özel oturum / test"
        task = self.server.store.assign(task["id"], "Test", session, 1, "inbox-assignment")
        route = "/api/sessions/" + quote(session, safe="") + "/inbox"
        before_events = self.server.store.events(task["id"])
        self.assertEqual(403, self.request("GET", "/api/sessions", token=False)[0])
        self.assertEqual(403, self.request("GET", route, token=False)[0])
        status, sessions, _ = self.request("GET", "/api/sessions")
        self.assertEqual(200, status, sessions)
        self.assertEqual(session, sessions["sessions"][0]["session_id"])
        self.assertFalse(sessions["sessions"][0]["identity_verified"])
        status, received, _ = self.request("GET", route)
        self.assertEqual(200, status, received)
        self.assertEqual(task["active_attempt_id"], received["items"][0]["attempt_id"])
        self.assertEqual(before_events, self.server.store.events(task["id"]))
        self.server.store.control_task(task["id"], "pause", 1, "inbox-pause")
        self.assertEqual([], self.request("GET", route)[1]["items"])

    def test_real_task_cycle_preserves_original_and_uses_result_bound_checks(self):
        body, task = self.task()
        task_id = task["id"]
        self.assertEqual(body["original_words"], task["original_words"])
        retried = self.request("POST", "/api/tasks", body)
        self.assertEqual(200, retried[0])
        self.assertEqual(task_id, retried[1]["id"])
        changed = dict(body, original_words="Başka istek")
        self.assertEqual(409, self.request("POST", "/api/tasks", changed)[0])
        status, task, _ = self.request("POST", f"/api/tasks/{task_id}/assign", {
            "participant": "ChatGPT (Şaman)", "session_id": "local-test-session",
            "expected_revision": task["revision"], "request_key": "assign-1"})
        self.assertEqual(200, status, task)
        attempt = task["active_attempt_id"]
        status, received, _ = self.request("POST", f"/api/attempts/{attempt}/receive", {
            "session_id": "local-test-session", "request_key": "receive-1"})
        self.assertEqual(200, status, received)
        self.assertEqual(task_id, received["task"]["id"])
        self.assertIn("context", received)
        artifact = self.root / "result.txt"
        artifact.write_bytes(body["original_words"].encode("utf-8"))
        status, task, _ = self.request("POST", f"/api/attempts/{attempt}/result", {
            "session_id": "local-test-session", "summary": "Sentetik çıktı yazıldı.",
            "artifacts": [str(artifact)], "request_key": "result-1"})
        self.assertEqual(200, status, task)
        self.assertNotEqual("completed", task["status"])
        status, task, _ = self.request("POST", f"/api/tasks/{task_id}/verify", {
            "checks": [{"criterion_id": "exact", "result_id": task["current_result_id"],
                        "passed": True, "evidence": "Yerel bayt karşılaştırması eşleşti.", "verifier": "test"}],
            "expected_revision": task["revision"], "request_key": "verify-1"})
        self.assertEqual(200, status, task)
        self.assertEqual("completed", task["status"])
        self.assertEqual(200, self.request("GET", f"/api/tasks/{task_id}/context")[0])
        self.assertTrue(self.request("GET", f"/api/tasks/{task_id}/events")[1]["events"])
        runtime = self.request("GET", "/api/runtime")[1]
        self.assertEqual("software_portable", runtime["execution_mode"])
        self.assertFalse(runtime["kernel_verified"])

    def test_revision_prevents_old_attempt_result(self):
        _, task = self.task()
        task_id = task["id"]
        _, assigned, _ = self.request("POST", f"/api/tasks/{task_id}/assign", {
            "participant": "Claude (Hacker)", "session_id": "hacker-test",
            "expected_revision": task["revision"], "request_key": "assign"})
        attempt = assigned["active_attempt_id"]
        self.request("POST", f"/api/attempts/{attempt}/receive", {"session_id": "hacker-test", "request_key": "receive"})
        status, revised, _ = self.request("POST", f"/api/tasks/{task_id}/revise", {
            "original_words": "Güncel kullanıcı düzeltmesi.", "expected_revision": assigned["revision"], "request_key": "revise"})
        self.assertEqual(200, status, revised)
        stale = self.request("POST", f"/api/attempts/{attempt}/result", {
            "session_id": "hacker-test", "summary": "Eski kapsama ait sonuç", "artifacts": [], "request_key": "late-result"})
        self.assertEqual(409, stale[0], stale[1])

    def test_transfer_compares_current_attempt_and_rejects_stale_assignment(self):
        _, task = self.task()
        path = f"/api/tasks/{task['id']}/assign"
        first = {"participant": "ChatGPT (Şaman)", "session_id": "session-1",
                 "expected_revision": task["revision"], "request_key": "first-assignment"}
        status, assigned, _ = self.request("POST", path, first)
        self.assertEqual(200, status, assigned)
        old_attempt = assigned["active_attempt_id"]
        missing = dict(first, session_id="session-2", request_key="missing-expected")
        self.assertEqual(409, self.request("POST", path, missing)[0])
        transfer = dict(first, session_id="session-2", request_key="transfer",
                        expected_active_attempt_id=old_attempt)
        status, moved, _ = self.request("POST", path, transfer)
        self.assertEqual(200, status, moved)
        self.assertNotEqual(old_attempt, moved["active_attempt_id"])
        stale = dict(transfer, session_id="session-3", request_key="stale-transfer")
        self.assertEqual(409, self.request("POST", path, stale)[0])
        current = self.request("GET", f"/api/tasks/{task['id']}")[1]
        self.assertEqual(moved["active_attempt_id"], current["active_attempt_id"])

    def test_kernel_loss_preserves_stop_controls_but_blocks_execution_changes(self):
        from ortak_kopru.adapters.windows_nt import KernelUnavailable
        body, task = self.task()
        self.server.backend = "nt-kernel"

        def missing_driver(*, strict=False):
            if strict:
                raise KernelUnavailable("removed")
            return {"backend": "nt-kernel", "ready": False, "state": "unavailable"}

        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=missing_driver):
            status, paused, _ = self.request("POST", f"/api/tasks/{task['id']}/control", {
                "action": "pause", "expected_revision": task["revision"], "request_key": "pause-after-loss"})
            self.assertEqual(200, status, paused)
            self.assertEqual("paused", paused["status"])
            status, error, _ = self.request("POST", f"/api/tasks/{task['id']}/control", {
                "action": "resume", "expected_revision": paused["revision"], "request_key": "resume-after-loss"})
            self.assertEqual(503, status, error)
            self.assertEqual("kernel_unavailable", error["error"]["code"])
            status, error, _ = self.request("POST", "/api/tasks", dict(body, request_key="new-after-loss"))
            self.assertEqual(503, status, error)
            status, cancelled, _ = self.request("POST", f"/api/tasks/{task['id']}/control", {
                "action": "cancel", "expected_revision": paused["revision"], "request_key": "cancel-after-loss"})
            self.assertEqual(200, status, cancelled)
            self.assertEqual("cancelled", cancelled["status"])
            runtime = self.request("GET", "/api/runtime")[1]
            self.assertEqual("nt-kernel", runtime["backend"])
            self.assertFalse(runtime["ready"])
            self.assertFalse(runtime["kernel_verified"])
        self.assertEqual(1, len(self.server.store.list_tasks()))
        self.assertEqual([], cancelled["attempts"])


class CLITests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-cli-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.state = self.root / "private"

    def run_cli(self, *args):
        result = subprocess.run([sys.executable, str(ROOT / "deus.py"), "--backend", "portable",
                                 "--state-dir", str(self.state), *args],
                                cwd=ROOT, capture_output=True, encoding="utf-8", timeout=15)
        return result, json.loads(result.stdout)

    def test_cli_create_restart_get_and_private_export(self):
        words = self.root / "words.txt"
        words.write_bytes("  Özgün söz\r\nİkinci satır\n".encode("utf-8"))
        result, response = self.run_cli("create", "--words-file", str(words), "--authority-source", "Yerel kullanıcı",
                                        "--authority-scope", "Sentetik çalışma", "--criterion", "Kaynak korunur",
                                        "--request-key", "first-task")
        self.assertEqual(0, result.returncode, (result.stdout, result.stderr))
        self.assertEqual("software_portable", response["runtime"]["execution_mode"])
        task = response["result"]
        self.assertEqual(words.read_bytes().decode("utf-8"), task["original_words"])
        result, response = self.run_cli("get", task["id"])
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertEqual(task["id"], response["result"]["id"])
        output = self.root / "private-export.json"
        result, response = self.run_cli("export", "--output", str(output))
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertTrue(output.is_file())
        before = output.read_bytes()
        result, response = self.run_cli("export", "--output", str(output))
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(before, output.read_bytes())
        result, response = self.run_cli("export", "--output", str(ROOT / "must-not-exist-private-export.json"))
        self.assertNotEqual(0, result.returncode)
        self.assertFalse((ROOT / "must-not-exist-private-export.json").exists())

    def test_default_kernel_failure_has_no_software_downgrade(self):
        from ortak_kopru.adapters.windows_nt import KernelUnavailable
        state = self.root / "not-created"
        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=KernelUnavailable("test missing driver")):
            with self.assertRaises(KernelUnavailable):
                create_server(state, port=0)
        self.assertFalse(state.exists())
        self.assertFalse(runtime_status("portable")["kernel_verified"])

    def test_cli_argument_error_is_json_and_does_not_create_store(self):
        result, response = self.run_cli("get")
        self.assertEqual(2, result.returncode)
        self.assertEqual("arguments", response["error"]["code"])
        self.assertFalse(self.state.exists())

    def test_cli_cancel_without_driver_keeps_nt_runtime_and_blocks_resume(self):
        from ortak_kopru.adapters.windows_nt import KernelUnavailable
        from ortak_kopru.cli import main
        from ortak_kopru.core import Store
        store = Store(self.state)
        task = store.create_task("Sentetik iş", {"actor": "Haluk", "source": "test", "scope": "test"},
                                 ["Sonuç kontrolü"], "create")

        def missing_driver(*, strict=False):
            if strict:
                raise KernelUnavailable("removed")
            return {"backend": "nt-kernel", "ready": False, "state": "unavailable"}

        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=missing_driver):
            output = io.StringIO()
            with redirect_stdout(output):
                code = main(["--state-dir", str(self.state), "control", task["id"], "pause",
                             "--revision", str(task["revision"]), "--request-key", "pause"])
            value = json.loads(output.getvalue())
            self.assertEqual(0, code, value)
            self.assertEqual("nt-kernel", value["runtime"]["backend"])
            self.assertFalse(value["runtime"]["ready"])
            self.assertEqual("paused", value["result"]["status"])
            output = io.StringIO()
            with redirect_stdout(output):
                code = main(["--state-dir", str(self.state), "control", task["id"], "resume",
                             "--revision", str(value["result"]["revision"]), "--request-key", "resume"])
            self.assertEqual(1, code)
            self.assertEqual("kernel_unavailable", json.loads(output.getvalue())["error"]["code"])


if __name__ == "__main__":
    unittest.main()
