import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))  # gömülü Python (python314._pth) çalışma dizinini yola eklemez
HANDOFF = ROOT / "devir" / "sahit"
spec = importlib.util.spec_from_file_location("handoff_generator", HANDOFF / "generate.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)

RECORD = re.compile(r'<article class="kayit(?:\s+[^"]*)?".*?</article>', re.S)
LINE_REF = re.compile(r"^`?([\w./-]+\.(?:ps1|py|json|md|cmd|yml)):(\d+)(?:-(\d+))?")
DOC_REF = re.compile(r"`([\w./-]+\.(?:ps1|py|json|md|cmd|yml)):(\d+)(?:-(\d+))?`")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


class HandoffBundleTests(unittest.TestCase):
    def setUp(self):
        self.source = read_json(HANDOFF / "source.json")
        self.manifest = read_json(HANDOFF / "manifest.json")

    def test_checked_in_files_match_deterministic_source(self):
        for filename, expected in generator.expected_outputs().items():
            with self.subTest(filename=filename):
                self.assertEqual(generator.read_lf(HANDOFF / filename), expected)

    def test_manifest_binds_version_date_source_outputs_and_pinned_files(self):
        manifest = self.manifest
        self.assertEqual(manifest["bundle_version"], self.source["bundle_version"])
        self.assertEqual(manifest["prepared_on"], self.source["prepared_on"])
        self.assertEqual(manifest["source_sha256"], hashlib.sha256(generator.read_lf(HANDOFF / "source.json")).hexdigest())
        for filename, digest in manifest["outputs_sha256"].items():
            self.assertEqual(hashlib.sha256(generator.read_lf(HANDOFF / filename)).hexdigest(), digest, filename)
        repository = self.source["verified_repository"]
        self.assertEqual(set(manifest["pinned_sources_sha256"]), set(repository["pinned_repository_files"]))
        self.assertEqual(set(manifest["observed_sources_sha256"]), set(repository["observed_repository_files"]))
        for relative, digest in manifest["pinned_sources_sha256"].items():
            self.assertEqual(hashlib.sha256(generator.read_lf(ROOT / relative)).hexdigest(), digest, relative)
        for digest in manifest["observed_sources_sha256"].values():
            self.assertRegex(digest, r"^[0-9a-f]{64}$")
        expected = hashlib.sha256(generator.stable_json({
            "source": manifest["source_sha256"], "outputs": manifest["outputs_sha256"], "pinned": manifest["pinned_sources_sha256"],
        })).hexdigest()
        self.assertEqual(manifest["bundle_sha256"], expected)

    def test_json_files_validate_against_schemas_and_reject_bad_input(self):
        schema = generator.load_schema("handoff.schema.json")
        self.assertEqual(generator.validate(self.source, schema), [])
        self.assertEqual(read_json(HANDOFF / "handoff.json"), self.source)
        self.assertEqual(generator.validate(self.manifest, generator.load_schema("manifest.schema.json")), [])
        accepted = json.loads(json.dumps(self.source))
        accepted["acceptance"]["accepted"] = True
        accepted["completeness_matrix"][0]["level"] = "tamam"
        del accepted["missing_sources"]
        errors = "\n".join(generator.validate(accepted, schema))
        self.assertIn("$.acceptance.accepted", errors)
        self.assertIn("$.completeness_matrix[0].level", errors)
        self.assertIn("missing missing_sources", errors)
        bad = generator.validate({"a": 1, "c": 2}, {"type": "object", "required": ["b"], "additionalProperties": False,
                                                    "properties": {"a": {"type": "string"}}})
        self.assertEqual(len(bad), 3)

    def test_completeness_missing_work_and_acceptance_are_explicit(self):
        levels = {row["level"] for row in self.source["completeness_matrix"]}
        self.assertEqual(levels, {"kesin", "kısmi", "eksik"})
        priorities = [item["priority"] for item in self.source["open_items"]]
        self.assertEqual(priorities, sorted(set(priorities)))
        self.assertEqual(priorities[0], 1)
        self.assertEqual(self.source["open_items"][0]["id"], "cli-acceptance")
        self.assertIs(self.source["acceptance"]["accepted"], False)
        self.assertTrue(self.source["prepared_state"].startswith("hazır/bekliyor"))
        self.assertTrue(all(item["state"] == "unverified" for item in self.source["verified_repository"]["previous_task_references"]))

    def test_source_keeps_requests_proposals_and_evidence_distinct(self):
        self.assertTrue(all(item["kind"] == "direct_user_request" for item in self.source["user_requests"]))
        self.assertTrue(all("classification" in item for item in self.source["conversation_excerpt"]))
        self.assertIn("tam ham sohbet", self.source["scope"]["completeness"].lower())

    def test_public_package_has_no_secret_like_or_identifier_patterns(self):
        text = "\n".join((HANDOFF / name).read_text(encoding="utf-8") for name in ("source.json", "manifest.json", "README.md", "START_HERE.md"))
        text += (ROOT / "deus_ex_machina" / "SOZLESME.md").read_text(encoding="utf-8")
        sys.path.insert(0, str(ROOT))
        from kopru_ekle import yasak_kontrol
        self.assertEqual(yasak_kontrol(text), [])

    def test_line_references_point_inside_existing_files(self):
        def check(path_text, start, end, origin):
            candidates = [ROOT / path_text, ROOT / "deus_ex_machina" / path_text]
            existing = [candidate for candidate in candidates if candidate.is_file()]
            self.assertTrue(existing, f"{origin}: {path_text} yok")
            total = len(existing[0].read_text(encoding="utf-8").splitlines())
            self.assertLessEqual(int(end or start), total, f"{origin}: {path_text}:{start}-{end} dosya {total} satır")
        rows = self.source["completeness_matrix"] + self.source["known_risks"]
        for row in rows:
            for reference in row["evidence"]:
                match = LINE_REF.match(reference)
                if match:
                    check(*match.groups(), origin=row["id"])
        for document in (HANDOFF / "README.md", ROOT / "deus_ex_machina" / "SOZLESME.md"):
            for match in DOC_REF.finditer(document.read_text(encoding="utf-8")):
                check(*match.groups(), origin=document.name)

    def test_static_html_is_script_free_and_loads_nothing_external(self):
        rendered = (HANDOFF / "handoff.html").read_text(encoding="utf-8")
        self.assertNotRegex(rendered, r"(?i)<(script|iframe|img|link|object|embed|form|base|video|audio|source)\b")
        self.assertNotRegex(rendered, r"(?i)<[^>]*\s(on\w+|src|href|action|srcset|style)\s*=")
        self.assertNotRegex(rendered, r"(?i)url\(|@import|javascript:|http-equiv")
        self.assertIn("<!doctype html>", rendered)

    def test_static_html_escapes_untrusted_user_text(self):
        source = json.loads(json.dumps(self.source))
        source["title"] = '<script src="x"></script>'
        source["user_requests"][0]["text"] = '<img src=x onerror="alert(1)">'
        rendered = generator.generated_files(source)["handoff.html"].decode("utf-8")
        self.assertNotRegex(rendered, r"<script\b|<iframe\b|<img\b|<link\b")
        self.assertIn("&lt;script", rendered)
        self.assertIn("&lt;img", rendered)

    def test_generator_cli_check_and_drift_pass(self):
        check = subprocess.run([sys.executable, str(HANDOFF / "generate.py"), "--check"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
        self.assertIn("bundle_sha256 " + self.manifest["bundle_sha256"][:12], check.stdout)
        drift = subprocess.run([sys.executable, str(HANDOFF / "generate.py"), "--drift"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(drift.returncode, 0, drift.stdout + drift.stderr)
        self.assertIn("informational", drift.stdout)

    def test_page_navigation_keeps_steering_and_deus_ex_machina_separate(self):
        page = (ROOT / "kopru.html").read_text(encoding="utf-8")
        for fragment in ('<a href="#yonlendirme">Steering</a>', '<a href="#deus_ex_machina">deus_ex_machina</a>',
                         '<section id="yonlendirme"', '<section id="deus_ex_machina"'):
            self.assertIn(fragment, page)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("kopru.html#yonlendirme", readme)
        self.assertIn("kopru.html#deus_ex_machina", readme)
        self.assertNotIn("#deus-ex-machina", readme)

    def test_old_record_blocks_are_unchanged_since_base_commit(self):
        base = self.source["main_snapshot_commit"]
        shown = subprocess.run(["git", "show", f"{base}:kopru.html"], cwd=ROOT, capture_output=True)
        if shown.returncode != 0:
            self.skipTest("taban commit okunamadı (sığ klon ya da git güvenli dizin ayarı): " + shown.stderr.decode("utf-8", "replace")[:120])
        baseline = RECORD.findall(shown.stdout.decode("utf-8"))
        current = RECORD.findall((ROOT / "kopru.html").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(baseline), 110)
        self.assertEqual(current[:len(baseline)], baseline)

    def test_existing_bridge_tools_still_work_read_only(self):
        from kopru_oku import Ayristirici
        from kopru_yanitla import bekleyenler, kayitlari_oku

        records = kayitlari_oku(str(ROOT / "kopru.html"))
        self.assertGreaterEqual(len(records), 110)
        self.assertEqual(Ayristirici().kayitlar, [])
        pending = bekleyenler(records, "Copilot")
        self.assertTrue(all(record["durum"] == "acik" and "Copilot" in record["kime"] for record in pending))
        before = (ROOT / "kopru.html").read_bytes()
        check = subprocess.run([sys.executable, str(ROOT / "kopru_ekle.py"), str(ROOT / "kopru.html"), "--kontrol"],
                               cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
        self.assertIn("dış yükleme yok", check.stdout)
        with tempfile.TemporaryDirectory() as directory:
            mirror = Path(directory) / "kopru.html"
            run = subprocess.run([sys.executable, str(ROOT / "kopru_ayna_uret.py"), str(ROOT / "kopru.html"), str(mirror)],
                                 cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertGreater(mirror.stat().st_size, 0)
        self.assertEqual((ROOT / "kopru.html").read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
