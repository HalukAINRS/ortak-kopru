"""One task across HTTP and CLI contributions, local receipts and fixed sources.

Fixtures are private and synthetic. GitHub is an injected in-memory reader;
no provider account, personal session or remote write is used.
"""

from contextlib import redirect_stdout
import hashlib
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


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru.adapters.github import git_blob_sha  # noqa: E402
from ortak_kopru.collaboration import JointService  # noqa: E402
from ortak_kopru.core import Store  # noqa: E402
from ortak_kopru.server import create_server  # noqa: E402


class FixedGitHub:
    """The ordinary GitHub read contract, with all bytes held in this test."""

    commit = "1" * 40
    tree = "2" * 40
    content = b"selected synthetic source\n"

    def __init__(self):
        self.calls = []

    def resolve_ref(self, repository, ref):
        self.calls.append(("resolve", repository, ref))
        return {"commit": self.commit, "tree": self.tree}

    def files_at(self, repository, commit, paths):
        self.calls.append(("files", repository, commit, list(paths)))
        return [{"path": path, "data": self.content, "bytes": len(self.content),
                 "blob_sha": git_blob_sha(self.content), "mode": "100644"}
                for path in paths]


def create_task(store, request_key="task"):
    return store.create_task(
        "Aynı işte üç görünür katkı ve kaynak.",
        {"actor": "Sentetik kullanıcı", "source": "Yerel sınama", "scope": "Yalnız test dosyaları"},
        ["Katkı ile gerçekleşme kanıtı ayrılır"], request_key)


def create_repository(directory):
    directory.mkdir()
    subprocess.run(["git", "init", "-q", str(directory)], check=True, capture_output=True, timeout=10)
    return directory


class JointHTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-joint-http-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repository = create_repository(self.root / "repository")
        self.server = create_server(self.root / "private", backend="portable", port=0)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.close)
        self.port = self.server.server_address[1]
        self.origin = f"http://127.0.0.1:{self.port}"
        self.task = create_task(self.server.store)
        self.base = f"/api/tasks/{self.task['id']}"

    def close(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=3)

    def request(self, method, path, value=None, *, headers=None, token=True):
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=10)
        try:
            actual = {"X-Deus-Token": self.server.token} if token else {}
            if method == "POST":
                actual.update({"Origin": self.origin, "Content-Type": "application/json"})
            if headers:
                actual.update(headers)
                actual = {key: value for key, value in actual.items() if value is not None}
            body = json.dumps(value, ensure_ascii=False).encode("utf-8") if value is not None else None
            connection.request(method, path, body=body, headers=actual)
            response = connection.getresponse()
            return response.status, json.loads(response.read())
        finally:
            connection.close()

    def contribution(self, author="ChatGPT", request_key="contribution"):
        return {"author": author, "session_id": f"sentetik-{author}",
                "relayed_by": "Yerel test aktarımı", "stage": 16,
                "body": "Özgün katkı\r\n  Son satır.\n", "references": ["sentetik-kaynak:1"],
                "expected_revision": 1, "request_key": request_key}

    def operation(self, request_key="operation"):
        return {"operation": "python_version", "cwd": str(self.repository),
                "expected_revision": 1, "request_key": request_key}

    def github(self, request_key="github"):
        return {"repository": "example/fixture", "ref": "main", "paths": ["selected.txt"],
                "expected_revision": 1, "request_key": request_key}

    def test_three_contributions_share_task_without_reassigning_and_retry_is_single(self):
        assigned = self.server.store.assign(self.task["id"], "Mevcut iş yürütücüsü", "existing-session", 1, "assign")
        first = None
        for index, author in enumerate(("ChatGPT", "Claude Code", "Gemini")):
            payload = self.contribution(author, f"contribution-{index}")
            status, record = self.request("POST", self.base + "/contribute", payload)
            self.assertEqual(200, status, record)
            self.assertEqual(payload["body"], record["body"])
            self.assertEqual(author, record["author"])
            if first is None:
                first = record
                self.assertEqual((200, record), self.request("POST", self.base + "/contribute", payload))
        status, joint = self.request("GET", self.base + "/joint")
        self.assertEqual(200, status, joint)
        self.assertEqual(self.task["id"], joint["task_id"])
        self.assertEqual(1, joint["revision"])
        self.assertFalse(joint["identity_verified"])
        self.assertEqual({"ChatGPT", "Claude Code", "Gemini"}, {item["author"] for item in joint["contributions"]})
        self.assertEqual(3, len(joint["contributions"]))
        self.assertEqual([], joint["operations"])
        status, unchanged = self.request("GET", self.base)
        self.assertEqual(200, status, unchanged)
        self.assertEqual(assigned["active_attempt_id"], unchanged["active_attempt_id"])
        self.assertEqual("ready", unchanged["status"])
        self.assertEqual(200, self.request("GET", self.base + "/context")[0])
        self.assertEqual(200, self.request("GET", self.base + "/events")[0])

    def test_joint_routes_keep_private_surface_and_exact_request_fields(self):
        self.assertEqual(403, self.request("GET", self.base + "/joint", token=False)[0])
        self.assertEqual(403, self.request("GET", self.base + "/joint", headers={"Host": f"other.invalid:{self.port}"})[0])
        payload = self.contribution()
        self.assertEqual(403, self.request("POST", self.base + "/contribute", payload, token=False)[0])
        self.assertEqual(403, self.request("POST", self.base + "/contribute", payload, headers={"Origin": None})[0])
        self.assertEqual(403, self.request("POST", self.base + "/contribute", payload, headers={"Origin": "https://other.invalid"})[0])
        before = self.server.store.events(self.task["id"])
        for route, body in (("contribute", payload), ("operate", self.operation()), ("github", self.github())):
            with self.subTest(route=route):
                self.assertEqual(400, self.request("POST", self.base + "/" + route, dict(body, unexpected=True))[0])
                missing = dict(body)
                missing.pop("expected_revision")
                self.assertEqual(400, self.request("POST", self.base + "/" + route, missing)[0])
        self.assertEqual(before, self.server.store.events(self.task["id"]))
        self.assertEqual(404, self.request("POST", self.base + "/github-fetch", self.github())[0])
        self.assertEqual(404, self.request("POST", f"/api/attempts/{self.task['id']}/contribute", payload)[0])

    def test_stale_revision_blocks_contribution_operation_and_source_before_receipt(self):
        self.server.store.revise_task(self.task["id"], "Yeni kapsam", 1, "revision")
        github = FixedGitHub()
        before = self.server.store.events(self.task["id"])
        with mock.patch("ortak_kopru.collaboration.JointService",
                        side_effect=lambda store: JointService(store, github_client=github)), \
                mock.patch("ortak_kopru.collaboration._run_local") as local:
            for route, body in (("contribute", self.contribution()), ("operate", self.operation()), ("github", self.github())):
                with self.subTest(route=route):
                    status, error = self.request("POST", self.base + "/" + route, body)
                    self.assertEqual(409, status, error)
                    self.assertEqual("conflict", error["error"]["code"])
            local.assert_not_called()
        self.assertEqual([], github.calls)
        self.assertEqual(before, self.server.store.events(self.task["id"]))

    def test_local_operation_and_pinned_github_source_have_same_task_receipts(self):
        status, operation = self.request("POST", self.base + "/operate", self.operation())
        self.assertEqual(200, status, operation)
        self.assertEqual("completed", operation["status"])
        self.assertEqual(64, operation["stage"])
        self.assertIsInstance(operation["receipt"], dict)
        github = FixedGitHub()
        with mock.patch("ortak_kopru.collaboration.JointService",
                        side_effect=lambda store: JointService(store, github_client=github)):
            status, source = self.request("POST", self.base + "/github", self.github())
        self.assertEqual(200, status, source)
        self.assertEqual("completed", source["status"])
        self.assertEqual(32, source["stage"])
        self.assertIn(("files", "example/fixture", github.commit, ["selected.txt"]), github.calls)
        status, joint = self.request("GET", self.base + "/joint")
        self.assertEqual(200, status, joint)
        self.assertEqual({operation["operation_id"], source["operation_id"]}, {item["operation_id"] for item in joint["operations"]})
        task = self.server.store.get_task(self.task["id"])
        self.assertEqual("ready", task["status"])
        self.assertIsNone(task["active_attempt_id"])
        self.assertTrue(any(item["sha256"] == hashlib.sha256(github.content).hexdigest() for item in task["sources"]))

    def test_kernel_loss_blocks_all_new_mutations_without_changing_backend(self):
        from ortak_kopru.adapters.windows_nt import KernelUnavailable
        self.server.backend = "nt-kernel"
        before = self.server.store.events(self.task["id"])
        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=KernelUnavailable("missing")):
            for route, body in (("contribute", self.contribution()), ("operate", self.operation()), ("github", self.github())):
                with self.subTest(route=route):
                    status, error = self.request("POST", self.base + "/" + route, body)
                    self.assertEqual(503, status, error)
                    self.assertEqual("kernel_unavailable", error["error"]["code"])
        self.assertEqual("nt-kernel", self.server.backend)
        self.assertEqual(before, self.server.store.events(self.task["id"]))


