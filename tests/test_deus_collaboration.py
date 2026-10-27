"""Shared-task regressions with synthetic sessions, bounded runners and GitHub bytes."""
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from threading import Event
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ortak_kopru.adapters.github import GitHubError, git_blob_sha
from ortak_kopru.backup import create_backup, restore_backup
from ortak_kopru.collaboration import JointService, OUTPUT_LIMIT
from ortak_kopru.core import Conflict, CoreError, Store
from ortak_kopru.handoff import create_handoff, verify_handoff


class SyntheticGitHub:
    """The branch moves after resolution; selected files must use the old commit."""
    commit, tree = "a" * 40, "b" * 40

    def __init__(self):
        self.calls = []
        self.branch = self.commit
        self.files = {"docs/fixture.txt": "Sabit kaynak.\n".encode("utf-8"),
                      "data.bin": b"\x00\xffimmutable\r\n"}
        self.fail = False
        self.corrupt = False

    def resolve_ref(self, repository, ref):
        self.calls.append(("resolve_ref", repository, ref))
        if self.fail:
            raise GitHubError("private-error-text-must-not-be-saved", status=403, code="forbidden")
        self.branch = "c" * 40
        return {"commit": self.commit, "tree": self.tree}

    def files_at(self, repository, commit, paths):
        self.calls.append(("files_at", repository, commit, tuple(paths)))
        if commit != self.commit:
            raise AssertionError("fetch followed the moved branch")
        return [{"path": path, "data": self.files[path], "bytes": len(self.files[path]),
                 "blob_sha": "0" * 40 if self.corrupt else git_blob_sha(self.files[path]),
                 "mode": "100644"} for path in paths]


