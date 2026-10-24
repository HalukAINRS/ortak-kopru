import copy
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
HANDOFF = ROOT / "devir" / "sahit"
spec = importlib.util.spec_from_file_location("handoff_generator", HANDOFF / "generate.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class HandoffBundleTests(unittest.TestCase):
    def test_checked_in_files_match_deterministic_source(self):
        outputs = generator.expected_outputs()
        for filename, expected in outputs.items():
            with self.subTest(filename=filename):
                self.assertEqual((HANDOFF / filename).read_bytes(), expected)

    def test_manifest_hashes_source_repository_files_and_outputs(self):
        source_bytes = (HANDOFF / "source.json").read_bytes()
        source = json.loads(source_bytes)
        manifest = json.loads((HANDOFF / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["source_sha256"], hashlib.sha256(source_bytes).hexdigest())
        self.assertEqual(manifest["source_snapshot_commit"], source["source_snapshot_commit"])
        for filename, digest in manifest["outputs_sha256"].items():
            self.assertEqual(hashlib.sha256((HANDOFF / filename).read_bytes()).hexdigest(), digest)
        for relative, digest in manifest["repo_sources_sha256"].items():
            self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), digest)

    def test_static_html_escapes_untrusted_user_text_and_has_no_external_assets(self):
        source = json.loads((HANDOFF / "source.json").read_text(encoding="utf-8"))
        source["title"] = '<script src="x"></script>'
        source["user_requests"][0]["text"] = '<img src=x onerror="alert(1)">'
        rendered = generator.generated_files(source)["handoff.html"].decode("utf-8")
        self.assertNotIn('<script src="x">', rendered)
        self.assertNotIn('<img src=x', rendered)
        self.assertIn("&lt;script", rendered)
        self.assertIn("&lt;img", rendered)
        self.assertNotRegex(rendered, r"<script\b|<iframe\b|<img\b|<link\b")

    def test_source_keeps_requests_proposals_and_evidence_distinct(self):
        source = json.loads((HANDOFF / "handoff.json").read_text(encoding="utf-8"))
        self.assertTrue(all(item["kind"] == "direct_user_request" for item in source["user_requests"]))
        self.assertTrue(all("classification" in item for item in source["conversation_excerpt"]))
        self.assertIn("hazır/bekliyor", source["prepared_state"])
        self.assertIn("tam ham sohbet", source["scope"]["completeness"].lower())
        self.assertTrue(all(item["state"] == "unverified" for item in source["verified_repository"]["previous_task_references"]))

    def test_old_record_blocks_are_byte_for_byte_unchanged_and_mirror_is_current(self):
        baseline = subprocess.run(
            ["git", "show", "950b76e7be8c1ef1e3cd59e099c5b988971a13f3:kopru.html"],
            cwd=ROOT,
            capture_output=True,
            check=True,
        ).stdout.decode("utf-8")
        current = (ROOT / "kopru.html").read_text(encoding="utf-8")
        pattern = re.compile(r'<article class="kayit(?:\s+[^"]*)?".*?</article>', re.S)
        self.assertEqual(pattern.findall(current), pattern.findall(baseline))

        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "kopru.html"
            subprocess.run(
                [sys.executable, str(ROOT / "kopru_ayna_uret.py"), str(ROOT / "kopru.html"), str(target)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual(target.read_bytes(), (ROOT / "ayna" / "kopru.html").read_bytes())

    def test_topic_navigation_keeps_steering_and_deus_ex_machina_separate(self):
        page = (ROOT / "kopru.html").read_text(encoding="utf-8")
        self.assertIn('<a href="#yonlendirme">Steering</a>', page)
        self.assertIn('<a href="#deus-ex-machina">deus_ex_machina</a>', page)
        self.assertIn('<section id="yonlendirme"', page)
        self.assertIn('<section id="deus-ex-machina"', page)
        self.assertIn("açıkça kabul edene kadar konu taslaktır", page)

    def test_legacy_reader_pending_filter_and_page_check_are_read_only(self):
        from kopru_oku import Ayristirici
        from kopru_yanitla import bekleyenler, kayitlari_oku

        records = kayitlari_oku(str(ROOT / "kopru.html"))
        self.assertGreaterEqual(len(records), 33)
        self.assertEqual(Ayristirici().kayitlar, [])
        pending = bekleyenler(records, "Copilot")
        self.assertTrue(all(record["durum"] == "acik" and "Copilot" in record["kime"] for record in pending))
        result = subprocess.run(
            [sys.executable, str(ROOT / "kopru_ekle.py"), str(ROOT / "kopru.html"), "--kontrol"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("dış yükleme yok", result.stdout)


if __name__ == "__main__":
    unittest.main()
