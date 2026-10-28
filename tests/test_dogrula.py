"""Birleşik doğrulama aracının kendi davranışı: durumlar, atlamalar, çıkış kodları."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import dogrula  # noqa: E402


class DogrulaTests(unittest.TestCase):
    def test_check_list_is_unique_and_points_at_existing_files(self):
        adlar = [ad for ad, *_ in dogrula.KONTROLLER]
        self.assertEqual(len(adlar), len(set(adlar)))
        for _ad, _aciklama, komut, _gerekli in dogrula.KONTROLLER:
            for parca in komut:
                if parca.startswith(str(ROOT)):
                    self.assertTrue(Path(parca).is_file(), parca)

    def test_failure_and_skip_statuses_without_running_real_checks(self):
        durum, ozet, cikti = dogrula.calistir("ornek", [sys.executable, "-c", "print('ilk'); print('son satir'); raise SystemExit(3)"], None)
        self.assertEqual(durum, "BAŞARISIZ")
        self.assertEqual(ozet, "son satir")
        self.assertIn("ilk", cikti)
        durum, ozet, _ = dogrula.calistir("sessiz", [sys.executable, "-c", "pass"], None)
        self.assertEqual((durum, ozet), ("TAMAM", "sorunsuz (çıktı yok)"))
        with mock.patch("shutil.which", return_value=None):
            durum, ozet, _ = dogrula.calistir("arac", ["yok-boyle-bir-arac"], "yok-boyle-bir-arac")
        self.assertEqual((durum, ozet), ("ATLANDI", "yok-boyle-bir-arac bulunamadı"))

    def test_command_line_lists_rejects_unknown_and_reports_failures(self):
        liste = subprocess.run([sys.executable, str(ROOT / "tools/dogrula.py"), "--liste"],
                               capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(liste.returncode, 0, liste.stderr)
        self.assertIn("testler", liste.stdout)
        self.assertIn("[pwsh]", liste.stdout)
        bilinmeyen = subprocess.run([sys.executable, str(ROOT / "tools/dogrula.py"), "--sadece", "yok"],
                                    capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(bilinmeyen.returncode, 2)
        self.assertIn("bilinmeyen kontrol: yok", bilinmeyen.stderr)
        sadece = subprocess.run([sys.executable, str(ROOT / "tools/dogrula.py"), "--sadece", "semalar"],
                                capture_output=True, text=True, cwd=ROOT, env={**os.environ, "GITHUB_ACTIONS": "true"})
        self.assertEqual(sadece.returncode, 0, sadece.stdout + sadece.stderr)
        self.assertIn("::group::semalar", sadece.stdout)
        self.assertIn("1 tamam, 0 başarısız, 0 atlandı", sadece.stdout)

    def test_main_exit_code_follows_failures_not_skips(self):
        kontroller = [("a", "", ["x"], None), ("b", "", ["y"], "yok"), ("c", "", ["z"], None)]
        sonuclar = {"a": ("TAMAM", "iyi", ""), "b": ("ATLANDI", "yok bulunamadı", ""), "c": ("BAŞARISIZ", "kötü", "ayrıntı")}
        with mock.patch.object(dogrula, "KONTROLLER", kontroller), \
             mock.patch.object(dogrula, "calistir", side_effect=lambda ad, komut, gerekli: sonuclar[ad]), \
             mock.patch("sys.argv", ["dogrula.py"]), mock.patch("builtins.print") as yazdir:
            self.assertEqual(dogrula.main(), 1)
        satirlar = [args[0] for args, _ in yazdir.call_args_list if args]
        self.assertIn("1 tamam, 1 başarısız, 1 atlandı (b)", satirlar)
        self.assertIn("ayrıntı", satirlar)
        sonuclar["c"] = ("TAMAM", "iyi", "")
        with mock.patch.object(dogrula, "KONTROLLER", kontroller), \
             mock.patch.object(dogrula, "calistir", side_effect=lambda ad, komut, gerekli: sonuclar[ad]), \
             mock.patch("sys.argv", ["dogrula.py"]), mock.patch("builtins.print"):
            self.assertEqual(dogrula.main(), 0)


if __name__ == "__main__":
    unittest.main()
