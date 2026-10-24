import contextlib
import datetime
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import kopru_yanitla
from ortak_kopru import context
from ortak_kopru.context import ContextError, canonical_bytes, compile_context
from ortak_kopru.reports import build_witness_report, write_witness_report
from ortak_kopru.runs import RunStore, contains_secret, verify_runs


UNKNOWN = sorted(context.UNKNOWN_LAYERS)


def sample_policy():
    return {
        "schema_version": 1,
        "policy_id": "test",
        "sources": [
            {"path": "instructions.md", "role": "application_instruction"},
            {"path": "evidence.html", "role": "untrusted_evidence"},
            {"path": "settings.json", "role": "configuration"},
            {"path": "kopru.html", "role": "untrusted_evidence"},
            {"path": "ayarlar.json", "role": "configuration"},
        ],
        "provider": {
            "requested": "anthropic",
            "model_requested": "fixture-model",
            "reasoning_requested": "none",
            "allowed_providers": [],
            "allowed_models": [],
            "allowed_reasoning": ["none"],
            "allowed_fallbacks": [],
        },
        "permissions": {
            "allow_provider_call": False,
            "allow_network": False,
            "allow_write": False,
            "tools": [],
        },
        "limits": {
            "max_source_bytes": 1024 * 1024,
            "max_rounds": 1,
            "timeout_seconds": 10,
            "max_output_bytes": 8192,
            "max_output_tokens": 100,
            "approval_max_minutes": 30,
        },
        "approvals_required": ["provider_call", "network", "write"],
        "layers": {"visibility": "partial", "strict": False, "accepted_unknown": []},
    }


class ContextFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "instructions.md").write_text("Application instructions", encoding="utf-8")
        (self.root / "evidence.html").write_text("<p>untrusted evidence</p>", encoding="utf-8")
        (self.root / "settings.json").write_text('{"provider":"fixture"}', encoding="utf-8")
        (self.root / "kopru.html").write_text("<p>bridge fixture</p>", encoding="utf-8")
        (self.root / "ayarlar.json").write_text('{"katilimcilar":[]}', encoding="utf-8")
        (self.root / "policy").mkdir()
        self.policy_path = self.root / "policy" / "policy.json"
        self.write_policy(sample_policy())

    def tearDown(self):
        self.temp.cleanup()

    def write_policy(self, value):
        self.policy_path.write_bytes(canonical_bytes(value))

    def compile(self, task="Task supplied by user."):
        return compile_context(self.root, self.policy_path, task, "task.txt")

    def authorized_context(self):
        policy = sample_policy()
        policy["provider"]["allowed_providers"] = ["anthropic"]
        policy["provider"]["allowed_models"] = ["fixture-model"]
        policy["layers"]["accepted_unknown"] = UNKNOWN
        policy["permissions"]["allow_provider_call"] = True
        policy["permissions"]["allow_network"] = True
        self.write_policy(policy)
        compiled, data, policy = self.compile()
        artifact = self.root / "compiled.json"
        artifact.write_bytes(data)
        approval = self.root / "approvals" / "approval.json"
        expiry = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)).isoformat()
        context.create_approval(compiled, policy, self.policy_path, expiry, approval, self.root)
        return compiled, artifact, approval

    def audited_call(self, participant, artifact, approval=None):
        return kopru_yanitla.denetlenebilir_cagir(
            participant,
            artifact,
            approval,
            self.policy_path,
            self.root / "kopru.html",
            self.root / "ayarlar.json",
        )


