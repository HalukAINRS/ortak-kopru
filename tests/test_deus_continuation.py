"""CLI integration for recovery and file handoff; only synthetic local data."""

from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ortak_kopru.adapters.windows_nt import KernelUnavailable  # noqa: E402
from ortak_kopru.cli import main  # noqa: E402
from ortak_kopru.core import Store  # noqa: E402


def missing_driver(*, strict=False):
    if strict:
        raise KernelUnavailable("synthetic unavailable driver")
    return {"ready": False, "state": "unavailable"}


class ContinuationCLITests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="deus-continuation-", dir="/tmp" if os.name != "nt" else None)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.state = self.root / "state"
        self.store = Store(self.state)
        self.source = self.root / "evidence.bin"
        self.source.write_bytes(b"\x00\xffsynthetic snapshot\r\n")
        self.task = self.store.create_task(
            "Kaynağı koruyarak devam et.",
            {"actor": "Haluk", "source": "Sentetik test", "scope": "Geçici test dosyaları"},
            ["Kaynak baytları korunur"], "create", sources=[self.source],
        )

    def invoke(self, *arguments):
        output = io.StringIO()
        with redirect_stdout(output):
            code = main(list(arguments))
        return code, json.loads(output.getvalue())

    def test_recovery_commands_work_without_driver_and_do_not_change_backend(self):
        backup = self.root / "backup"
        restored = self.root / "restored"
        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=missing_driver):
            code, value = self.invoke("--state-dir", str(self.state), "backup", "--output", str(backup))
            self.assertEqual(0, code, value)
            self.assertEqual("nt-kernel", value["runtime"]["backend"])
            self.assertFalse(value["runtime"]["ready"])
            self.assertEqual("private_data_maintenance", value["operation_scope"])
            code, value = self.invoke("backup-verify", str(backup))
            self.assertEqual(0, code, value)
            self.source.write_bytes(b"changed after backup")
            code, value = self.invoke("--state-dir", str(restored), "restore", str(backup))
            self.assertEqual(0, code, value)
            self.assertFalse(value["runtime"]["kernel_verified"])
            recovered = Store(restored)
            self.assertEqual(self.task, recovered.get_task(self.task["id"]))
            source = self.task["sources"][0]
            self.assertEqual(b"\x00\xffsynthetic snapshot\r\n", (restored / source["snapshot"]).read_bytes())
            before = recovered.export_data()
            code, value = self.invoke("--state-dir", str(restored), "restore", str(backup))
            self.assertEqual(1, code, value)
            after = recovered.export_data()
            self.assertEqual(before["tasks"], after["tasks"])
            self.assertEqual(before["events"], after["events"])
            code, value = self.invoke("--state-dir", str(restored), "assign", self.task["id"],
                                      "--participant", "test", "--session", "test-session",
                                      "--revision", "1", "--request-key", "must-not-assign")
            self.assertEqual(1, code, value)
            self.assertEqual("kernel_unavailable", value["error"]["code"])

    def test_missing_backup_source_does_not_create_empty_state(self):
        missing = self.root / "missing-state"
        target = self.root / "must-not-be-published"
        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=missing_driver):
            code, value = self.invoke("--state-dir", str(missing), "backup", "--output", str(target))
        self.assertEqual(1, code, value)
        self.assertFalse(missing.exists())
        self.assertFalse(target.exists())

    def test_inbox_and_complete_handoff_do_not_create_delivery_receipt(self):
        session = "Özel oturum / fixture"
        task = self.store.assign(self.task["id"], "Test katılımcısı", session, 1, "assign")
        attempt = task["active_attempt_id"]
        prefix = ("--backend", "portable", "--state-dir", str(self.state))
        code, sessions = self.invoke(*prefix, "sessions")
        self.assertEqual(0, code, sessions)
        self.assertEqual(session, sessions["result"]["sessions"][0]["session_id"])
        self.assertFalse(sessions["result"]["sessions"][0]["identity_verified"])
        code, inbox = self.invoke(*prefix, "inbox", "--session", session)
        self.assertEqual(0, code, inbox)
        self.assertEqual(attempt, inbox["result"]["items"][0]["attempt_id"])
        before_events = self.store.events(self.task["id"])
        package = self.root / "handoff"
        code, prepared = self.invoke(*prefix, "handoff", attempt, "--session", session, "--output", str(package))
        self.assertEqual(0, code, prepared)
        manifest = prepared["result"]["manifest"]
        self.assertEqual(attempt, manifest["attempt_id"])
        self.assertFalse(manifest["preparation"]["delivery_receipt"])
        with mock.patch("ortak_kopru.adapters.windows_nt.query_status", side_effect=missing_driver):
            code, verified = self.invoke("handoff-verify", str(package))
        self.assertEqual(0, code, verified)
        self.assertFalse(verified["runtime"]["ready"])
        self.assertEqual(manifest, verified["result"]["manifest"])
        self.assertEqual(before_events, self.store.events(self.task["id"]))
        self.assertEqual("assigned", self.store.get_task(self.task["id"])["attempts"][0]["status"])
        source = self.task["sources"][0]
        self.assertEqual(self.source.read_bytes(), (package / source["snapshot"]).read_bytes())
        self.store.control_task(self.task["id"], "cancel", 1, "cancel")
        code, inbox = self.invoke(*prefix, "inbox", "--session", session)
        self.assertEqual(0, code, inbox)
        self.assertEqual([], inbox["result"]["items"])
        code, value = self.invoke(*prefix, "receive", attempt, "--session", session, "--request-key", "stale-receive")
        self.assertEqual(1, code, value)
        self.assertEqual("conflict", value["error"]["code"])


if __name__ == "__main__":
    unittest.main()
