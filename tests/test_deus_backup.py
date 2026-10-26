"""Private backup regressions with synthetic data and no installed services."""
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
import hashlib
import json
import os
from pathlib import Path
import shutil
import sqlite3
import stat
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ortak_kopru import backup, local_files
from ortak_kopru.backup import BackupError, create_backup, restore_backup, verify_backup
from ortak_kopru.core import Store
from ortak_kopru.local_files import LocalFileError, copy_verified_file, file_record, new_private_directory, read_regular_file, write_private_file


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-backup-", dir="/tmp" if os.name != "nt" else None)
        self.root = Path(self.tmp.name)
        self.state = self.root / "state"
        self.store = Store(self.state)
        self.output = self.root / "backup"
        self.restored = self.root / "restored"
        self.source = self.root / "seçili kaynak.txt"
        self.source.write_bytes("Özgün kaynak.\nBu metin görev yetkisi değildir.\n".encode("utf-8"))
        self.counter = 0

    def tearDown(self):
        self.tmp.cleanup()

    def key(self):
        self.counter += 1
        return f"fixture-{self.counter}"

    def create_task(self, **changes):
        args = {
            "original_words": "  Kullanıcının özgün sözleri.\n",
            "authority": {"actor": "fixture owner", "source": "current synthetic input", "scope": "selected fixture only"},
            "criteria": ["Özgün kaynak aynı", "Sonuç denetlendi"],
            "request_key": self.key(), "sources": [str(self.source)],
        }
        args.update(changes)
        return self.store.create_task(**args)

    def populated_history(self):
        original = self.create_task(request_key="original-create")
        artifact = self.root / "çıktı.bin"
        artifact.write_bytes(b"\x00\xffactual output bytes\r\n")
        task = original
        for index in range(2):
            if index:
                task = self.store.revise_task(task["id"], "Kullanıcının açık düzeltmesi.", 1, self.key())
            session = f"session-{index}"
            task = self.store.assign(task["id"], "fixture participant", session, task["revision"], self.key(), expected_active_attempt_id=task["active_attempt_id"])
            self.store.receive(task["active_attempt_id"], session, self.key())
            task = self.store.submit_result(task["active_attempt_id"], session, f"Sonuç {index}", [str(artifact)], self.key())
        checks = [{"criterion_id": criterion["id"], "result_id": task["current_result_id"], "passed": True,
                   "evidence": "synthetic test receipt", "verifier": "fixture owner"} for criterion in task["criteria"]]
        task = self.store.verify_task(task["id"], checks, task["revision"], self.key())
        return original, task, artifact

    def reseal(self, mutate=None):
        """Recompute checksums so schema/reference tests reach deeper checks."""
        manifest = json.loads((self.output / "manifest.json").read_text(encoding="utf-8"))
        manifest["database"] = file_record(self.output / "deus.sqlite3", relative_path="deus.sqlite3")
        if mutate:
            mutate(manifest)
        data = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
        (self.output / "manifest.json").write_bytes(data)
        (self.output / "manifest.sha256").write_text(hashlib.sha256(data).hexdigest() + "\n", encoding="ascii")

    def assert_no_staging(self):
        self.assertEqual(list(self.root.glob(".deus-stage-*")), [])

    def symlink(self, source, destination, directory=False):
        try:
            destination.symlink_to(source, target_is_directory=directory)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f"This test account cannot create a symlink: {exc}")

    def test_round_trip_preserves_history_checks_retries_and_exact_bytes(self):
        original, current, artifact = self.populated_history()
        source_bytes, artifact_bytes = self.source.read_bytes(), artifact.read_bytes()
        events = self.store.events()
        self.source.unlink()
        artifact.unlink()
        orphan = hashlib.sha256(b"unreferenced").hexdigest()
        (self.state / "objects" / orphan).write_bytes(b"unreferenced")
        (self.state / "objects" / ".snapshot-interrupted").write_bytes(b"partial")
        (self.state / "broker.token").write_text("synthetic token excluded", encoding="utf-8")

        manifest = create_backup(self.state, self.output)
        self.assertEqual(verify_backup(self.output), manifest)
        self.assertEqual(manifest["counts"], {"tasks": 1, "events": len(events), "results": 2, "objects": 2})
        self.assertEqual(manifest["integrity"], "sha256_not_authentication")
        self.assertFalse((self.output / "broker.token").exists())
        self.assertFalse((self.output / "objects" / orphan).exists())
        self.assertEqual(len(list((self.output / "objects").iterdir())), 2)
        self.assertEqual(restore_backup(self.output, self.restored), manifest)
        restored = Store(self.restored)
        self.assertEqual(restored.get_task(current["id"]), current)
        self.assertEqual(restored.events(), events)
        self.assertEqual(restored.context_bundle(current["id"])["sources"][0]["text"].encode("utf-8"), source_bytes)
        self.assertEqual((self.restored / current["results"][0]["artifacts"][0]["snapshot"]).read_bytes(), artifact_bytes)
        self.store = restored
        self.assertEqual(self.create_task(request_key="original-create"), original)
        self.assertEqual(restored.get_task(current["id"])["status"], "completed")
        self.assertEqual({path.name for path in self.restored.iterdir()}, {"deus.sqlite3", "objects"})

    def test_empty_store_round_trip_is_valid(self):
        manifest = create_backup(self.state, self.output)
        self.assertEqual(manifest["objects"], [])
        restore_backup(self.output, self.restored)
        self.assertEqual(Store(self.restored).list_tasks(), [])

    def test_wal_backup_includes_committed_state_and_excludes_active_write(self):
        self.create_task()
        with closing(sqlite3.connect(self.store.path)) as writer:
            self.assertEqual(writer.execute("PRAGMA journal_mode=WAL").fetchone()[0], "wal")
            committed = self.create_task(original_words="Committed through WAL", request_key="wal-committed")
            writer.execute("BEGIN IMMEDIATE")
            writer.execute("UPDATE tasks SET original_words='not committed' WHERE id=?", (committed["id"],))
            try:
                manifest = create_backup(self.state, self.output)
            finally:
                writer.rollback()
        self.assertEqual(manifest["counts"]["tasks"], 2)
        self.assertFalse((self.output / "deus.sqlite3-wal").exists())
        self.assertFalse((self.output / "deus.sqlite3-shm").exists())
        restore_backup(self.output, self.restored)
        self.assertEqual(Store(self.restored).get_task(committed["id"]), committed)

    def test_concurrent_writer_after_snapshot_cannot_change_object_selection(self):
        first = self.create_task()
        copying, written = threading.Event(), threading.Event()
        real_copy = backup.copy_verified_file

        def writer():
            if not copying.wait(5):
                raise AssertionError("backup did not reach object copy")
            later_source = self.root / "later.txt"
            later_source.write_bytes(b"later source")
            later = Store(self.state).create_task("later task", first["authority"], ["later criterion"], "later-create", [str(later_source)])
            written.set()
            return later

        def concurrent_copy(*args, **kwargs):
            copying.set()
            self.assertTrue(written.wait(5))
            return real_copy(*args, **kwargs)

        with ThreadPoolExecutor(max_workers=1) as pool:
            future = pool.submit(writer)
            with patch.object(backup, "copy_verified_file", side_effect=concurrent_copy):
                manifest = create_backup(self.state, self.output)
            later = future.result(timeout=5)
        self.assertEqual(len(self.store.list_tasks()), 2)
        self.assertEqual(manifest["counts"]["tasks"], 1)
        self.assertEqual(manifest["counts"]["objects"], 1)
        restore_backup(self.output, self.restored)
        self.assertEqual([task["id"] for task in Store(self.restored).list_tasks()], [first["id"]])
        self.assertNotEqual(first["id"], later["id"])

    def test_existing_targets_are_never_changed(self):
        self.create_task()
        create_backup(self.state, self.output)
        before = (self.output / "manifest.json").read_bytes()
        with self.assertRaises(BackupError):
            create_backup(self.state, self.output)
        self.assertEqual((self.output / "manifest.json").read_bytes(), before)
        self.restored.mkdir()
        marker = self.restored / "keep.txt"
        marker.write_bytes(b"keep these existing bytes")
        with self.assertRaises(BackupError):
            restore_backup(self.output, self.restored)
        self.assertEqual(marker.read_bytes(), b"keep these existing bytes")
        self.assertEqual(list(self.restored.iterdir()), [marker])
        self.assert_no_staging()

    def test_two_backups_to_one_new_target_have_exactly_one_winner(self):
        self.create_task()
        barrier = threading.Barrier(2)
        real_publish = local_files._publish_no_replace

        def together(*args):
            barrier.wait(timeout=5)
            return real_publish(*args)

        def attempt():
            try:
                return create_backup(self.state, self.output)
            except BackupError:
                return None

        with patch.object(local_files, "_publish_no_replace", side_effect=together):
            with ThreadPoolExecutor(max_workers=2) as pool:
                results = list(pool.map(lambda _: attempt(), range(2)))
        winners = [item for item in results if item is not None]
        self.assertEqual(len(winners), 1)
        self.assertEqual(verify_backup(self.output), winners[0])
        self.assert_no_staging()

    def test_partial_copy_failure_publishes_nothing_and_retry_succeeds(self):
        self.create_task()

        def interrupted(source, destination, expected, **kwargs):
            with destination.open("xb") as stream:
                stream.write(b"par")
            raise OSError("synthetic disk-full failure")

        with patch.object(backup, "copy_verified_file", side_effect=interrupted):
            with self.assertRaises(BackupError):
                create_backup(self.state, self.output)
        self.assertFalse(self.output.exists())
        self.assert_no_staging()
        self.assertEqual(create_backup(self.state, self.output), verify_backup(self.output))

    def test_corrupt_live_object_refuses_backup_without_poisoning_retry(self):
        task = self.create_task()
        object_path = self.state / task["sources"][0]["snapshot"]
        original = object_path.read_bytes()
        object_path.write_bytes(b"corrupt")
        with self.assertRaises(BackupError):
            create_backup(self.state, self.output)
        self.assertFalse(self.output.exists())
        self.assert_no_staging()
        object_path.write_bytes(original)
        create_backup(self.state, self.output)
        self.assertEqual(verify_backup(self.output)["counts"]["objects"], 1)

    def test_object_corruption_and_missing_objects_reject_restore(self):
        self.create_task()
        manifest = create_backup(self.state, self.output)
        path = self.output / manifest["objects"][0]["path"]
        original = path.read_bytes()
        for changed in (b"x" * len(original), None):
            with self.subTest(changed="missing" if changed is None else "same-size corruption"):
                if changed is None:
                    path.unlink()
                else:
                    path.write_bytes(changed)
                with self.assertRaises(BackupError):
                    restore_backup(self.output, self.restored)
                self.assertFalse(self.restored.exists())

    def test_manifest_and_database_byte_tampering_are_detected(self):
        self.create_task()
        create_backup(self.state, self.output)
        manifest_path = self.output / "manifest.json"
        original = manifest_path.read_bytes()
        manifest_path.write_bytes(original + b" ")
        with self.assertRaises(BackupError):
            verify_backup(self.output)
        manifest_path.write_bytes(original)
        database = self.output / "deus.sqlite3"
        data = database.read_bytes()
        database.write_bytes(data[:-1] + bytes([data[-1] ^ 1]))
        with self.assertRaises(BackupError):
            verify_backup(self.output)

    def test_checksum_does_not_make_unknown_or_incomplete_schema_valid(self):
        for sql in ("UPDATE metadata SET value='999' WHERE key='schema_version'", "DROP TABLE checks"):
            with self.subTest(sql=sql):
                create_backup(self.state, self.output)
                with closing(sqlite3.connect(self.output / "deus.sqlite3")) as db:
                    with db:
                        db.execute(sql)
                self.reseal()
                with self.assertRaises(BackupError):
                    restore_backup(self.output, self.restored)
                self.assertFalse(self.restored.exists())
                shutil.rmtree(self.output)

    def test_source_unknown_schema_is_rejected_without_modifying_source(self):
        with closing(sqlite3.connect(self.store.path)) as db:
            with db:
                db.execute("UPDATE metadata SET value='999' WHERE key='schema_version'")
        before = file_record(self.store.path)
        with self.assertRaises(BackupError):
            create_backup(self.state, self.output)
        self.assertEqual(file_record(self.store.path), before)
        self.assertFalse(self.output.exists())
        self.assert_no_staging()

    def test_foreign_key_corruption_is_rejected_even_after_resealing(self):
        self.create_task()
        create_backup(self.state, self.output)
        with closing(sqlite3.connect(self.output / "deus.sqlite3")) as db:
            with db:
                db.execute("UPDATE sources SET task_id='missing-task'")
        self.reseal()
        with self.assertRaises(BackupError):
            verify_backup(self.output)

    def test_missing_revision_chain_and_changed_original_cannot_be_restored(self):
        task = self.create_task()
        self.store.revise_task(task["id"], "second revision", 1, self.key())
        self.store.revise_task(task["id"], "third revision", 2, self.key())
        for sql in (
            "DELETE FROM revisions",
            "DELETE FROM revisions WHERE revision=2",
            "UPDATE tasks SET revision=4",
            "UPDATE tasks SET original_words='changed original'",
        ):
            with self.subTest(sql=sql):
                create_backup(self.state, self.output)
                with closing(sqlite3.connect(self.output / "deus.sqlite3")) as db:
                    with db:
                        db.execute(sql)
                    self.assertEqual(db.execute("PRAGMA integrity_check").fetchall(), [("ok",)])
                    self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])
                self.reseal()
                with self.assertRaises(BackupError):
                    restore_backup(self.output, self.restored)
                self.assertFalse(self.restored.exists())
                shutil.rmtree(self.output)

    def test_missing_live_revision_is_not_published_as_valid_backup(self):
        self.create_task()
        with closing(sqlite3.connect(self.store.path)) as db:
            with db:
                db.execute("DELETE FROM revisions")
        with self.assertRaises(BackupError):
            create_backup(self.state, self.output)
        self.assertFalse(self.output.exists())
        self.assert_no_staging()

    def test_unreadable_core_json_records_cannot_be_restored(self):
        self.populated_history()
        for sql in (
            "UPDATE tasks SET authority='[]'",
            "UPDATE tasks SET criteria='null'",
            "UPDATE tasks SET criteria='[]'",
            "UPDATE events SET data='null'",
            "UPDATE requests SET response='[]'",
            "UPDATE results SET artifacts='not json'",
            "UPDATE sources SET data='[]'",
        ):
            with self.subTest(sql=sql):
                create_backup(self.state, self.output)
                with closing(sqlite3.connect(self.output / "deus.sqlite3")) as db:
                    with db:
                        db.execute(sql)
                self.reseal()
                with self.assertRaises(BackupError):
                    restore_backup(self.output, self.restored)
                self.assertFalse(self.restored.exists())
                shutil.rmtree(self.output)

    def test_task_attempt_result_and_check_links_are_validated_beyond_sql_foreign_keys(self):
        _, first, _ = self.populated_history()
        second = self.create_task()
        second = self.store.revise_task(second["id"], "second task revision two", 1, self.key())
        second = self.store.assign(second["id"], "second participant", "second session", 2, self.key())
        self.store.receive(second["active_attempt_id"], "second session", self.key())
        second = self.store.submit_result(second["active_attempt_id"], "second session", "second result", [], self.key())
        cases = (
            ("UPDATE tasks SET active_attempt_id=? WHERE id=?", (second["active_attempt_id"], first["id"])),
            ("UPDATE tasks SET current_result_id=? WHERE id=?", (second["current_result_id"], first["id"])),
            ("UPDATE tasks SET current_result_id=? WHERE id=?", (first["results"][0]["id"], first["id"])),
            ("UPDATE results SET attempt_id=? WHERE id=?", (second["active_attempt_id"], first["current_result_id"])),
            ("UPDATE results SET revision=1 WHERE id=?", (first["current_result_id"],)),
            ("UPDATE checks SET task_id=? WHERE result_id=?", (second["id"], first["current_result_id"])),
            ("UPDATE checks SET criterion_id='unknown' WHERE task_id=? AND criterion_id='criterion-1'", (first["id"],)),
            ("DELETE FROM checks WHERE task_id=?", (first["id"],)),
        )
        for sql, parameters in cases:
            with self.subTest(sql=sql):
                create_backup(self.state, self.output)
                with closing(sqlite3.connect(self.output / "deus.sqlite3")) as db:
                    with db:
                        db.execute(sql, parameters)
                    self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])
                self.reseal()
                with self.assertRaises(BackupError):
                    restore_backup(self.output, self.restored)
                self.assertFalse(self.restored.exists())
                shutil.rmtree(self.output)

    def test_every_live_state_and_historical_checks_survive_round_trip(self):
        for wanted in ("ready", "assigned", "running", "awaiting_verification", "blocked", "paused", "cancelled", "completed", "corrected"):
            task = self.create_task()
            if wanted == "ready":
                continue
            task = self.store.assign(task["id"], "fixture participant", wanted, 1, self.key())
            if wanted == "assigned":
                continue
            self.store.receive(task["active_attempt_id"], wanted, self.key())
            if wanted == "running":
                continue
            task = self.store.submit_result(task["active_attempt_id"], wanted, "synthetic result", [], self.key())
            if wanted == "awaiting_verification":
                continue
            check = {"criterion_id": "criterion-1", "result_id": task["current_result_id"], "passed": False,
                     "evidence": "historical synthetic receipt", "verifier": "fixture owner"}
            task = self.store.verify_task(task["id"], [check], 1, self.key())
            if wanted == "paused":
                self.store.control_task(task["id"], "pause", 1, self.key())
            elif wanted == "cancelled":
                self.store.control_task(task["id"], "cancel", 1, self.key())
            elif wanted == "completed":
                self.store.verify_task(task["id"], [{**check, "criterion_id": criterion["id"], "passed": True} for criterion in task["criteria"]], 1, self.key())
            elif wanted == "corrected":
                self.store.revise_task(task["id"], "a later correction retains earlier checks", 1, self.key())
        expected = self.store.list_tasks()
        self.assertEqual({task["status"] for task in expected}, {"ready", "running", "awaiting_verification", "blocked", "paused", "cancelled", "completed"})
        create_backup(self.state, self.output)
        restore_backup(self.output, self.restored)
        restored = Store(self.restored)
        self.assertEqual(restored.list_tasks(), expected)
        self.assertEqual(restored.events(), self.store.events())

    def test_database_reference_traversal_is_rejected_even_after_resealing(self):
        self.create_task()
        create_backup(self.state, self.output)
        with closing(sqlite3.connect(self.output / "deus.sqlite3")) as db:
            reference = json.loads(db.execute("SELECT data FROM sources").fetchone()[0])
            reference["snapshot"] = "../outside.txt"
            with db:
                db.execute("UPDATE sources SET data=?", (json.dumps(reference),))
        self.reseal()
        with self.assertRaises(BackupError):
            verify_backup(self.output)

    def test_manifest_cannot_select_arbitrary_paths_or_wrong_counts(self):
        self.create_task()
        create_backup(self.state, self.output)
        baseline = (self.output / "manifest.json").read_bytes()
        mutations = (
            lambda item: item["database"].update(path="../outside.sqlite3"),
            lambda item: item["objects"][0].update(path="objects/../../outside.txt"),
            lambda item: item["counts"].update(tasks=999),
        )
        for mutate in mutations:
            with self.subTest(mutation=mutate):
                (self.output / "manifest.json").write_bytes(baseline)
                self.reseal(mutate)
                with self.assertRaises(BackupError):
                    verify_backup(self.output)

    def test_unreferenced_extra_backup_file_is_rejected(self):
        self.create_task()
        create_backup(self.state, self.output)
        (self.output / "objects" / ("0" * 64)).write_bytes(b"extra")
        with self.assertRaises(BackupError):
            verify_backup(self.output)

    def test_symlinked_object_is_not_followed(self):
        self.create_task()
        manifest = create_backup(self.state, self.output)
        path = self.output / manifest["objects"][0]["path"]
        target = self.root / "external-copy"
        path.replace(target)
        self.symlink(target, path)
        with self.assertRaises(BackupError):
            verify_backup(self.output)

    def test_private_paths_refuse_git_and_source_nested_destinations(self):
        with self.assertRaises(BackupError):
            create_backup(self.state, self.state / "backup")
        self.assertFalse((self.state / "backup").exists())
        create_backup(self.state, self.output)
        with self.assertRaises(BackupError):
            restore_backup(self.output, self.output / "restore")
        git = self.root / "git"
        (git / ".git").mkdir(parents=True)
        (git / ".git" / "HEAD").write_text("ref: refs/heads/main\n", encoding="ascii")
        with self.assertRaises(BackupError):
            create_backup(self.state, git / "backup")
        with self.assertRaises(BackupError):
            restore_backup(self.output, git / "restore")
        self.assertFalse((git / "backup").exists())
        self.assertFalse((git / "restore").exists())

    def test_symlink_parent_cannot_redirect_private_destination(self):
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        link = self.root / "link"
        self.symlink(elsewhere, link, directory=True)
        with self.assertRaises(BackupError):
            create_backup(self.state, link / "backup")
        self.assertEqual(list(elsewhere.iterdir()), [])

    def test_verify_is_read_only_and_never_adds_sqlite_sidecars(self):
        self.create_task()
        create_backup(self.state, self.output)
        before = {path.relative_to(self.output): (file_record(path), path.stat().st_mtime_ns)
                  for path in self.output.rglob("*") if path.is_file()}
        verify_backup(self.output)
        after = {path.relative_to(self.output): (file_record(path), path.stat().st_mtime_ns)
                 for path in self.output.rglob("*") if path.is_file()}
        self.assertEqual(before, after)

    def test_restore_checks_bytes_again_if_backup_changes_after_verification(self):
        self.create_task()
        manifest = create_backup(self.state, self.output)
        real_copy = backup.copy_verified_file
        object_path = self.output / manifest["objects"][0]["path"]

        def change_after_database_copy(source, destination, expected, **kwargs):
            result = real_copy(source, destination, expected, **kwargs)
            if source.name == "deus.sqlite3":
                object_path.write_bytes(b"x" * object_path.stat().st_size)
            return result

        with patch.object(backup, "copy_verified_file", side_effect=change_after_database_copy):
            with self.assertRaises(BackupError):
                restore_backup(self.output, self.restored)
        self.assertFalse(self.restored.exists())
        self.assert_no_staging()


class LocalFileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="deus-files-", dir="/tmp" if os.name != "nt" else None)
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_target_created_during_build_is_preserved_even_when_empty(self):
        target = self.root / "new"
        with self.assertRaises(LocalFileError):
            with new_private_directory(target) as staging:
                write_private_file(staging / "data", b"ours")
                target.mkdir()
        self.assertTrue(target.is_dir())
        self.assertEqual(list(target.iterdir()), [])
        self.assertEqual(list(self.root.glob(".deus-stage-*")), [])

    def test_copy_fsync_failure_removes_incomplete_file_and_allows_retry(self):
        source, destination = self.root / "source", self.root / "copy"
        source.write_bytes(b"real copied bytes")
        expected = file_record(source)
        with patch.object(local_files.os, "fsync", side_effect=OSError("synthetic flush failure")):
            with self.assertRaises(LocalFileError):
                copy_verified_file(source, destination, expected)
        self.assertFalse(destination.exists())
        self.assertEqual(copy_verified_file(source, destination, expected), expected)
        self.assertEqual(destination.read_bytes(), source.read_bytes())

    def test_copy_hash_mismatch_never_leaves_an_output(self):
        source, destination = self.root / "source", self.root / "copy"
        source.write_bytes(b"unexpected bytes")
        expected = {"bytes": source.stat().st_size, "sha256": "0" * 64}
        with self.assertRaises(LocalFileError):
            copy_verified_file(source, destination, expected)
        self.assertFalse(destination.exists())

    def test_bounded_read_and_new_file_do_not_overwrite(self):
        path = self.root / "bytes"
        write_private_file(path, b"1234")
        self.assertEqual(read_regular_file(path, maximum=4), b"1234")
        with self.assertRaises(LocalFileError):
            read_regular_file(path, maximum=3)
        with self.assertRaises(LocalFileError):
            write_private_file(path, b"other")
        self.assertEqual(path.read_bytes(), b"1234")

    @unittest.skipIf(os.name == "nt", "POSIX mode bits do not describe Windows ACLs")
    def test_new_data_and_parent_directories_are_private_on_posix(self):
        target = self.root / "new-parent" / "destination"
        with new_private_directory(target) as staging:
            write_private_file(staging / "data", b"private")
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(target.parent.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE((target / "data").stat().st_mode), 0o600)


if __name__ == "__main__":
    unittest.main()
