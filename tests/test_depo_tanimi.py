"""Dokuz koordinatlı depo tanımı: sözleşme, ölçümlerin depoyla eşliği ve sapmanın yakalanması.

Ağ veya sağlayıcı çağrısı yoktur; docs/depo-tanimi.json yalnız okunur, kopyası üzerinde oynanır.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import depo_tanimi  # noqa: E402
import sema_denetle  # noqa: E402

SORULAR = ["Ne?", "Nerede?", "Ne zaman?", "Ne kadar?", "Nereden?", "Neden?", "Nasıl?", "Ne için?", "Nereye?"]


class DepoTanimiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tanim = json.loads(depo_tanimi.TANIM.read_text(encoding="utf-8"))
        cls.olcum = depo_tanimi.olc()

    def test_nine_coordinates_in_order_follow_the_contract(self):
        self.assertEqual(list(self.tanim["koordinatlar"]), list(depo_tanimi.KOORDINATLAR))
        self.assertEqual([k["soru"] for k in self.tanim["koordinatlar"].values()], SORULAR)
        self.assertEqual(sema_denetle.dogrula(sema_denetle.sema_yukle("depo-tanimi"), self.tanim), [])
        for ad, koordinat in self.tanim["koordinatlar"].items():
            with self.subTest(koordinat=ad):
                self.assertTrue(koordinat["yanit"].endswith("."))
                self.assertGreaterEqual(len(koordinat["ogeler"]), 3)

    def test_recorded_measurements_match_the_repository_now(self):
        self.assertEqual(self.tanim["koordinatlar"]["ne_kadar"]["olcumler"], self.olcum)
        self.assertEqual(depo_tanimi.denetle(self.tanim, self.olcum), [])

    def test_drift_in_measurements_paths_and_ledger_times_is_reported(self):
        bozuk = copy.deepcopy(self.tanim)
        bozuk["koordinatlar"]["ne_kadar"]["olcumler"]["kopru_kaydi"] += 1
        bozuk["koordinatlar"]["nasil"]["ogeler"][0]["dayanak"] = "yok/boyle-bir-dosya.py#bolum"
        defter = next(oge for oge in bozuk["koordinatlar"]["ne_zaman"]["ogeler"] if oge.get("dayanak") == "kopru.html")
        defter["zaman"] = "2020-01-01T00:00:00Z"
        hatalar = "\n".join(depo_tanimi.denetle(bozuk, self.olcum))
        self.assertIn("ne_kadar.olcumler.kopru_kaydi: kayıtlı", hatalar)
        self.assertIn("nasil.ogeler[0].dayanak: depoda yok", hatalar)
        self.assertIn("defterdeki zamanlarla eşleşmiyor", hatalar)
        eksik = copy.deepcopy(self.tanim)
        del eksik["koordinatlar"]["nereye"]
        self.assertTrue(depo_tanimi.denetle(eksik, self.olcum)[0].startswith("sözleşme: "))

    def test_reference_paths_ignore_anchors_lines_and_web_addresses(self):
        self.assertEqual(depo_tanimi.dayanak_yolu("README.md#yerleştirme"), ROOT / "README.md")
        self.assertEqual(depo_tanimi.dayanak_yolu("kopru_ekle.py:32"), ROOT / "kopru_ekle.py")
        self.assertIsNone(depo_tanimi.dayanak_yolu("https://github.com/HalukAINRS/ortak-kopru"))

    def test_byte_and_line_measurements_do_not_depend_on_line_endings(self):
        with tempfile.TemporaryDirectory() as tmp:
            lf, crlf = Path(tmp) / "lf.txt", Path(tmp) / "crlf.txt"
            lf.write_bytes("bir\nüç\n".encode())
            crlf.write_bytes("bir\r\nüç\r\n".encode())
            self.assertEqual(depo_tanimi._bayt(lf), depo_tanimi._bayt(crlf))
            self.assertEqual(depo_tanimi._satir(lf), depo_tanimi._satir(crlf))

    def test_ledger_measurements_agree_with_the_ledger_reader(self):
        self.assertEqual(self.olcum["kopru_kaydi"], 179)
        self.assertEqual(self.olcum["ilk_kayit_zamani"], "2026-10-23T22:55:00+03:00")
        self.assertLessEqual(self.olcum["yanit_bagli_kayit"], self.olcum["kopru_kaydi"])
        self.assertEqual(self.olcum["rafine_duzeltilen"] + self.olcum["rafine_acik"], self.olcum["rafine_bulgusu"])

    def test_command_line_check_passes_and_measure_mode_does_not_write(self):
        once = depo_tanimi.TANIM.read_bytes()
        kontrol = subprocess.run([sys.executable, str(ROOT / "tools/depo_tanimi.py"), "--check"],
                                 capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(kontrol.returncode, 0, kontrol.stdout + kontrol.stderr)
        self.assertIn("dokuz koordinat", kontrol.stdout)
        olc = subprocess.run([sys.executable, str(ROOT / "tools/depo_tanimi.py"), "--olc"],
                             capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(olc.returncode, 0, olc.stderr)
        self.assertEqual(json.loads(olc.stdout), self.olcum)
        self.assertEqual(depo_tanimi.TANIM.read_bytes(), once)


if __name__ == "__main__":
    unittest.main()
