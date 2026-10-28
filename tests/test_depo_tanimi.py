"""Dokuz koordinatlı depo tanımı: sözleşme, ölçümlerin depoyla eşliği ve sapmanın yakalanması.

Ağ veya sağlayıcı çağrısı yoktur; docs/gecmis/depo-tanimi.json yalnız okunur, kopyası üzerinde oynanır.
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
        kayitli = self.tanim["koordinatlar"]["ne_kadar"]["olcumler"]
        self.assertEqual(set(kayitli), set(self.olcum))
        katilar = set(self.olcum) - depo_tanimi.BUYUYEN - depo_tanimi.BUYUYEN_ZAMAN - depo_tanimi.ANLIK
        self.assertEqual({k: kayitli[k] for k in katilar}, {k: self.olcum[k] for k in katilar})
        self.assertEqual(depo_tanimi.denetle(self.tanim, self.olcum), [])

    def test_new_ledger_records_on_main_do_not_break_the_check_but_shrinking_does(self):
        # Ana dala bot ya da yerel gönderici yeni kayıt ve günlük eklediğinde ilgisiz PR'lar kızarmamalı.
        sonra = dict(self.olcum)
        for anahtar in ("izlenen_dosya", "kopru_kaydi", "acik_durumlu_kayit", "yanit_bagli_kayit",
                        "defter_bayti", "cagri_gunlugu", "cagri_gunlugu_bayti"):
            sonra[anahtar] = self.olcum[anahtar] + 3
        sonra["son_kayit_zamani"] = sonra["defter_son_guncelleme"] = "2026-11-02T08:00:00+00:00"
        self.assertEqual(depo_tanimi.denetle(self.tanim, sonra), [])
        bilgiler = "\n".join(depo_tanimi.buyuyenler(self.tanim, sonra))
        self.assertIn("kopru_kaydi:", bilgiler)
        self.assertIn("son_kayit_zamani:", bilgiler)
        geri = dict(self.olcum, kopru_kaydi=self.olcum["kopru_kaydi"] - 1,
                    son_kayit_zamani="2026-10-01T00:00:00+00:00")
        hatalar = "\n".join(depo_tanimi.denetle(self.tanim, geri))
        self.assertIn("kopru_kaydi: kayıtlı", hatalar)
        self.assertIn("yalnız büyüyebilir", hatalar)
        self.assertIn("geriye gidemez", hatalar)
        yapisal = dict(self.olcum, json_sozlesmesi=self.olcum["json_sozlesmesi"] + 1)
        self.assertIn("json_sozlesmesi", "\n".join(depo_tanimi.denetle(self.tanim, yapisal)))

    def test_everyday_code_and_document_changes_are_information_not_errors(self):
        # Başka bir katılımcının test, satır veya belge eklemesi tanımı bozmaz; tarihli değer korunur.
        sonra = dict(self.olcum)
        for anahtar in depo_tanimi.ANLIK:
            sonra[anahtar] = self.olcum[anahtar] + 7
        sonra["python_satiri"] = self.olcum["python_satiri"] - 40
        self.assertEqual(depo_tanimi.denetle(self.tanim, sonra), [])
        self.assertIn("test_yontemi:", "\n".join(depo_tanimi.buyuyenler(self.tanim, sonra)))
        siniflar = [depo_tanimi.BUYUYEN, depo_tanimi.BUYUYEN_ZAMAN, depo_tanimi.ANLIK]
        for i, a in enumerate(siniflar):
            for b in siniflar[i + 1:]:
                self.assertFalse(a & b)
        self.assertTrue(set().union(*siniflar) <= set(self.olcum))

    def test_ledger_times_stay_valid_after_later_records(self):
        zamanlar = depo_tanimi.defter_zamanlari() | {"2026-11-02T08:00:00+00:00"}
        self.assertEqual(depo_tanimi.denetle(self.tanim, self.olcum, zamanlar), [])
        self.assertIn(self.olcum["ilk_kayit_zamani"], depo_tanimi.defter_zamanlari())

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
        self.assertEqual(depo_tanimi.dayanak_yolu("defter/kopru_ekle.py:32"), ROOT / "defter" / "kopru_ekle.py")
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
        # Düzeltilen ve açık bulgular toplamı aşmaz; kalanlar düzeltilmedi ya da geri çekildi diye kapanmıştır.
        bulgular = [b for yol in sorted((ROOT / "docs" / "gecmis" / "rafine").glob("*.json"))
                    for b in json.loads(yol.read_text(encoding="utf-8"))["findings"]]
        kapanan = sum(1 for b in bulgular if b["resolution"] in ("düzeltilmedi", "geri çekildi"))
        self.assertEqual(self.olcum["rafine_duzeltilen"] + self.olcum["rafine_acik"] + kapanan, self.olcum["rafine_bulgusu"])

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