class ContextTests(ContextFixture):
    def test_repeated_compile_is_byte_identical_and_trust_roles_remain_distinct(self):
        first, first_bytes, _ = self.compile()
        second, second_bytes, _ = self.compile()
        self.assertEqual(first_bytes, second_bytes)
        self.assertEqual(first["context_sha256"], second["context_sha256"])
        payload = json.loads(first["messages"][1]["content"])
        self.assertEqual(payload["user_task"]["role"], "user_task")
        self.assertEqual(payload["sources"]["untrusted_evidence"][0]["content"], "<p>untrusted evidence</p>")
        system = json.loads(first["messages"][0]["content"])
        self.assertEqual(system["application_instructions"][0]["content"], "Application instructions")
        self.assertNotIn("untrusted evidence", first["messages"][0]["content"])
        self.assertEqual(first["layers"]["visibility"], "partial")
        self.assertIn("provider_training", first["layers"]["unknown"])

    def test_source_change_changes_digest(self):
        first, _, _ = self.compile()
        (self.root / "evidence.html").write_text("<p>changed evidence</p>", encoding="utf-8")
        second, _, _ = self.compile()
        self.assertNotEqual(first["context_sha256"], second["context_sha256"])

    def test_crlf_task_file_hashes_raw_source_and_compiles_normalized_messages(self):
        task_path = self.root / "task.txt"
        task_path.write_bytes(b"First line\r\nSecond line\r\n")
        task_text = task_path.read_text(encoding="utf-8")
        compiled, _, _ = compile_context(
            self.root, self.policy_path, task_text, "task.txt", task_is_file=True
        )
        payload = json.loads(compiled["messages"][1]["content"])
        self.assertEqual(payload["user_task"]["content"], "First line\nSecond line\n")
        task_source = next(item for item in compiled["sources"] if item["role"] == "user_task")
        self.assertEqual(task_source["sha256"], context.sha256(task_path.read_bytes()))

    def test_traversal_bad_schema_bad_encoding_and_size_are_rejected(self):
        policy = sample_policy()
        policy["sources"][0]["path"] = "../outside.md"
        with self.assertRaises(ContextError):
            context.validate_policy(policy)
        policy = sample_policy()
        policy["unexpected"] = True
        with self.assertRaises(ContextError):
            context.validate_policy(policy)
        (self.root / "instructions.md").write_bytes(b"\xff")
        with self.assertRaises(ContextError):
            self.compile()
        (self.root / "instructions.md").write_text("x" * 100, encoding="utf-8")
        policy = sample_policy()
        policy["sources"][0]["max_bytes"] = 10
        self.write_policy(policy)
        with self.assertRaises(ContextError):
            self.compile()

    def test_symlink_escape_and_source_change_race_are_rejected(self):
        outside = Path(self.temp.name).parent / (Path(self.temp.name).name + "-outside.txt")
        outside.write_text("outside", encoding="utf-8")
        try:
            try:
                (self.root / "escape.md").symlink_to(outside)
            except (NotImplementedError, OSError):
                pass
            else:
                policy = sample_policy()
                policy["sources"][0] = {"path": "escape.md", "role": "application_instruction"}
                self.write_policy(policy)
                with self.assertRaises(ContextError):
                    self.compile()
        finally:
            outside.unlink(missing_ok=True)

        self.write_policy(sample_policy())
        real_read = context._read_snapshot
        seen = 0

        def race(root, source):
            nonlocal seen
            if source["path"] == "evidence.html":
                seen += 1
                if seen == 2:
                    (self.root / "evidence.html").write_text("<p>raced</p>", encoding="utf-8")
            return real_read(root, source)

        with mock.patch.object(context, "_read_snapshot", side_effect=race):
            with self.assertRaisesRegex(ContextError, "changed"):
                self.compile()

    def test_strict_uncertainty_denied_but_limited_mode_is_visible(self):
        policy = sample_policy()
        policy["layers"]["strict"] = True
        self.write_policy(policy)
        with self.assertRaisesRegex(ContextError, "Strict"):
            self.compile()
        policy["layers"]["accepted_unknown"] = UNKNOWN
        self.write_policy(policy)
        compiled, _, _ = self.compile()
        self.assertEqual(set(compiled["layers"]["accepted_unknown"]), set(UNKNOWN))

    def test_default_policy_denies_provider_approval_and_hash_change_invalidates_approval(self):
        compiled, _, policy = self.compile()
        expiry = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)).isoformat()
        approval_path = self.root / "approvals" / "approval.json"
        with self.assertRaisesRegex(ContextError, "denies"):
            context.create_approval(compiled, policy, self.policy_path, expiry, approval_path, self.root)

        policy = sample_policy()
        policy["provider"]["allowed_providers"] = ["anthropic"]
        policy["provider"]["allowed_models"] = ["fixture-model"]
        policy["layers"]["accepted_unknown"] = UNKNOWN
        policy["permissions"]["allow_provider_call"] = True
        policy["permissions"]["allow_network"] = True
        self.write_policy(policy)
        compiled, _, policy = self.compile()
        approval = context.create_approval(compiled, policy, self.policy_path, expiry, approval_path, self.root)
        self.assertTrue(approval["approved"])
        self.assertTrue(approval["approval_is_local_assertion_not_identity_or_signature"])
        context.verify_approval(compiled, policy, self.policy_path, approval_path, self.root)
        context.consume_approval(approval_path)
        with self.assertRaisesRegex(ContextError, "consumed"):
            context.consume_approval(approval_path)
        (self.root / "evidence.html").write_text("changed", encoding="utf-8")
        with self.assertRaisesRegex(ContextError, "Source changed"):
            context.verify_approval(compiled, policy, self.policy_path, approval_path, self.root)

    def test_pre_call_failure_prevents_provider_adapter_call(self):
        compiled, data, _ = self.compile()
        artifact = self.root / "compiled.json"
        artifact.write_bytes(data)
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir"
        ) as provider_call:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                result = self.audited_call(
                    {"ad": "fixture", "saglayici": "anthropic", "model": "fixture-model"},
                    artifact,
                    None,
                )
        self.assertIsNone(result)
        self.assertIn(compiled["context_sha256"], stdout.getvalue())
        provider_call.assert_not_called()

    def test_unsupported_anthropic_reasoning_is_rejected_before_provider_call(self):
        policy = sample_policy()
        policy["provider"]["requested"] = "anthropic"
        policy["provider"]["model_requested"] = "fixture-model"
        policy["provider"]["reasoning_requested"] = "high"
        policy["provider"]["allowed_providers"] = ["anthropic"]
        policy["provider"]["allowed_models"] = ["fixture-model"]
        policy["provider"]["allowed_reasoning"] = ["high"]
        policy["layers"]["accepted_unknown"] = UNKNOWN
        policy["permissions"]["allow_provider_call"] = True
        policy["permissions"]["allow_network"] = True
        self.write_policy(policy)
        compiled, data, policy = self.compile()
        artifact = self.root / "compiled.json"
        artifact.write_bytes(data)
        expiry = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)).isoformat()
        approval = self.root / "approvals" / "approval.json"
        context.create_approval(compiled, policy, self.policy_path, expiry, approval, self.root)
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir"
        ) as provider_call:
            with self.assertRaisesRegex(ContextError, "does not send a reasoning setting"):
                self.audited_call(
                    {
                        "saglayici": "anthropic",
                        "model": "fixture-model",
                        "dusunme": "high",
                        "anahtar_degiskeni": None,
                    },
                    artifact,
                    approval,
                )
        provider_call.assert_not_called()

    def test_secret_like_outgoing_context_is_blocked_before_provider_call(self):
        policy = sample_policy()
        policy["provider"]["allowed_providers"] = ["anthropic"]
        policy["provider"]["allowed_models"] = ["fixture-model"]
        policy["layers"]["accepted_unknown"] = UNKNOWN
        policy["permissions"]["allow_provider_call"] = True
        policy["permissions"]["allow_network"] = True
        self.write_policy(policy)
        compiled, data, _ = compile_context(
            self.root, self.policy_path, "Handle this token-like text: sk-12345678901234567890"
        )
        artifact = self.root / "compiled.json"
        artifact.write_bytes(data)
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir"
        ) as provider_call:
            with self.assertRaisesRegex(ContextError, "secret-like"):
                self.audited_call(
                    {"saglayici": "anthropic", "model": "fixture-model"},
                    artifact,
                    None,
                )
        provider_call.assert_not_called()

    def test_run_storage_fails_closed_before_call_when_pre_record_is_unwritable(self):
        policy = sample_policy()
        policy["provider"]["allowed_providers"] = ["anthropic"]
        policy["provider"]["allowed_models"] = ["fixture-model"]
        policy["layers"]["accepted_unknown"] = UNKNOWN
        policy["permissions"]["allow_provider_call"] = True
        policy["permissions"]["allow_network"] = True
        self.write_policy(policy)
        compiled, data, policy = self.compile()
        artifact = self.root / "compiled.json"
        artifact.write_bytes(data)
        approvals = self.root / "approvals"
        approvals.mkdir()
        expiry = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)).isoformat()
        approval = approvals / "approval.json"
        context.create_approval(compiled, policy, self.policy_path, expiry, approval, self.root)
        (self.root / "runs").write_text("not a directory", encoding="utf-8")
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir"
        ) as provider_call:
            with self.assertRaises(ContextError):
                self.audited_call(
                    {
                        "ad": "fixture",
                        "saglayici": "anthropic",
                        "model": "fixture-model",
                        "anahtar_degiskeni": None,
                    },
                    artifact,
                    approval,
                )
        provider_call.assert_not_called()

    def test_approved_call_is_recorded_once_and_response_stays_local(self):
        compiled, artifact, approval = self.authorized_context()
        metadata = {
            "request_body_sha256": "a" * 64,
            "observed_model": "fixture-model",
            "reasoning_sent": None,
        }
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir", return_value=("fixture response", {"output": 1}, metadata)
        ) as provider_call:
            run_id = self.audited_call(
                {
                    "saglayici": "anthropic",
                    "model": "fixture-model",
                    "anahtar_degiskeni": None,
                },
                artifact,
                approval,
            )
            with self.assertRaisesRegex(ContextError, "consumed"):
                self.audited_call(
                    {
                        "saglayici": "anthropic",
                        "model": "fixture-model",
                        "anahtar_degiskeni": None,
                    },
                    artifact,
                    approval,
                )
        self.assertIsNotNone(run_id)
        provider_call.assert_called_once()
        events = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted((self.root / "runs").glob(f"{run_id}.*.json"))
        ]
        self.assertEqual([event["status"] for event in events], ["ready", "attempted", "succeeded"])
        public = "".join(event_file.read_text(encoding="utf-8") for event_file in (self.root / "runs").glob("*.json"))
        self.assertNotIn("fixture response", public)
        self.assertIn("fixture response", (self.root / "runs" / "private" / run_id / "raw-0002.json").read_text())

    def test_secret_like_provider_response_and_error_are_not_public(self):
        for response in ("ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012", RuntimeError("HTTP 500: private body")):
            with self.subTest(response_type=type(response).__name__):
                shutil.rmtree(self.root / "approvals", ignore_errors=True)
                compiled, artifact, approval = self.authorized_context()
                if isinstance(response, Exception):
                    mocked = mock.patch.object(kopru_yanitla, "cagir", side_effect=response)
                else:
                    mocked = mock.patch.object(
                        kopru_yanitla,
                        "cagir",
                        return_value=(
                            response,
                            {},
                            {
                                "request_body_sha256": "a" * 64,
                                "observed_model": "fixture-model",
                                "reasoning_sent": None,
                            },
                        ),
                    )
                with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mocked as provider_call:
                    with self.assertRaises(ContextError):
                        self.audited_call(
                            {
                                "saglayici": "anthropic",
                                "model": "fixture-model",
                                "anahtar_degiskeni": None,
                            },
                            artifact,
                            approval,
                        )
                provider_call.assert_called_once()
                public = "".join(path.read_text(encoding="utf-8") for path in (self.root / "runs").glob("*.json"))
                self.assertNotIn(str(response), public)
                private = "".join(
                    path.read_text(encoding="utf-8")
                    for path in (self.root / "runs" / "private").rglob("*.json")
                )
                self.assertIn(str(response), private)

    def test_audited_loop_and_output_budgets_fail_before_repeat_or_publication(self):
        policy = sample_policy()
        policy["provider"]["allowed_providers"] = ["anthropic"]
        policy["provider"]["allowed_models"] = ["fixture-model"]
        policy["layers"]["accepted_unknown"] = UNKNOWN
        policy["permissions"]["allow_provider_call"] = True
        policy["permissions"]["allow_network"] = True
        policy["limits"]["max_rounds"] = 2
        policy["limits"]["max_output_bytes"] = 8
        self.write_policy(policy)
        compiled, data, policy = self.compile()
        artifact = self.root / "compiled.json"
        artifact.write_bytes(data)
        approval = self.root / "approvals" / "approval.json"
        expiry = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)).isoformat()
        context.create_approval(compiled, policy, self.policy_path, expiry, approval, self.root)
        kat = {"saglayici": "anthropic", "model": "fixture-model", "anahtar_degiskeni": None}
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir"
        ) as provider_call:
            with self.assertRaisesRegex(ContextError, "exactly one"):
                self.audited_call(kat, artifact, approval)
        provider_call.assert_not_called()

        # A fresh approval/context permits one call, but an oversized response stays private.
        policy["limits"]["max_rounds"] = 1
        self.write_policy(policy)
        compiled, data, policy = self.compile()
        artifact.write_bytes(data)
        approval = self.root / "approvals" / "oversized.json"
        context.create_approval(compiled, policy, self.policy_path, expiry, approval, self.root)
        response_metadata = {
            "request_body_sha256": "a" * 64,
            "observed_model": "fixture-model",
            "reasoning_sent": None,
        }
        with mock.patch.object(kopru_yanitla, "BURASI", str(self.root)), mock.patch.object(
            kopru_yanitla, "cagir", return_value=("x" * 20, {}, response_metadata)
        ) as provider_call:
            with self.assertRaisesRegex(ContextError, "output-byte budget"):
                self.audited_call(kat, artifact, approval)
        provider_call.assert_called_once()
        public = "".join(path.read_text(encoding="utf-8") for path in (self.root / "runs").glob("*.json"))
        self.assertNotIn("x" * 20, public)
        private = "".join(
            path.read_text(encoding="utf-8") for path in (self.root / "runs" / "private").rglob("*.json")
        )
        self.assertIn("x" * 20, private)

    def test_legacy_fallback_remains_but_audited_fallback_is_never_attempted(self):
        failure = RuntimeError("HTTP 400: unsupported effort")
        response = {"content": [{"type": "text", "text": "OK"}], "usage": {}}
        with mock.patch.object(kopru_yanitla, "http_json", side_effect=[failure, response]) as request:
            answer, _ = kopru_yanitla.cagir("anthropic", "fixture", "", "system", "user", 10, "xhigh")
        self.assertEqual(answer, "OK")
        self.assertEqual(request.call_count, 2)
        with mock.patch.object(kopru_yanitla, "http_json", side_effect=failure) as request:
            with self.assertRaisesRegex(RuntimeError, "HTTP 400"):
                kopru_yanitla.cagir(
                    "anthropic", "fixture", "", "system", "user", 10, "xhigh", allow_fallback=False
                )
        self.assertEqual(request.call_count, 1)

    def test_audited_http_response_body_is_byte_limited(self):
        class FakeResponse:
            def __init__(self):
                self.body = b'{"response":"' + b"x" * 200 + b'"}'

            def __enter__(self):
                return self

            def __exit__(self, *_):
                return False

            def read(self, size=-1):
                result, self.body = self.body[:size], self.body[size:]
                return result

        token = kopru_yanitla.API_RESPONSE_LIMIT.set(32)
        try:
            with mock.patch.object(kopru_yanitla.urllib.request, "urlopen", return_value=FakeResponse()):
                with self.assertRaisesRegex(RuntimeError, "byte limit"):
                    kopru_yanitla.http_json("https://fixture.invalid", {}, {})
        finally:
            kopru_yanitla.API_RESPONSE_LIMIT.reset(token)


