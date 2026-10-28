"""Şimdi ve sonrası kaydının (docs/rafine-sorulari.json) denetimleri, hesapları ve belge tabloları.

Sentetik veri ve geçici dizin kullanılır; sağlayıcı, ağ veya kanonik sayfaya yazım yoktur.
"""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import depo_tanimi  # noqa: E402
import rafine_sorulari as rs  # noqa: E402


class GercekKayitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.veri = json.loads(rs.KAYIT.read_text(encoding="utf-8"))
        cls.hesap = rs.hesapla()
        cls.bulgular = rs.bulgulari_oku()
        cls.anahtarlar = set(depo_tanimi.olc())

    def denetle(self, veri):
        return rs.denetle(veri, self.hesap, self.bulgular, self.anahtarlar)

    def test_repository_record_and_document_are_consistent(self):
        self.assertEqual(self.denetle(self.veri), [])
        metin = rs.BELGE.read_text(encoding="utf-8")
        self.assertEqual(rs.belge_denetle(metin, rs.tablolar(self.veri)), [])

    def test_every_scenario_must_say_how_it_is_undone(self):
        bozuk = copy.deepcopy(self.veri)
        del bozuk["sonra"]["senaryolar"][1]["varyantlar"]["nasil.geri_alinir"]
        self.assertIn("sonra.S02: 'nasil.geri_alinir' yanıtlanmalı (her öneri geri alınabilir olmalı)", self.denetle(bozuk))

    def test_variants_must_be_defined_used_and_belong_to_their_root(self):
        bozuk = copy.deepcopy(self.veri)
        bozuk["sorular"][0]["varyantlar"].append({"id": "ne.kullanilmayan", "soru": "?", "anlam": "sınama"})
        bozuk["sonra"]["senaryolar"][0]["varyantlar"]["nereye.tanimsiz"] = "x"
        bozuk["simdi"]["ne"]["ogeler"][0]["varyant"] = "nerede.calisir"
        hatalar = "\n".join(self.denetle(bozuk))
        self.assertIn("ne.kullanilmayan tanımlı ama hiçbir yanıtta kullanılmıyor", hatalar)
        self.assertIn("tanımsız nereye.tanimsiz", hatalar)
        self.assertIn("nerede.calisir bu köke ait değil", hatalar)

    def test_open_findings_must_be_bound_to_a_scenario(self):
        bozuk = copy.deepcopy(self.veri)
        for senaryo in bozuk["sonra"]["senaryolar"]:
            senaryo["kaynak_bulgu"] = [b for b in senaryo["kaynak_bulgu"] if b != "R-19"]
        self.assertIn("sonra: açık bulgu R-19 hiçbir senaryoya bağlı değil", self.denetle(bozuk))
        bozuk["sonra"]["senaryolar"][0]["kaynak_bulgu"] = ["R-99"]
        self.assertIn("sonra.S01.kaynak_bulgu: bulgu kayıtlarında yok R-99", self.denetle(bozuk))

    def test_prerequisites_must_exist_and_have_no_cycle(self):
        bozuk = copy.deepcopy(self.veri)
        bozuk["sonra"]["senaryolar"][0]["onkosul"] = ["S08"]
        self.assertTrue(any("döngü var" in hata for hata in self.denetle(bozuk)))
        bozuk["sonra"]["senaryolar"][0]["onkosul"] = ["S42"]
        self.assertIn("sonra.S01.onkosul: tanımsız S42", self.denetle(bozuk))

    def test_order_follows_prerequisites(self):
        sirali, hatalar = rs.sira(self.veri["sonra"]["senaryolar"])
        self.assertEqual(hatalar, [])
        self.assertEqual(sorted(sirali), sorted(s["id"] for s in self.veri["sonra"]["senaryolar"]))
        for senaryo in self.veri["sonra"]["senaryolar"]:
            for onkosul in senaryo["onkosul"]:
                self.assertLess(sirali.index(onkosul), sirali.index(senaryo["id"]))

    def test_combinations_need_two_roots_and_cover_all_nine(self):
        bozuk = copy.deepcopy(self.veri)
        bozuk["birlesimler"][0]["sorular"] = ["nereden", "nereden"]
        self.assertIn("birlesimler.B01: en az iki farklı kök soru birleşmeli", self.denetle(bozuk))
        bozuk = copy.deepcopy(self.veri)
        bozuk["birlesimler"] = [b for b in bozuk["birlesimler"] if "nasil" not in b["sorular"]]
        self.assertIn("birlesimler: 'nasil' hiçbir birleşimde geçmiyor", self.denetle(bozuk))

    def test_full_nine_summary_does_not_inflate_pair_coverage(self):
        kapsam = rs.kapsam(self.veri)
        self.assertEqual(kapsam["olasi_cift"], 36)
        self.assertEqual(kapsam["dokuzlu_ozet"], 1)
        yalniz_ozet = {"birlesimler": [b for b in self.veri["birlesimler"] if len(b["sorular"]) == 9]}
        self.assertEqual(rs.kapsam(yalniz_ozet)["cift"], 0)
        self.assertLess(kapsam["cift"], 36)

    def test_computed_values_are_dated_observations_not_errors(self):
        degisik = copy.deepcopy(self.veri)
        degisik["hesaplanan"] = {anahtar: "eski" for anahtar in self.hesap}
        self.assertEqual(self.denetle(degisik), [])
        bozuk = copy.deepcopy(self.veri)
        bozuk["sonra"]["senaryolar"][3]["olcumler"] = ["olmayan_olcum"]
        self.assertIn("sonra.S04.olcumler: bilinmeyen ölçüm olmayan_olcum", self.denetle(bozuk))

    def test_document_tables_drift_is_detected_and_regenerated(self):
        uretilen = rs.tablolar(self.veri)
        metin = rs.BELGE.read_text(encoding="utf-8")
        bozuk = metin.replace("| Ne? |", "| Ne?? |", 1)
        self.assertIn("belge: 'karsilastirma' tablosu kayıtla uyumsuz", rs.belge_denetle(bozuk, uretilen))
        self.assertEqual(rs.belge_guncelle(bozuk, uretilen), metin)
        eksik = metin.replace("<!-- uretilen:senaryolar -->", "", 1)
        self.assertIn("belge: 'senaryolar' tablosunun işaretleri yok", rs.belge_denetle(eksik, uretilen))
        self.assertIn("\\|", rs._hucre("a|b"))

    def test_command_line_check_and_order(self):
        kontrol = subprocess.run([sys.executable, str(ROOT / "tools/rafine_sorulari.py"), "--check"],
                                 capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(kontrol.returncode, 0, kontrol.stdout + kontrol.stderr)
        self.assertIn("belgedeki tablolar tutarlı", kontrol.stdout)
        sira = subprocess.run([sys.executable, str(ROOT / "tools/rafine_sorulari.py"), "--sira"],
                              capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(sira.returncode, 0, sira.stderr)
        satirlar = [satir.split()[1] for satir in sira.stdout.splitlines()]
        self.assertLess(satirlar.index("S07"), satirlar.index("S08"))
        self.assertLess(satirlar.index("S03"), satirlar.index("S07"))


class HesapTests(unittest.TestCase):
    def test_call_logs_ledger_copy_share_and_thinned_estimate(self):
        with tempfile.TemporaryDirectory() as tmp:
            dizin = Path(tmp)
            ileti = "## Kullanıcı iletisi\n\n" + "defter " * 100 + "\n\n"
            for ad in ("20261023-210000Z-Claude.md", "20261024-101157Z-Copilot.md"):
                (dizin / ad).write_text("# başlık\n\n## Sonuç\n\nok\n\n## Sistem istemi\n\nsistem\n\n" + ileti
                                        + "## Ham yanıt\n\n{}\n", encoding="utf-8", newline="\r\n")
            (dizin / "README.md").write_text("açıklama", encoding="utf-8")
            (dizin / "atlandi.log").write_text("2026-10-25 11:23:46Z Gemini: yok\n2026-10-25 12:41:50Z Gemini: yok\n", encoding="utf-8")
            olcum = rs.gunlukleri_olc(dizin)
        tek = len(("# başlık\n\n## Sonuç\n\nok\n\n## Sistem istemi\n\nsistem\n\n" + ileti + "## Ham yanıt\n\n{}\n").encode("utf-8"))
        ileti_bayti = len(ileti.encode("utf-8"))
        self.assertEqual(olcum["gunluk_sayisi"], 2)
        self.assertEqual(olcum["gunluk_bayti"], 2 * tek)
        self.assertEqual(olcum["gunluk_ileti_bayti"], 2 * ileti_bayti)
        self.assertEqual(olcum["gunluk_inceltilmis_bayt_tahmini"], 2 * (tek - ileti_bayti + rs.REFERANS_BAYTI))
        self.assertEqual(olcum["gunluk_yazilan_gun"], 2)
        self.assertEqual((olcum["ilk_gunluk_zamani"], olcum["son_gunluk_zamani"]),
                         ("2026-10-23T21:00:00Z", "2026-10-24T10:11:57Z"))
        self.assertEqual((olcum["atlandi_satiri"], olcum["son_atlandi_zamani"]), (2, "2026-10-25T12:41:50Z"))

    def test_unanswerable_addresses_respect_layer_and_ignore_humans(self):
        def kayit(no, kimden, kime, durum="acik", yanit=None):
            return {"id": f"k-{no:04d}", "kimden": kimden, "kime": kime, "durum": durum, "yanit": yanit,
                    "zaman": "2026-10-26T00:00:00+00:00", "konu": "x", "govde": "x", "dayanak": ""}
        kayitlar = [kayit(1, "Sen", "Gemini (Şahit)"), kayit(2, "Sen", "Claude (Hacker)"),
                    kayit(3, "Claude (Hacker)", "Sen, Haluk"), kayit(4, "Sen", "Gemini (Şahit)", durum="kapandi"),
                    kayit(5, "Sen", "Gemini"), kayit(6, "Sen", "Copilot (Şahit)")]
        kimlikler = {("claude", "hacker"), ("gemini", "api")}
        yetimler = rs.yetim_kayitlar(kayitlar, kimlikler)
        self.assertEqual(yetimler, {"copilot (şahit)": {"k-0006"}, "gemini (şahit)": {"k-0001"}})

    def test_configured_routes_include_fallbacks(self):
        kimlikler = rs.yapilandirilmis_kimlikler([ROOT / "ayarlar.json"])
        self.assertIn(("claude", "max"), kimlikler)
        self.assertIn(("claude", "api"), kimlikler)
        self.assertEqual(len(kimlikler), 4)


if __name__ == "__main__":
    unittest.main()
