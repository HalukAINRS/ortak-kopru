#!/usr/bin/env python3
"""Ortak Köprü sayfasının iki sürümünü birleştirir. Birden çok yazan (yerel izleyici, GitHub Actions botu, Gemini ve
ChatGPT'nin GitHub aktarımları) aynı <!-- KAYIT-SONU --> işaretinin önüne kayıt eklediği için git bunları kendi
başına birleştiremez. Kural: uzak (ortak) sürüm esas alınır; yalnız yerelde olan kayıtlar yeni numarayla sona eklenir.
Kayıtların kendisi değişmez; zamanı korunur; yalnız numarası değişebilir. Yalnız standart kütüphane.

Kullanım:
  python3 kopru_birlestir.py uzak.html yerel.html cikti.html   # iki dosyadan
  python3 kopru_birlestir.py --rebase kopru.html               # git rebase çakışmasında: aşama 2 (uzak) ve 3 (yerel) birleşir, dosyaya yazılır
  python3 kopru_birlestir.py --rebase-metin kayit/atlandi.log  # satır günlüğü: iki tarafın satırları birleştirilir

Bir kaydın kimliği (kimden, zaman, konu) üçlüsüdür. Yerelde olup uzakta olmayan kayıtlar, yanıt alanları da gerekirse
yeni numaralara çevrilerek kopru_ekle.py ile eklenir; böylece denetim ve sayaçlar aynı yoldan geçer.
"""
import json, os, re, subprocess, sys, tempfile

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
from kopru_oku import Ayristirici  # noqa: E402


def kayitlar(metin):
    ay = Ayristirici()
    ay.feed(metin)
    return ay.kayitlar


def anahtar(k):
    return (k.get("kimden") or "", k.get("zaman") or "", k.get("konu") or "")


def kayitsiz(metin):
    """Sayfanın kayıt dışı kısmı (bölümler, kurallar, dosya); kayıt gövdeleri çıkarılmış."""
    return re.sub(r'<article class="kayit" id="k-\d{4}".*?</article>\s*', "", metin, flags=re.S)


def ekle(sayfa_yolu, veri):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8", dir=os.path.dirname(os.path.abspath(sayfa_yolu))) as fh:
        json.dump(veri, fh, ensure_ascii=False)
        gecici = fh.name
    try:
        s = subprocess.run([sys.executable, "-I", "-X", "utf8", os.path.join(BURASI, "kopru_ekle.py"), sayfa_yolu, "--json", gecici],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
    finally:
        os.unlink(gecici)
    if s.returncode != 0:
        raise RuntimeError((s.stdout + s.stderr).strip())
    return s.stdout.strip().splitlines()[-1]


def birlestir(uzak_metin, yerel_metin, cikti_yolu):
    uzak, yerel = kayitlar(uzak_metin), kayitlar(yerel_metin)
    uzak_anahtarlar = {anahtar(k) for k in uzak}
    yalniz_yerel = [k for k in yerel if anahtar(k) not in uzak_anahtarlar]
    yerel_idler = {k["id"] for k in yalniz_yerel}
    if kayitsiz(uzak_metin) != kayitsiz(yerel_metin):
        print("UYARI: sayfanın kayıt dışı kısmı iki sürümde farklı; uzak (ortak) sürüm esas alındı, yereldeki kayıt dışı değişiklik varsa elle taşı.", file=sys.stderr)
    with open(cikti_yolu, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(uzak_metin)
    eslem = {}
    for k in yalniz_yerel:  # yerel sıra korunur
        yanit = k.get("yanit") or ""
        if yanit in yerel_idler:
            yanit = eslem.get(yanit, "")
        veri = {"kimden": k["kimden"], "kime": k["kime"], "konu": k["konu"], "govde": k.get("govde") or "",
                "dayanak": k.get("dayanak") or "", "yanit": yanit, "durum": k.get("durum") or "acik", "zaman": k.get("zaman") or ""}
        yeni = ekle(cikti_yolu, veri)
        eslem[k["id"]] = yeni
        print(f"eklendi: yerel {k['id']} → {yeni} ({k['kimden']}: {k['konu'][:60]})")
    print(f"birleşti: uzak {len(uzak)} kayıt + yerel {len(yalniz_yerel)} kayıt → {cikti_yolu}")
    return eslem


def git_asama(asama, yol):
    s = subprocess.run(["git", "show", f":{asama}:{yol}"], capture_output=True)
    if s.returncode != 0:
        raise SystemExit(f"HATA: git show :{asama}:{yol} başarısız: {s.stderr.decode('utf-8', 'replace')[:300]}")
    return s.stdout.decode("utf-8", "replace")


def main():
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    a = sys.argv[1:]
    if len(a) == 2 and a[0] == "--rebase":
        yol = a[1]
        birlestir(git_asama(2, yol), git_asama(3, yol), yol)  # rebase sırasında :2 = üzerine gelinen (uzak), :3 = yeniden oynatılan (yerel)
        return
    if len(a) == 2 and a[0] == "--rebase-metin":
        yol = a[1]
        satirlar, gorulen = [], set()
        for asama in (2, 3):
            for sat in git_asama(asama, yol).splitlines():
                if sat not in gorulen:
                    gorulen.add(sat); satirlar.append(sat)
        with open(yol, "w", encoding="utf-8", newline="\n") as fh:
            fh.write("\n".join(satirlar) + ("\n" if satirlar else ""))
        print(f"birleşti: {yol}, {len(satirlar)} satır")
        return
    if len(a) == 3:
        birlestir(open(a[0], encoding="utf-8").read(), open(a[1], encoding="utf-8").read(), a[2])
        return
    sys.exit(__doc__)


if __name__ == "__main__":
    main()
