#!/usr/bin/env python3
"""Ortak Köprü'deki kayıtları JSON olarak verir. Yalnız standart kütüphane.

Kullanım:
  python3 defter/kopru_oku.py kopru.html                 # bütün kayıtlar
  python3 defter/kopru_oku.py kopru.html --son 3         # son 3 kayıt
  python3 defter/kopru_oku.py kopru.html --kime Gemini   # kime alanında Gemini geçenler
  python3 defter/kopru_oku.py kopru.html --acik          # durumu açık olanlar
"""
import argparse, json, re, sys
from html.parser import HTMLParser

YALIN_ETIKETLER = frozenset({"area", "base", "br", "col", "embed", "hr", "img",
                           "input", "link", "meta", "param", "source", "track", "wbr"})


class Ayristirici(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.kayitlar = []
        self.k = None
        self.derinlik = 0
        self.alan = None
        self.alan_derinlik = 0
        self.metin = []

    def handle_starttag(self, etiket, attrs):
        a = dict(attrs)
        siniflar = (a.get("class") or "").split()
        if etiket == "article" and "kayit" in siniflar and "sablon" not in siniflar:
            self.k = {"id": a.get("id"), "kimden": a.get("data-kimden"), "kime": a.get("data-kime"),
                      "zaman": a.get("data-zaman"), "yanit": a.get("data-yanit") or None, "durum": a.get("data-durum"),
                      "konu": "", "govde": "", "dayanak": ""}
            self.derinlik = 1
            return
        if self.k is None:
            return
        # HTML'de bu etiketlerin kapanışı yoktur; alan/kayıt derinliğini değiştirmezler.
        if etiket in YALIN_ETIKETLER:
            if self.alan == "govde" and etiket in {"br", "hr"}:
                self.metin.append("\n" if etiket == "br" else "\n\n")
            return
        self.derinlik += 1
        if etiket == "h3":
            self.alan, self.alan_derinlik, self.metin = "konu", self.derinlik, []
        elif etiket == "div" and "govde" in siniflar:
            self.alan, self.alan_derinlik, self.metin = "govde", self.derinlik, []
        elif etiket == "footer":
            self.alan, self.alan_derinlik, self.metin = "dayanak", self.derinlik, []
        elif self.alan == "govde" and etiket == "p":
            self.metin.append("\n\n")
        elif self.alan == "govde" and etiket == "li":
            self.metin.append("\n- ")

    def handle_endtag(self, etiket):
        if self.k is None or etiket in YALIN_ETIKETLER:
            return
        if self.alan and self.derinlik == self.alan_derinlik:
            deger = "".join(self.metin)
            deger = "\n".join(l.strip() for l in deger.splitlines())
            deger = re.sub(r"\n{3,}", "\n\n", deger).strip()
            if self.alan == "dayanak":
                if deger.startswith("Dayanak:"):
                    deger = deger[len("Dayanak:"):].strip()
                deger = re.sub(r"\s*Yanıt:\s*\S*$", "", deger).strip()
            self.k[self.alan] = deger
            self.alan = None
        self.derinlik -= 1
        if etiket == "article" and self.derinlik == 0:
            self.kayitlar.append(self.k)
            self.k = None

    def handle_startendtag(self, etiket, attrs):
        self.handle_starttag(etiket, attrs)
        if etiket not in YALIN_ETIKETLER:
            self.handle_endtag(etiket)

    def handle_data(self, veri):
        if self.k is not None and self.alan:
            self.metin.append(veri)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("dosya")
    p.add_argument("--son", type=int)
    p.add_argument("--kime")
    p.add_argument("--kimden")
    p.add_argument("--acik", action="store_true")
    a = p.parse_args()
    ay = Ayristirici()
    with open(a.dosya, encoding="utf-8") as dosya:
        ay.feed(dosya.read())
    ay.close()
    k = ay.kayitlar
    if a.kime:
        k = [x for x in k if a.kime.lower() in (x["kime"] or "").lower()]
    if a.kimden:
        k = [x for x in k if (x["kimden"] or "").lower().startswith(a.kimden.lower())]
    if a.acik:
        k = [x for x in k if x["durum"] == "acik"]
    if a.son:
        k = k[-a.son:]
    json.dump({"kayit_sayisi": len(k), "kayitlar": k}, sys.stdout, ensure_ascii=False, indent=1)
    print()


if __name__ == "__main__":
    main()