class JointCLITests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-joint-cli-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repository = create_repository(self.root / "repository")
        self.state = self.root / "private"
        self.task = create_task(Store(self.state))

    def cli(self, *args, state=None):
        command = [sys.executable, str(ROOT / "deus.py"), "--backend", "portable",
                   "--state-dir", str(state or self.state), *args]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, encoding="utf-8", timeout=20)
        self.assertTrue(result.stdout.strip(), result.stderr)
        return result.returncode, json.loads(result.stdout)

    def test_contribution_file_and_joint_survive_separate_cli_processes(self):
        body = self.root / "contribution.txt"
        words = "  Oturumun görünür katkısı.\r\nİkinci satır.\n"
        body.write_bytes(words.encode("utf-8"))
        args = ("contribute", self.task["id"], "--author", "ChatGPT", "--session", "sentetik-sohbet",
                "--relayed-by", "Yerel test", "--stage", "16", "--body-file", str(body),
                "--reference", "kaynak:1", "--reference", "kaynak:2", "--revision", "1", "--request-key", "cli-contribution")
        code, response = self.cli(*args)
        self.assertEqual(0, code, response)
        contribution = response["result"]
        self.assertEqual(words, contribution["body"])
        self.assertEqual(["kaynak:1", "kaynak:2"], contribution["references"])
        self.assertEqual("portable", response["runtime"]["backend"])
        self.assertFalse(response["runtime"]["kernel_verified"])
        self.assertEqual(contribution, self.cli(*args)[1]["result"])
        code, response = self.cli("joint", self.task["id"])
        self.assertEqual(0, code, response)
        self.assertEqual(1, len(response["result"]["contributions"]))
        self.assertFalse(response["result"]["identity_verified"])

    def test_actual_local_cli_receipt_keeps_failure_with_nonzero_exit(self):
        base = ("operate", self.task["id"], "--revision", "1")
        code, response = self.cli(*base, "--cwd", str(self.repository), "--operation", "python_version", "--request-key", "python")
        self.assertEqual(0, code, response)
        self.assertEqual("completed", response["result"]["status"])
        self.assertEqual(64, response["result"]["stage"])
        self.assertIsInstance(response["result"]["receipt"], dict)
        # The fixture directory is deliberately not a Git worktree.
        code, response = self.cli(*base, "--cwd", str(self.root), "--operation", "repo_revision", "--request-key", "not-a-repository")
        self.assertEqual(1, code, response)
        self.assertNotEqual("completed", response["result"]["status"])
        self.assertIsInstance(response["result"]["receipt"], dict)
        self.assertNotIn("error", response)
        _, joint = self.cli("joint", self.task["id"])
        self.assertEqual(2, len(joint["result"]["operations"]))

    def test_invalid_stage_or_unlisted_operation_fails_before_opening_state(self):
        state = self.root / "not-created"
        contribution = ("contribute", self.task["id"], "--author", "Test", "--session", "test",
                        "--relayed-by", "test", "--body", "test", "--revision", "1", "--request-key", "bad-stage")
        cases = [contribution, (*contribution, "--stage", "33"),
                 ("operate", self.task["id"], "--operation", "shell", "--cwd", str(self.root), "--revision", "1", "--request-key", "shell"),
                 ("github-fetch", self.task["id"], "--repository", "example/fixture", "--ref", "main", "--path", "a", "--stage", "8", "--revision", "1", "--request-key", "bad-source-stage")]
        for args in cases:
            with self.subTest(args=args):
                code, response = self.cli(*args, state=state)
                self.assertEqual(2, code, response)
                self.assertEqual("arguments", response["error"]["code"])
                self.assertFalse(state.exists())

    def test_new_commands_keep_default_nt_gate_before_opening_store(self):
        from ortak_kopru.adapters.windows_nt import KernelUnavailable
        from ortak_kopru.cli import main
        state = self.root / "nt-not-created"
        cases = [
            ["joint", self.task["id"]],
            ["contribute", self.task["id"], "--author", "Test", "--session", "test", "--relayed-by", "test", "--stage", "16", "--body", "test", "--revision", "1", "--request-key", "c"],
            ["operate", self.task["id"], "--operation", "python_version", "--cwd", str(self.root), "--revision", "1", "--request-key", "o"],
            ["github-fetch", self.task["id"], "--repository", "example/fixture", "--ref", "main", "--path", "a", "--revision", "1", "--request-key", "g"],
        ]
        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=KernelUnavailable("missing")):
            for args in cases:
                with self.subTest(command=args[0]):
                    output = io.StringIO()
                    with redirect_stdout(output):
                        code = main(["--state-dir", str(state), *args])
                    self.assertEqual(1, code)
                    self.assertEqual("kernel_unavailable", json.loads(output.getvalue())["error"]["code"])
                    self.assertFalse(state.exists())

    def test_failed_and_unknown_operation_receipts_are_not_hidden_by_cli(self):
        from ortak_kopru.cli import main
        args = ["--backend", "portable", "--state-dir", str(self.state), "operate", self.task["id"],
                "--operation", "python_version", "--cwd", str(self.root), "--revision", "1", "--request-key", "mock-status"]
        for status in ("failed", "timeout", "output_limit", "spawn_error", "unknown"):
            with self.subTest(status=status):
                receipt = {"operation_id": "synthetic-operation", "status": status,
                           "receipt": None if status == "unknown" else {"status": status}}
                output = io.StringIO()
                with mock.patch.object(JointService, "operate", return_value=receipt), redirect_stdout(output):
                    code = main(args)
                self.assertEqual(1, code)
                response = json.loads(output.getvalue())
                self.assertEqual(receipt, response["result"])
                self.assertNotIn("error", response)

    def test_github_cli_passes_selected_paths_and_default_stage_without_network(self):
        from ortak_kopru.cli import main
        receipt = {"operation_id": "synthetic-source", "status": "completed", "receipt": {"commit": "1" * 40}}
        output = io.StringIO()
        with mock.patch.object(JointService, "fetch_github", return_value=receipt) as fetch, redirect_stdout(output):
            code = main(["--backend", "portable", "--state-dir", str(self.state), "github-fetch", self.task["id"],
                         "--repository", "example/fixture", "--ref", "release", "--path", "a.txt", "--path", "b.txt",
                         "--revision", "1", "--request-key", "selected-source"])
        self.assertEqual(0, code)
        self.assertEqual(receipt, json.loads(output.getvalue())["result"])
        self.assertEqual(["a.txt", "b.txt"], fetch.call_args.kwargs["paths"])
        self.assertEqual("release", fetch.call_args.kwargs["ref"])
        self.assertEqual(32, fetch.call_args.kwargs["stage"])
        self.assertEqual(1, fetch.call_args.kwargs["expected_revision"])


if __name__ == "__main__":
    unittest.main()
