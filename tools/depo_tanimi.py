#!/usr/bin/env python3
"""Dokuz koordinatlı depo tanımını (docs/depo-tanimi.json) depodan ölçer ve denetler.

Tanımın anlatı kısmı elle yazılır; "Ne kadar" koordinatının ölçümleri ise bu araçla
depodan üretilir. --check yazmadan şunları denetler: tanım sözleşmesine uyum, ölçümlerin
çalışma ağacıyla eşliği, depo içi dayanak yollarının varlığı ve "Ne zaman" koordinatındaki
defter zamanlarının kopru.html ile eşliği. Böylece tanım sessizce eskiyemez.

Ölçümler platformdan bağımsızdır: dosya listesi Git'ten alınır, bayt ve satır sayıları
CRLF→LF normalleştirilerek hesaplanır, testler çalıştırılmadan AST ile sayılır.

Kullanım:
    python tools/depo_tanimi.py            # ölçümleri yenile (yalnız ne_kadar.olcumler yazılır)
    python tools/depo_tanimi.py --check    # yazmadan denetle; uyumsuzlukta çıkış 1
    python tools/depo_tanimi.py --olc      # ölçümleri JSON olarak yazdır
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import subprocess
import sys

KOK = Path(__file__).resolve().parents[1]
TANIM = KOK / "docs" / "depo-tanimi.json"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK))
sys.path.insert(0, str(KOK / "tools"))

from kopru_oku import Ayristirici  # noqa: E402
import dogrula  # noqa: E402
import okuma_yayini_uret  # noqa: E402
import sema_denetle  # noqa: E402

KOORDINATLAR = ("ne", "nerede", "ne_zaman", "ne_kadar", "nereden", "neden", "nasil", "ne_icin", "nereye")


def _dosyalar() -> list[str]:
    cikti = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=KOK)
    return sorted(ad for ad in set(cikti.decode("utf-8").split("\0")) if ad and (KOK / ad).is_file())


def _bayt(yol: Path) -> bytes:
    return yol.read_bytes().replace(b"\r\n", b"\n")


def _satir(yol: Path) -> int:
    return len(_bayt(yol).decode("utf-8-sig").splitlines())


def _test_yontemi(yol: Path) -> int:
    agac = ast.parse(_bayt(yol).decode("utf-8-sig"), filename=str(yol))
    return sum(1 for sinif in ast.walk(agac) if isinstance(sinif, ast.ClassDef)
               for oge in sinif.body
               if isinstance(oge, (ast.FunctionDef, ast.AsyncFunctionDef)) and oge.name.startswith("test"))


def olc() -> dict[str, int | str]:
    """Depoyu ölçer; aynı ağaçta her platformda aynı değerleri verir."""
    dosyalar = _dosyalar()
    python = [ad for ad in dosyalar if ad.endswith(".py")]
    paket = [ad for ad in python if ad.startswith("src/ortak_kopru/")]
    testler = [ad for ad in python if Path(ad).name.startswith("test_")]
    gunlukler = [ad for ad in dosyalar if ad.startswith("kayit/") and ad.endswith(".md") and ad != "kayit/README.md"]

    belge = (KOK / "kopru.html").read_text(encoding="utf-8")
    ayristirici = Ayristirici()
    ayristirici.feed(belge)
    ayristirici.close()
    kayitlar = ayristirici.kayitlar
    guncelleme = re.search(r'id="son-guncelleme" datetime="([^"]+)"', belge)

    bulgular = []
    for yol in sorted((KOK / "docs" / "rafine").glob("*.json")):
        bulgular.extend(json.loads(yol.read_text(encoding="utf-8"))["findings"])

    return {
        "izlenen_dosya": len(dosyalar),
        "python_dosyasi": len(python),
        "python_satiri": sum(_satir(KOK / ad) for ad in python),
        "paket_modulu": len(paket),
        "paket_satiri": sum(_satir(KOK / ad) for ad in paket),
        "test_dosyasi": len(testler),
        "test_yontemi": sum(_test_yontemi(KOK / ad) for ad in testler),
        "json_sozlesmesi": sum(1 for ad in dosyalar if ad.startswith("schemas/") and ad.endswith(".schema.json")),
        "is_akisi": sum(1 for ad in dosyalar if ad.startswith(".github/workflows/")),
        "powershell_betigi": sum(1 for ad in dosyalar if ad.endswith(".ps1")),
        "belge": sum(1 for ad in dosyalar if ad.startswith("docs/") and ad.endswith(".md")),
        "okuma_sayfasi": len(okuma_yayini_uret.PAGES),
        "dogrulama_kontrolu": len(dogrula.KONTROLLER),
        "kopru_kaydi": len(kayitlar),
        "acik_durumlu_kayit": sum(1 for kayit in kayitlar if kayit["durum"] == "acik"),
        "yanit_bagli_kayit": sum(1 for kayit in kayitlar if kayit["yanit"]),
        "ilk_kayit_zamani": kayitlar[0]["zaman"] if kayitlar else "yok",
        "son_kayit_zamani": kayitlar[-1]["zaman"] if kayitlar else "yok",
        "defter_son_guncelleme": guncelleme.group(1) if guncelleme else "yok",
        "defter_bayti": len(_bayt(KOK / "kopru.html")),
        "cagri_gunlugu": len(gunlukler),
        "cagri_gunlugu_bayti": sum(len(_bayt(KOK / ad)) for ad in gunlukler),
        "rafine_bulgusu": len(bulgular),
        "rafine_duzeltilen": sum(1 for bulgu in bulgular if bulgu["resolution"] == "düzeltildi"),
        "rafine_acik": sum(1 for bulgu in bulgular if bulgu["resolution"] in ("açık", "doğrulanmadı")),
    }


def dayanak_yolu(dayanak: str) -> Path | None:
    """Depo içi dayanağın yolunu döndürür; https adresleri için None."""
    if dayanak.startswith(("https://", "http://")):
        return None
    yol = re.split(r"[#:]", dayanak, maxsplit=1)[0].strip()
    return KOK / yol


def denetle(tanim: dict, olcum: dict) -> list[str]:
    sema = sema_denetle.sema_yukle("depo-tanimi")
    hatalar = [f"sözleşme: {hata}" for hata in sema_denetle.dogrula(sema, tanim)]
    if hatalar:
        return hatalar
    kayitli = tanim["koordinatlar"]["ne_kadar"].get("olcumler", {})
    for anahtar in sorted(set(kayitli) | set(olcum)):
        if kayitli.get(anahtar) != olcum.get(anahtar):
            hatalar.append(f"ne_kadar.olcumler.{anahtar}: kayıtlı {kayitli.get(anahtar)!r}, ölçülen {olcum.get(anahtar)!r}")
    defter_zamanlari = {olcum.get("ilk_kayit_zamani"), olcum.get("son_kayit_zamani"), olcum.get("defter_son_guncelleme")}
    for sira, oge in enumerate(tanim["koordinatlar"]["ne_zaman"]["ogeler"]):
        if oge.get("dayanak") == "kopru.html" and oge.get("zaman") not in defter_zamanlari:
            hatalar.append(f"ne_zaman.ogeler[{sira}].zaman: {oge.get('zaman')!r} defterdeki zamanlarla eşleşmiyor")
    for koordinat in KOORDINATLAR:
        for sira, oge in enumerate(tanim["koordinatlar"][koordinat]["ogeler"]):
            yol = dayanak_yolu(oge.get("dayanak", "https://"))
            if yol is not None and not yol.exists():
                hatalar.append(f"{koordinat}.ogeler[{sira}].dayanak: depoda yok ({oge['dayanak']})")
    return hatalar


def main() -> int:
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    kip = parser.add_mutually_exclusive_group()
    kip.add_argument("--check", action="store_true", help="yazmadan denetle")
    kip.add_argument("--olc", action="store_true", help="yalnız ölçümleri yazdır")
    args = parser.parse_args()
    olcum = olc()
    if args.olc:
        print(json.dumps(olcum, ensure_ascii=False, indent=2))
        return 0
    tanim = json.loads(TANIM.read_text(encoding="utf-8"))
    if not args.check:
        tanim["koordinatlar"]["ne_kadar"]["olcumler"] = olcum
        TANIM.write_text(json.dumps(tanim, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    hatalar = denetle(tanim, olcum)
    for hata in hatalar:
        print(hata)
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/depo_tanimi.py")
        return 1
    print(f"TAMAM: dokuz koordinat, {len(olcum)} ölçüm ve bütün depo içi dayanaklar tutarlı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