class RunAndReportTests(ContextFixture):
    def setUp(self):
        super().setUp()
        self.compiled, _, _ = self.compile()

    def test_exclusive_runs_do_not_overwrite_and_tampering_is_detected(self):
        run_root = self.root / "runs"

        def write_run(_):
            handle = RunStore(run_root).start(self.compiled, {"provider_requested": "fixture"})
            handle.append("attempted", {"request_sha256": "a" * 64})
            handle.append("succeeded", {"response_sha256": "b" * 64})
            return handle.run_id

        with ThreadPoolExecutor(max_workers=8) as pool:
            run_ids = list(pool.map(write_run, range(16)))
        self.assertEqual(len(set(run_ids)), 16)
        self.assertEqual(verify_runs(run_root), [])
        event_file = next(run_root.glob("*.0001.json"))
        event = json.loads(event_file.read_text(encoding="utf-8"))
        event["metadata"]["request_sha256"] = "changed"
        event_file.write_text(json.dumps(event), encoding="utf-8")
        self.assertTrue(any("hash mismatch" in error for error in verify_runs(run_root)))

    def test_sensitive_raw_output_never_appears_in_public_event(self):
        run_root = self.root / "runs"
        handle = RunStore(run_root).start(self.compiled, {"provider_requested": "fixture"})
        secret = "sk-12345678901234567890"
        handle.append("failed", {"error_type": "FixtureError"}, raw={"response": secret})
        public = "".join(path.read_text(encoding="utf-8") for path in run_root.glob("*.json"))
        private = "".join(path.read_text(encoding="utf-8") for path in (run_root / "private").rglob("*.json"))
        self.assertNotIn(secret, public)
        self.assertIn(secret, private)
        self.assertTrue(contains_secret(secret))

    def test_witness_formats_share_sources_and_escape_html(self):
        source_ids = sorted(item["sha256"] for item in self.compiled["sources"])
        report = build_witness_report(
            self.compiled,
            [
                {
                    "provider": "fixture-only",
                    "model": "not-live",
                    "source_ids": source_ids,
                    "output": "<script>alert(1)</script>",
                    "claims": ["fixture claim"],
                    "interpretations": ["fixture interpretation"],
                    "recommendations": ["Option A"],
                    "user_approvals": [],
                    "actions": [],
                }
            ],
            example=True,
        )
        base = self.root / "reports" / "cross"
        json_path, txt_path, html_path = write_witness_report(report, base)
        self.assertEqual(json.loads(json_path.read_text())["source_ids"], source_ids)
        for path in (txt_path, html_path):
            text = path.read_text(encoding="utf-8")
            self.assertTrue(all(item in text for item in source_ids))
        self.assertNotIn("<script>", html_path.read_text(encoding="utf-8"))
        with self.assertRaisesRegex(ContextError, "secret-pattern"):
            build_witness_report(self.compiled, [{"output": "ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012"}])


