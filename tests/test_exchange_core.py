"""Transfer persistence and selected bytes; no network or task runtime."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru.core import CoreError
from ortak_kopru.exchange import ExchangeConflict, ExchangeError, ExchangeStore, validate_path
from ortak_kopru import exchange


class ExchangeStoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "local-source.txt"
        self.source.write_bytes(b"selected bytes\x00\xff")
        self.store = ExchangeStore(self.root / "exchange")
        self.target = {"provider": "github", "repository": "example/project", "base_ref": "main"}

    def prepare(self, key="prepare-1", *, selections=None, target=None, purpose="Seçilmiş raporu paylaş"):
        return self.store.prepare_outbound(
            selections or [{"source": str(self.source), "path": "reports/result.bin"}],
            self.target if target is None else target, purpose, key)

    def package(self, record):
        return self.store.packages / record["id"]

    def object(self, record):
        return self.package(record) / record["manifest"]["files"][0]["object"]

    def test_selected_bytes_survive_original_change_and_deletion_without_task(self):
        record = self.prepare()
        self.assertEqual(record["state"], "prepared")
        self.assertFalse((self.store.directory / "deus.sqlite3").exists())
        selected = self.source.read_bytes()
        digest = hashlib.sha256(selected).hexdigest()
        self.source.write_bytes(b"new local work")
        self.source.unlink()
        reopened = ExchangeStore(self.store.directory, create=False)
        self.assertEqual(reopened.read_object(record["id"], digest), selected)
        self.assertEqual(reopened.verify(record["id"])["id"], record["id"])
        result = reopened.materialize(record["id"], self.root / "review-copy")
        self.assertEqual((Path(result["output_path"]) / "reports/result.bin").read_bytes(), selected)
        self.assertEqual(set(result["files"][0]), {"path", "bytes", "sha256"})

    def test_package_and_materialized_files_exclude_private_context_and_other_files(self):
        (self.root / "not-selected.txt").write_text("unrelated private material", encoding="utf-8")
        record = self.prepare(purpose="private operator intent")
        manifest_text = (self.package(record) / "manifest.json").read_text(encoding="utf-8")
        for private_text in (str(self.source), "private operator intent", "prepare-1", "unrelated private material"):
            self.assertNotIn(private_text, manifest_text)
        manifest = json.loads(manifest_text)
        self.assertEqual(set(manifest), {"schema_version", "kind", "files"})
        self.assertEqual(record["source_paths"]["reports/result.bin"], str(self.source.resolve()))
        destination = self.root / "selected-only"
        self.store.materialize(record["id"], destination)
        self.assertEqual([p.relative_to(destination).as_posix() for p in destination.rglob("*") if p.is_file()],
                         ["reports/result.bin"])

    def test_replay_is_one_record_and_changed_intent_conflicts(self):
        first = self.prepare()
        self.assertEqual(self.prepare(), first)
        self.assertEqual(len(self.store.list_transfers()), 1)
        self.assertEqual(len(self.store.events(first["id"])), 1)
        for kwargs in ({"purpose": "different intent"},
                       {"target": {**self.target, "repository": "example/other"}},
                       {"selections": [{"source": str(self.source), "path": "other.bin"}]}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ExchangeConflict):
                self.prepare(**kwargs)
        self.source.write_bytes(b"changed content")
        with self.assertRaises(ExchangeConflict):
            self.prepare()
        self.assertEqual(len(list(self.store.packages.iterdir())), 1)

    def test_inbound_source_is_private_and_replay_binds_exact_remote_version(self):
        origin = {"provider": "github", "repository": "example/project", "commit": "a" * 40}
        files = [{"path": "readme.txt", "data": b"received result", "source": {"path": "README.md", "blob_sha": "b" * 40}}]
        record = self.store.record_inbound(files, origin, "Kaynak al", "fetch-1")
        self.assertEqual(record["state"], "received")
        self.assertIsNone(record["target"])
        self.assertEqual(record["origin"], origin)
        self.assertEqual(self.store.record_inbound(files, origin, "Kaynak al", "fetch-1"), record)
        self.assertNotIn("blob_sha", (self.package(record) / "manifest.json").read_text())
        with self.assertRaises(ExchangeConflict):
            self.store.record_inbound(files, {**origin, "commit": "c" * 40}, "Kaynak al", "fetch-1")

    def test_git_project_sources_are_allowed_but_private_stores_are_not(self):
        project = self.root / "project"
        (project / ".git").mkdir(parents=True)
        (project / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
        source = project / "report.txt"
        source.write_bytes(b"project report")
        record = self.prepare(selections=[{"source": str(source), "path": "report.txt"}])
        self.assertEqual(record["manifest"]["files"][0]["bytes"], len(b"project report"))
        with self.assertRaises(CoreError):
            ExchangeStore(project / "private")
        self.assertFalse((project / "private").exists())
        task = self.root / "existing-task-state"
        task.mkdir()
        (task / "deus.sqlite3").write_bytes(b"task state must not be changed")
        for destination in (task, task / "transfers"):
            with self.subTest(destination=destination), self.assertRaises(ExchangeError):
                ExchangeStore(destination)
        self.assertEqual((task / "deus.sqlite3").read_bytes(), b"task state must not be changed")

    def test_missing_read_only_store_does_not_create_files(self):
        missing = self.root / "absent" / "exchange"
        with self.assertRaises(ExchangeError):
            ExchangeStore(missing, create=False)
        self.assertFalse((self.root / "absent").exists())

    def test_future_schema_is_rejected_without_mutation(self):
        with sqlite3.connect(self.store.path) as db:
            db.execute("UPDATE metadata SET value='999' WHERE key='schema_version'")
        before = self.store.path.read_bytes()
        with self.assertRaises(ExchangeError):
            ExchangeStore(self.store.directory)
        self.assertEqual(self.store.path.read_bytes(), before)

    def test_simultaneous_first_use_initializes_one_complete_ledger(self):
        directory = self.root / "simultaneous"
        with ThreadPoolExecutor(max_workers=2) as pool:
            stores = list(pool.map(lambda _: ExchangeStore(directory), range(2)))
        self.assertEqual(stores[0].list_transfers(), [])
        self.assertEqual(stores[1].list_transfers(), [])
        self.assertEqual(ExchangeStore(directory, create=False).list_transfers(), [])

    def test_interruption_after_initialization_commit_keeps_database(self):
        original_db = ExchangeStore._db

        @contextmanager
        def interrupted(store, *, write=False):
            with original_db(store, write=write) as db:
                yield db
            if write:
                raise InterruptedError("interrupted after initialization commit")

        directory = self.root / "interrupted-initialization"
        with mock.patch.object(ExchangeStore, "_db", interrupted):
            with self.assertRaises(InterruptedError):
                ExchangeStore(directory)
        self.assertEqual(ExchangeStore(directory, create=False).list_transfers(), [])

    def test_unsafe_or_platform_colliding_paths_are_rejected_before_package(self):
        bad_paths = ("../x", "/absolute", "C:/local", "a\\b", "a//b", "a/./b", ".git/config",
                     ".GIT/config", "NUL.txt", "COM1", "COM¹.txt", "a.", "a ", "a\nname")
        for index, path in enumerate(bad_paths):
            with self.subTest(path=path), self.assertRaises(ExchangeError):
                self.prepare(key=f"bad-{index}", selections=[{"source": str(self.source), "path": path}])
        for first, second in (("Result.txt", "result.txt"), ("folder", "folder/file.txt"),
                              ("Folder/a", "folder/b"), ("é.txt", "e\u0301.txt")):
            with self.subTest(first=first, second=second), self.assertRaises(ExchangeError):
                self.prepare(selections=[{"source": str(self.source), "path": first},
                                         {"source": str(self.source), "path": second}])
        self.assertEqual(self.store.list_transfers(), [])
        self.assertEqual(list(self.store.packages.iterdir()), [])
        self.assertEqual(validate_path(".github/config.json"), ".github/config.json")

    def test_source_link_or_parent_link_is_not_followed(self):
        link = self.root / "link.txt"
        linked_parent = self.root / "linked-parent"
        parent = self.root / "real-parent"
        parent.mkdir()
        (parent / "data").write_bytes(b"actual")
        try:
            link.symlink_to(self.source)
            linked_parent.symlink_to(parent, target_is_directory=True)
        except OSError:
            self.skipTest("Creating symlinks requires a separate Windows privilege.")
        for source in (link, linked_parent / "data"):
            with self.subTest(source=source), self.assertRaises(ExchangeError):
                self.prepare(selections=[{"source": str(source), "path": "data"}])
        self.assertEqual(self.store.list_transfers(), [])

    def test_inbound_and_outbound_limits_never_publish_partial_package(self):
        with mock.patch.object(exchange, "MAX_FILE_BYTES", 5):
            with self.assertRaises(CoreError):
                self.prepare()
            with self.assertRaises(ExchangeError):
                self.store.record_inbound([{"path": "a", "data": b"123456", "source": {}}], {}, "p", "i")
        self.source.write_bytes(b"1234")
        with mock.patch.object(exchange, "MAX_TOTAL_BYTES", 7):
            with self.assertRaises(ExchangeError):
                self.prepare(selections=[{"source": str(self.source), "path": "a"},
                                         {"source": str(self.source), "path": "b"}])
        self.assertEqual(self.store.list_transfers(), [])
        self.assertEqual(list(self.store.packages.iterdir()), [])

    def test_corrupt_missing_or_extra_payload_is_not_verified_or_materialized(self):
        record = self.prepare()
        original = self.object(record).read_bytes()
        self.object(record).write_bytes(b"corrupt")
        with self.assertRaises(ExchangeError):
            self.store.verify(record["id"])
        with self.assertRaises(ExchangeError):
            self.prepare()
        with self.assertRaises(ExchangeError):
            self.store.materialize(record["id"], self.root / "bad-output")
        self.assertFalse((self.root / "bad-output").exists())
        self.object(record).write_bytes(original)
        extra = self.package(record) / "objects" / "unlisted"
        extra.write_bytes(b"extra")
        with self.assertRaises(ExchangeError):
            self.store.verify(record["id"])
        extra.unlink()
        self.object(record).unlink()
        with self.assertRaises(ExchangeError):
            self.store.verify(record["id"])

    def test_manifest_cannot_smuggle_private_fields_or_change_ledger_binding(self):
        record = self.prepare()
        manifest = record["manifest"]
        with_private = {**manifest, "source_path": str(self.source)}
        (self.package(record) / "manifest.json").write_text(json.dumps(with_private), encoding="utf-8")
        with self.assertRaises(ExchangeError):
            self.store.verify(record["id"])
        manifest["files"][0]["path"] = "renamed.bin"
        (self.package(record) / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with self.assertRaises(ExchangeError):
            self.store.verify(record["id"])

    def test_snapshot_write_failure_and_db_failure_clean_up_and_allow_retry(self):
        original_write = exchange.write_private_file
        calls = 0

        def fail_manifest(path, data):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated disk failure")
            return original_write(path, data)

        with mock.patch.object(exchange, "write_private_file", side_effect=fail_manifest):
            with self.assertRaises(CoreError):
                self.prepare()
        self.assertEqual(self.store.list_transfers(), [])
        self.assertEqual(list(self.store.packages.iterdir()), [])
        with mock.patch.object(self.store, "_event", side_effect=ExchangeError("simulated ledger failure")):
            with self.assertRaises(ExchangeError):
                self.prepare()
        self.assertEqual(self.store.list_transfers(), [])
        self.assertEqual(list(self.store.packages.iterdir()), [])
        self.assertEqual(self.prepare()["state"], "prepared")

    def test_post_commit_exception_preserves_package_even_if_cleanup_cannot_read_ledger(self):
        original_db = self.store._db
        for unreadable_cleanup in (False, True):
            with self.subTest(unreadable_cleanup=unreadable_cleanup):
                @contextmanager
                def interrupted(*, write=False):
                    if not write and unreadable_cleanup:
                        raise ExchangeError("cannot establish commit outcome")
                    with original_db(write=write) as db:
                        yield db
                    if write:
                        raise InterruptedError("interrupted after transfer commit")

                key = "committed-" + str(unreadable_cleanup)
                with mock.patch.object(self.store, "_db", interrupted):
                    with self.assertRaises(InterruptedError):
                        self.prepare(key)
                record = next(item for item in self.store.list_transfers() if item["request_key"] == key)
                self.assertEqual(self.store.verify(record["id"])["id"], record["id"])
                self.assertEqual(self.prepare(key)["id"], record["id"])
                self.assertEqual(len(self.store.events(record["id"])), 1)

    def test_materialize_preserves_existing_destination_and_rechecks_copy(self):
        record = self.prepare()
        existing = self.root / "existing"
        existing.mkdir()
        (existing / "mine").write_bytes(b"keep")
        with self.assertRaises(CoreError):
            self.store.materialize(record["id"], existing)
        self.assertEqual((existing / "mine").read_bytes(), b"keep")
        with self.assertRaises(ExchangeError):
            self.store.materialize(record["id"], self.store.directory / "output")
        original_verify = self.store.verify

        def change_after_check(identity):
            result = original_verify(identity)
            self.object(record).write_bytes(b"mutated after verify")
            return result

        destination = self.root / "raced-output"
        with mock.patch.object(self.store, "verify", side_effect=change_after_check):
            with self.assertRaises(CoreError):
                self.store.materialize(record["id"], destination)
        self.assertFalse(destination.exists())

    def test_concurrent_prepare_reuses_record_and_compare_and_swap_has_one_winner(self):
        with ThreadPoolExecutor(max_workers=2) as pool:
            records = list(pool.map(lambda _: self.prepare(), range(2)))
        self.assertEqual(records[0]["id"], records[1]["id"])
        self.assertEqual(len(list(self.store.packages.iterdir())), 1)
        identity = records[0]["id"]

        def update(index):
            try:
                self.store.update(identity, expected_states=["prepared"], state="planned", plan={"attempt": index})
                return "won"
            except ExchangeConflict:
                return "conflict"

        with ThreadPoolExecutor(max_workers=2) as pool:
            self.assertCountEqual(list(pool.map(update, range(2))), ["won", "conflict"])
        self.assertEqual(len(self.store.events(identity)), 2)
        with self.assertRaises(ExchangeError):
            self.store.update(identity, expected_states=["planned"], state="planned", target={"other": "target"})

    def test_operation_lock_is_per_transfer_and_does_not_hold_database_transaction(self):
        record = self.prepare()
        other = self.prepare("prepare-other")
        with self.store.operation(record["id"]):
            with self.assertRaises(ExchangeConflict):
                with self.store.operation(record["id"]):
                    self.fail("second operation must not enter")
            with self.store.operation(other["id"]):
                self.store.update(other["id"], expected_states=["prepared"], state="planned", plan={"value": 1})
            self.store.update(record["id"], expected_states=["prepared"], state="planned", plan={"value": 2})
        with self.store.operation(record["id"]):
            self.assertEqual(self.store.get(record["id"])["state"], "planned")

    def test_operation_lock_blocks_other_process_and_is_released_on_process_exit(self):
        record = self.prepare()
        script = """
import os, sys
from ortak_kopru.exchange import ExchangeStore, ExchangeConflict
store = ExchangeStore(sys.argv[1], create=False)
try:
    with store.operation(sys.argv[2]):
        os._exit(0)
except ExchangeConflict:
    sys.exit(17)
"""
        environment = {**os.environ, "PYTHONPATH": str(ROOT / "src")}
        args = [sys.executable, "-c", script, str(self.store.directory), record["id"]]
        with self.store.operation(record["id"]):
            result = subprocess.run(args, env=environment, capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 17, result.stderr)
        crashed = subprocess.run(args, env=environment, capture_output=True, text=True, timeout=15)
        self.assertEqual(crashed.returncode, 0, crashed.stderr)
        with self.store.operation(record["id"]):
            pass


if __name__ == "__main__":
    unittest.main()
