"""Depo haritası (docs/harita.json): her dosya tek alanda, eski adlar, künyeler, komutlar ve üretilen belge.

Gerçek harita ve onun bozulmuş kopyaları kullanılır; ağ, sağlayıcı çağrısı ya da dosya yazımı yoktur.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import shlex
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import harita  # noqa: E402


class HaritaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.veri = json.loads(harita.KAYIT.read_text(encoding="utf-8"))
        cls.dosyalar = harita.izlenen_dosyalar()

    def denetle(self, veri, dosyalar=None):
        return harita.denetle(veri, self.dosyalar if dosyalar is None else dosyalar)

    def test_repository_map_is_consistent_and_document_is_current(self):
        self.assertEqual(self.denetle(self.veri), [])
        uretilen = {"harita": harita.acilis._ayir(harita.belge(self.veri))}
        self.assertEqual(harita.acilis.belge_denetle("harita.md", harita.BELGE.read_text(encoding="utf-8"), uretilen), [])

    def test_every_file_belongs_to_exactly_one_area(self):
        for yol in self.dosyalar:
            with self.subTest(yol=yol):
                self.assertEqual(len(harita.alan_bul(self.veri, yol)), 1)
        self.assertIn("yeni-kok-dosyasi.txt: hiçbir alanda değil",
                      self.denetle(self.veri, self.dosyalar + ["yeni-kok-dosyasi.txt"]))
        bozuk = copy.deepcopy(self.veri)
        bozuk["alanlar"][0]["kapsam"].append("kapi.py")
        self.assertIn("kapi.py: birden çok alanda (giris, girisler)", self.denetle(bozuk))

    def test_root_shows_only_entries_pages_ledger_and_area_folders(self):
        kok = {yol.split("/", 1)[0] + ("/" if "/" in yol else "") for yol in self.dosyalar}
        dosyalar = sorted(k for k in kok if not k.endswith("/"))
        self.assertEqual(dosyalar, sorted([
            ".gitattributes", ".gitignore", ".nojekyll", "CITATION.cff", "CONTRIBUTING.md", "README.md",
            "kapi.py", "deus.py", "Kopru_Izle.cmd", "kopru.html",
            "index.html", "acilis.html", "mimari.html", "not-defteri.html", "durum.html", "kaynaklar.html", "okuma.css"]))
        agac = harita._kok_agaci(self.veri)
        for klasor in sorted(k for k in kok if k.endswith("/")):
            with self.subTest(klasor=klasor):
                self.assertIn(klasor, agac)

    def test_described_files_must_exist_and_stay_in_their_area(self):
        bozuk = copy.deepcopy(self.veri)
        alan = next(a for a in bozuk["alanlar"] if a["kimlik"] == "defter")
        alan["dosyalar"].append({"yol": "defter/olmayan.py", "tur": "arac", "ne": "Sınama."})
        alan["dosyalar"].append({"yol": "tools/dogrula.py", "tur": "arac", "ne": "Yanlış alanda."})
        hatalar = self.denetle(bozuk)
        self.assertIn("defter/olmayan.py: tanımlı ama depoda yok", hatalar)
        self.assertIn("tools/dogrula.py: 'defter' alanının kapsamında değil", hatalar)
        self.assertIn("tools/dogrula.py: iki kez tanımlı", hatalar)

    def test_fully_described_areas_reject_undescribed_files(self):
        bozuk = copy.deepcopy(self.veri)
        alan = next(a for a in bozuk["alanlar"] if a["kimlik"] == "araclar")
        alan["dosyalar"] = [d for d in alan["dosyalar"] if d["yol"] != "tools/harita.py"]
        self.assertIn("tools/harita.py: 'araclar' alanında ama tanımı yok", self.denetle(bozuk))

    def test_old_names_resolve_and_never_shadow_a_living_file(self):
        eski = {ad: d["yol"] for _, d in harita.tanimlar(self.veri) for ad in d.get("eski_adlar", [])}
        for ad, yeni in {"kopru_ekle.py": "defter/kopru_ekle.py", "ayarlar-yerel.json": "katilimcilar/ayarlar-yerel.json",
                         "kopru_gonder.ps1": "yerel/kopru_gonder.ps1", "docs/ACILIS.md": "docs/acilis.md",
                         "docs/TEKNIK.md": "docs/teknik/README.md", "docs/GECMIS.md": "docs/gecmis/README.md",
                         "docs/rafine-sorulari.json": "docs/gecmis/simdi-ve-sonrasi.json"}.items():
            with self.subTest(ad=ad):
                self.assertEqual(eski[ad], yeni)
                # Git'in listesine bakılır: Windows'ta dosya sistemi büyük/küçük harfe duyarsızdır ve
                # docs/ACILIS.md sorusu docs/acilis.md'yi bulur; eski ad yine de izlenen bir dosya değildir.
                self.assertNotIn(ad, self.dosyalar)
                self.assertTrue((ROOT / yeni).is_file())
        self.assertTrue(harita.nerede(self.veri, "kopru_ekle.py")[0].startswith("defter/kopru_ekle.py"))
        self.assertTrue(harita.nerede(self.veri, "SIMDI_VE_SONRASI.md")[0].startswith("docs/gecmis/simdi-ve-sonrasi.md"))
        bozuk = copy.deepcopy(self.veri)
        next(d for _, d in harita.tanimlar(bozuk) if d["yol"] == "README.md")["eski_adlar"] = ["kapi.py"]
        self.assertIn("kapi.py: eski ad olarak geçiyor ama hâlâ bir dosya", self.denetle(bozuk))

    def test_commands_and_sources_must_point_at_real_files(self):
        bozuk = copy.deepcopy(self.veri)
        dosya = next(d for _, d in harita.tanimlar(bozuk) if d["yol"] == "defter/kopru_oku.py")
        dosya["calistir"] = "python kopru_oku.py kopru.html --acik"
        dosya["kunye"] = {"sahibi": "Haluk", "hazirlayan": "Sınama", "tarih": "2026-10-28", "kaynaklar": ["yok.json"], "okur": "sınama"}
        hatalar = self.denetle(bozuk)
        self.assertIn("defter/kopru_oku.py: gösterdiği dosya yok (kopru_oku.py)", hatalar)
        self.assertIn("defter/kopru_oku.py: gösterdiği dosya yok (yok.json)", hatalar)

    def test_read_only_commands_run_on_a_fresh_machine(self):
        komutlar = [(d["yol"], d["calistir"]) for _, d in harita.tanimlar(self.veri) if d.get("yan_etkisiz")]
        self.assertGreaterEqual(len(komutlar), 10)
        for yol, komut in komutlar:
            with self.subTest(yol=yol):
                parcalar = shlex.split(komut)
                self.assertEqual(parcalar[0], "python")
                sonuc = subprocess.run([sys.executable, *parcalar[1:]], cwd=ROOT, capture_output=True, text=True,
                                       encoding="utf-8", errors="replace", timeout=180)
                self.assertEqual(sonuc.returncode, 0, sonuc.stdout[-800:] + sonuc.stderr[-800:])

    def test_new_documents_open_with_a_plain_paragraph(self):
        kunyeli = [d["yol"] for _, d in harita.tanimlar(self.veri) if "kunye" in d and d["tur"] == "belge"]
        self.assertIn("docs/acilis.md", kunyeli)
        self.assertIn("docs/harita.md", kunyeli)
        for yol in kunyeli:
            with self.subTest(yol=yol):
                self.assertEqual(harita.sade_paragraf(yol, harita.ilk_paragraf((ROOT / yol).read_text(encoding="utf-8"))), [])
        self.assertTrue(any("kod biçimi" in h for h in harita.sade_paragraf("x", "Bu belge `kod` taşır.")))
        self.assertTrue(any("dosya adı" in h for h in harita.sade_paragraf("x", "Bu belge harita.json dosyasından gelir.")))
        self.assertTrue(any("bir paragrafla açılmalı" in h for h in harita.sade_paragraf("x", "| a | b |")))
        uzun = " ".join(["kelime"] * 31) + "."
        self.assertTrue(any("kelimelik cümle" in h for h in harita.sade_paragraf("x", uzun)))

    def test_repository_can_be_cited(self):
        self.assertEqual(harita.atif_denetle(self.veri), [])
        metin = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        self.assertIn('title: "Ortak Köprü"', metin)
        self.assertIn('repository-code: "https://github.com/HalukAINRS/ortak-kopru"', metin)

    def test_command_line_check_and_lookup(self):
        sonuc = subprocess.run([sys.executable, str(ROOT / "tools/harita.py"), "--check"],
                               capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(sonuc.returncode, 0, sonuc.stdout + sonuc.stderr)
        self.assertIn("alanda", sonuc.stdout)
        bul = subprocess.run([sys.executable, str(ROOT / "tools/harita.py"), "--nerede", "kopru_gonder.ps1"],
                             capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
        self.assertEqual(bul.returncode, 0)
        self.assertIn("yerel/kopru_gonder.ps1", bul.stdout)


if __name__ == "__main__":
    unittest.main()
