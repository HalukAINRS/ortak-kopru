#!/usr/bin/env python3
"""Açılıştan gerçeğe giden yolu (docs/yol.json) depoya karşı hesaplar, denetler ve belgelerini üretir.

Yol, açılıştaki niyeti ve altı ilkeyi gerçeğe dönüştürecek adımlardır. Bir adımın durumu kayda
yazılmaz; ölçütlerinden hesaplanır:
  tamam               bütün ölçütler karşılanıyor;
  ufukta              zorunlu olmayan ve henüz bitmemiş adım;
  onkosul-bekliyor    ön koşullarından biri tamam değil;
  karar-bekliyor      sahibinin vereceği karar henüz verilmedi;
  disaridan-bekleniyor yalnız elle doldurulan (dış dünyaya bağlı) ölçütleri var;
  atilabilir          ön koşulları bitti, karar beklemiyor; atılmayı bekliyor.

Denetim:
  - sözleşmeye uyum; adım numaraları 0'dan sırayla, kimlikler tekil;
  - ön koşullar var olan adımları gösterir ve döngü yoktur; tamam olan bir adımın ön koşulları da tamamdır;
  - bağlı bulgular rafine kayıtlarında, bağlı senaryolar şimdi ve sonrası kaydında vardır;
  - ölçütler türlerinin gerektirdiği alanları taşır;
  - açılışla tutarlılık: açılışta tam işlemeyen her ilkenin yolda en az bir zorunlu adımı vardır;
    bir ilkenin bütün zorunlu adımları bittiyse açılıştaki durumu güncellenmelidir; tam işleyen bir
    ilkeye bağlı açık zorunlu adım kalamaz;
  - çizimler: ressam, mimar ve mühendis türlerinin her biri en az bir kez; klavye çizim kuralları;
  - docs/yol.md sade kalır (açılışın okunabilirlik denetimi) ve iki belge kayıtla eşleşir.

Kullanım:
    python tools/yol.py              # belgeleri kayıttan yaz ve denetle
    python tools/yol.py --check      # yazmadan denetle; uyumsuzlukta çıkış 1
    python tools/yol.py --durum      # her adımın hesaplanan durumunu ve ölçütlerini JSON olarak yaz
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

KOK = Path(__file__).resolve().parents[1]
KAYIT = KOK / "docs" / "yol.json"
BELGE = KOK / "docs" / "yol.md"
TEKNIK = KOK / "docs" / "teknik" / "yol-teknik.md"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK / "tools"))

import acilis  # noqa: E402
import cizim  # noqa: E402
import sema_denetle  # noqa: E402

DURUM_METNI = {
    "tamam": "Tamam.",
    "atilabilir": "Atılabilir: ön koşulu bitti ve bir karar beklemiyor.",
    "karar-bekliyor": "Sahibinin kararını bekliyor; ön koşulu bitti.",
    "onkosul-bekliyor": "Ön koşulunun bitmesini bekliyor.",
    "disaridan-bekleniyor": "Dışarıdan bir katkı bekleniyor.",
    "ufukta": "Ufukta; zorunlu değil.",
}
KISA_DURUM = {"tamam": "tamam", "atilabilir": "atılabilir", "karar-bekliyor": "karar",
              "onkosul-bekliyor": "ön koşul", "disaridan-bekleniyor": "dışarıdan", "ufukta": "ufukta"}
BUYUKLUK = {"küçük": "Küçük bir değişiklik.", "orta": "Orta büyüklükte bir iş.", "büyük": "Büyük bir iş."}
SAYI_ADI = {0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş", 6: "altı", 7: "yedi", 8: "sekiz",
            9: "dokuz", 10: "on"}
SAYI_IYELIK = {0: "hiçbiri", 1: "biri", 2: "ikisi", 3: "üçü", 4: "dördü", 5: "beşi", 6: "altısı", 7: "yedisi",
               8: "sekizi", 9: "dokuzu", 10: "onu"}
CIZIM_TURU = {"ressam": "ressam çizimi", "mimar": "mimar çizimi", "muhendis": "mühendis çizimi"}
OLCUT_ALANLARI = {"dosya_var": ("yol",), "dosya_icerir": ("yol", "desen"), "dosya_icermez": ("yol", "desen"),
                  "test_var": ("yol", "ad"), "bulgu_kapali": ("kimlik",), "elle": ("aciklama", "en_az", "kanit")}


def _acilis() -> dict:
    return json.loads(acilis.KAYIT.read_text(encoding="utf-8"))


def olcut(o: dict, bulgular: dict[str, str]) -> tuple[bool, str]:
    """Bir ölçütün bugün karşılanıp karşılanmadığı ve okunabilir tarifi."""
    tur = o["tur"]
    yol = KOK / o["yol"] if "yol" in o else None
    if tur == "dosya_var":
        return yol.is_file(), f"`{o['yol']}` var"
    if tur in ("dosya_icerir", "dosya_icermez"):
        icerir = yol.is_file() and o["desen"] in yol.read_text(encoding="utf-8")
        if tur == "dosya_icerir":
            return icerir, f"`{o['yol']}` içinde `{o['desen']}` geçer"
        return yol.is_file() and not icerir, f"`{o['yol']}` içinde `{o['desen']}` geçmez"
    if tur == "test_var":
        var = yol.is_file() and re.search(rf"def {re.escape(o['ad'])}\(", yol.read_text(encoding="utf-8")) is not None
        return var, f"`{o['yol']}` içinde `{o['ad']}` sınaması var (CI'da geçer)"
    if tur == "bulgu_kapali":
        return bulgular.get(o["kimlik"]) == "düzeltildi", f"{o['kimlik']} bulgusu düzeltildi"
    return len(o["kanit"]) >= o["en_az"], f"elle: {o['aciklama']} ({len(o['kanit'])}/{o['en_az']} adres)"


def durumlar(yol: dict, bulgular: dict[str, str] | None = None) -> dict[str, dict]:
    bulgular = acilis._rafine_bulgulari() if bulgular is None else bulgular
    adimlar = {a["kimlik"]: a for a in yol["adimlar"]}
    sonuc: dict[str, dict] = {}

    def hesapla(kimlik: str, yigin: tuple = ()) -> str:
        if kimlik in sonuc:
            return sonuc[kimlik]["durum"]
        if kimlik in yigin or kimlik not in adimlar:
            return "onkosul-bekliyor"
        adim = adimlar[kimlik]
        sonuclar = [(olcut(o, bulgular)) for o in adim["olcutler"]]
        onkosul = [hesapla(k, yigin + (kimlik,)) for k in adim["onkosul"]]
        if all(ok for ok, _ in sonuclar):
            durum = "tamam"
        elif not adim["zorunlu"]:
            durum = "ufukta"
        elif any(d != "tamam" for d in onkosul):
            durum = "onkosul-bekliyor"
        elif adim["karar"] and adim["karar"]["verildi"] is None:
            durum = "karar-bekliyor"
        elif all(o["tur"] == "elle" for o in adim["olcutler"]):
            durum = "disaridan-bekleniyor"
        else:
            durum = "atilabilir"
        sonuc[kimlik] = {"durum": durum, "olcutler": [{"tarif": t, "karsilaniyor": ok} for ok, t in sonuclar]}
        return durum

    for a in yol["adimlar"]:
        hesapla(a["kimlik"])
    return sonuc


def denetle(yol: dict, veri_acilis: dict | None = None, bulgular: dict[str, str] | None = None,
            senaryolar: set[str] | None = None) -> list[str]:
    hatalar = [f"sözleşme: {h}" for h in sema_denetle.dogrula(sema_denetle.sema_yukle("yol"), yol)]
    if hatalar:
        return hatalar
    veri_acilis = _acilis() if veri_acilis is None else veri_acilis
    bulgular = acilis._rafine_bulgulari() if bulgular is None else bulgular
    senaryolar = acilis._senaryolar() if senaryolar is None else senaryolar
    adimlar = yol["adimlar"]
    if [a["no"] for a in adimlar] != list(range(len(adimlar))):
        hatalar.append("adimlar: numaralar 0'dan sırayla olmalı")
    kimlikler = [a["kimlik"] for a in adimlar]
    for k in sorted({k for k in kimlikler if kimlikler.count(k) > 1}):
        hatalar.append(f"adimlar: '{k}' kimliği birden çok kez")
    for a in adimlar:
        konum = f"adimlar[{a['no']}] {a['kimlik']}"
        for k in a["onkosul"]:
            if k not in kimlikler:
                hatalar.append(f"{konum}: ön koşul yok ({k})")
        for b in a.get("bulgular", []):
            if b not in bulgular:
                hatalar.append(f"{konum}: bulgu rafine kayıtlarında yok ({b})")
        for s in a.get("senaryolar", []):
            if s not in senaryolar:
                hatalar.append(f"{konum}: senaryo kaydında yok ({s})")
        for i, o in enumerate(a["olcutler"]):
            eksik = [alan for alan in OLCUT_ALANLARI[o["tur"]] if alan not in o]
            fazla = sorted(set(o) - {"tur"} - set(OLCUT_ALANLARI[o["tur"]]))
            if eksik or fazla:
                hatalar.append(f"{konum}.olcutler[{i}]: '{o['tur']}' için eksik {eksik} / fazla {fazla}")
    # döngü
    komsu = {a["kimlik"]: [k for k in a["onkosul"] if k in kimlikler] for a in adimlar}
    renk: dict[str, int] = {}

    def gez(k: str) -> bool:
        renk[k] = 1
        for n in komsu[k]:
            if renk.get(n) == 1 or (renk.get(n) is None and gez(n)):
                return True
        renk[k] = 2
        return False
    if any(renk.get(k) is None and gez(k) for k in komsu):
        hatalar.append("adimlar: ön koşullarda döngü var")
        return hatalar
    if hatalar:
        return hatalar
    hesap = durumlar(yol, bulgular)
    ada = {a["kimlik"]: a for a in adimlar}
    for a in adimlar:
        if hesap[a["kimlik"]]["durum"] == "tamam":
            for k in a["onkosul"]:
                if hesap[k]["durum"] != "tamam":
                    hatalar.append(f"adimlar[{a['no']}] {a['kimlik']}: tamam görünüyor ama ön koşulu '{k}' tamam değil")
    for ilke in veri_acilis["ilkeler"]:
        bagli = [a for a in adimlar if ilke["no"] in a["ilkeler"] and a["zorunlu"]]
        acik = [a["kimlik"] for a in bagli if hesap[a["kimlik"]]["durum"] != "tamam"]
        ad = f"{ilke['no']}. ilke ({ilke['ad']})"
        if ilke["durum"] == "uygulanıyor" and acik:
            hatalar.append(f"{ad}: açılışta tam işliyor ama yolda açık zorunlu adımı var ({', '.join(acik)})")
        if ilke["durum"] != "uygulanıyor":
            if not bagli:
                hatalar.append(f"{ad}: açılışta '{ilke['durum']}' ama yolda zorunlu adımı yok")
            elif not acik:
                hatalar.append(f"{ad}: yoldaki bütün zorunlu adımları tamam; açılıştaki durum 'uygulanıyor' olarak güncellenmeli")
    turler = {c["tur"] for c in yol["cizimler"]}
    for tur in ("ressam", "mimar", "muhendis"):
        if tur not in turler:
            hatalar.append(f"cizimler: {CIZIM_TURU[tur]} yok")
    ck = [c["kimlik"] for c in yol["cizimler"]]
    for k in sorted({k for k in ck if ck.count(k) > 1}):
        hatalar.append(f"cizimler: '{k}' kimliği birden çok kez")
    bolumler = {"belge": {"varilacak_yer", "plan"}, "teknik": {"akis"}}
    for c in yol["cizimler"]:
        if c["bolum"] not in bolumler[c["yer"]]:
            hatalar.append(f"cizimler: '{c['kimlik']}' için bölüm '{c['bolum']}' {c['yer']} belgesinde yok")
        hatalar += cizim.denetle(f"çizim {c['kimlik']}", _blok(c["metin"]))
    del ada
    return hatalar


# ---------- üretim ----------

def _blok(metin: str) -> str:
    return "```text\n" + metin.rstrip("\n") + "\n```"


def _cizim(c: dict) -> list[str]:
    return [f"**{c['baslik']}** · {CIZIM_TURU[c['tur']]}", _blok(c["metin"])]


def _ilke_adlari(veri_acilis: dict) -> dict[int, str]:
    return {i["no"]: i["ad"] for i in veri_acilis["ilkeler"]}


def agac(yol: dict, hesap: dict[str, dict], genislik: int = cizim.EN_GENIS) -> str:
    """Yolun ağacı: her adım ilk ön koşulunun altında; sağda hesaplanan durum."""
    adimlar = {a["kimlik"]: a for a in yol["adimlar"]}
    cocuk: dict[str | None, list[str]] = {}
    for a in yol["adimlar"]:
        cocuk.setdefault(a["onkosul"][0] if a["onkosul"] else None, []).append(a["kimlik"])
    sutun = genislik - 12
    satirlar = []

    def isaret(k: str) -> str:
        d = hesap[k]["durum"]
        return ("■ " if d == "tamam" else "◇ " if d == "ufukta" else "□ ") + KISA_DURUM[d]

    def yaz(k: str, onek: str, kok: bool, son: bool) -> None:
        a = adimlar[k]
        bas = "" if kok else ("└─▶ " if son else "├─▶ ")
        ek = "" if len(a["onkosul"]) < 2 else f" (+{len(a['onkosul']) - 1})"
        etiket = f"{onek}{bas}({a['no']}) {a['ad']}{ek}"
        if len(etiket) > sutun - 1:
            etiket = etiket[:sutun - 2] + "…"
        satirlar.append(etiket.ljust(sutun) + isaret(k))
        alt = cocuk.get(k, [])
        for i, c in enumerate(alt):
            yeni = onek + ("" if kok else ("    " if son else "│   "))
            yaz(c, yeni if not kok else onek + " ", False, i == len(alt) - 1)

    for k in cocuk.get(None, []):
        yaz(k, "  ", True, True)
    return "\n".join(satirlar)


def gosterge(yol: dict, veri_acilis: dict, hesap: dict[str, dict]) -> str:
    """İlkelerin göstergesi: her ilkeye bağlı adımlar (■ biten, □ açık, ◇ ufuk) ve açılıştaki durum."""
    satirlar = ["  " + "ilke".ljust(34) + "  " + "adımlar".ljust(8) + "  açılışta", "  " + "─" * 34 + "  " + "─" * 8 + "  " + "─" * 16]
    for ilke in veri_acilis["ilkeler"]:
        hucre = ""
        for a in yol["adimlar"]:
            if ilke["no"] in a["ilkeler"]:
                d = hesap[a["kimlik"]]["durum"]
                hucre += "■" if d == "tamam" else ("◇" if d == "ufukta" else "□")
        ad = f"{ilke['no']} {ilke['ad']}"
        if len(ad) > 34:
            ad = ad[:33] + "…"
        satirlar.append(f"  {ad.ljust(34)}  {hucre.ljust(8)}  {acilis.SADE_DURUM[ilke['durum']]}")
    return "\n".join(satirlar)


AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


def _tarih(gun: str) -> str:
    """2026-10-28 → 28 Ekim 2026."""
    yil, ay, g = gun.split("-")
    return f"{int(g)} {AYLAR[int(ay) - 1]} {yil}"


def _ne_zaman(a: dict, adlar: dict[str, str], hesap: dict[str, dict]) -> str:
    biten = [adlar[k] for k in a["onkosul"] if hesap[k]["durum"] == "tamam"]
    bekleyen = [adlar[k] for k in a["onkosul"] if hesap[k]["durum"] != "tamam"]
    parcalar = []
    if bekleyen:
        parcalar.append("Önce şu adımın bitmesi gerekiyor: " + ", ".join(bekleyen) + ".")
    if biten:
        parcalar.append("Ön koşulu bitti: " + ", ".join(biten) + ".")
    metin = " ".join(parcalar) if parcalar else "Bir ön koşulu yok."
    if a["karar"]:
        if a["karar"]["verildi"] is None:
            metin += f" Ayrıca {a['karar']['kim']}'un bir karar vermesi gerekiyor. {a['karar']['soru']}"
            g = a["karar"].get("gorus")
            if g:
                metin += f" Görüş ({g['kimden']}, {_tarih(g['tarih'])}). {g['oneri']} {g['ozet']} Karar yine {a['karar']['kim']}'ta."
        else:
            metin += f" {a['karar']['kim']} kararını verdi: {a['karar']['verildi']['yanit']}"
    return metin


def _ne_icin(a: dict, ilke_adlari: dict[int, str]) -> str:
    adlar = [f"{n}. ilke ({ilke_adlari[n]})" for n in a["ilkeler"]]
    return ("Bu adım şu ilkeye hizmet eder: " if len(adlar) == 1 else "Bu adım şu ilkelere hizmet eder: ") + ", ".join(adlar) + "."


def _ozet(yol: dict, veri_acilis: dict, hesap: dict[str, dict]) -> str:
    durumlar_ = [i["durum"] for i in veri_acilis["ilkeler"]]
    s = SAYI_IYELIK
    metin = (f"Bugün altı ilkenin {s[durumlar_.count('uygulanıyor')]} tam olarak işliyor, "
             f"{s[durumlar_.count('kısmen')]} kısmen işliyor.")
    adimlar = yol["adimlar"]
    d = [hesap[a["kimlik"]]["durum"] for a in adimlar]
    tam, ufuk = d.count("tamam"), d.count("ufukta")
    metin += f" Yolun {SAYI_ADI[len(adimlar)]} adımından {s[tam]} tamam, {s[len(adimlar) - tam - ufuk]} açık"
    metin += f", {s[ufuk]} ufukta." if ufuk else "."
    atilabilir = [a["ad"] for a in adimlar if hesap[a["kimlik"]]["durum"] == "atilabilir"]
    karar = [a["ad"] for a in adimlar if hesap[a["kimlik"]]["durum"] == "karar-bekliyor"]
    if atilabilir:
        metin += " Şu an atılabilecek adım: " + ", ".join(atilabilir) + "."
    if karar:
        metin += (" Kararı bekleyen adım: " if len(karar) == 1 else " Kararı bekleyen adımlar: ") + ", ".join(karar) + "."
    onkosul = [a["ad"] for a in adimlar if hesap[a["kimlik"]]["durum"] == "onkosul-bekliyor"]
    disaridan = [a["ad"] for a in adimlar if hesap[a["kimlik"]]["durum"] == "disaridan-bekleniyor"]
    if onkosul:
        metin += (" Bir ön koşulun bitmesini bekleyen adım: " if len(onkosul) == 1
                  else " Bir ön koşulun bitmesini bekleyen adımlar: ") + ", ".join(onkosul) + "."
    if disaridan:
        metin += (" Dışarıdan birinin gelmesini bekleyen adım: " if len(disaridan) == 1
                  else " Dışarıdan birinin gelmesini bekleyen adımlar: ") + ", ".join(disaridan) + "."
    return metin


def _sozluk(veri_acilis: dict, metin: str) -> list[str]:
    gorunen = acilis._kucuk(acilis._gorunen(cizim.cizimsiz(metin)))
    gecenler = [m for m in veri_acilis["sozluk"] if any(acilis._kucuk(p) in gorunen for p in m["terim"].split(" ve "))]
    if not gecenler:
        return []
    return ["## Birkaç kelime",
            "Bu sayfada geçen birkaç kelime: " + " ".join(f"**{m['terim']}:** {m['anlam']}" for m in gecenler)]


def belge(yol: dict, veri_acilis: dict, hesap: dict[str, dict]) -> str:
    adlar = {a["kimlik"]: a["ad"] for a in yol["adimlar"]}
    ilke_adlari = _ilke_adlari(veri_acilis)
    cizimler = {c["bolum"]: c for c in yol["cizimler"] if c["yer"] == "belge"}
    p = list(yol["giris"])
    p += ["## Bugün nerede duruyoruz", _ozet(yol, veri_acilis, hesap),
          "Aşağıdaki gösterge her ilkeye bağlı adımları sayar. Dolu kare biten, boş kare açık, eşkenar dörtgen ufuktaki adımı gösterir.",
          "**İlkelerin göstergesi** · mühendis çizimi", _blok(gosterge(yol, veri_acilis, hesap))]
    p += ["## Varılacak yer"] + yol["varilacak_yer"] + _cizim(cizimler["varilacak_yer"])
    p += ["## Yapının planı"] + yol["plan"] + _cizim(cizimler["plan"])
    p += ["## Adımlar",
          f"Yol {SAYI_ADI[len(yol['adimlar'])]} adımdan oluşuyor. Aşağıdaki ağaçta her adım, bitmesini beklediği adımın altında duruyor. "
          "Sağdaki işaret adımın bugünkü durumunu gösteriyor.",
          "**Yolun ağacı** · mühendis çizimi", _blok(agac(yol, hesap))]
    for a in yol["adimlar"]:
        s = a["sade"]
        p += [f"### {a['no']}. {a['ad']}",
              f"**Durum:** {DURUM_METNI[hesap[a['kimlik']]['durum']]}",
              f"**Ne?** {s['ne']}", f"**Neden?** {s['neden']}", f"**Nerede?** {s['nerede']}",
              f"**Nereden nereye?** {s['yon']}", f"**Nasıl?** {s['nasil']}",
              f"**Ne zaman?** {_ne_zaman(a, adlar, hesap)}", f"**Ne için?** {_ne_icin(a, ilke_adlari)}",
              f"**Ne kadar?** {BUYUKLUK[a['buyukluk']]}", f"**Bitince:** {s['sonra']}"]
    p += ["## Bu yol nasıl izlenir"] + yol["izleme"]
    p += ["## Siz ne yapabilirsiniz"] + yol["okur"]
    p += _sozluk(veri_acilis, "\n\n".join(p))
    return "\n\n".join(p) + "\n"


def _hucre(metin: str) -> str:
    return metin.replace("|", "\\|").replace("\n", " ")


def teknik_belge(yol: dict, veri_acilis: dict, hesap: dict[str, dict]) -> str:
    adlar = {a["kimlik"]: a["ad"] for a in yol["adimlar"]}
    p = list(yol["teknik_giris"])
    satirlar = ["| Adım | İlkeler | Ön koşul | Karar | Yön | Büyüklük | Bulgu, senaryo | Durum |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for a in yol["adimlar"]:
        karar = "—" if not a["karar"] else (f"{a['karar']['kim']}: bekliyor" if a["karar"]["verildi"] is None
                                           else f"{a['karar']['kim']}: {a['karar']['verildi']['tarih']}")
        bag = ", ".join(a.get("bulgular", []) + a.get("senaryolar", [])) or "—"
        satirlar.append(f"| {a['no']}. {a['ad']} (`{a['kimlik']}`) | {', '.join(map(str, a['ilkeler']))}"
                        f"{'' if a['zorunlu'] else ' (ufuk)'} | {', '.join(a['onkosul']) or '—'} | {karar} | "
                        f"{_hucre(a['teknik']['yon'])} | {a['buyukluk']} | {bag} | {hesap[a['kimlik']]['durum']} |")
    p += ["## Adımlar", "\n".join(satirlar),
          "**Yolun ağacı** · mühendis çizimi", _blok(agac(yol, hesap)),
          "**İlkelerin göstergesi** · mühendis çizimi", _blok(gosterge(yol, veri_acilis, hesap))]
    for a in yol["adimlar"]:
        t = a["teknik"]
        p += [f"### {a['no']}. {a['ad']}", t["nasil"],
              "Dokunacağı yerler: " + ", ".join(f"`{y}`" for y in t["nerede"]) + ".",
              f"Geri alma: {t['geri_alma']}"]
        if a["karar"]:
            p.append(f"Karar ({a['karar']['kim']}): {a['karar']['soru']}")
            g = a["karar"].get("gorus")
            if g:
                p.append(f"Görüş ({g['kimden']}, {g['tarih']}): {g['oneri']} {g['gerekce']}")
        sat = ["| Ölçüt | Bugün |", "| --- | --- |"]
        for o in hesap[a["kimlik"]]["olcutler"]:
            sat.append(f"| {_hucre(o['tarif'])} | {'karşılanıyor' if o['karsilaniyor'] else 'karşılanmıyor'} |")
        p.append("\n".join(sat))
    p += ["## Akışlar", "Gelen kutusu ve yanıt adımları tamamlandığında bir katkının izleyeceği yol aşağıdadır. "
          "Parantez içindeki sayılar o geçişi koruyan ilkedir."]
    for c in yol["cizimler"]:
        if c["yer"] == "teknik":
            p += _cizim(c)
    p += ["## Kurallar",
          "Adımın durumu kayda yazılmaz; ölçütlerden hesaplanır. Tamam olan bir adımın ön koşulları da tamam olmalıdır. "
          "Açılışta tam işlemeyen her ilkenin en az bir zorunlu adımı vardır. Bir ilkenin bütün zorunlu adımları bittiğinde "
          "açılıştaki durumu `uygulanıyor` olarak güncellenmeden denetim geçmez; tam işleyen bir ilkeye bağlı açık zorunlu adım kalamaz.",
          "Yeni bir adım eklemek için kayda bir adım nesnesi yazılır: bağlı ilkeler, ön koşullar, gerekiyorsa karar, sade ve teknik "
          "anlatım, geri alma yolu ve en az bir ölçüt. Ölçüt türleri: " + ", ".join(f"`{k}`" for k in OLCUT_ALANLARI) + ". "
          "Sonra `python tools/yol.py` iki belgeyi yeniden yazar."]
    del adlar
    return "\n\n".join(p) + "\n"


def bloklar(yol: dict, veri_acilis: dict, hesap: dict[str, dict]) -> dict[Path, dict[str, str]]:
    return {BELGE: {"yol": acilis._ayir(belge(yol, veri_acilis, hesap))},
            TEKNIK: {"yol_teknik": acilis._ayir(teknik_belge(yol, veri_acilis, hesap))}}


def okunabilirlik_denetle(veri_acilis: dict, metin: str) -> list[str]:
    terimler = [m["terim"] for m in veri_acilis["sozluk"]]
    return acilis.okunabilirlik("docs/yol.md", metin, terimler, ayrim_bagi=True) + cizim.denetle("docs/yol.md", metin)


def main() -> int:
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    kip = parser.add_mutually_exclusive_group()
    kip.add_argument("--check", action="store_true", help="yazmadan denetle")
    kip.add_argument("--durum", action="store_true", help="adımların hesaplanan durumunu JSON olarak yaz")
    args = parser.parse_args()
    yol = json.loads(KAYIT.read_text(encoding="utf-8"))
    veri_acilis = _acilis()
    hatalar = denetle(yol, veri_acilis)
    if not hatalar:
        hesap = durumlar(yol)
        if args.durum:
            print(json.dumps({a["kimlik"]: dict(no=a["no"], ad=a["ad"], **hesap[a["kimlik"]]) for a in yol["adimlar"]},
                             ensure_ascii=False, indent=2))
            return 0
        for hedef, uretilen in bloklar(yol, veri_acilis, hesap).items():
            metin = hedef.read_text(encoding="utf-8") if hedef.is_file() else ""
            if not args.check and metin:
                yeni = acilis.belge_guncelle(metin, uretilen)
                if yeni != metin:
                    hedef.write_text(yeni, encoding="utf-8", newline="\n")
                    metin = yeni
            hatalar += acilis.belge_denetle(hedef.relative_to(KOK).as_posix(), metin, uretilen)
        if BELGE.is_file():
            hatalar += okunabilirlik_denetle(veri_acilis, BELGE.read_text(encoding="utf-8"))
    for hata in hatalar:
        print(hata)
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/yol.py")
        return 1
    d = [hesap[a["kimlik"]]["durum"] for a in yol["adimlar"]]
    print(f"TAMAM: {len(d)} adım ({d.count('tamam')} tamam, {d.count('atilabilir')} atılabilir, "
          f"{d.count('karar-bekliyor')} karar, {d.count('onkosul-bekliyor')} ön koşul, "
          f"{d.count('disaridan-bekleniyor')} dışarıdan, {d.count('ufukta')} ufukta); açılışla tutarlı, "
          "iki belge kayıtla uyumlu, yol sayfası sade.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
