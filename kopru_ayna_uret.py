#!/usr/bin/env python3
"""Kanonik kopru.html'den ayna sürümünü üretir (ayna/kopru.html): dış iskelet (doctype, html, head, body etiketleri)
çıkarılır; title, meta ve style korunur; gövde olduğu gibi kalır. Yayım aracı iskeleti kendi ekler.
Kullanım: python3 kopru_ayna_uret.py kopru.html ayna/kopru.html
kopru_gonder.ps1 her gönderimden önce bunu çalıştırır; ayna böylece kanonik dosyanın gerisinde kalmaz."""
import os, re, sys


def uret(kaynak, hedef):
    t = open(kaynak, encoding="utf-8").read()
    head = re.search(r"<head>(.*?)</head>", t, re.S).group(1)
    body = re.search(r"<body>(.*?)</body>", t, re.S).group(1)
    title = re.search(r"<title>.*?</title>", head, re.S).group(0)
    metas = [m for m in re.findall(r"<meta [^>]*>", head) if "charset" not in m and 'name="viewport"' not in m]
    style = re.search(r"<style>.*?</style>", head, re.S).group(0)
    out = title + "\n" + "\n".join(metas) + "\n" + style + "\n" + body.strip() + "\n"
    if re.search(r'(src|href)="https?://(?!github\.com|raw\.githubusercontent\.com|halukainrs\.github\.io|claude\.ai)', out):
        print("UYARI: aynada beklenmeyen dış adres var", file=sys.stderr)
    os.makedirs(os.path.dirname(os.path.abspath(hedef)), exist_ok=True)
    eski = open(hedef, encoding="utf-8").read() if os.path.exists(hedef) else None
    if eski == out:
        print(f"ayna güncel: {hedef}")
        return False
    with open(hedef, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    print(f"ayna yenilendi: {hedef} ({len(out)} karakter)")
    return True


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    uret(sys.argv[1], sys.argv[2])