def local_receipt(operation, cwd, *, status="completed", output=b"fixture\n", exit_code=0):
    def stream(data):
        return {"text": data.decode("utf-8", errors="backslashreplace"), "captured_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(), "truncated": False}
    return {"operation": operation, "argv": ["synthetic-runner", operation], "cwd": cwd,
            "platform": {"system": "fixture", "release": "fixture", "machine": "fixture",
                         "python_implementation": "fixture", "python_version": "fixture"},
            "started_at": "2026-10-27T00:00:00+00:00",
            "finished_at": "2026-10-27T00:00:00.001+00:00", "duration_ms": 1,
            "exit_code": exit_code, "status": status, "stdout": stream(output),
            "stderr": stream(b"")}


class JointTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-joint-", dir="/tmp" if os.name != "nt" else None)
        self.root = Path(self.tmp.name).resolve()
        self.store = Store(self.root / "state")
        self.remote = SyntheticGitHub()
        self.service = JointService(self.store, github_client=self.remote)
        self.counter = 0
        self.task = self.create()

    def tearDown(self):
        self.tmp.cleanup()

    def key(self):
        self.counter += 1
        return f"joint-fixture-{self.counter}"

    def create(self):
        return self.store.create_task("Birlikte seçilen kaynakları inceleyin.",
                                      {"actor": "fixture owner", "source": "current synthetic input",
                                       "scope": "selected fixture observations"},
                                      ["Sonucu ayrıca denetle"], self.key())

    def contribute(self, **changes):
        values = {"task_id": self.task["id"], "author": "ChatGPT fixture",
                  "session_id": "existing-session-A", "relayed_by": "fixture owner",
                  "stage": 16, "body": "Öneri; yürütüm kanıtı değildir.",
                  "expected_revision": 1, "request_key": self.key()}
        values.update(changes)
        return self.service.contribute(**values)

    def operate(self, **changes):
        values = {"task_id": self.task["id"], "operation": "python_version",
                  "cwd": str(self.root), "expected_revision": 1, "request_key": self.key()}
        values.update(changes)
        return self.service.operate(**values)

    def fetch(self, **changes):
        values = {"task_id": self.task["id"], "repository": "fixture/project", "ref": "main",
                  "paths": ["docs/fixture.txt", "data.bin"], "expected_revision": 1,
                  "request_key": self.key()}
        values.update(changes)
        return self.service.fetch_github(**values)

    def test_three_existing_sessions_preserve_active_attempt_and_authority(self):
        assigned = self.store.assign(self.task["id"], "original receiver", "live-session", 1, self.key())
        self.store.receive(assigned["active_attempt_id"], "live-session", self.key())
        before = self.store.get_task(self.task["id"])
        reference = self.root / "not-to-be-opened.txt"
        reference.write_text("FILE-CONTENT-MUST-NOT-BE-READ", encoding="utf-8")
        for index, author in enumerate(("ChatGPT fixture", "Claude Code fixture", "Gemini fixture")):
            self.contribute(author=author, session_id=f"existing-{index}",
                            stage=(16, 32, 128)[index], references=[str(reference), "k-0042"])
        after, view = self.store.get_task(self.task["id"]), self.service.view(self.task["id"])
        for field in ("active_attempt_id", "current_result_id", "status", "revision", "authority", "attempts"):
            self.assertEqual(after[field], before[field])
        self.assertEqual(len(view["contributions"]), 3)
        self.assertEqual(len(after["sources"]), 3)
        for item in view["contributions"]:
            self.assertFalse(item["identity_verified"])
            self.assertFalse(item["instruction_authority"])
            self.assertFalse(item["execution_evidence"])
            self.assertFalse(item["historical"])
            self.assertEqual(item["relayed_by"], "fixture owner")
        context = self.store.context_bundle(self.task["id"])
        self.assertNotIn("FILE-CONTENT-MUST-NOT-BE-READ", json.dumps(context))
        self.assertEqual(context["sources"][0]["category"], "contribution")

    def test_contribution_idempotency_conflict_and_historical_revision(self):
        first = self.contribute(request_key="same-contribution")
        self.assertEqual(first, self.contribute(request_key="same-contribution"))
        with self.assertRaises(Conflict):
            self.contribute(request_key="same-contribution", body="Changed intent")
        self.store.revise_task(self.task["id"], "Yeni kapsam", 1, self.key())
        old = self.contribute(request_key="same-contribution")
        self.assertTrue(old["historical"])
        self.assertEqual(old["revision"], 1)
        self.assertEqual(old["id"], first["id"])
        self.assertEqual(len(self.store.get_task(self.task["id"])["sources"]), 1)
        with self.assertRaises(Conflict):
            self.contribute()
        new = self.contribute(expected_revision=2, stage=128)
        self.assertFalse(new["historical"])

    def test_revision_and_closed_states_reject_all_new_work_before_external_calls(self):
        self.store.revise_task(self.task["id"], "Revision two", 1, self.key())
        with patch("ortak_kopru.collaboration._run_local") as runner:
            for action in (self.contribute, self.operate, self.fetch):
                with self.assertRaises(Conflict):
                    action()
            self.store.control_task(self.task["id"], "pause", 2, self.key())
            for action in (self.contribute, self.operate, self.fetch):
                with self.assertRaises(Conflict):
                    action(expected_revision=2)
            self.store.control_task(self.task["id"], "cancel", 2, self.key())
            for action in (self.contribute, self.operate, self.fetch):
                with self.assertRaises(Conflict):
                    action(expected_revision=2)
            runner.assert_not_called()
        self.assertEqual(self.remote.calls, [])
        self.assertEqual(self.service.view(self.task["id"])["operations"], [])

    def test_completed_task_does_not_accept_new_contributions_or_operations(self):
        assigned = self.store.assign(self.task["id"], "fixture", "s", 1, self.key())
        attempt = assigned["active_attempt_id"]
        self.store.receive(attempt, "s", self.key())
        result = self.store.submit_result(attempt, "s", "fixture result", [], self.key())
        self.store.verify_task(self.task["id"], [{"criterion_id": "criterion-1",
            "result_id": result["current_result_id"], "passed": True,
            "evidence": "synthetic check", "verifier": "fixture owner"}], 1, self.key())
        with patch("ortak_kopru.collaboration._run_local") as runner:
            for action in (self.contribute, self.operate, self.fetch):
                with self.assertRaises(Conflict):
                    action()
            runner.assert_not_called()
        self.assertEqual(self.remote.calls, [])

    def test_exact_stage_and_literal_reference_validation(self):
        for stage in (True, "16", 1, 8, 256, None):
            for action in (self.contribute, self.operate, self.fetch):
                with self.assertRaises(CoreError):
                    action(stage=stage)
        for references in (["x"] * 65, [{"path": "not-opened"}], "https://example.invalid"):
            with self.assertRaises(CoreError):
                self.contribute(references=references)
        item = self.contribute(stage=128, references=["https://example.invalid/record", "k-0001"])
        self.assertEqual(item["references"], ["https://example.invalid/record", "k-0001"])
        with self.assertRaises(CoreError):
            self.operate(operation="arbitrary shell command")

    def test_concurrent_claim_and_retry_start_only_one_process(self):
        entered, release = Event(), Event()

        def run(operation, cwd, **_):
            self.assertEqual(self.store.events(self.task["id"])[-1]["kind"], "operation_prepared")
            entered.set()
            if not release.wait(5):
                raise RuntimeError("fixture runner not released")
            return local_receipt(operation, cwd)

        other = JointService(Store(self.store.directory))
        with patch("ortak_kopru.collaboration._run_local", side_effect=run) as runner:
            with ThreadPoolExecutor(max_workers=2) as pool:
                first = pool.submit(self.operate, request_key="claim-once")
                try:
                    self.assertTrue(entered.wait(5))
                    duplicate = pool.submit(other.operate, self.task["id"], "python_version",
                                            str(self.root), 1, "claim-once").result(timeout=5)
                    self.assertEqual(duplicate["status"], "unknown")
                    self.assertIsNone(duplicate["receipt"])
                    runner.assert_called_once()
                finally:
                    release.set()
                complete = first.result(timeout=5)
            self.assertEqual(complete["operation_id"], duplicate["operation_id"])
            self.assertEqual(self.operate(request_key="claim-once"), complete)
            runner.assert_called_once()
        kinds = [event["kind"] for event in self.store.events(self.task["id"])]
        self.assertEqual(kinds.count("operation_prepared"), 1)
        self.assertEqual(kinds.count("operation_finished"), 1)
        with self.assertRaises(Conflict):
            self.operate(request_key="claim-once", operation="repo_status")

    def test_revision_can_change_during_execution_and_old_receipt_is_preserved(self):
        def run(operation, cwd, **_):
            Store(self.store.directory).revise_task(self.task["id"], "New instruction", 1, "during-run")
            return local_receipt(operation, cwd)
        with patch("ortak_kopru.collaboration._run_local", side_effect=run):
            result = self.operate(request_key="old-revision-run")
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["revision"], 1)
        self.assertTrue(result["historical"])
        task = self.store.get_task(self.task["id"])
        self.assertEqual((task["revision"], task["status"], task["current_result_id"]), (2, "ready", None))
        self.assertEqual(task["sources"][0]["revision"], 1)
        self.assertEqual(self.store.events(self.task["id"])[-1]["revision"], 1)
        with patch("ortak_kopru.collaboration._run_local") as runner:
            self.assertEqual(self.operate(request_key="old-revision-run"), result)
            runner.assert_not_called()

    def test_failed_cli_receipt_does_not_complete_task_and_is_not_retried(self):
        receipt = local_receipt("python_version", str(self.root), status="failed", exit_code=7)
        with patch("ortak_kopru.collaboration._run_local", return_value=receipt) as runner:
            result = self.operate(request_key="failed-once")
            self.assertEqual(self.operate(request_key="failed-once"), result)
            runner.assert_called_once()
        self.assertEqual(result["receipt"]["exit_code"], 7)
        self.assertEqual(result["status"], "failed")
        task = self.store.get_task(self.task["id"])
        self.assertEqual(task["status"], "ready")
        self.assertEqual(task["results"], [])
        self.assertEqual(len(task["sources"]), 1)

    def test_interruption_leaves_unknown_and_restart_never_reexecutes(self):
        with patch("ortak_kopru.collaboration._run_local", side_effect=KeyboardInterrupt):
            with self.assertRaises(KeyboardInterrupt):
                self.operate(request_key="interrupted")
        restarted = JointService(Store(self.store.directory))
        with patch("ortak_kopru.collaboration._run_local") as runner:
            result = restarted.operate(self.task["id"], "python_version", str(self.root), 1, "interrupted")
            runner.assert_not_called()
        self.assertEqual(result["status"], "unknown")
        self.assertIsNone(result["receipt"])
        self.assertEqual(result["source_ids"], [])
        # A deliberate new key creates another operation; it cannot rewrite the
        # uncertain record or retroactively turn it into successful evidence.
        with patch("ortak_kopru.collaboration._run_local",
                   return_value=local_receipt("python_version", str(self.root))) as runner:
            fresh = restarted.operate(self.task["id"], "python_version", str(self.root),
                                      1, "explicit-new-attempt")
            runner.assert_called_once()
            original = restarted.operate(self.task["id"], "python_version", str(self.root),
                                         1, "interrupted")
            runner.assert_called_once()
        self.assertNotEqual(fresh["operation_id"], result["operation_id"])
        self.assertEqual(fresh["status"], "completed")
        self.assertEqual(original, result)
        self.assertEqual(len(restarted.view(self.task["id"])["operations"]), 2)

    def test_start_errors_and_unexpected_errors_have_bounded_distinct_receipts(self):
        for failure, status in ((ValueError("secret-error"), "spawn_error"),
                                (OSError("secret-error"), "spawn_error"),
                                (RuntimeError("secret-error"), "unknown")):
            with patch("ortak_kopru.collaboration._run_local", side_effect=failure):
                result = self.operate()
            self.assertEqual(result["status"], status)
            self.assertNotIn("secret-error", json.dumps(result))
            self.assertTrue(result["source_ids"])
        with patch("ortak_kopru.collaboration._run_local", return_value={"status": "completed"}):
            self.assertEqual(self.operate()["status"], "unknown")

    @unittest.skipUnless(shutil.which("git"), "Git is required for the fixed local runner")
    def test_real_runner_platform_receipt_is_retained_by_service(self):
        repository = self.root / "synthetic-repository"
        repository.mkdir()
        subprocess.run(["git", "init", "--quiet", str(repository)], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10)
        result = self.operate(cwd=str(repository))
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["receipt"]["exit_code"], 0)
        self.assertEqual(set(result["receipt"]["platform"]),
                         {"system", "release", "machine", "python_implementation", "python_version"})
        self.assertIn("Python ", result["receipt"]["stdout"]["text"])
        source = self.store.get_task(self.task["id"])["sources"][0]
        captured = json.loads((self.store.directory / source["snapshot"]).read_text(encoding="utf-8"))
        self.assertEqual(captured["receipt"], result["receipt"])
        self.assertEqual(self.store.get_task(self.task["id"])["status"], "ready")

    def test_invalid_utf8_expansion_preserves_bounded_bytes_and_hash(self):
        data = b"\xff" * OUTPUT_LIMIT
        receipt = local_receipt("python_version", str(self.root), output=data)
        self.assertEqual(len(receipt["stdout"]["text"]), 4 * OUTPUT_LIMIT)
        with patch("ortak_kopru.collaboration._run_local", return_value=receipt):
            result = self.operate()
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["receipt"]["stdout"]["captured_bytes"], OUTPUT_LIMIT)
        self.assertEqual(result["receipt"]["stdout"]["sha256"], hashlib.sha256(data).hexdigest())
        self.assertEqual(result["receipt"]["stdout"]["text"], "\\xff" * OUTPUT_LIMIT)
        receipt["stdout"]["text"] += "x"
        with patch("ortak_kopru.collaboration._run_local", return_value=receipt):
            self.assertEqual(self.operate()["status"], "unknown")

    def test_github_pins_commit_and_snapshots_exact_bytes_separately_from_local_head(self):
        result = self.fetch(request_key="pinned-fetch")
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["receipt"]["commit"], self.remote.commit)
        self.assertNotEqual(self.remote.branch, result["receipt"]["commit"])
        self.assertEqual(result["kind"], "github_fetch")
        sources = self.store.get_task(self.task["id"])["sources"]
        remote_sources = [item for item in sources if item["category"] == "operation_source"]
        self.assertEqual(len(remote_sources), 2)
        for item in remote_sources:
            provenance = item["provenance"]
            data = self.remote.files[provenance["path"]]
            self.assertEqual(provenance["commit"], self.remote.commit)
            self.assertEqual(provenance["blob_sha"], git_blob_sha(data))
            self.assertEqual(item["sha256"], hashlib.sha256(data).hexdigest())
            self.assertEqual((self.store.directory / item["snapshot"]).read_bytes(), data)
        self.assertFalse(self.service.exchange_directory.is_relative_to(self.store.directory))
        self.assertEqual(self.fetch(request_key="pinned-fetch"), result)
        self.assertEqual(len(self.remote.calls), 2)
        with self.assertRaises(Conflict):
            self.fetch(request_key="pinned-fetch", paths=["data.bin"])

    def test_github_failure_and_invalid_blob_do_not_claim_file_evidence(self):
        self.remote.fail = True
        result = self.fetch(request_key="failed-fetch")
        self.assertEqual(result["status"], "failed")
        self.assertEqual(result["receipt"]["error"]["http_status"], 403)
        self.assertNotIn("private-error", json.dumps(self.store.export_data()))
        self.assertEqual(self.fetch(request_key="failed-fetch"), result)
        self.assertEqual(len(self.remote.calls), 1)
        self.remote.fail, self.remote.corrupt = False, True
        self.assertEqual(self.fetch()["status"], "failed")
        self.assertTrue(all(source["category"] == "operation_receipt"
                            for source in self.store.get_task(self.task["id"])["sources"]))

    def test_backup_restore_and_handoff_keep_contribution_receipt_and_remote_bytes(self):
        contribution = self.contribute()
        operation = self.fetch(request_key="persist-fetch")
        receipt = local_receipt("python_version", str(self.root))
        with patch("ortak_kopru.collaboration._run_local", return_value=receipt):
            self.operate(request_key="persist-cli")
        task = self.store.assign(self.task["id"], "fixture receiver", "existing-target", 1, self.key())
        expected = self.service.view(self.task["id"])
        before = self.store.get_task(self.task["id"])
        create_backup(self.store.directory, self.root / "backup")
        shutil.rmtree(self.service.exchange_directory)
        restore_backup(self.root / "backup", self.root / "restored")
        restored = Store(self.root / "restored")
        service = JointService(restored)
        self.assertEqual(service.view(self.task["id"]), expected)
        for source in before["sources"]:
            self.assertEqual((restored.directory / source["snapshot"]).read_bytes(),
                             (self.store.directory / source["snapshot"]).read_bytes())
        with patch("ortak_kopru.collaboration._run_local") as runner:
            self.assertEqual(service.operate(self.task["id"], "python_version", str(self.root), 1,
                                             "persist-cli")["status"], "completed")
            runner.assert_not_called()
        self.assertEqual(service.fetch_github(self.task["id"], "fixture/project", "main",
                                              ["docs/fixture.txt", "data.bin"], 1, "persist-fetch"), operation)
        package = self.root / "handoff"
        manifest = create_handoff(restored, task["active_attempt_id"], "existing-target", package)
        self.assertEqual(verify_handoff(package), manifest)
        context = json.loads((package / "context.json").read_text(encoding="utf-8"))
        self.assertIn(contribution["id"], {source["record_id"] for source in context["sources"]})
        for source in before["sources"]:
            self.assertEqual((package / source["snapshot"]).read_bytes(),
                             (restored.directory / source["snapshot"]).read_bytes())
        self.assertFalse(manifest["preparation"]["delivery_receipt"])

    def test_snapshot_failure_keeps_prepared_unknown_without_a_false_finish(self):
        receipt = local_receipt("python_version", str(self.root))
        with patch("ortak_kopru.collaboration._run_local", return_value=receipt), \
                patch.object(self.store, "_snapshot_bytes", side_effect=CoreError("fixture capture failed")):
            with self.assertRaises(CoreError):
                self.operate(request_key="capture-failure")
        with patch("ortak_kopru.collaboration._run_local") as runner:
            result = self.operate(request_key="capture-failure")
            runner.assert_not_called()
        self.assertEqual(result["status"], "unknown")
        self.assertIsNone(result["receipt"])
        self.assertEqual(self.store.get_task(self.task["id"])["sources"], [])


if __name__ == "__main__":
    unittest.main()
