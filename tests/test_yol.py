"""Açılıştan gerçeğe yol (docs/yol.json): hesaplanan durumlar, ön koşullar, açılışla tutarlılık, belgeler ve çizimler.

Gerçek kayıt ve bozulmuş kopyaları kullanılır; ölçütler depoya karşı hesaplanır, hiçbir dosya yazılmaz.
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
import cizim  # noqa: E402
import okuma_yayini_uret  # noqa: E402
import yol  # noqa: E402


class YolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.yol = json.loads(yol.KAYIT.read_text(encoding="utf-8"))
        cls.acilis = json.loads(acilis.KAYIT.read_text(encoding="utf-8"))
        cls.bulgular = acilis._rafine_bulgulari()

    def denetle(self, kayit, acilis_kaydi=None, bulgular=None):
        return yol.denetle(kayit, acilis_kaydi or self.acilis, bulgular or self.bulgular)

    def adim(self, kayit, kimlik):
        return next(a for a in kayit["adimlar"] if a["kimlik"] == kimlik)

    def acik_kopya(self, *kimlikler):
        """Kaydın, verilen adımları bitmemiş ve kararsız sayılan bir kopyası."""
        kayit = copy.deepcopy(self.yol)
        for kimlik in kimlikler:
            a = self.adim(kayit, kimlik)
            a["olcutler"] = [{"tur": "dosya_var", "yol": "olmayan-dosya.txt"}]
            if a.get("karar"):
                a["karar"]["verildi"] = None
        return kayit

    def test_repository_path_is_consistent_and_documents_are_current(self):
        self.assertEqual(self.denetle(self.yol), [])
        hesap = yol.durumlar(self.yol, self.bulgular)
        for hedef, uretilen in yol.bloklar(self.yol, self.acilis, hesap).items():
            with self.subTest(belge=hedef.name):
                self.assertEqual(acilis.belge_denetle(hedef.name, hedef.read_text(encoding="utf-8"), uretilen), [])

    def test_states_are_computed_from_criteria_not_written(self):
        # Zemin her zaman tamamdır. Öteki adımlar kendi kopyalarında açılıp kapatılır; böylece yol
        # ilerledikçe (bir adım bitince, bir karar verilince) bu sınamanın değişmesi gerekmez.
        self.assertEqual(yol.durumlar(self.yol, self.bulgular)["zemin"]["durum"], "tamam")
        kayit = self.acik_kopya("sinir", "katki-kalibi", "gelen-kutusu", "kapinin-genislemesi")
        hesap = yol.durumlar(kayit, self.bulgular)
        self.assertEqual(hesap["sinir"]["durum"], "karar-bekliyor")
        self.assertEqual(hesap["katki-kalibi"]["durum"], "atilabilir")
        self.assertEqual(hesap["gelen-kutusu"]["durum"], "onkosul-bekliyor")
        self.assertEqual(hesap["kapinin-genislemesi"]["durum"], "ufukta")
        # Ön koşul bitince karar bekleyen adım karar bekler hâle gelir.
        self.adim(kayit, "katki-kalibi")["olcutler"] = [{"tur": "dosya_var", "yol": "kopru.html"}]
        self.assertEqual(yol.durumlar(kayit, self.bulgular)["gelen-kutusu"]["durum"], "karar-bekliyor")
        # Karar verilince adım atılabilir olur; bulgu kapanır ve ölçütler karşılanınca tamam olur.
        self.adim(kayit, "sinir")["karar"]["verildi"] = {"tarih": "2026-10-29", "yanit": "Evet, daraltılsın."}
        self.assertEqual(yol.durumlar(kayit, self.bulgular)["sinir"]["durum"], "atilabilir")
        self.adim(kayit, "sinir")["olcutler"] = [{"tur": "dosya_var", "yol": "kopru.html"}]
        self.assertEqual(yol.durumlar(kayit, self.bulgular)["sinir"]["durum"], "tamam")

    def test_an_opinion_is_shown_but_does_not_decide(self):
        kayit = self.acik_kopya("sinir")
        self.adim(kayit, "sinir")["karar"]["gorus"] = {"kimden": "Sınama", "tarih": "2026-10-28", "oneri": "Önerim: evet.",
                                                      "ozet": "Kısa bir gerekçe.", "gerekce": "Uzun bir gerekçe."}
        self.assertEqual(yol.durumlar(kayit, self.bulgular)["sinir"]["durum"], "karar-bekliyor")
        self.assertEqual(self.denetle(kayit), [])
        metin = yol.BELGE.read_text(encoding="utf-8")
        for a in self.yol["adimlar"]:
            g = (a["karar"] or {}).get("gorus")
            if g and a["karar"]["verildi"] is None:
                with self.subTest(adim=a["kimlik"]):
                    self.assertIn(g["oneri"], metin)
                    self.assertIn(f"Karar yine {a['karar']['kim']}'ta.", metin)
        eksik = copy.deepcopy(kayit)
        del self.adim(eksik, "sinir")["karar"]["gorus"]["gerekce"]
        self.assertTrue(any(h.startswith("sözleşme: $.adimlar[1].karar") for h in self.denetle(eksik)))

    def test_each_criterion_type_reads_the_repository(self):
        bulgular = {"R-01": "düzeltildi", "R-17": "açık"}
        durumlar = [
            ({"tur": "dosya_var", "yol": "kopru.html"}, True),
            ({"tur": "dosya_var", "yol": "olmayan.txt"}, False),
            ({"tur": "dosya_icerir", "yol": "tools/dogrula.py", "desen": "tools/yol.py"}, True),
            ({"tur": "dosya_icermez", "yol": "yerel/kopru_gonder.ps1", "desen": "git add -A"}, False),
            ({"tur": "test_var", "yol": "tests/test_yol.py", "ad": "test_each_criterion_type_reads_the_repository"}, True),
            ({"tur": "test_var", "yol": "tests/test_yol.py", "ad": "test_olmayan"}, False),
            ({"tur": "bulgu_kapali", "kimlik": "R-01"}, True),
            ({"tur": "bulgu_kapali", "kimlik": "R-17"}, False),
            ({"tur": "elle", "aciklama": "x", "en_az": 1, "kanit": []}, False),
            ({"tur": "elle", "aciklama": "x", "en_az": 1, "kanit": ["https://github.com/HalukAINRS/ortak-kopru/issues/30"]}, True),
        ]
        for olcut, beklenen in durumlar:
            with self.subTest(olcut=olcut):
                self.assertEqual(yol.olcut(olcut, bulgular)[0], beklenen)

    def test_prerequisites_must_exist_and_never_loop(self):
        kayit = copy.deepcopy(self.yol)
        self.adim(kayit, "zemin")["onkosul"] = ["yanit-donusu"]
        self.assertIn("adimlar: ön koşullarda döngü var", self.denetle(kayit))
        kayit = copy.deepcopy(self.yol)
        self.adim(kayit, "katki-kalibi")["onkosul"] = ["olmayan-adim"]
        self.assertIn("adimlar[2] katki-kalibi: ön koşul yok (olmayan-adim)", self.denetle(kayit))
        kayit = self.acik_kopya("katki-kalibi")
        self.adim(kayit, "gelen-kutusu")["olcutler"] = [{"tur": "dosya_var", "yol": "kopru.html"}]
        self.assertIn("adimlar[3] gelen-kutusu: tamam görünüyor ama ön koşulu 'katki-kalibi' tamam değil", self.denetle(kayit))

    def test_opening_and_path_must_agree(self):
        # Kısmen işleyen bir ilkenin bütün zorunlu adımları biterse açılış güncellenmek zorunda.
        kayit = copy.deepcopy(self.yol)
        for a in kayit["adimlar"]:
            if 4 in a["ilkeler"]:
                a["olcutler"] = [{"tur": "dosya_var", "yol": "kopru.html"}]
        self.assertIn("4. ilke (Sınır): yoldaki bütün zorunlu adımları tamam; açılıştaki durum 'uygulanıyor' olarak güncellenmeli",
                      self.denetle(kayit))
        # Tam işleyen bir ilkeye açık zorunlu adım bağlanamaz.
        kayit = self.acik_kopya("katki-kalibi")
        self.adim(kayit, "katki-kalibi")["ilkeler"].append(3)
        self.assertIn("3. ilke (Köken ve sahiplik): açılışta tam işliyor ama yolda açık zorunlu adımı var (katki-kalibi)",
                      self.denetle(kayit))
        # Kısmen işleyen her ilkenin yolda bir adımı olmalı.
        kayit = copy.deepcopy(self.yol)
        for a in kayit["adimlar"]:
            a["ilkeler"] = [n for n in a["ilkeler"] if n != 5] or [6]
        self.assertTrue(any(h.startswith("5. ilke (Açık katılım): açılışta 'kısmen' ama yolda zorunlu adımı yok")
                            for h in self.denetle(kayit)))

    def test_links_to_findings_and_scenarios_must_exist(self):
        kayit = copy.deepcopy(self.yol)
        self.adim(kayit, "sinir")["bulgular"] = ["R-99"]
        self.adim(kayit, "sinir")["senaryolar"] = ["S77"]
        hatalar = self.denetle(kayit)
        self.assertIn("adimlar[1] sinir: bulgu rafine kayıtlarında yok (R-99)", hatalar)
        self.assertIn("adimlar[1] sinir: senaryo kaydında yok (S77)", hatalar)

    def test_path_page_answers_nine_questions_per_step_in_plain_words(self):
        metin = yol.BELGE.read_text(encoding="utf-8")
        for a in self.yol["adimlar"]:
            with self.subTest(adim=a["kimlik"]):
                bolum = metin.split(f"### {a['no']}. {a['ad']}", 1)[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
                for etiket in ("**Durum:**", "**Ne?**", "**Neden?**", "**Nerede?**", "**Nereden nereye?**", "**Nasıl?**",
                               "**Ne zaman?**", "**Ne için?**", "**Ne kadar?**", "**Bitince:**"):
                    self.assertIn(etiket, bolum)
        self.assertEqual(yol.okunabilirlik_denetle(self.acilis, metin), [])
        self.assertNotIn("R-17", cizim.cizimsiz(metin))

    def test_three_kinds_of_keyboard_drawings_support_the_content(self):
        metin = yol.BELGE.read_text(encoding="utf-8")
        for tur in ("ressam çizimi", "mimar çizimi", "mühendis çizimi"):
            with self.subTest(tur=tur):
                self.assertIn(tur, metin)
        self.assertGreaterEqual(len(cizim.cizimler(metin)), 4)
        self.assertEqual(cizim.denetle("yol.md", metin), [])
        self.assertIn("ressam çizimi", (ROOT / "docs" / "acilis.md").read_text(encoding="utf-8"))
        govde, _ = okuma_yayini_uret.render(metin)
        self.assertGreaterEqual(govde.count("<pre"), 4)
        kayit = copy.deepcopy(self.yol)
        kayit["cizimler"] = [c for c in kayit["cizimler"] if c["tur"] != "mimar"]
        self.assertIn("cizimler: mimar çizimi yok", self.denetle(kayit))

    def test_drawing_rules(self):
        iyi = "```text\n┌──┐ kapı ▶ köprü · ırmak\n└──┘\n```\n"
        self.assertEqual(cizim.denetle("x", iyi), [])
        self.assertTrue(any("sütun" in h for h in cizim.denetle("x", "```text\n" + "─" * 65 + "\n```\n")))
        self.assertTrue(any("sekme" in h for h in cizim.denetle("x", "```text\na\tb\n```\n")))
        self.assertTrue(any("tek genişlikli" in h for h in cizim.denetle("x", "```text\nkapı 🚪\n```\n")))
        self.assertTrue(any("boşluk" in h for h in cizim.denetle("x", "```text\nkapı \n```\n")))
        self.assertEqual(cizim.cizimsiz("Önce.\n\n" + iyi + "\nSonra.").split(), ["Önce.", "Sonra."])

    def test_tree_drawing_follows_prerequisites(self):
        agac = yol.agac(self.yol, yol.durumlar(self.yol, self.bulgular)).splitlines()
        self.assertTrue(agac[0].lstrip().startswith("(0) Zemin"))
        sira = [satir.split(")")[0].split("(")[-1] for satir in agac]
        self.assertLess(sira.index("2"), sira.index("3"))
        self.assertLess(sira.index("3"), sira.index("4"))
        self.assertLess(sira.index("4"), sira.index("6"))
        self.assertTrue(all(len(satir) <= cizim.EN_GENIS for satir in agac))

    def test_command_line_check_and_state_json(self):
        sonuc = subprocess.run([sys.executable, str(ROOT / "tools/yol.py"), "--check"],
                               capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(sonuc.returncode, 0, sonuc.stdout + sonuc.stderr)
        durum = subprocess.run([sys.executable, str(ROOT / "tools/yol.py"), "--durum"],
                               capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        veri = json.loads(durum.stdout)
        self.assertEqual(veri["zemin"]["durum"], "tamam")
        self.assertIn("olcutler", veri["sinir"])


if __name__ == "__main__":
    unittest.main()
