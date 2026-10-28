#!/usr/bin/env python3
"""Bugünkü depodan yeni oluşuma dönüşümü (docs/donusum.json) ölçer, prova eder, denetler ve belgelerini üretir.

Dönüşüm, GitHub'daki ana dalın, ayrı bir dalda kurulan yeni oluşuma geçişidir. Aşamaların durumu
kayda elle yazılmaz; ölçütlerden hesaplanır:
  tamam             bütün ölçütler karşılanıyor;
  istege-bagli      zorunlu olmayan ve henüz bitmemiş aşama;
  onkosul-bekliyor  ön koşullarından biri tamam değil;
  karar-bekliyor    sahibinin vereceği karar henüz verilmedi;
  elle-bekleniyor   yalnız elle doldurulan (dış dünyadaki bir olaya bağlı) ölçütleri var;
  atilabilir        ön koşulları bitti, karar beklemiyor.

Ölçüt türleri:
  dosya_var, dosya_yok, dosya_icerir   bir Git sürümünde ('ana' ya da 'dal') dosya ve içerik;
  ata                                  bir sürüm o dalın geçmişinde mi (birleşme geçmişi koruyor mu);
  eski_adlar_cozulur                   tabandaki her dosya bugün yerinde mi, değilse eski adı haritada mı;
  prova_gecti                          kayıttaki son prova başarılı mı;
  dallar_yerlesik                      bekleyen öteki önerilerin hiçbiri yeri değişen dosyaya dokunmuyor
                                       ve haritada yeri olmayan dosya eklemiyor mu;
  elle                                 dış dünyadaki bir olayın kanıt adresleri yazıldı mı.

Git'e bakan ölçütler yalnız --olc ve --durum kiplerinde hesaplanır; belgeler kayıttaki son ölçümden
üretilir. Böylece belgeler her makinede aynı çıkar, ölçüm ise tarihlidir.

Kullanım:
    python tools/donusum.py                    # belgeleri kayıttan yaz ve denetle
    python tools/donusum.py --check            # yazmadan denetle
    python tools/donusum.py --durum [--ana R] [--dal R]       # aşamaların canlı durumu (yazmaz)
    python tools/donusum.py --olc [--ana R] [--dal R] --yaz   # son ölçümü kayda yaz, belgeleri yenile
    python tools/donusum.py --prova [--ana R] [--dal R] [--yaz]   # birleşmeyi ana dalın geçici kopyasında dene
    python tools/donusum.py --dallar [--ana R] [--yaz]        # bekleyen önerileri yeni yerleşime göre çözümle
"""
from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

KOK = Path(__file__).resolve().parents[1]
KAYIT = KOK / "docs" / "donusum.json"
BELGE = KOK / "docs" / "donusum.md"
TEKNIK = KOK / "docs" / "teknik" / "donusum-teknik.md"
VARSAYILAN_ANA = "origin/main"
VARSAYILAN_DAL = "origin/claude/rafine-2026-10-28"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK / "tools"))

import acilis  # noqa: E402
import cizim  # noqa: E402
import harita  # noqa: E402
import sema_denetle  # noqa: E402

DURUMLAR = ("tamam", "atilabilir", "karar-bekliyor", "onkosul-bekliyor", "elle-bekleniyor", "istege-bagli")
DURUM_METNI = {
    "tamam": "Tamam.",
    "atilabilir": "Atılabilir: ön koşulu bitti ve bir karar beklemiyor.",
    "karar-bekliyor": "Sahibinin kararını bekliyor; ön koşulu bitti.",
    "onkosul-bekliyor": "Ön koşulunun bitmesini bekliyor.",
    "elle-bekleniyor": "Ön koşulu bitti; olduğu görülünce kanıtı yazılacak.",
    "istege-bagli": "İsteğe bağlı; dönüşümü beklemez.",
}
KISA = {"tamam": "tamam", "atilabilir": "atılabilir", "karar-bekliyor": "karar", "onkosul-bekliyor": "ön koşul",
        "elle-bekleniyor": "kanıt", "istege-bagli": "isteğe bağlı"}
OLCUT_ALANLARI = {"dosya_var": ("yol",), "dosya_yok": ("yol",), "dosya_icerir": ("yol", "desen"), "ata": ("surum",),
                  "eski_adlar_cozulur": ("taban",), "prova_gecti": (), "dallar_yerlesik": (),
                  "elle": ("aciklama", "en_az", "kanit")}
GIT_TURLERI = {"dosya_var", "dosya_yok", "dosya_icerir", "ata", "eski_adlar_cozulur"}
CIZIM_TURU = {"ressam": "ressam çizimi", "mimar": "mimar çizimi", "muhendis": "mühendis çizimi"}
SAYI = {0: "hiçbiri", 1: "biri", 2: "ikisi", 3: "üçü", 4: "dördü", 5: "beşi", 6: "altısı", 7: "yedisi", 8: "sekizi",
        9: "dokuzu", 10: "onu", 11: "on biri", 12: "on ikisi"}
SAYI_ADI = {0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz",
            10: "on", 11: "on bir", 12: "on iki", 13: "on üç"}


# ---------- Git ----------

