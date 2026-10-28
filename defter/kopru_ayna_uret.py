#!/usr/bin/env python3
"""Kanonik kopru.html'den ayna sürümünü üretir (ayna/kopru.html): dış iskelet (doctype, html, head, body etiketleri)
çıkarılır; title, meta ve style korunur; gövde olduğu gibi kalır. Yayım aracı iskeleti kendi ekler.
Kullanım: python3 defter/kopru_ayna_uret.py kopru.html ayna/kopru.html [--kontrol]
yerel/kopru_gonder.ps1 her gönderimden önce bunu çalıştırır; ayna böylece kanonik dosyanın gerisinde kalmaz."""
import argparse
import os
import re
import sys
import tempfile


def uretim_metni(kaynak):
    with open(kaynak, encoding="utf-8") as fh:
        t = fh.read()
    head_match = re.search(r"<head>(.*?)</head>", t, re.S)
    body_match = re.search(r"<body>(.*?)</body>", t, re.S)
    if not head_match or not body_match:
        raise ValueError("Kanonik sayfada head ve body bölümleri gerekli.")
    head, body = head_match.group(1), body_match.group(1)
    title_match = re.search(r"<title>.*?</title>", head, re.S)
    style_match = re.search(r"<style>.*?</style>", head, re.S)
    if not title_match or not style_match:
        raise ValueError("Kanonik sayfada title ve style bölümleri gerekli.")
    title = title_match.group(0)
    metas = [m for m in re.findall(r"<meta [^>]*>", head) if "charset" not in m and 'name="viewport"' not in m]
    style = style_match.group(0)
    out = title + "\n" + "\n".join(metas) + "\n" + style + "\n" + body.strip() + "\n"
    if re.search(r'(src|href)="https?://(?!github\.com|raw\.githubusercontent\.com|halukainrs\.github\.io|claude\.ai)', out):
        print("UYARI: aynada beklenmeyen dış adres var", file=sys.stderr)
    return out


def uret(kaynak, hedef, kontrol=False):
    out = uretim_metni(kaynak)
    eski = None
    if os.path.exists(hedef):
        with open(hedef, encoding="utf-8") as fh:
            eski = fh.read()
    if eski == out:
        print(f"ayna güncel: {hedef}")
        return False
    if kontrol:
        raise ValueError(f"Ayna güncel değil: {hedef}; kopru_ayna_uret.py ile yeniden üretin.")
    klasor = os.path.dirname(os.path.abspath(hedef))
    os.makedirs(klasor, exist_ok=True)
    fd, gecici = tempfile.mkstemp(prefix="ayna-", suffix=".html", dir=klasor)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(out)
        os.replace(gecici, hedef)
    finally:
        if os.path.exists(gecici):
            os.unlink(gecici)
    print(f"ayna yenilendi: {hedef} ({len(out)} karakter)")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kaynak")
    parser.add_argument("hedef")
    parser.add_argument("--kontrol", action="store_true", help="Yazmadan ayna eşliğini doğrula.")
    args = parser.parse_args()
    try:
        uret(args.kaynak, args.hedef, args.kontrol)
    except (OSError, ValueError) as exc:
        print(f"HATA: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
