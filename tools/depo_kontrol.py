#!/usr/bin/env python3
"""Depo bütünlüğünü çevrimdışı, dosya yazmadan ve sağlayıcı çağırmadan denetler.

Denetlenenler: Python sözdizimi, JSON dosyaları, defterdeki kayıt kimliklerinin tekilliği ve sırası, yanıt bağları,
görünür sayaç, kayıt ekleyicinin içerik kuralları (yasak desen, dış yükleme), aynanın defterle eşliği ve
katılımcı ayarlarındaki çağrı yollarının imzaları.

Kullanım:
    python tools/depo_kontrol.py      # her şeyi denetler; sorun varsa çıkış 1
"""
import ast
import json
from pathlib import Path
import re
import subprocess
import sys

KOK = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK / "defter"))

from kopru_ayna_uret import uret  # noqa: E402
from kopru_ekle import ISARET, KATILIMCILAR, dis_yukleme_kontrol, yasak_kontrol  # noqa: E402
from kopru_oku import Ayristirici  # noqa: E402
from kopru_yanitla import yol_kimligi  # noqa: E402


def denetle():
    hatalar = []
    yollar = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=KOK
    ).decode("utf-8").split("\0")
    py_sayisi = json_sayisi = 0
    for ad in sorted(set(yollar) - {""}):
        yol = KOK / ad
        if yol.suffix not in {".py", ".json"}:
            continue
        try:
            metin = yol.read_text(encoding="utf-8-sig")
            if yol.suffix == ".py":
                ast.parse(metin, filename=ad)
                py_sayisi += 1
            else:
                json.loads(metin)
                json_sayisi += 1
        except (OSError, SyntaxError, ValueError) as exc:
            hatalar.append(f"{ad}: {type(exc).__name__}")

    belge = (KOK / "kopru.html").read_text(encoding="utf-8")
    ay = Ayristirici()
    ay.feed(belge)
    ay.close()
    idler = [k["id"] for k in ay.kayitlar]
    html_idler = re.findall(r'<article class="kayit" id="(k-\d{4})"', belge)
    if belge.count(ISARET) != 1:
        hatalar.append("kopru.html: tek kayıt sonu işareti gerekli")
    if idler != html_idler or len(idler) != len(set(idler)):
        hatalar.append("kopru.html: kayıt ayrıştırması veya kimlik tekilliği bozuk")
    if idler != [f"k-{i:04d}" for i in range(1, len(idler) + 1)]:
        hatalar.append("kopru.html: kayıt numaraları sıralı ve kesintisiz değil")
    oncekiler = set()
    for kayit in ay.kayitlar:
        if kayit["yanit"] and kayit["yanit"] not in oncekiler:
            hatalar.append(f"{kayit['id']}: yanıt bağı önceki gerçek bir kaydı göstermiyor")
        oncekiler.add(kayit["id"])
    sayac = re.search(r'<b id="kayit-sayisi">(\d+)</b>', belge)
    if not sayac or int(sayac[1]) != len(idler):
        hatalar.append("kopru.html: görünür kayıt sayacı gerçek kayıtlarla eşleşmiyor")
    if dis_yukleme_kontrol(belge):
        hatalar.append("kopru.html: dış kaynak yüklemesi var")
    if yasak_kontrol(belge):
        hatalar.append("kopru.html: yasak desen var")
    try:
        uret(KOK / "kopru.html", KOK / "ayna/kopru.html", kontrol=True)
    except (OSError, ValueError) as exc:
        hatalar.append(str(exc))

    for ad in ("katilimcilar/ayarlar.json", "katilimcilar/ayarlar-yerel.json"):
        try:
            ayarlar = json.loads((KOK / ad).read_text(encoding="utf-8"))
            for kat in ayarlar["katilimcilar"]:
                for yol in [kat] + ([kat["yedek"]] if kat.get("yedek") else []):
                    imza = yol_kimligi(kat["ad"], kat, yol)
                    if imza.split(" ")[0].split("(")[0] not in KATILIMCILAR:
                        hatalar.append(f"{ad}: kayıt ekleyicinin kabul etmediği üretici imzası")
        except (OSError, KeyError, TypeError, ValueError) as exc:
            hatalar.append(f"{ad}: çağrı yolu doğrulanamadı ({type(exc).__name__})")

    for hata in hatalar:
        print(f"HATA: {hata}", file=sys.stderr)
    if hatalar:
        return 1
    print(f"TAMAM: {py_sayisi} Python, {json_sayisi} JSON; {len(idler)} kayıt, yanıt bağları, sayaç, ayna ve imzalar tutarlı.")
    return 0


if __name__ == "__main__":
    if any(arg in ("-h", "--help") for arg in sys.argv[1:]):
        print(__doc__)
        sys.exit(0)
    sys.exit(denetle())