def git(*args: str, kok: Path = KOK, kontrol: bool = True) -> str:
    sonuc = subprocess.run(["git", *args], cwd=kok, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if kontrol and sonuc.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {sonuc.stderr.strip()}")
    return sonuc.stdout


def surum(ref: str, kok: Path = KOK) -> str:
    """Sürümün tam kimliği; yoksa boş metin."""
    return git("rev-parse", "--verify", "--quiet", ref + "^{commit}", kok=kok, kontrol=False).strip()


def dosyalar(ref: str, kok: Path = KOK) -> set[str]:
    return set(git("ls-tree", "-r", "--name-only", "-z", ref, kok=kok).split("\0")) - {""}


def icerik(ref: str, yol: str, kok: Path = KOK) -> str | None:
    sonuc = subprocess.run(["git", "show", f"{ref}:{yol}"], cwd=kok, capture_output=True)
    return sonuc.stdout.decode("utf-8", "replace") if sonuc.returncode == 0 else None


def ata_mi(eski: str, ref: str, kok: Path = KOK) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", eski, ref], cwd=kok, capture_output=True).returncode == 0


def eski_ad_haritasi(metin: str | None) -> dict[str, str]:
    if not metin:
        return {}
    veri = json.loads(metin)
    return {ad: d["yol"] for alan in veri["alanlar"] for d in alan["dosyalar"] for ad in d.get("eski_adlar", [])}


# ---------- ölçüt ve durum ----------

def olcut(o: dict, kayit: dict, refler: dict[str, str] | None, kok: Path = KOK) -> tuple[bool | None, str]:
    """(karşılanıyor mu, tarif). Git'e bakan ölçüt sürümler verilmezse None döner."""
    tur, hangi = o["tur"], o.get("ref", "ana")
    ad = "ana dalda" if hangi == "ana" else "yeni oluşumun dalında"
    if tur == "elle":
        return len(o["kanit"]) >= o["en_az"], f"elle: {o['aciklama']} ({len(o['kanit'])}/{o['en_az']} kanıt)"
    if tur == "prova_gecti":
        p = kayit["son_prova"]
        return p["basarili"], f"son prova başarılı ({p['zaman'][:16].replace('T', ' ')}, {p['birlesme']}, {p['dogrulama']})"
    if tur == "dallar_yerlesik":
        bekleyen = [o_["no"] for o_ in kayit["acik_calismalar"]["oneriler"] if o_["tasinan"] or o_["alansiz"]]
        return not bekleyen, f"bekleyen önerilerin hepsi yeni yerleşimde (taşınması gereken: {len(bekleyen)})"
    sahip = "ana dalın" if hangi == "ana" else "yeni oluşumun dalının"
    tarif = {"dosya_var": f"{ad} `{o.get('yol')}` var", "dosya_yok": f"{ad} `{o.get('yol')}` yok",
             "dosya_icerir": f"{ad} `{o.get('yol')}` içinde “{o.get('desen')}” geçer",
             "ata": f"`{o.get('surum', '')[:7]}` {sahip} geçmişinde",
             "eski_adlar_cozulur": f"`{o.get('taban', '')[:7]}` sürümündeki her dosya {ad} yerinde ya da eski adıyla haritada"}[tur]
    if refler is None:
        return None, tarif
    ref = refler[hangi]
    if tur == "dosya_var":
        return o["yol"] in dosyalar(ref, kok), tarif
    if tur == "dosya_yok":
        return o["yol"] not in dosyalar(ref, kok), tarif
    if tur == "dosya_icerir":
        metin = icerik(ref, o["yol"], kok)
        return metin is not None and o["desen"] in metin, tarif
    if tur == "ata":
        return ata_mi(o["surum"], ref, kok), tarif
    if not surum(o["taban"], kok):
        return False, tarif + " (taban sürümü bu depoda yok)"
    bugun = dosyalar(ref, kok)
    eski = eski_ad_haritasi(icerik(ref, "docs/harita.json", kok))
    eksik = [ad_ for ad_ in dosyalar(o["taban"], kok) if ad_ not in bugun and ad_ not in eski]
    return not eksik, tarif + (f" (bulunamayan: {len(eksik)})" if eksik else "")


def durumlar(kayit: dict, refler: dict[str, str] | None, kok: Path = KOK) -> dict[str, dict]:
    """Aşamaların durumu. refler verilmezse Git ölçütleri kayıttaki son ölçümden okunur."""
    onceki = {d["kimlik"]: d for d in kayit["son_olcum"]["durumlar"]}
    asamalar = {a["kimlik"]: a for a in kayit["asamalar"]}
    sonuc: dict[str, dict] = {}

    def hesapla(kimlik: str, yigin: tuple = ()) -> str:
        if kimlik in sonuc:
            return sonuc[kimlik]["durum"]
        if kimlik in yigin or kimlik not in asamalar:
            return "onkosul-bekliyor"
        a = asamalar[kimlik]
        satirlar = []
        for i, o in enumerate(a["olcutler"]):
            ok, tarif = olcut(o, kayit, refler, kok)
            if ok is None:
                eski = onceki.get(kimlik, {}).get("olcutler", [])
                ok = eski[i]["karsilaniyor"] if i < len(eski) else False
            satirlar.append({"tarif": tarif, "karsilaniyor": bool(ok)})
        onkosul = [hesapla(k, yigin + (kimlik,)) for k in a["onkosul"]]
        if all(s["karsilaniyor"] for s in satirlar):
            durum = "tamam"
        elif not a["zorunlu"]:
            durum = "istege-bagli"
        elif any(d != "tamam" for d in onkosul):
            durum = "onkosul-bekliyor"
        elif a["karar"] and a["karar"]["verildi"] is None:
            durum = "karar-bekliyor"
        elif all(o["tur"] == "elle" for o, s in zip(a["olcutler"], satirlar) if not s["karsilaniyor"]):
            durum = "elle-bekleniyor"
        else:
            durum = "atilabilir"
        sonuc[kimlik] = {"durum": durum, "olcutler": satirlar}
        return durum

    for a in kayit["asamalar"]:
        hesapla(a["kimlik"])
    return sonuc


def _simdi() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def olc(kayit: dict, ana: str, dal: str, kok: Path = KOK) -> dict:
    refler = {"ana": ana, "dal": dal}
    hesap = durumlar(kayit, refler, kok)
    return {"zaman": _simdi(), "ana": ana, "ana_surum": surum(ana, kok), "dal": dal, "dal_surum": surum(dal, kok),
            "durumlar": [{"kimlik": a["kimlik"], **hesap[a["kimlik"]]} for a in kayit["asamalar"]]}


# ---------- prova ve bekleyen öneriler ----------

def prova(ana: str, dal: str, kok: Path = KOK, dogrulama: list[str] | None = None) -> dict:
    """Ana dalın geçici bir kopyasında yeni oluşumu birleştirir, denetimleri ve eski adları sınar, kopyayı siler."""
    ana_surum, dal_surum = surum(ana, kok), surum(dal, kok)
    gecici = Path(tempfile.mkdtemp(prefix="ortak-kopru-prova-"))
    agac = gecici / "agac"
    sonuc = {"zaman": _simdi(), "ana": ana, "ana_surum": ana_surum, "dal": dal, "dal_surum": dal_surum,
             "birlesme": "temiz", "cakisanlar": [], "dogrulama": "", "eski_adlar": "", "basarili": False}
    try:
        git("worktree", "add", "--detach", "--quiet", str(agac), ana_surum, kok=kok)
        birlesme = subprocess.run(["git", "-c", "user.name=Ortak Köprü provası", "-c", "user.email=prova@example.invalid",
                                   "merge", "--no-ff", "--no-edit", "--quiet", dal_surum],
                                  cwd=agac, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if birlesme.returncode != 0:
            sonuc["birlesme"] = "çakışma"
            sonuc["cakisanlar"] = sorted(git("diff", "--name-only", "--diff-filter=U", kok=agac, kontrol=False).split())
            return sonuc
        komut = dogrulama or [sys.executable, "tools/dogrula.py"]
        d = subprocess.run(komut, cwd=agac, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=1800)
        satirlar = [s for s in d.stdout.strip().splitlines() if s.strip()]
        sonuc["dogrulama"] = satirlar[-1] if satirlar else f"çıkış {d.returncode}"
        sonuc["basarili"] = d.returncode == 0
        if (agac / "tools" / "harita.py").is_file():
            e = subprocess.run([sys.executable, "tools/harita.py", "--check", "--ref", ana_surum], cwd=agac,
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            sonuc["eski_adlar"] = (e.stdout.strip().splitlines() or [""])[-1]
            sonuc["basarili"] = sonuc["basarili"] and e.returncode == 0
        return sonuc
    finally:
        git("worktree", "remove", "--force", str(agac), kok=kok, kontrol=False)
        shutil.rmtree(gecici, ignore_errors=True)


def dal_cozumle(no: int, hedef_dal: str, ana: str, harita_verisi: dict, kok: Path = KOK, ref: str | None = None) -> dict:
    """Bir önerinin dokunduğu dosyalar: yeri değişenler (eski → yeni) ve haritada yeri olmayan kök öğeler."""
    ref = ref or f"origin/pr/{no}"
    taban_ref = f"origin/{hedef_dal}" if hedef_dal != "main" else ana
    if not surum(taban_ref, kok) or not surum(ref, kok):
        raise RuntimeError(f"#{no}: {taban_ref} ya da {ref} yerelde yok; önce: git fetch origin "
                           "'+refs/heads/*:refs/remotes/origin/*' '+refs/pull/*/head:refs/remotes/origin/pr/*'")
    taban = git("merge-base", taban_ref, ref, kok=kok).strip()
    eski = {ad: d["yol"] for _, d in harita.tanimlar(harita_verisi) for ad in d.get("eski_adlar", [])}
    tasinan, alansiz, sayi = [], set(), 0
    for satir in git("diff", "--name-status", "--no-renames", taban, ref, kok=kok).splitlines():
        durum, yol = satir.split("\t", 1)
        sayi += 1
        if yol in eski:
            tasinan.append([yol, eski[yol]])
        elif durum != "D" and not harita.alan_bul(harita_verisi, yol):
            ust = yol.split("/", 1)[0]
            # Haritada bilinen bir klasörün içindeyse dosyanın kendisi, yeni bir klasörse yalnız klasör gösterilir.
            bilinen = any(d.startswith(ust + "/") for alan in harita_verisi["alanlar"] for d in alan["kapsam"])
            alansiz.add(yol if "/" in yol and bilinen else ust + ("/" if "/" in yol else ""))
    return {"surum": surum(ref, kok), "dosya": sayi, "tasinan": sorted(tasinan), "alansiz": sorted(alansiz)}


# ---------- denetim ----------

def denetle(kayit: dict) -> list[str]:
    hatalar = [f"sözleşme: {h}" for h in sema_denetle.dogrula(sema_denetle.sema_yukle("donusum"), kayit)]
    if hatalar:
        return hatalar
    asamalar = kayit["asamalar"]
    if [a["no"] for a in asamalar] != list(range(len(asamalar))):
        hatalar.append("asamalar: numaralar 0'dan sırayla olmalı")
    kimlikler = [a["kimlik"] for a in asamalar]
    for k in sorted({k for k in kimlikler if kimlikler.count(k) > 1}):
        hatalar.append(f"asamalar: '{k}' kimliği birden çok kez")
    for a in asamalar:
        konum = f"asamalar[{a['no']}] {a['kimlik']}"
        for k in a["onkosul"]:
            if k not in kimlikler:
                hatalar.append(f"{konum}: ön koşul yok ({k})")
            elif kimlikler.index(k) >= kimlikler.index(a["kimlik"]):
                hatalar.append(f"{konum}: ön koşul ({k}) kendisinden sonra geliyor")
        for i, o in enumerate(a["olcutler"]):
            gerekli = OLCUT_ALANLARI[o["tur"]]
            eksik = [alan for alan in gerekli if alan not in o]
            fazla = sorted(set(o) - {"tur"} - set(gerekli) - ({"ref"} if o["tur"] in GIT_TURLERI - {"eski_adlar_cozulur"} else set()))
            if eksik or fazla:
                hatalar.append(f"{konum}.olcutler[{i}]: '{o['tur']}' için eksik {eksik} / fazla {fazla}")
        for komut in a["teknik"]["komutlar"]:
            for yol in harita.KOMUT_YOLU.findall(komut):
                if not (KOK / yol).exists() and yol not in _eski_adlar():
                    hatalar.append(f"{konum}: komutun gösterdiği dosya yok ({yol})")
    if not any(a["karar"] for a in asamalar if a["kimlik"] == "birlesme"):
        hatalar.append("asamalar: birleştirme aşaması sahibinin kararına bağlı olmalı")
    for s in kayit["hedef"]["gecmis_surumleri"]:
        if not any(o["tur"] == "ata" and o["surum"] == s for a in asamalar for o in a["olcutler"]):
            hatalar.append(f"hedef.gecmis_surumleri: {s[:7]} için bir 'ata' ölçütü yok")
    # son ölçüm: aşamaları kapsar, ön koşullarla tutarlı, kayda bağlı ölçütler güncel
    olcum = {d["kimlik"]: d for d in kayit["son_olcum"]["durumlar"]}
    if sorted(olcum) != sorted(kimlikler):
        hatalar.append("son_olcum: aşamaların hepsini tam bir kez kapsamalı; python tools/donusum.py --olc --yaz")
        return hatalar
    for a in asamalar:
        d = olcum[a["kimlik"]]
        if len(d["olcutler"]) != len(a["olcutler"]):
            hatalar.append(f"son_olcum: '{a['kimlik']}' ölçüt sayısı kayıttan farklı; yeniden ölçün")
            continue
        if d["durum"] == "tamam" and any(olcum[k]["durum"] != "tamam" for k in a["onkosul"]):
            hatalar.append(f"son_olcum: '{a['kimlik']}' tamam ama ön koşulu tamam değil")
        for i, o in enumerate(a["olcutler"]):
            if o["tur"] not in GIT_TURLERI:
                simdi, _ = olcut(o, kayit, None)
                if simdi != d["olcutler"][i]["karsilaniyor"]:
                    hatalar.append(f"son_olcum: '{a['kimlik']}' ölçütü kayıtla uyuşmuyor (kanıt ya da prova değişti); yeniden ölçün")
    hesap = durumlar(kayit, None)
    for a in asamalar:
        if hesap[a["kimlik"]]["durum"] != olcum[a["kimlik"]]["durum"]:
            hatalar.append(f"son_olcum: '{a['kimlik']}' durumu yeniden hesapta farklı ({olcum[a['kimlik']]['durum']} → "
                           f"{hesap[a['kimlik']]['durum']}); yeniden ölçün")
    # Mimar (önce ve sonra) ve mühendis (ağaç, iş çizelgesi) çizimleri kayıttan üretilir; ressam çizimi elle yapılır.
    if "ressam" not in {c["tur"] for c in kayit["cizimler"]}:
        hatalar.append("cizimler: ressam çizimi yok")
    for c in kayit["cizimler"]:
        if c["yer"] == "belge" and c["bolum"] != "yol":
            hatalar.append(f"cizimler: '{c['kimlik']}' için bölüm '{c['bolum']}' sade belgede yok")
    for c in kayit["cizimler"]:
        hatalar += cizim.denetle(f"çizim {c['kimlik']}", _blok(c["metin"]))
    return hatalar


def _eski_adlar() -> set[str]:
    veri = json.loads(harita.KAYIT.read_text(encoding="utf-8"))
    return {ad for _, d in harita.tanimlar(veri) for ad in d.get("eski_adlar", [])}


# ---------- çizimler ----------

def _blok(metin: str) -> str:
    return "```text\n" + metin.rstrip("\n") + "\n```"


def _cizim(baslik: str, tur: str, metin: str) -> list[str]:
    return [f"**{baslik}** · {CIZIM_TURU[tur]}", _blok(metin)]


def agac(kayit: dict, hesap: dict[str, dict], genislik: int = cizim.EN_GENIS) -> str:
    """Aşamaların ağacı: her aşama son ön koşulunun altında; sağda durumu."""
    asamalar = {a["kimlik"]: a for a in kayit["asamalar"]}
    cocuk: dict[str | None, list[str]] = {}
    for a in kayit["asamalar"]:
        cocuk.setdefault(a["onkosul"][-1] if a["onkosul"] else None, []).append(a["kimlik"])
    sutun = genislik - 14          # en uzun durum işareti: ◇ isteğe bağlı
    satirlar = []

    def isaret(k: str) -> str:
        d = hesap[k]["durum"]
        return ("■ " if d == "tamam" else "◇ " if d == "istege-bagli" else "□ ") + KISA[d]

    def yaz(k: str, onek: str, kok_mu: bool, son: bool) -> None:
        a = asamalar[k]
        bas = "" if kok_mu else ("└─▶ " if son else "├─▶ ")
        ek = "" if len(a["onkosul"]) < 2 else f" (+{len(a['onkosul']) - 1})"
        etiket = f"{onek}{bas}({a['no']}) {a['ad']}{ek}"
        if len(etiket) > sutun - 1:
            etiket = etiket[:sutun - 2] + "…"
        satirlar.append(etiket.ljust(sutun) + isaret(k))
        alt = cocuk.get(k, [])
        for i, c in enumerate(alt):
            yeni = onek + ("" if kok_mu else ("    " if son else "│   "))
            yaz(c, yeni if not kok_mu else onek + " ", False, i == len(alt) - 1)

    for k in cocuk.get(None, []):
        yaz(k, "  ", True, True)
    return "\n".join(satirlar)


def matris(kayit: dict) -> str:
    """Kim ne zaman: satırlar aşamaları atanlar, sütunlar aşamalar; ● o aşamada iş yapan."""
    kimler: list[str] = []
    for a in kayit["asamalar"]:
        if a["kim"] not in kimler:
            kimler.append(a["kim"])
    genis = max(len(k) for k in kimler + ["aşama"]) + 2
    bas = "  " + "aşama".ljust(genis) + "".join(f"{a['no']:>3}" for a in kayit["asamalar"])
    cizgi = "  " + "─" * (genis - 2) + "  " + "─" * (3 * len(kayit["asamalar"]) - 1)
    satirlar = [bas, cizgi]
    for k in kimler:
        satirlar.append("  " + k.ljust(genis) + "".join("  ●" if a["kim"] == k else "  ·" for a in kayit["asamalar"]))
    return "\n".join(satirlar)


def once_sonra(kayit: dict, harita_verisi: dict, kok_bugun: int) -> str:
    """Önce ve sonra: tabandaki yerlerden bugünkü alanlara, eski adlardan sayılarak."""
    gruplar: dict[tuple[str, str], int] = {}
    for _, d in harita.tanimlar(harita_verisi):
        for ad in d.get("eski_adlar", []):
            once = ad.rsplit("/", 1)[0] + "/" if "/" in ad else "kök"
            sonra = d["yol"].rsplit("/", 1)[0] + "/" if "/" in d["yol"] else "kök"
            gruplar[(once, sonra)] = gruplar.get((once, sonra), 0) + 1
    sol = 32
    satirlar = ["  " + "ÖNCE · bugünkü ana dal".ljust(sol) + "    SONRA · yeni oluşum",
                "  " + "─" * sol + "    " + "─" * 26,
                "  " + f"kökte {kayit['baslangic']['kok_dosya']} dosya".ljust(sol) + "    " + f"kökte {kok_bugun} dosya ve alanlar"]
    sira = sorted(gruplar.items(), key=lambda x: (x[0][0] != "kök", x[0][0], -x[1], x[0][1]))
    for (once, sonra), n in sira:
        etiket = f"kökten {n} dosya" if once == "kök" else f"{once} altından {n} dosya"
        satirlar.append("  " + etiket.ljust(sol) + "──▶ " + ("aynı yerde, yeni adla" if once == sonra else sonra))
    satirlar += ["", "  yerinde kalan: ortak defter, aynası, Web sayfaları,",
                 "  çağrı kayıtları ve kökteki üç çalıştırma girişi"]
    return "\n".join(satirlar)


# ---------- belgeler ----------

def _ozet(kayit: dict, hesap: dict[str, dict]) -> str:
    o = kayit["son_olcum"]
    d = [hesap[a["kimlik"]]["durum"] for a in kayit["asamalar"]]
    zaman = o["zaman"][:16].replace("T", " ")
    metin = (f"Son ölçüm {zaman} UTC'de, ana dalın o anki hâline karşı yapıldı. "
             f"Dönüşümün {SAYI_ADI[len(d)]} aşamasından "
             + (f"{SAYI[d.count('tamam')]} tamam." if d.count("tamam") else "henüz hiçbiri tamam değil."))
    for durum, cumle in (("atilabilir", "Şu an atılabilecek aşama"), ("karar-bekliyor", "Kararı bekleyen aşama"),
                         ("elle-bekleniyor", "Kanıtı beklenen aşama")):
        adlar = [a["ad"] for a in kayit["asamalar"] if hesap[a["kimlik"]]["durum"] == durum]
        if adlar:
            metin += f" {cumle}: " + ", ".join(adlar) + "."
    if "onkosul-bekliyor" in d:
        metin += " Öteki zorunlu aşamalar bir ön koşulun bitmesini bekliyor."
    p = kayit["son_prova"]
    if not p["dogrulama"] and p["birlesme"] == "temiz":
        metin += " Birleşmenin provası henüz yapılmadı."
    elif p["birlesme"] == "çakışma":
        metin += " Son provada birleşme çakıştı; çakışan dosyalar teknik ektedir."
    else:
        metin += " Son provada birleşme temiz çıktı ve denetimler " + ("geçti." if p["basarili"] else "geçmedi.")
    return metin


def _acik_ozet(kayit: dict) -> str:
    oneriler = kayit["acik_calismalar"]["oneriler"]
    tasiyan = [o for o in oneriler if o["tasinan"]]
    alansiz = [o for o in oneriler if o["alansiz"]]
    return (f"GitHub'da {SAYI_ADI[len(oneriler)]} değişiklik önerisi daha bekliyor. "
            f"{SAYI[len(tasiyan)].capitalize()} yeri değişen dosyalara dokunuyor. "
            f"{SAYI[len(alansiz)].capitalize()} haritada yeri olmayan yeni klasör ya da dosya ekliyor. "
            "Bunlar yeni yerleşime taşınınca ana dala girebilir; hangisinin neyi taşıması gerektiği teknik ektedir.")


def belge(kayit: dict, hesap: dict[str, dict], harita_verisi: dict, kok_bugun: int) -> str:
    adlar = {a["kimlik"]: a["ad"] for a in kayit["asamalar"]}
    cizimler = {c["bolum"]: c for c in kayit["cizimler"] if c["yer"] == "belge"}
    p = list(kayit["giris"])
    p += ["## Bugün nerede duruyoruz", _ozet(kayit, hesap),
          "Aşağıdaki ağaçta her aşama, bitmesini beklediği aşamanın altında duruyor. Dolu kare biten, boş kare açık, "
          "eşkenar dörtgen isteğe bağlı aşamayı gösterir.",
          *_cizim("Dönüşümün ağacı", "muhendis", agac(kayit, hesap))]
    p += ["## Ne değişecek"] + kayit["degisenler"] + [
        "Aşağıdaki plan, dosyaların bugün nerede durduğunu ve nereye gideceğini gösteriyor. Sayılar haritadaki eski adlardan "
        "çıkarılıyor; bir dosya taşındıkça plan kendiliğinden değişir.",
        *_cizim("Önce ve sonra", "mimar", once_sonra(kayit, harita_verisi, kok_bugun))]
    p += ["## Ne değişmeyecek"] + kayit["degismeyenler"]
    c = cizimler["yol"]
    p += ["## Yol"] + kayit["yol"] + _cizim(c["baslik"], c["tur"], c["metin"])
    p += ["## Aşamalar",
          "Aşağıdaki iş çizelgesinde satırlar aşamaları atanları, sütunlar aşamaları gösteriyor. Dolu nokta, o aşamada işin "
          "kimde olduğunu belirtiyor.",
          *_cizim("Kim ne zaman", "muhendis", matris(kayit))]
    for a in kayit["asamalar"]:
        s = a["sade"]
        bekledigi = [adlar[k] for k in a["onkosul"]]
        ne_zaman = ((f"Önce şu aşama{'nın' if len(bekledigi) == 1 else 'ların'} bitmesi gerekiyor: " + ", ".join(bekledigi) + ".")
                    if bekledigi else "Bir ön koşulu yok.")
        if a["karar"]:
            ne_zaman += (f" Ayrıca {a['karar']['kim']}'un bir karar vermesi gerekiyor. {a['karar']['soru']}"
                         if a["karar"]["verildi"] is None else f" {a['karar']['kim']} kararını verdi: {a['karar']['verildi']['yanit']}")
        p += [f"### {a['no']}. {a['ad']}",
              f"**Durum:** {DURUM_METNI[hesap[a['kimlik']]['durum']]}", f"**Kim?** {a['kim'][0].upper() + a['kim'][1:]}.",
              f"**Ne?** {s['ne']}", f"**Neden?** {s['neden']}", f"**Nasıl?** {s['nasil']}", f"**Ne zaman?** {ne_zaman}",
              f"**Geri dönüş:** {s['geri']}", f"**Bitince:** {s['sonra']}"]
    p += ["## Bekleyen öteki öneriler", _acik_ozet(kayit)]
    p += ["## Geri dönüş"] + kayit["geri_donus"]
    p += ["## Siz ne yapabilirsiniz"] + kayit["okur"]
    p += _sozluk("\n\n".join(p))
    return "\n\n".join(p) + "\n"


def _sozluk(metin: str) -> list[str]:
    veri = json.loads(acilis.KAYIT.read_text(encoding="utf-8"))
    gorunen = acilis._kucuk(acilis._gorunen(cizim.cizimsiz(metin)))
    gecen = [m for m in veri["sozluk"] if any(acilis._kucuk(p) in gorunen for p in m["terim"].split(" ve "))]
    return ["## Birkaç kelime", "Bu sayfada geçen birkaç kelime: " + " ".join(f"**{m['terim']}:** {m['anlam']}" for m in gecen)] if gecen else []


def _hucre(metin: str) -> str:
    return metin.replace("|", "\\|").replace("\n", " ")


def teknik_belge(kayit: dict, hesap: dict[str, dict]) -> str:
    b, h, o, pr = kayit["baslangic"], kayit["hedef"], kayit["son_olcum"], kayit["son_prova"]
    p = list(kayit["teknik_giris"])
    p += ["## Başlangıç ve hedef",
          f"Başlangıç: `{b['dal']}` @ `{b['surum']}` ({b['tarih'][:10]}), kökte {b['kok_dosya']} dosya. "
          f"Hedef: `{h['dal']}`, değişiklik önerisi #{h['oneri']}. Ana dalın geçmişinde kalması beklenen sürümler: "
          + ", ".join(f"`{s[:7]}`" for s in h["gecmis_surumleri"]) + "."]
    satirlar = ["| Aşama | Kim | Ön koşul | Karar | Zorunlu | Durum |", "| --- | --- | --- | --- | --- | --- |"]
    for a in kayit["asamalar"]:
        karar = "—" if not a["karar"] else (f"{a['karar']['kim']}: bekliyor" if a["karar"]["verildi"] is None
                                           else f"{a['karar']['kim']}: {a['karar']['verildi']['tarih']}")
        satirlar.append(f"| {a['no']}. {a['ad']} (`{a['kimlik']}`) | {a['kim']} | {', '.join(a['onkosul']) or '—'} | {karar} | "
                        f"{'evet' if a['zorunlu'] else 'hayır'} | {hesap[a['kimlik']]['durum']} |")
    p += ["## Aşamalar", f"Son ölçüm: {o['zaman']} · ana `{o['ana']}` @ `{o['ana_surum'][:7]}` · dal `{o['dal']}` @ "
          f"`{o['dal_surum'][:7]}`. Canlı durum için: `python tools/donusum.py --durum`.", "\n".join(satirlar)]
    for a in kayit["asamalar"]:
        t = a["teknik"]
        p += [f"### {a['no']}. {a['ad']}", "```sh\n" + "\n".join(t["komutlar"]) + "\n```",
              "Dokunduğu yerler: " + ", ".join(y if " " in y else f"`{y}`" for y in t["dokunur"]) + ".",
              f"Geri dönüş: {t['geri_donus']}"]
        if a["karar"]:
            p.append(f"Karar ({a['karar']['kim']}): {a['karar']['soru']}")
        sat = ["| Ölçüt | Son ölçümde |", "| --- | --- |"]
        for s in hesap[a["kimlik"]]["olcutler"]:
            sat.append(f"| {_hucre(s['tarif'])} | {'karşılanıyor' if s['karsilaniyor'] else 'karşılanmıyor'} |")
        p.append("\n".join(sat))
    p += ["## Prova",
          f"Son prova {pr['zaman']}: ana `{pr['ana']}` @ `{pr['ana_surum'][:7]}` ile dal `{pr['dal']}` @ `{pr['dal_surum'][:7]}` "
          f"geçici bir çalışma ağacında birleştirildi. Birleşme: {pr['birlesme']}"
          + (f" ({', '.join(f'`{c}`' for c in pr['cakisanlar'])})" if pr["cakisanlar"] else "")
          + f". Doğrulama: {pr['dogrulama'] or '—'}. Eski adlar: {pr['eski_adlar'] or '—'}. "
          f"Sonuç: {'başarılı' if pr['basarili'] else 'başarısız'}.",
          "Prova ana dala ve bu çalışma ağacına dokunmaz; geçici ağaç iş bitince silinir. Yenilemek için: "
          "`python tools/donusum.py --prova --yaz`."]
    ac = kayit["acik_calismalar"]
    satirlar = ["| Öneri | Hedef dal | Dosya | Yeri değişen dosyalar (eski → yeni) | Haritada yeri olmayan |", "| --- | --- | --- | --- | --- |"]
    for x in ac["oneriler"]:
        tasinan = "<br>".join(f"`{e}` → `{y}`" for e, y in x["tasinan"]) or "—"
        alansiz = ", ".join(f"`{a}`" for a in x["alansiz"]) or "—"
        satirlar.append(f"| #{x['no']} {_hucre(x['baslik'])} | `{x['hedef_dal']}` | {x['dosya']} | {tasinan} | {alansiz} |")
    p += ["## Bekleyen öteki öneriler",
          f"Çözümleme {ac['olculdu']}, taban `{ac['taban'][:7]}`. Her öneri kendi hedef dalıyla ortak atasına göre "
          "karşılaştırılır. Yeri değişen dosyanın yeni yeri haritadaki eski adlardan bulunur. Haritada yeri olmayan kök öğeler, "
          "öneri birleşmeden önce bir alana bağlanmalıdır; yoksa harita denetimi kırılır.", "\n".join(satirlar),
          "Bir dalı yeni yerleşime taşımanın kısa yolu: dal yeni ana dalın üzerine alınır (`git rebase origin/main`); yeri "
          "değişen dosyalarda Git çoğu zaman yeni yeri kendisi bulur; bulamazsa `python tools/harita.py --nerede ESKI_AD` "
          "yeni yolu söyler. Yeni klasörler `docs/harita.json` içinde bir alana bağlanır ve `python tools/harita.py` çalıştırılır."]
    p += ["## Geri dönüş", "Birleşme bir birleştirme kaydıyla yapılırsa tek adımda geri alınır: GitHub'da birleşmiş önerinin "
          "sayfasındaki geri alma düğmesi (Revert) ya da `git revert -m 1 <birleşme>`. Geri almanın kendisi de bir kayıttır; "
          "dönüşüm yeniden denenmek istenirse önce geri almanın geri alınması gerekir."]
    for c in kayit["cizimler"]:
        if c["yer"] == "teknik":
            p += _cizim(c["baslik"], c["tur"], c["metin"])
    p += ["## Kurallar",
          "Aşamanın durumu kayda yazılmaz; ölçütlerden hesaplanır. Git'e bakan ölçütler (" + ", ".join(f"`{t}`" for t in sorted(GIT_TURLERI))
          + ") yalnız `--olc` ve `--durum` kiplerinde ana dala ya da yeni oluşumun dalına karşı hesaplanır; belgeler kayıttaki son "
          "ölçümden üretilir. Kayda bağlı ölçütler (`elle`, `prova_gecti`, `dallar_yerlesik`) her denetimde yeniden hesaplanır; "
          "son ölçümle uyuşmazlarsa denetim yeniden ölçüm ister. Tamam olan bir aşamanın ön koşulları da tamam olmalıdır. "
          "Birleştirme aşaması sahibinin kararına bağlıdır. Ana dalın geçmişinde kalması beklenen her sürüm için bir `ata` ölçütü vardır."]
    return "\n\n".join(p) + "\n"


def bloklar(kayit: dict, hesap: dict[str, dict], harita_verisi: dict, kok_bugun: int) -> dict[Path, dict[str, str]]:
    return {BELGE: {"donusum": acilis._ayir(belge(kayit, hesap, harita_verisi, kok_bugun))},
            TEKNIK: {"donusum_teknik": acilis._ayir(teknik_belge(kayit, hesap))}}


def okunabilirlik_denetle(metin: str) -> list[str]:
    veri = json.loads(acilis.KAYIT.read_text(encoding="utf-8"))
    terimler = [m["terim"] for m in veri["sozluk"]]
    return acilis.okunabilirlik("docs/donusum.md", cizim.cizimsiz(metin), terimler, ayrim_bagi=True) + cizim.denetle("docs/donusum.md", metin)


def kok_dosya_sayisi() -> int:
    return sum(1 for ad in harita.izlenen_dosyalar() if "/" not in ad)


def _yaz(kayit: dict) -> None:
    KAYIT.write_text(json.dumps(kayit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    kip = parser.add_mutually_exclusive_group()
    kip.add_argument("--check", action="store_true", help="yazmadan denetle")
    kip.add_argument("--durum", action="store_true", help="aşamaların canlı durumunu yaz (kayda dokunmaz)")
    kip.add_argument("--olc", action="store_true", help="aşamaları ölç")
    kip.add_argument("--prova", action="store_true", help="birleşmeyi ana dalın geçici kopyasında dene")
    kip.add_argument("--dallar", action="store_true", help="bekleyen önerileri çözümle")
    parser.add_argument("--ana", default=VARSAYILAN_ANA, help=f"ana dal sürümü (varsayılan {VARSAYILAN_ANA})")
    parser.add_argument("--dal", default=VARSAYILAN_DAL, help=f"yeni oluşumun dalı (varsayılan {VARSAYILAN_DAL})")
    parser.add_argument("--yaz", action="store_true", help="sonucu kayda yaz ve belgeleri yenile")
    args = parser.parse_args()
    kayit = json.loads(KAYIT.read_text(encoding="utf-8"))
    if args.durum or args.olc or args.prova or args.dallar:
        eksik = [r for r in (args.ana, args.dal) if not surum(r)]
        if eksik:
            print(f"Sürüm bulunamadı: {', '.join(eksik)}. Önce: git fetch origin "
                  "'+refs/heads/*:refs/remotes/origin/*' '+refs/pull/*/head:refs/remotes/origin/pr/*'")
            return 2
    if args.durum:
        hesap = durumlar(kayit, {"ana": args.ana, "dal": args.dal})
        print(json.dumps({a["kimlik"]: dict(no=a["no"], ad=a["ad"], **hesap[a["kimlik"]]) for a in kayit["asamalar"]},
                         ensure_ascii=False, indent=2))
        return 0
    if args.olc or args.prova or args.dallar:
        if args.olc:
            kayit["son_olcum"] = olc(kayit, args.ana, args.dal)
            print(json.dumps({d["kimlik"]: d["durum"] for d in kayit["son_olcum"]["durumlar"]}, ensure_ascii=False))
        if args.prova:
            kayit["son_prova"] = prova(args.ana, args.dal)
            print(json.dumps(kayit["son_prova"], ensure_ascii=False, indent=2))
        if args.dallar:
            hv = json.loads(harita.KAYIT.read_text(encoding="utf-8"))
            ac = kayit["acik_calismalar"]
            ac["olculdu"], ac["taban"] = _simdi(), surum(args.ana)
            for x in ac["oneriler"]:
                x.update(dal_cozumle(x["no"], x["hedef_dal"], args.ana, hv))
                print(f"#{x['no']}: {x['dosya']} dosya, taşınan {len(x['tasinan'])}, alansız {x['alansiz']}")
        if not args.yaz:
            return 0
        if args.prova or args.dallar:     # kayda bağlı ölçütler değişti; son ölçüm de yenilenir
            kayit["son_olcum"] = olc(kayit, args.ana, args.dal)
        _yaz(kayit)
    hatalar = denetle(kayit)
    if not hatalar:
        hesap = durumlar(kayit, None)
        hv = json.loads(harita.KAYIT.read_text(encoding="utf-8"))
        for hedef, uretilen in bloklar(kayit, hesap, hv, kok_dosya_sayisi()).items():
            metin = hedef.read_text(encoding="utf-8") if hedef.is_file() else ""
            if not args.check and metin:
                yeni = acilis.belge_guncelle(metin, uretilen)
                if yeni != metin:
                    hedef.write_text(yeni, encoding="utf-8", newline="\n")
                    metin = yeni
            hatalar += acilis.belge_denetle(hedef.relative_to(KOK).as_posix(), metin, uretilen)
        if BELGE.is_file():
            hatalar += okunabilirlik_denetle(BELGE.read_text(encoding="utf-8"))
        if TEKNIK.is_file():
            hatalar += cizim.denetle("docs/teknik/donusum-teknik.md", TEKNIK.read_text(encoding="utf-8"))
    for hata in hatalar:
        print(hata)
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/donusum.py")
        return 1
    d = [x["durum"] for x in kayit["son_olcum"]["durumlar"]]
    print(f"TAMAM: {len(d)} aşama ({d.count('tamam')} tamam, {d.count('atilabilir')} atılabilir, {d.count('karar-bekliyor')} karar, "
          f"{d.count('elle-bekleniyor')} kanıt, {d.count('onkosul-bekliyor')} ön koşul, {d.count('istege-bagli')} isteğe bağlı); "
          f"son ölçüm {kayit['son_olcum']['zaman'][:16]}, ana {kayit['son_olcum']['ana_surum'][:7]}; iki belge kayıtla uyumlu, sayfa sade.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
