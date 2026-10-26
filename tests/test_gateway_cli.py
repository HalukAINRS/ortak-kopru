"""Gateway command contracts with synthetic files and no live provider calls."""
from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru.adapters.github import GitHubError  # noqa: E402
from ortak_kopru.gateway_cli import main  # noqa: E402


class ReadOnlyGitHub:
    """An explicit fake for one pinned incoming file; no transport involved."""

    commit = "a" * 40
    tree = "b" * 40
    data = "Dış kaynaktan gelen içerik.\n".encode("utf-8") + b"\x00\xff"

    def __init__(self):
        self.requests = []

    def resolve_ref(self, repository, ref):
        self.requests.append(("resolve", repository, ref))
        return {"commit": self.commit, "tree": self.tree}

    def files_at(self, repository, commit, paths):
        if commit != self.commit:
            raise AssertionError("Incoming reads must use the resolved commit")
        self.requests.append(("files", repository, commit, paths))
        blob = hashlib.sha1(b"blob " + str(len(self.data)).encode("ascii") + b"\0" + self.data,
                            usedforsecurity=False).hexdigest()
        return [{"path": path, "blob_sha": blob, "mode": "100644",
                 "bytes": len(self.data), "data": self.data} for path in paths]


class GatewayCLITests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="gateway-cli-",
                                                dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.state = self.root / "exchange"
        project = self.root / "existing-project"
        project.mkdir()
        (project / ".git").mkdir()
        (project / ".git" / "HEAD").write_text("ref: refs/heads/main\n", encoding="utf-8")
        self.source = project / "rapor.bin"
        self.data = "Önceden üretilmiş yerel çıktı.\n".encode("utf-8") + b"\0\xff"
        self.source.write_bytes(self.data)
        (project / "unselected.txt").write_text("UNSELECTED_PRIVATE_FIXTURE", encoding="utf-8")
        self.selection = self.root / "selection.json"
        self.selection.write_text(json.dumps([
            {"source": str(self.source), "path": "reports/rapor.bin"}
        ]), encoding="utf-8")

    def invoke(self, *arguments):
        output = io.StringIO()
        with redirect_stdout(output):
            try:
                code = main(list(arguments))
            except SystemExit as exc:
                code = exc.code
        raw = output.getvalue()
        return code, json.loads(raw), raw

    def command(self, *arguments):
        return self.invoke("--exchange-dir", str(self.state), *arguments)

    def prepare(self, request_key="prepare-fixture"):
        code, value, _ = self.command(
            "prepare", "--selection", str(self.selection), "--repo", "example/project",
            "--purpose", "Seçilmiş sentetik çıktı", "--request-key", request_key)
        self.assertEqual(0, code, value)
        return value["result"]

    def test_existing_local_output_prepares_and_materializes_without_task_or_provider(self):
        with mock.patch("ortak_kopru.gateway_cli.GitHubClient.from_env",
                        side_effect=AssertionError("Offline commands must not create a provider client")), \
             mock.patch("ortak_kopru.core.Store.__init__",
                        side_effect=AssertionError("Gateway must not create a task Store")), \
             mock.patch("ortak_kopru.adapters.windows_nt.query_status",
                        side_effect=AssertionError("Gateway must not request the NT device")):
            prepared = self.prepare()
            self.source.write_bytes(b"changed after selection")
            code, shown, _ = self.command("show", prepared["id"])
            self.assertEqual(0, code, shown)
            self.assertEqual("user_mode_exchange", shown["execution_scope"])
            self.assertEqual("not_requested", shown["kernel_scope"])
            self.assertEqual("outbound", shown["result"]["direction"])
            manifest = shown["result"]["manifest"]
            manifest_text = json.dumps(manifest)
            self.assertNotIn(str(self.source), manifest_text)
            self.assertNotIn("UNSELECTED_PRIVATE_FIXTURE", manifest_text)
            self.assertEqual(["reports/rapor.bin"], [f["path"] for f in manifest["files"]])
            code, verified, _ = self.command("verify", prepared["id"])
            self.assertEqual(0, code, verified)
            output = self.root / "review-copy"
            code, extracted, _ = self.command("materialize", prepared["id"], "--output", str(output))
            self.assertEqual(0, code, extracted)
            self.assertEqual(self.data, (output / "reports" / "rapor.bin").read_bytes())
            self.assertEqual(["reports/rapor.bin"],
                             sorted(p.relative_to(output).as_posix() for p in output.rglob("*") if p.is_file()))
            code, listing, _ = self.command("list")
            self.assertEqual(0, code, listing)
            self.assertEqual([prepared["id"]], [r["id"] for r in listing["result"]["transfers"]])
            code, events, _ = self.command("events", prepared["id"])
            self.assertEqual(0, code, events)
            self.assertTrue(events["result"]["events"])
        self.assertEqual([], list(self.root.rglob("deus.sqlite3")))

    def test_read_commands_do_not_create_missing_exchange_area(self):
        for arguments in (("list",), ("show", "x_" + "1" * 32), ("verify", "x_" + "1" * 32)):
            with self.subTest(arguments=arguments):
                code, value, _ = self.command(*arguments)
                self.assertEqual(1, code, value)
                self.assertIn("error", value)
                self.assertFalse(self.state.exists())

    def test_selection_json_is_strict_before_creating_state(self):
        samples = (
            '[{"source":"one","source":"two","path":"report.txt"}]',
            '[{"source":"one","path":"report.txt","size":NaN}]',
            '{"source":"one","path":"report.txt"}',
            '[]',
        )
        for raw in samples:
            with self.subTest(raw=raw):
                self.selection.write_text(raw, encoding="utf-8")
                code, value, _ = self.command(
                    "prepare", "--selection", str(self.selection), "--repo", "example/project",
                    "--purpose", "Fixture", "--request-key", "invalid")
                self.assertEqual(1, code, value)
                self.assertFalse(self.state.exists())

    def test_argument_errors_require_plan_binding_and_do_not_echo_unknown_token_value(self):
        code, value, raw = self.command("send", "x_" + "2" * 32)
        self.assertEqual(2, code, value)
        self.assertEqual("arguments", value["error"]["code"])
        self.assertIn("--plan-hash", raw)
        self.assertFalse(self.state.exists())
        synthetic_secret = "synthetic-credential-not-for-output"
        code, value, raw = self.command("list", "--token", synthetic_secret)
        self.assertEqual(2, code, value)
        self.assertNotIn(synthetic_secret, raw)
        self.assertFalse(self.state.exists())

    def test_provider_and_unexpected_errors_do_not_print_raw_messages(self):
        record = self.prepare()
        synthetic_secret = "synthetic-provider-secret"
        failures = (
            (GitHubError(synthetic_secret, status=403, code="forbidden"), "forbidden"),
            (GitHubError(synthetic_secret, code="network_error", ambiguous=True), "network_error"),
            (RuntimeError(synthetic_secret), "internal_error"),
        )
        for failure, expected_code in failures:
            with self.subTest(expected_code=expected_code), \
                 mock.patch("ortak_kopru.gateway_cli.GitHubClient.from_env", return_value=object()), \
                 mock.patch("ortak_kopru.gateway_cli.gateway.plan", side_effect=failure):
                code, value, raw = self.command("plan", record["id"])
                self.assertEqual(1, code, value)
                self.assertEqual(expected_code, value["error"]["code"])
                self.assertNotIn(synthetic_secret, raw)

    def test_send_uncertainty_is_a_failing_process_exit_with_inspectable_record(self):
        record = self.prepare()
        for state, expected_code in (("unknown", 1), ("conflict", 1), ("failed", 1), ("published", 0)):
            with self.subTest(state=state), \
                 mock.patch("ortak_kopru.gateway_cli.GitHubClient.from_env", return_value=object()), \
                 mock.patch("ortak_kopru.gateway_cli.gateway.send", return_value={**record, "state": state}):
                code, value, _ = self.command("send", record["id"], "--plan-hash", "f" * 64)
                self.assertEqual(expected_code, code, value)
                self.assertEqual(state, value["result"]["state"])

    def test_fetch_uses_pinned_source_and_leaves_local_work_untouched(self):
        client = ReadOnlyGitHub()
        with mock.patch("ortak_kopru.gateway_cli.GitHubClient.from_env", return_value=client):
            code, value, _ = self.command(
                "fetch", "--repo", "example/project", "--ref", "review-branch",
                "--path", "docs/source.bin", "--purpose", "Kaynak tedariki", "--request-key", "fetch")
        self.assertEqual(0, code, value)
        record = value["result"]
        self.assertEqual("inbound", record["direction"])
        self.assertEqual("received", record["state"])
        self.assertEqual("files", client.requests[-1][0])
        self.assertEqual(client.commit, client.requests[-1][2])
        self.assertEqual(self.data, self.source.read_bytes())
        output = self.root / "incoming-review"
        code, value, _ = self.command("materialize", record["id"], "--output", str(output))
        self.assertEqual(0, code, value)
        self.assertEqual(client.data, (output / "docs" / "source.bin").read_bytes())
        self.assertEqual([], list(self.root.rglob("deus.sqlite3")))

    def test_entry_help_works_from_an_unrelated_directory(self):
        result = subprocess.run([sys.executable, str(ROOT / "kapi.py"), "--help"],
                                cwd=self.root, text=True, encoding="utf-8", capture_output=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("--exchange-dir", result.stdout)
        self.assertIn("materialize", result.stdout)
        self.assertFalse(self.state.exists())


if __name__ == "__main__":
    unittest.main()
