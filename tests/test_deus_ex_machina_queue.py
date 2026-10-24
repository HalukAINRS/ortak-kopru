import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # gömülü Python (python314._pth) çalışma dizinini yola eklemez
from deus_ex_machina import task_queue as queue  # noqa: E402


class TaskQueueTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.path = Path(self.temporary.name) / "private" / "tasks.json"
        self.words = "Tam kullanıcı sözü; metin olarak kalmalı."
        self.criteria = ["Kaynak görüldü", "Kullanıcı sonucu kabul etti"]

    def tearDown(self):
        self.temporary.cleanup()

    def create(self, scope="manual_cli", topic="deus_ex_machina", participant="Şahit"):
        return queue.create_task(self.path, self.words, topic, participant, self.criteria, ["README.md"], scope)

    def test_task_contract_and_complete_lifecycle(self):
        task = self.create()
        self.assertEqual(task["original_user_words"], self.words)
        self.assertEqual(task["status"], "planned")
        self.assertEqual(task["approval"]["state"], "pending")
        self.assertEqual(task["evidence_sources"][0]["sha256"], "unknown")

        with self.assertRaises(queue.QueueError):
            queue.approve_task(self.path, task["task_id"], "manual_cli")
        queue.approve_task(self.path, task["task_id"], "manual_cli", confirm_reviewed=True)

        with mock.patch.object(subprocess, "run", side_effect=AssertionError("must not spawn any CLI")) as run:
            started = queue.begin_manual_task(self.path, task["task_id"], confirm_manual_cli=True)
        run.assert_not_called()
        self.assertEqual(started["status"], "running")
        self.assertEqual(started["approval"]["state"], "consumed")
        self.assertEqual(started["result"], None)

        with self.assertRaises(queue.QueueError):
            queue.begin_manual_task(self.path, task["task_id"], confirm_manual_cli=True)
        saved = queue.record_result(self.path, task["task_id"], "Katılımcı önerisi", ["README.md:1"], ["report.txt"])
        self.assertEqual(saved["status"], "unverified")
        self.assertEqual(saved["result"]["classification"], "participant_output_not_user_instruction")
        self.assertEqual(saved["artifact_refs"], ["report.txt"])
        with self.assertRaises(queue.QueueError):
            queue.complete_task(self.path, task["task_id"], self.criteria, confirm_acceptance=False)
        with self.assertRaisesRegex(queue.QueueError, "locally observed"):
            queue.complete_task(self.path, task["task_id"], self.criteria, confirm_acceptance=True)
        with self.assertRaises(queue.QueueError):
            queue.complete_task(self.path, task["task_id"], self.criteria[:1], confirm_acceptance=True)

        with self.assertRaises(queue.QueueError):
            queue.verify_evidence(self.path, task["task_id"], "README.md", "v1", "short", "read", "review", True)
        verified = queue.verify_evidence(
            self.path, task["task_id"], "README.md", "reviewed checkout", "a" * 64,
            "local file read", "acceptance check", confirm_observed=True,
        )
        self.assertEqual(verified["evidence_sources"][0]["evidence_status"], "verified_by_local_operator")
        done = queue.complete_task(self.path, task["task_id"], self.criteria, confirm_acceptance=True)
        self.assertEqual(done["status"], "completed")
        self.assertEqual(done["verification"]["classification"], "local_operator_assertion_not_identity_verified")
        self.assertFalse(done["approval"]["identity_verified"])

    def test_read_only_approval_has_separate_read_only_lifecycle(self):
        task = self.create(scope="read_only")
        queue.approve_task(self.path, task["task_id"], "read_only", confirm_reviewed=True)
        with self.assertRaisesRegex(queue.QueueError, "manual_cli"):
            queue.begin_manual_task(self.path, task["task_id"], confirm_manual_cli=True)
        with mock.patch.object(subprocess, "run", side_effect=AssertionError("must not spawn any CLI")) as run:
            started = queue.begin_read_only_task(self.path, task["task_id"], confirm_read_only_work=True)
        run.assert_not_called()
        self.assertEqual(started["status"], "running")
        self.assertEqual(started["approval"]["state"], "consumed")
        with self.assertRaises(queue.QueueError):
            queue.begin_read_only_task(self.path, task["task_id"], confirm_read_only_work=True)

        saved = queue.record_result(self.path, task["task_id"], "Yerel salt-okunur inceleme sonucu")
        self.assertEqual(saved["status"], "unverified")
        self.assertEqual(saved["result"]["classification"], "local_operator_observation_not_user_instruction")
        queue.verify_evidence(
            self.path, task["task_id"], "README.md", "reviewed checkout", "b" * 64,
            "local file read", "acceptance check", confirm_observed=True,
        )
        done = queue.complete_task(self.path, task["task_id"], self.criteria, confirm_acceptance=True)
        self.assertEqual(done["status"], "completed")

    def test_read_only_begin_rejects_manual_cli_scope(self):
        task = self.create(scope="manual_cli")
        queue.approve_task(self.path, task["task_id"], "manual_cli", confirm_reviewed=True)
        with self.assertRaisesRegex(queue.QueueError, "read_only"):
            queue.begin_read_only_task(self.path, task["task_id"], confirm_read_only_work=True)
        self.assertEqual(queue.list_tasks(self.path)[0]["status"], "planned")

    def test_unknown_and_shell_like_participant_targets_are_rejected(self):
        with self.assertRaises(queue.QueueError):
            self.create(participant="Hacker; rm -rf /")
        with self.assertRaises(queue.QueueError):
            self.create(participant="unregistered")

    def test_topic_filters_are_independent(self):
        first = self.create(topic="Steering")
        second = self.create(topic="deus_ex_machina", participant="Hacker")
        self.assertEqual([task["task_id"] for task in queue.list_tasks(self.path, "Steering")], [first["task_id"]])
        self.assertEqual([task["task_id"] for task in queue.list_tasks(self.path, "deus_ex_machina")], [second["task_id"]])

    def test_queue_lock_blocks_second_writer(self):
        self.path.parent.mkdir(parents=True)
        Path(str(self.path) + ".lock").write_text("busy", encoding="ascii")
        with self.assertRaisesRegex(queue.QueueError, "locked"):
            self.create()
        self.assertFalse(self.path.exists())

    def test_cli_queue_is_local_json_and_does_not_spawn(self):
        with mock.patch.object(subprocess, "run", side_effect=AssertionError("unexpected process launch")) as run:
            with contextlib.redirect_stdout(io.StringIO()) as output:
                code = queue.main([
                    "--queue", str(self.path), "create", "--words", self.words,
                    "--topic", "deus_ex_machina", "--participant", "Gemini",
                    "--criterion", self.criteria[0], "--permission-scope", "read_only",
                ])
        run.assert_not_called()
        self.assertEqual(code, 0)
        task_id = output.getvalue().strip()
        stored = json.loads(self.path.read_text(encoding="utf-8"))["tasks"][0]
        self.assertEqual(stored["task_id"], task_id)
        self.assertEqual(stored["original_user_words"], self.words)


if __name__ == "__main__":
    unittest.main()
