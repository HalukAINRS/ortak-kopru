"""Açılış kaydı (docs/acilis.json): niyet, beşli ve dörtlü, 20 kesişim, altı ilke, dört yüzün eşliği ve sade açılışın okunabilirliği.

Gerçek kayıt ve sentetik bozulmalar kullanılır; ağ, sağlayıcı veya kanonik defter yazımı yoktur.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import acilis  # noqa: E402
import okuma_yayini_uret  # noqa: E402


class AcilisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.veri = json.loads(acilis.KAYIT.read_text(encoding="utf-8"))
        cls.bulgular = acilis._rafine_bulgulari()
        cls.senaryolar = acilis._senaryolar()

    def denetle(self, veri):
        return acilis.denetle(veri, self.bulgular, self.senaryolar)

    def test_repository_record_and_all_three_faces_agree(self):
        self.assertEqual(self.denetle(self.veri), [])
        for yol, uretilen in acilis.bloklar(self.veri).items():
            with self.subTest(yuz=yol.name):
                self.assertEqual(acilis.belge_denetle(yol.name, yol.read_text(encoding="utf-8"), uretilen), [])

    def test_intent_is_carried_verbatim_with_owner_and_time(self):
        soz = self.veri["niyet"]["soz"]
        self.assertTrue(soz.startswith("Bu GitHub Reposu'nun Niyeti = Dış Dünya (Web) ile Yerel (Bilgisayarım)"))
        self.assertEqual(self.veri["niyet"]["sahibi"], "Haluk")
        for yol in (ROOT / "README.md", ROOT / "docs" / "WEB_GIRISI.md", ROOT / "docs" / "ACILIS.md"):
            with self.subTest(yuz=yol.name):
                self.assertIn(soz, yol.read_text(encoding="utf-8"))
        self.assertIn("28 Ekim 2026", acilis.readme_blogu(self.veri))

    def test_five_and_four_are_complete_disjoint_and_all_twenty_crossings_asked_once(self):
        self.assertEqual(set(acilis.BESLI) & set(acilis.DORTLU), set())
        self.assertEqual(len(set(acilis.BESLI + acilis.DORTLU)), 9)
        bozuk = copy.deepcopy(self.veri)
        bozuk["kesisimler"][1] = dict(bozuk["kesisimler"][0])
        hatalar = self.denetle(bozuk)
        self.assertIn("kesisimler: ne × nereye sorulmamış", hatalar)
        self.assertIn("kesisimler: ne × nereden birden çok kez sorulmuş", hatalar)
        bozuk = copy.deepcopy(self.veri)
        bozuk["gruplar"]["kapi"]["sorular"] = ["ne", "nerede", "nasil", "ne_zaman", "neden"]
        self.assertTrue(any(h.startswith("gruplar.kapi") for h in self.denetle(bozuk)))

    def test_six_principles_each_join_gate_and_passage_and_together_cover_nine(self):
        bozuk = copy.deepcopy(self.veri)
        bozuk["ilkeler"][2]["sorular"] = ["nereden", "neden"]
        self.assertIn("ilkeler[3]: en az bir kapı (beşli) ve bir geçiş (dörtlü) sorusunu bağlamalı", self.denetle(bozuk))
        bozuk = copy.deepcopy(self.veri)
        for ilke in bozuk["ilkeler"]:
            ilke["sorular"] = [k for k in ilke["sorular"] if k != "neden"] + (["nereye"] if ilke["sorular"] == ["nasil", "ne_zaman", "neden"] else [])
        self.assertIn("ilkeler: 'neden' hiçbir ilkede geçmiyor", self.denetle(bozuk))
        bozuk = copy.deepcopy(self.veri)
        bozuk["ilkeler"][0]["no"], bozuk["ilkeler"][1]["no"] = 2, 1
        self.assertIn("ilkeler: numaralar 1'den 6'ya sırayla olmalı", self.denetle(bozuk))
        bozuk = copy.deepcopy(self.veri)
        bozuk["ilkeler"] = bozuk["ilkeler"][:5]
        self.assertTrue(any("en az 6 öğe" in h for h in self.denetle(bozuk)))

    def test_distance_must_be_written_and_linked_to_open_work(self):
        bozuk = copy.deepcopy(self.veri)
        del bozuk["ilkeler"][0]["eksik"]
        self.assertIn("ilkeler[1]: 'kısmen' durumunda eksik yazılmalı", self.denetle(bozuk))
        bozuk = copy.deepcopy(self.veri)
        bozuk["ilkeler"][2]["senaryolar"] = ["S02"]
        self.assertIn("ilkeler[3]: uygulanan ilke açık bulgu veya senaryoya bağlanmamalı", self.denetle(bozuk))
        bozuk = copy.deepcopy(self.veri)
        bozuk["ilkeler"][1]["senaryolar"] = ["S77"]
        bozuk["ilkeler"][1]["dayanaklar"] = ["olmayan/dosya.py"]
        hatalar = self.denetle(bozuk)
        self.assertIn("ilkeler[2].senaryolar: senaryo kaydında yok S77", hatalar)
        self.assertIn("ilkeler[2].dayanaklar: depoda yok (olmayan/dosya.py)", hatalar)

    def test_closing_a_linked_finding_forces_the_principle_to_be_rewritten(self):
        kapanmis = dict(self.bulgular, **{"R-17": "düzeltildi"})
        hatalar = acilis.denetle(self.veri, kapanmis, self.senaryolar)
        self.assertIn("ilkeler[2].bulgular: R-17 kapanmış (düzeltildi); ilkenin durumu yeniden yazılmalı", hatalar)
        self.assertIn("ilkeler[4].bulgular: R-17 kapanmış (düzeltildi); ilkenin durumu yeniden yazılmalı", hatalar)

    def test_faces_drift_is_detected_and_regenerated(self):
        uretilen = acilis.bloklar(self.veri)[ROOT / "README.md"]
        metin = (ROOT / "README.md").read_text(encoding="utf-8")
        bozuk = metin.replace("**Karşılıklılık.**", "**Karşılıklılk.**", 1)
        self.assertIn("README.md: 'acilis' bloğu açılış kaydıyla uyumsuz", acilis.belge_denetle("README.md", bozuk, uretilen))
        self.assertEqual(acilis.belge_guncelle(bozuk, uretilen), metin)
        eksik = metin.replace("<!-- uretilen:acilis -->", "", 1)
        self.assertIn("README.md: 'acilis' bloğunun işaretleri yok", acilis.belge_denetle("README.md", eksik, uretilen))

    def test_web_block_stays_inside_the_reader_subset_and_hides_markers(self):
        uretilen = acilis.bloklar(self.veri)[ROOT / "docs" / "WEB_GIRISI.md"]["acilis"]
        govde, _ = okuma_yayini_uret.render("<!-- uretilen:acilis -->\n" + uretilen + "<!-- /uretilen:acilis -->\n")
        self.assertNotIn("&lt;!--", govde)
        self.assertEqual(govde.count("<li>"), 6)
        self.assertIn("<strong>Niyet</strong>", govde)

    def test_matrix_has_five_rows_and_four_columns(self):
        satirlar = acilis.matris(self.veri).strip().splitlines()
        self.assertEqual(len(satirlar), 2 + 5)
        self.assertTrue(all(satir.count(" | ") == 4 for satir in satirlar[2:]))

    def test_first_contact_pages_pass_the_readability_check(self):
        self.assertEqual(acilis.okunabilirlik_denetle(self.veri), [])
        acilis_metni = (ROOT / "docs" / "ACILIS.md").read_text(encoding="utf-8")
        for yasak in ("`", "R-17", "S09", ".py", ".json"):
            with self.subTest(yasak=yasak):
                self.assertNotIn(yasak, acilis_metni)
        self.assertNotIn("|", acilis_metni, "sade açılış belgesi tablo taşımaz")

    def test_readability_rejects_code_files_ids_and_unexplained_jargon(self):
        terimler = [madde["terim"] for madde in self.veri["sozluk"]]
        temiz = "Bu yer bir kapıdır. Dosyalar buradan geçer."
        self.assertEqual(acilis.okunabilirlik("örnek", temiz, terimler), [])
        hatalar = acilis.okunabilirlik("örnek", "Kapıyı `kapi.py` açar.", terimler)
        self.assertTrue(any("kod biçimi" in h for h in hatalar), hatalar)
        hatalar = acilis.okunabilirlik("örnek", "Ayrıntı docs/kapi.json içinde.", terimler)
        self.assertTrue(any("dosya adı" in h for h in hatalar), hatalar)
        hatalar = acilis.okunabilirlik("örnek", "Bu iş 47066cc ile geldi.", terimler)
        self.assertTrue(any("commit kimliği" in h for h in hatalar), hatalar)
        for kimlik in ("R-17", "S09", "k-0179"):
            with self.subTest(kimlik=kimlik):
                hatalar = acilis.okunabilirlik("örnek", f"Açık iş {kimlik} olarak duruyor.", terimler)
                self.assertTrue(any("iç kimlik" in h for h in hatalar), hatalar)
        hatalar = acilis.okunabilirlik("örnek", "Her gönderimde CI çalışır.", terimler)
        self.assertTrue(any("'CI'" in h for h in hatalar), hatalar)
        # Sözlükte açıklanan terim serbesttir; açıklama kalkarsa yeniden yakalanır.
        self.assertEqual(acilis.okunabilirlik("örnek", "Bir Issue yazın.", terimler), [])
        self.assertTrue(acilis.okunabilirlik("örnek", "Bir Issue yazın.", [t for t in terimler if t != "Issue"]))

    def test_readability_limits_sentence_length_but_not_the_quoted_intent(self):
        uzun = " ".join(["kelime"] * (acilis.EN_UZUN_CUMLE + 1)) + "."
        hatalar = acilis.okunabilirlik("örnek", uzun, [])
        self.assertTrue(any("kelimelik cümle" in h for h in hatalar), hatalar)
        orta = ". ".join([" ".join(["kelime"] * (acilis.ORTALAMA_CUMLE + 2))] * 3) + "."
        self.assertTrue(any("ortalama cümle" in h for h in acilis.okunabilirlik("örnek", orta, [])))
        alinti = "Niyet şöyle yazıldı: “" + " ".join(["söz"] * 60) + "” Kısa bir cümle."
        self.assertEqual(acilis.okunabilirlik("örnek", alinti, []), [])

    def test_opening_must_point_to_technical_and_history_pages(self):
        terimler = [madde["terim"] for madde in self.veri["sozluk"]]
        metin = "Bu yer bir kapıdır. Teknik konular [teknik ayrıntılar](TEKNIK.md) sayfasında."
        hatalar = acilis.okunabilirlik("örnek", metin, terimler, ayrim_bagi=True)
        self.assertEqual(hatalar, ["örnek: geçmiş işler sayfasına (GECMIS.md) bağlantı yok"])
        metin += " Eski işler [geçmiş işler](docs/GECMIS.md) sayfasında."
        self.assertEqual(acilis.okunabilirlik("örnek", metin, terimler, ayrim_bagi=True), [])
        for sayfa in ("TEKNIK.md", "GECMIS.md"):
            with self.subTest(sayfa=sayfa):
                self.assertTrue((ROOT / "docs" / sayfa).is_file())

    def test_readme_moves_technical_and_historical_sections_out(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        basliklar = [satir[3:] for satir in readme.splitlines() if satir.startswith("## ")]
        self.assertEqual(basliklar, ["Buradan başlayın"])
        teknik = (ROOT / "docs" / "TEKNIK.md").read_text(encoding="utf-8")
        gecmis = (ROOT / "docs" / "GECMIS.md").read_text(encoding="utf-8")
        for baslik in ("## Köprü dosyaları", "## Yerleştirme", "## Otomasyon", "## Bakım ve doğrulama"):
            with self.subTest(teknik=baslik):
                self.assertIn(baslik, teknik)
        for baslik in ("## Açılışa giden yol", "## Değişiklik geçmişi", "## deus_ex_machina ve Şaman devri"):
            with self.subTest(gecmis=baslik):
                self.assertIn(baslik, gecmis)

    def test_command_line_check(self):
        sonuc = subprocess.run([sys.executable, str(ROOT / "tools/acilis.py"), "--check"],
                               capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(sonuc.returncode, 0, sonuc.stdout + sonuc.stderr)
        self.assertIn("20 kesişim ve 6 ilke", sonuc.stdout)


if __name__ == "__main__":
    unittest.main()
