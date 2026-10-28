"""Dönüşüm yolu (docs/donusum.json): ölçütler, durumlar, prova, bekleyen önerilerin çözümlemesi ve belgeler.

Git'e bakan ölçütler geçici, sentetik bir depoda sınanır; gerçek ana dala, ağa ya da sağlayıcıya dokunulmaz.
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

import cizim  # noqa: E402
import donusum  # noqa: E402

ORTAM = {**os.environ, "GIT_AUTHOR_NAME": "Sınama", "GIT_AUTHOR_EMAIL": "test@example.invalid",
         "GIT_COMMITTER_NAME": "Sınama", "GIT_COMMITTER_EMAIL": "test@example.invalid",
         "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}


class SentetikDepo:
    """Ana dal: kökte iki araç. Yeni oluşum dalı: biri defter/ altına taşınır, harita eski adı tutar."""

    def __init__(self, kok: Path):
        self.kok = kok
        self.git("init", "-q", "--initial-branch=main")
        (kok / "kopru_ekle.py").write_text("print('ekle')\n", encoding="utf-8")
        (kok / "kapi.py").write_text("print('kapı')\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "taban")
        self.taban = self.surum("HEAD")
        self.git("switch", "-q", "-c", "olusum")
        (kok / "defter").mkdir()
        self.git("mv", "kopru_ekle.py", "defter/kopru_ekle.py")
        (kok / "docs").mkdir()
        harita = {"alanlar": [{"dosyalar": [{"yol": "defter/kopru_ekle.py", "eski_adlar": ["kopru_ekle.py"]}]}]}
        (kok / "docs" / "harita.json").write_text(json.dumps(harita), encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "yeni oluşum")
        self.olusum = self.surum("HEAD")
        self.git("switch", "-q", "main")

    def git(self, *args: str) -> str:
        return subprocess.run(["git", *args], cwd=self.kok, env=ORTAM, check=True, capture_output=True, text=True).stdout

    def surum(self, ref: str) -> str:
        return self.git("rev-parse", ref).strip()


class DonusumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kayit = json.loads(donusum.KAYIT.read_text(encoding="utf-8"))

    def setUp(self):
        self.gecici = tempfile.TemporaryDirectory(prefix="donusum-sinama-")
        self.addCleanup(self.gecici.cleanup)
        self.depo = SentetikDepo(Path(self.gecici.name))

    def olc(self, o: dict, ana: str = "main", dal: str = "olusum") -> bool:
        ok, _ = donusum.olcut(o, self.kayit, {"ana": ana, "dal": dal}, self.depo.kok)
        return ok

    # ---------- gerçek kayıt ----------

    def test_repository_record_and_documents_agree(self):
        self.assertEqual(donusum.denetle(self.kayit), [])
        hesap = donusum.durumlar(self.kayit, None)
        hv = json.loads(donusum.harita.KAYIT.read_text(encoding="utf-8"))
        for yol, uretilen in donusum.bloklar(self.kayit, hesap, hv, donusum.kok_dosya_sayisi()).items():
            with self.subTest(belge=yol.name):
                self.assertEqual(donusum.acilis.belge_denetle(yol.name, yol.read_text(encoding="utf-8"), uretilen), [])

    def test_plain_page_is_readable_and_drawings_keep_their_rules(self):
        metin = donusum.BELGE.read_text(encoding="utf-8")
        self.assertEqual(donusum.okunabilirlik_denetle(metin), [])
        for tur in ("ressam çizimi", "mimar çizimi", "mühendis çizimi"):
            with self.subTest(tur=tur):
                self.assertIn(tur, metin)
        self.assertGreaterEqual(len(cizim.cizimler(metin)), 4)
        self.assertEqual(cizim.denetle("teknik", donusum.TEKNIK.read_text(encoding="utf-8")), [])

    def test_merge_waits_for_the_owner_and_keeps_history(self):
        birlesme = next(a for a in self.kayit["asamalar"] if a["kimlik"] == "birlesme")
        self.assertEqual(birlesme["kim"], "Haluk")
        self.assertEqual(birlesme["karar"]["kim"], "Haluk")      # karar verilmiş ya da bekliyor olabilir
        atalar = {o["surum"] for o in birlesme["olcutler"] if o["tur"] == "ata"}
        self.assertEqual(atalar, set(self.kayit["hedef"]["gecmis_surumleri"]))
        bozuk = copy.deepcopy(self.kayit)
        next(a for a in bozuk["asamalar"] if a["kimlik"] == "birlesme")["karar"] = None
        self.assertIn("asamalar: birleştirme aşaması sahibinin kararına bağlı olmalı", donusum.denetle(bozuk))

    def test_every_stage_has_a_way_back_and_runs_after_its_prerequisites(self):
        for a in self.kayit["asamalar"]:
            with self.subTest(asama=a["kimlik"]):
                self.assertTrue(a["sade"]["geri"] and a["teknik"]["geri_donus"])
        bozuk = copy.deepcopy(self.kayit)
        bozuk["asamalar"][1]["onkosul"] = ["kapanis"]
        self.assertTrue(any("kendisinden sonra geliyor" in h for h in donusum.denetle(bozuk)))

    def test_evidence_written_by_hand_requires_a_new_measurement(self):
        bozuk = copy.deepcopy(self.kayit)
        elle = next(o for a in bozuk["asamalar"] if a["kimlik"] == "yerel-hazirlik" for o in a["olcutler"])
        # Kanıtın karşılanma durumunu tersine çevir: kayıt bugün hangi hâldeyse sınama ona bağlı kalmaz.
        elle["kanit"] = [] if len(elle["kanit"]) >= elle["en_az"] else ["kanıt"] * elle["en_az"]
        self.assertTrue(any("yeniden ölçün" in h for h in donusum.denetle(bozuk)))

    # ---------- ölçütler sentetik depoda ----------

    def test_git_criteria_read_the_right_version(self):
        self.assertTrue(self.olc({"tur": "dosya_var", "ref": "dal", "yol": "defter/kopru_ekle.py"}))
        self.assertFalse(self.olc({"tur": "dosya_var", "yol": "defter/kopru_ekle.py"}))
        self.assertTrue(self.olc({"tur": "dosya_yok", "ref": "dal", "yol": "kopru_ekle.py"}))
        self.assertFalse(self.olc({"tur": "dosya_yok", "yol": "kopru_ekle.py"}))
        self.assertTrue(self.olc({"tur": "dosya_icerir", "yol": "kapi.py", "desen": "kapı"}))
        self.assertFalse(self.olc({"tur": "ata", "surum": self.depo.olusum}))
        self.assertTrue(self.olc({"tur": "ata", "surum": self.depo.olusum}, ana="olusum"))

    def test_merge_commit_keeps_history_but_squash_does_not(self):
        o = {"tur": "ata", "surum": self.depo.olusum}
        self.depo.git("switch", "-q", "-c", "sikistirma")
        self.depo.git("merge", "-q", "--squash", "olusum")
        self.depo.git("commit", "-q", "-m", "tek kayıt")
        self.assertTrue(self.olc({"tur": "dosya_var", "yol": "docs/harita.json"}, ana="sikistirma"))
        self.assertFalse(self.olc(o, ana="sikistirma"))
        self.depo.git("switch", "-q", "main")
        self.depo.git("merge", "-q", "--no-ff", "--no-edit", "olusum")
        self.assertTrue(self.olc(o))

    def test_old_names_resolve_only_after_the_map_arrives(self):
        o = {"tur": "eski_adlar_cozulur", "taban": self.depo.taban}
        self.assertTrue(self.olc(o))                       # ana dal bugün tabanın kendisi
        self.assertTrue(self.olc(o, ana="olusum"))         # taşınan dosyanın eski adı haritada
        self.depo.git("switch", "-q", "olusum")
        self.depo.git("rm", "-q", "docs/harita.json")
        self.depo.git("commit", "-q", "-m", "harita yok")
        self.assertFalse(self.olc(o, ana="olusum"))

    def test_statuses_follow_prerequisites_decisions_and_evidence(self):
        kayit = copy.deepcopy(self.kayit)
        # Kaydın bugünkü kararlarından ve kanıtlarından bağımsız bir başlangıç.
        for a in kayit["asamalar"]:
            if a["karar"]:
                a["karar"]["verildi"] = None
            for o in a["olcutler"]:
                if o["tur"] == "elle":
                    o["kanit"] = []
        kayit["son_prova"]["basarili"] = False
        hesap = donusum.durumlar(kayit, {"ana": "main", "dal": "olusum"}, self.depo.kok)
        self.assertEqual(hesap["birlesme"]["durum"], "onkosul-bekliyor")
        self.assertEqual(hesap["lisans"]["durum"], "istege-bagli")
        kayit["son_prova"]["basarili"] = True
        for a in kayit["asamalar"]:
            if a["kimlik"] == "olusum":
                a["olcutler"] = [{"tur": "dosya_var", "ref": "dal", "yol": "defter/kopru_ekle.py"}]
            if a["kimlik"] == "yerel-hazirlik":
                a["olcutler"][0]["kanit"] = ["yerel çıktı"]
        hesap = donusum.durumlar(kayit, {"ana": "main", "dal": "olusum"}, self.depo.kok)
        self.assertEqual([hesap[k]["durum"] for k in ("olusum", "prova", "yerel-hazirlik")], ["tamam"] * 3)
        self.assertEqual(hesap["birlesme"]["durum"], "karar-bekliyor")
        next(a for a in kayit["asamalar"] if a["kimlik"] == "birlesme")["karar"]["verildi"] = {"tarih": "2026-10-28", "yanit": "evet"}
        hesap = donusum.durumlar(kayit, {"ana": "main", "dal": "olusum"}, self.depo.kok)
        self.assertEqual(hesap["birlesme"]["durum"], "atilabilir")
        self.assertEqual(hesap["bulut"]["durum"], "onkosul-bekliyor")

    # ---------- prova ve bekleyen öneriler ----------

    def test_rehearsal_merges_in_a_throwaway_copy_and_reports_conflicts(self):
        sonuc = donusum.prova("main", "olusum", self.depo.kok,
                              [sys.executable, "-c", "print('3 tamam, 0 başarısız')"])
        self.assertEqual((sonuc["birlesme"], sonuc["basarili"], sonuc["dogrulama"]), ("temiz", True, "3 tamam, 0 başarısız"))
        self.assertNotIn("olusum", self.depo.git("log", "--oneline", "main"))
        self.assertEqual(self.depo.git("worktree", "list").count("\n"), 1)
        self.depo.git("switch", "-q", "olusum")
        (self.depo.kok / "kapi.py").write_text("print('dalda değişti')\n", encoding="utf-8")
        self.depo.git("commit", "-q", "-am", "dal")
        self.depo.git("switch", "-q", "main")
        (self.depo.kok / "kapi.py").write_text("print('ana dalda değişti')\n", encoding="utf-8")
        self.depo.git("commit", "-q", "-am", "çakışacak değişiklik")
        sonuc = donusum.prova("main", "olusum", self.depo.kok, [sys.executable, "-c", "print('çalışmamalı')"])
        self.assertEqual(sonuc["birlesme"], "çakışma")
        self.assertFalse(sonuc["basarili"])
        self.assertEqual(sonuc["cakisanlar"], ["kapi.py"])
        self.assertEqual(self.depo.git("worktree", "list").count("\n"), 1)

    def test_open_proposals_learn_where_their_files_went(self):
        self.depo.git("switch", "-q", "-c", "oneri", self.depo.taban)
        (self.depo.kok / "kopru_ekle.py").write_text("print('öneri')\n", encoding="utf-8")
        (self.depo.kok / "yeni_klasor").mkdir()
        (self.depo.kok / "yeni_klasor" / "not.md").write_text("not\n", encoding="utf-8")
        self.depo.git("add", ".")
        self.depo.git("commit", "-q", "-m", "öneri")
        harita = json.loads(donusum.harita.KAYIT.read_text(encoding="utf-8"))
        sonuc = donusum.dal_cozumle(99, "main", "main", harita, self.depo.kok, ref="oneri")
        self.assertEqual(sonuc["tasinan"], [["kopru_ekle.py", "defter/kopru_ekle.py"]])
        self.assertEqual(sonuc["alansiz"], ["yeni_klasor/"])
        self.assertEqual(sonuc["dosya"], 2)

    # ---------- üretilen çizimler ----------

    def test_generated_drawings_follow_the_record(self):
        hesap = donusum.durumlar(self.kayit, None)
        agac = donusum.agac(self.kayit, hesap)
        for a in self.kayit["asamalar"]:
            with self.subTest(asama=a["kimlik"]):
                self.assertIn(f"({a['no']}) ", agac)
        matris = donusum.matris(self.kayit).splitlines()
        self.assertEqual(sum(s.count("●") for s in matris), len(self.kayit["asamalar"]))
        hv = json.loads(donusum.harita.KAYIT.read_text(encoding="utf-8"))
        plan = donusum.once_sonra(self.kayit, hv, 18)
        self.assertIn("──▶ defter/", plan)
        self.assertIn(f"kökte {self.kayit['baslangic']['kok_dosya']} dosya", plan)
        for ad, metin in (("ağaç", agac), ("matris", "\n".join(matris)), ("plan", plan)):
            with self.subTest(cizim=ad):
                self.assertEqual(cizim.denetle(ad, donusum._blok(metin)), [])


if __name__ == "__main__":
    unittest.main()
