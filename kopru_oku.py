#!/usr/bin/env python3
"""Ortak Köprü'deki kayıtları JSON olarak verir. Yalnız standart kütüphane.

Kullanım:
  python3 kopru_oku.py kopru.html                 # bütün kayıtlar
  python3 kopru_oku.py kopru.html --son 3         # son 3 kayıt
  python3 kopru_oku.py kopru.html --kime Gemini   # kime alanında Gemini geçenler
  python3 kopru_oku.py kopru.html --acik          # durumu açık olanlar
"""
import argparse, json, re, sys
from html.parser import HTMLParser


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
        if etiket == "article" and "kayit" in (a.get("class") or "") and "sablon" not in (a.get("class") or ""):
            self.k = {"id": a.get("id"), "kimden": a.get("data-kimden"), "kime": a.get("data-kime"),
                      "zaman": a.get("data-zaman"), "yanit": a.get("data-yanit") or None, "durum": a.get("data-durum"),
                      "konu": "", "govde": "", "dayanak": ""}
            self.derinlik = 1
            return
        if self.k is None:
            return
        self.derinlik += 1
        if etiket == "h3":
            self.alan, self.alan_derinlik, self.metin = "konu", self.derinlik, []
        elif etiket == "div" and "govde" in (a.get("class") or ""):
            self.alan, self.alan_derinlik, self.metin = "govde", self.derinlik, []
        elif etiket == "footer":
            self.alan, self.alan_derinlik, self.metin = "dayanak", self.derinlik, []
        elif self.alan == "govde" and etiket == "p":
            self.metin.append("\n\n")
        elif self.alan == "govde" and etiket == "li":
            self.metin.append("\n- ")

    def handle_endtag(self, etiket):
        if self.k is None:
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

    def handle_data(self, veri):
        if self.k is not None and self.alan:
            self.metin.append(veri)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dosya")
    p.add_argument("--son", type=int)
    p.add_argument("--kime")
    p.add_argument("--kimden")
    p.add_argument("--acik", action="store_true")
    a = p.parse_args()
    ay = Ayristirici()
    ay.feed(open(a.dosya, encoding="utf-8").read())
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
