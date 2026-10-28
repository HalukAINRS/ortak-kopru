#!/usr/bin/env python3
"""Tarihsel tek iş aracı (24 Ekim 2026): “Yerel ikili, önbellek ve tarayıcı profili kanıtları” tablosundaki models_cache.json satırına Haluk'un k-0021'de
bildirdiği güncel durum notunu ekler (bir kez; varsa dokunmaz). Kayıtlara dokunmaz.
Kullanım: python3 defter/kanit_satiri_guncelle.py kopru.html            # ekler
          python3 defter/kanit_satiri_guncelle.py kopru.html --kontrol  # yalnız satırı gösterir"""
import os, re, sys, tempfile

NOT = '<b>[k-0008/k-0012 Güncel Durum: Seçilmiş Emanet Denetimi + xhigh kilidi]</b> '


def main():
    if any(arg in ("-h", "--help") for arg in sys.argv[1:]):
        print(__doc__)
        return
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    yol = sys.argv[1]; kontrol = "--kontrol" in sys.argv
    t = open(yol, encoding="utf-8").read()
    b = re.search(r'<div id="y-yerel-kanitlar" class="alt">.*?\n  </div>\n', t, re.S)
    if not b:
        sys.exit("HATA: y-yerel-kanitlar bölümü yok.")
    bolum = b.group(0)
    m = re.search(r"<tr>(<td>[^<]*<code>models_cache\.json</code>[^<]*</td>)<td>(.*?)</td>", bolum, re.S)
    if not m:
        sys.exit("HATA: models_cache.json satırı bulunamadı.")
    satir = m.group(0)
    print("satır:", re.sub(r"<[^>]+>", "", satir)[:200])
    if "Seçilmiş Emanet" in satir:
        print("zaten güncel; değişiklik yok."); return
    if kontrol:
        print("not yok; --kontrol olmadan çalıştırınca eklenir."); return
    yeni_satir = satir.replace("</td><td>", "</td><td>" + NOT, 1)
    yeni_bolum = bolum.replace(satir, yeni_satir, 1)
    yeni = t[:b.start()] + yeni_bolum + t[b.end():]
    fd, gecici = tempfile.mkstemp(prefix="kopru-", suffix=".html", dir=os.path.dirname(os.path.abspath(yol)))
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(yeni)
    os.replace(gecici, yol)
    print("eklendi: models_cache.json satırının ikinci hücresinin başına not kondu.")


if __name__ == "__main__":
    main()
