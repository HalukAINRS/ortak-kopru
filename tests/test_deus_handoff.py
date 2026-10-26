"""Session discovery and complete handoff packages without live providers."""
from concurrent.futures import ThreadPoolExecutor
import copy
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from threading import Event
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ortak_kopru.core import Conflict, CoreError, NotFound, Store
from ortak_kopru.handoff import create_handoff, inbox, list_sessions, verify_handoff
from ortak_kopru.local_files import copy_verified_file


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-handoff-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.store = Store(self.root / "state")
        self.counter = 0

    def key(self):
        self.counter += 1
        return f"handoff-request-{self.counter}"

    def assigned(self, *, sources=None, session="session-A", participant="Local receiver"):
        task = self.store.create_task("  Continue this exact work.\nKeep the source bytes.  ",
            {"actor": "Local owner", "source": "offline fixture", "scope": "fixture files"},
            ["Result checked"], self.key(), sources=sources)
        return self.store.assign(task["id"], participant, session, 1, self.key())

    def test_sessions_and_inbox_only_report_current_recorded_work(self):
        self.assertEqual(list_sessions(self.store), {"sessions": []})
        self.assertEqual(inbox(self.store, "unknown")["items"], [])
        first = self.assigned(participant="Receiver A")
        second = self.assigned(participant="Receiver B")
        self.store.receive(first["active_attempt_id"], "session-A", self.key())
        row = list_sessions(self.store)["sessions"][0]
        self.assertEqual(row["participants"], ["Receiver A", "Receiver B"])
        self.assertEqual((row["attempt_count"], row["active_count"], row["pending_count"], row["received_count"]),
                         (2, 2, 1, 1))
        self.assertEqual(row["liveness"], "not_observed")
        self.assertFalse(row["identity_verified"])
        self.assertEqual({item["task_id"] for item in inbox(self.store, "session-A")["items"]},
                         {first["id"], second["id"]})
        transferred = self.store.assign(first["id"], "Receiver C", "session-B", 1, self.key(),
                                       expected_active_attempt_id=first["active_attempt_id"])
        self.assertEqual([item["attempt_id"] for item in inbox(self.store, "session-B")["items"]],
                         [transferred["active_attempt_id"]])
        self.assertEqual([item["task_id"] for item in inbox(self.store, "session-A")["items"]], [second["id"]])
        self.store.receive(second["active_attempt_id"], "session-A", self.key())
        self.store.submit_result(second["active_attempt_id"], "session-A", "Ready for checking", [], self.key())
        self.store.control_task(first["id"], "pause", 1, self.key())
        self.assertEqual(inbox(self.store, "session-A")["items"], [])
        self.assertEqual(inbox(self.store, "session-B")["items"], [])
        self.assertEqual(sum(item["active_count"] for item in list_sessions(self.store)["sessions"]), 0)

    def test_complete_package_includes_binary_omitted_text_and_previous_artifact(self):
        text_source, binary_source, artifact = (self.root / name for name in ("text.txt", "binary.bin", "result.bin"))
        text_source.write_bytes(b"source beyond the small context text budget")
        binary_source.write_bytes(b"\xff\x00\x80binary")
        artifact.write_bytes(b"actual previous result bytes\x00\xff")
        task = self.assigned(sources=[str(text_source), str(binary_source)])
        first_attempt = task["active_attempt_id"]
        self.store.receive(first_attempt, "session-A", self.key())
        self.store.submit_result(first_attempt, "session-A", "Previous result", [str(artifact), str(binary_source)], self.key())
        task = self.store.assign(task["id"], "Next receiver", "session-B", 1, self.key(),
                                 expected_active_attempt_id=first_attempt)
        before_task, before_events = self.store.get_task(task["id"]), self.store.events()
        package = self.root / "handoff"
        with patch("ortak_kopru.core.MAX_CONTEXT_TEXT_BYTES", 4):
            manifest = create_handoff(self.store, task["active_attempt_id"], "session-B", package)
        self.assertEqual(verify_handoff(package), manifest)
        context = json.loads((package / "context.json").read_text(encoding="utf-8"))
        self.assertEqual(context["sources"][0]["text_omitted_reason"], "context_budget")
        self.assertEqual(context["sources"][1]["text_omitted_reason"], "utf8_text_not_available")
        self.assertEqual(context["original_words"], task["original_words"])
        self.assertEqual(context["handoff_attempt"]["session_id"], "session-B")
        self.assertEqual(len(manifest["objects"]), 3)  # Duplicate binary source/artifact shares one snapshot.
        for source in context["sources"] + context["previous_results"][0]["artifacts"]:
            original = self.store.directory / source["snapshot"]
            self.assertEqual((package / source["snapshot"]).read_bytes(), original.read_bytes())
        self.assertEqual(self.store.get_task(task["id"]), before_task)
        self.assertEqual(self.store.events(), before_events)
        self.assertFalse(manifest["preparation"]["delivery_receipt"])
        self.assertTrue(manifest["preparation"]["live_receive_required"])
        self.assertEqual(before_task["attempts"][-1]["delivery_status"], "pending")
        self.assertEqual({p.name for p in package.iterdir()}, {"manifest.json", "context.json", "objects"})

    def test_live_assignment_is_required_for_preparation_not_offline_integrity(self):
        task = self.assigned()
        package = self.root / "intact-after-cancel"
        manifest = create_handoff(self.store, task["active_attempt_id"], "session-A", package)
        self.store.control_task(task["id"], "cancel", 1, self.key())
        self.assertEqual(verify_handoff(package), manifest)
        with self.assertRaises(Conflict):
            self.store.receive(task["active_attempt_id"], "session-A", self.key())
        with self.assertRaises(Conflict):
            create_handoff(self.store, task["active_attempt_id"], "session-A", self.root / "obsolete")
        self.assertFalse((self.root / "obsolete").exists())

    def test_slow_handoff_copy_does_not_delay_live_cancel(self):
        source = self.root / "source.txt"
        source.write_bytes(b"immutable snapshot bytes")
        task = self.assigned(sources=[str(source)])
        package = self.root / "copy-in-progress"
        copy_started, release_copy = Event(), Event()

        def blocked_copy(*args, **kwargs):
            copy_started.set()
            if not release_copy.wait(timeout=10):
                raise TimeoutError("test copy was not released")
            return copy_verified_file(*args, **kwargs)

        with patch("ortak_kopru.handoff.copy_verified_file", side_effect=blocked_copy):
            with ThreadPoolExecutor(max_workers=2) as pool:
                preparation = pool.submit(create_handoff, self.store, task["active_attempt_id"], "session-A", package)
                try:
                    self.assertTrue(copy_started.wait(timeout=5))
                    cancellation = pool.submit(self.store.control_task, task["id"], "cancel", 1, self.key())
                    cancelled = cancellation.result(timeout=5)
                    self.assertEqual(cancelled["status"], "cancelled")
                    self.assertFalse(package.exists())
                finally:
                    release_copy.set()
                manifest = preparation.result(timeout=10)
        self.assertEqual(manifest["preparation"]["task_status"], "ready")
        self.assertEqual(verify_handoff(package), manifest)
        self.assertEqual(self.store.get_task(task["id"])["status"], "cancelled")
        with self.assertRaises(Conflict):
            self.store.receive(task["active_attempt_id"], "session-A", self.key())

    def test_preparation_rejects_wrong_session_and_superseded_or_finished_work(self):
        for change in ("pause", "revise", "transfer", "result"):
            with self.subTest(change=change):
                task = self.assigned()
                attempt = task["active_attempt_id"]
                with self.assertRaises(Conflict):
                    create_handoff(self.store, attempt, "wrong-session", self.root / (change + "-wrong"))
                if change == "pause":
                    self.store.control_task(task["id"], "pause", 1, self.key())
                elif change == "revise":
                    self.store.revise_task(task["id"], "Updated work", 1, self.key())
                elif change == "transfer":
                    self.store.assign(task["id"], "Next receiver", "session-B", 1, self.key(),
                                      expected_active_attempt_id=attempt)
                else:
                    self.store.receive(attempt, "session-A", self.key())
                    self.store.submit_result(attempt, "session-A", "Result", [], self.key())
                with self.assertRaises(Conflict):
                    create_handoff(self.store, attempt, "session-A", self.root / change)
                self.assertFalse((self.root / change).exists())
        with self.assertRaises(NotFound):
            create_handoff(self.store, "missing", "session-A", self.root / "missing")

    def test_verification_rejects_changed_bytes_binding_paths_and_unlisted_content(self):
        source = self.root / "source.txt"
        source.write_bytes(b"exact fixture source")
        task = self.assigned(sources=[str(source)])
        original = self.root / "original"
        manifest = create_handoff(self.store, task["active_attempt_id"], "session-A", original)
        for failure in ("object", "missing", "context", "binding", "traversal", "omitted", "extra", "version"):
            with self.subTest(failure=failure):
                package = self.root / failure
                shutil.copytree(original, package)
                changed = copy.deepcopy(manifest)
                obj = package / changed["objects"][0]["path"]
                if failure == "object":
                    obj.write_bytes(b"changed bytes")
                elif failure == "missing":
                    obj.unlink()
                elif failure == "context":
                    (package / "context.json").write_bytes(b"{}")
                elif failure == "binding":
                    changed["session_id"] = "other-session"
                elif failure == "traversal":
                    changed["objects"][0]["path"] = "../source.txt"
                elif failure == "omitted":
                    changed["objects"] = []
                elif failure == "extra":
                    (package / "unexpected.txt").write_bytes(b"not manifested")
                else:
                    changed["schema_version"] = True
                (package / "manifest.json").write_text(json.dumps(changed), encoding="utf-8")
                with self.assertRaises(CoreError):
                    verify_handoff(package)

    @unittest.skipIf(os.name == "nt", "Creating symlinks requires a separate Windows privilege.")
    def test_verification_rejects_object_and_directory_links(self):
        source = self.root / "source.txt"
        source.write_bytes(b"fixture bytes")
        task = self.assigned(sources=[str(source)])
        package = self.root / "package"
        manifest = create_handoff(self.store, task["active_attempt_id"], "session-A", package)
        obj = package / manifest["objects"][0]["path"]
        obj.unlink()
        obj.symlink_to(source)
        with self.assertRaises(CoreError):
            verify_handoff(package)
        link = self.root / "package-link"
        link.symlink_to(package, target_is_directory=True)
        with self.assertRaises(CoreError):
            verify_handoff(link)

    def test_failed_copy_corrupt_previous_artifact_and_existing_destination_do_not_publish(self):
        source = self.root / "source.txt"
        source.write_bytes(b"fixture bytes")
        task = self.assigned(sources=[str(source)])
        before = self.store.events()
        with patch("ortak_kopru.handoff.copy_verified_file", side_effect=CoreError("injected copy failure")):
            with self.assertRaises(CoreError):
                create_handoff(self.store, task["active_attempt_id"], "session-A", self.root / "failed")
        self.assertFalse((self.root / "failed").exists())
        self.assertEqual(list(self.root.glob(".deus-stage-*")), [])
        self.assertEqual(self.store.events(), before)
        existing = self.root / "existing"
        existing.mkdir()
        (existing / "keep").write_bytes(b"unchanged")
        with self.assertRaises(CoreError):
            create_handoff(self.store, task["active_attempt_id"], "session-A", existing)
        self.assertEqual((existing / "keep").read_bytes(), b"unchanged")
        self.store.receive(task["active_attempt_id"], "session-A", self.key())
        artifact = self.root / "artifact.bin"
        artifact.write_bytes(b"actual artifact")
        result = self.store.submit_result(task["active_attempt_id"], "session-A", "Result", [str(artifact)], self.key())
        current = self.store.assign(task["id"], "New receiver", "session-A", 1, self.key(),
                                    expected_active_attempt_id=task["active_attempt_id"])
        snapshot = self.store.directory / result["results"][0]["artifacts"][0]["snapshot"]
        snapshot.write_bytes(b"corrupt")
        with self.assertRaises(CoreError):
            create_handoff(self.store, current["active_attempt_id"], "session-A", self.root / "corrupt")
        self.assertFalse((self.root / "corrupt").exists())

    def test_private_destination_and_explicit_package_limits(self):
        task = self.assigned()
        checkout = self.root / "checkout"
        checkout.mkdir()
        (checkout / ".git").write_text("gitdir: fixture", encoding="utf-8")
        for destination in (checkout / "handoff", self.store.directory / "handoff"):
            with self.assertRaises(CoreError):
                create_handoff(self.store, task["active_attempt_id"], "session-A", destination)
            self.assertFalse(destination.exists())
        with patch("ortak_kopru.handoff.MAX_PACKAGE_BYTES", 1):
            with self.assertRaises(CoreError):
                create_handoff(self.store, task["active_attempt_id"], "session-A", self.root / "large")
        self.assertFalse((self.root / "large").exists())
        with self.assertRaises(CoreError):
            inbox(self.store, "")


if __name__ == "__main__":
    unittest.main()