class LegacyRegressionTests(unittest.TestCase):
    def test_legacy_check_and_pending_list_stay_offline_and_read_only(self):
        repository = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temp:
            page = Path(temp) / "kopru.html"
            shutil.copyfile(repository / "kopru.html", page)
            original = page.read_bytes()
            check = subprocess.run(
                [sys.executable, str(repository / "kopru_ekle.py"), str(page), "--kontrol"],
                check=True,
                capture_output=True,
                text=True,
            )
            pending = subprocess.run(
                [sys.executable, str(repository / "kopru_yanitla.py"), str(page), "--bekleyenler", "Claude"],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn("TAMAM", check.stdout)
            self.assertIsInstance(json.loads(pending.stdout), list)
            self.assertEqual(page.read_bytes(), original)

    def test_context_workflow_is_read_only_and_offline_from_provider_perspective(self):
        repository = Path(__file__).resolve().parents[1]
        workflow = (repository / ".github" / "workflows" / "context-checks.yml").read_text(encoding="utf-8")
        self.assertIn("contents: read", workflow)
        self.assertIn("python -m unittest discover -s tests -v", workflow)
        self.assertNotIn("secrets.", workflow)
        self.assertNotIn("run: python kopru_yanitla.py", workflow)


if __name__ == "__main__":
    unittest.main()
