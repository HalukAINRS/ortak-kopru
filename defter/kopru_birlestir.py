#!/usr/bin/env python3
"""Ortak Köprü sayfasının iki sürümünü birleştirir. Birden çok yazan (yerel izleyici, GitHub Actions botu, Gemini ve
ChatGPT'nin GitHub aktarımları) aynı <!-- KAYIT-SONU --> işaretinin önüne kayıt eklediği için git bunları kendi
başına birleştiremez. Kural: uzak (ortak) sürüm esas alınır; yalnız yerelde olan kayıtlar yeni numarayla sona eklenir.
Kayıtların kendisi değişmez; zamanı korunur; yalnız numarası değişebilir. Yalnız standart kütüphane.

Kullanım:
  python3 defter/kopru_birlestir.py uzak.html yerel.html cikti.html   # iki dosyadan
  python3 defter/kopru_birlestir.py --rebase kopru.html               # git rebase çakışmasında: aşama 2 (uzak) ve 3 (yerel) birleşir, dosyaya yazılır
  python3 defter/kopru_birlestir.py --rebase-metin kayit/atlandi.log  # satır günlüğü: iki tarafın satırları birleştirilir

Bir kaydın kimliği (kimden, zaman, konu) üçlüsüdür. Aynı kimlikte farklı içerik otomatik çözülemez.
Yerelde olup uzakta olmayan kayıtlar, yanıt alanları da gerekirse yeni numaralara çevrilerek kopru_ekle.py ile
denetlenir; özgün HTML gövdeleri korunur. Birleştirme ancak tamamı başarılıysa atomik olarak yazılır.
"""
import json, os, re, subprocess, sys, tempfile
from html.parser import HTMLParser
from urllib.parse import urlsplit

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
from kopru_oku import Ayristirici  # noqa: E402

KAYIT = re.compile(r'<article class="kayit" id="k-\d{4,}"[^>]*>.*?</article>', re.S)


class KayitHTMLKontrol(HTMLParser):
    """Özgün biçimi korurken ekleyicinin HTML kaçışlamasını etkin içerikle aşma."""
    etiketler = {"article", "header", "span", "time", "h3", "div", "p", "ul", "ol", "li",
                 "footer", "a", "code", "pre", "em", "strong", "b", "i", "br", "blockquote"}
    alanlar = {"class", "id", "title", "lang", "dir", "role", "datetime", "data-kimden",
               "data-kime", "data-zaman", "data-yanit", "data-durum"}

    def handle_starttag(self, etiket, attrs):
        if etiket not in self.etiketler:
            raise ValueError(f"Kayıt HTML'i denetimden geçmedi: desteklenmeyen {etiket} etiketi.")
        for ad, deger in attrs:
            if etiket == "a" and ad == "href":
                if urlsplit(deger or "").scheme.lower() not in ("", "http", "https"):
                    raise ValueError("Kayıt HTML'i denetimden geçmedi: etkin bağlantı şeması.")
            elif ad not in self.alanlar and not ad.startswith("aria-"):
                raise ValueError(f"Kayıt HTML'i denetimden geçmedi: desteklenmeyen {ad} alanı.")


def kayitlar(metin):
    ay = Ayristirici()
    ay.feed(metin)
    return ay.kayitlar


def anahtar(k):
    return (k.get("kimden") or "", k.get("zaman") or "", k.get("konu") or "")


def kayitsiz(metin):
    """Kayıtlar ve ekleyicinin ürettiği sayaç değerleri dışındaki sayfa içeriği."""
    metin = re.sub(KAYIT.pattern + r"\s*", "", metin, flags=re.S)
    metin = re.sub(r'(<b id="kayit-sayisi">)\d+(</b>)', r"\g<1>#\g<2>", metin)
    metin = re.sub(r'<time id="son-guncelleme" datetime="[^"]*">[^<]*</time>',
                   '<time id="son-guncelleme"></time>', metin)
    return re.sub(r'(Son kayıt: <a href="#)k-\d{4,}(">)k-\d{4,}(</a>)',
                  r"\g<1>#\g<2>#\g<3>", metin)


def sayfa_oku(metin):
    """Belirsiz kimlik, yinelenen numara ve kopuk yanıtla birleştirmeyi durdur."""
    if metin.count("<!-- KAYIT-SONU -->") != 1:
        raise ValueError("Sayfada tek bir KAYIT-SONU işareti bulunmalı.")
    kayit = kayitlar(metin)
    ham = KAYIT.findall(metin)
    if len(kayit) != len(ham):
        raise ValueError("Kayıt HTML yapısı otomatik birleştirmeye uygun değil.")
    idler, kimlikler = {}, {}
    for k, blok in zip(kayit, ham):
        if k["id"] in idler or anahtar(k) in kimlikler:
            raise ValueError("Yinelenen kayıt numarası ya da kimliği; elle inceleme gerekli.")
        idler[k["id"]] = k
        kimlikler[anahtar(k)] = k
        k["_html"] = blok
    for k in kayit:
        if k.get("yanit") and k["yanit"] not in idler:
            raise ValueError(f"{k['id']}: yanıt verilen kayıt sayfada yok.")
    return kayit, idler, kimlikler


def numarala(blok, eski, yeni, eski_yanit, yeni_yanit):
    """Yalnız kaydın kimlik alanlarını değiştir; gövde ve dayanak metnine dokunma."""
    blok = blok.replace(f'id="{eski}"', f'id="{yeni}"', 1)
    blok = blok.replace(f'<span class="kid">{eski}</span>', f'<span class="kid">{yeni}</span>', 1)
    if eski_yanit:
        blok = blok.replace(f'data-yanit="{eski_yanit}"', f'data-yanit="{yeni_yanit}"', 1)
        blok = re.sub(r'(<footer\b[^>]*>.*?Yanıt: )<a href="#' + re.escape(eski_yanit) + r'">' +
                      re.escape(eski_yanit) + r'</a>',
                      lambda m: m[1] + f'<a href="#{yeni_yanit}">{yeni_yanit}</a>', blok, count=1, flags=re.S)
    return blok


def icerik(k, idler):
    # Numaralar önceki bir birleşmede değişmiş olabilir; yanıtın mantıksal hedefi aynı kalmalı.
    yanit = anahtar(idler[k["yanit"]]) if k.get("yanit") else None
    return (numarala(k["_html"], k["id"], "KAYIT", k.get("yanit"), "YANIT"), yanit)


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


def birlestir(uzak_metin, yerel_metin, cikti_yolu, taban_metin=None):
    uzak, uzak_idler, uzak_kimlikler = sayfa_oku(uzak_metin)
    yerel, yerel_idler, yerel_kimlikler = sayfa_oku(yerel_metin)
    if kayitsiz(uzak_metin) != kayitsiz(yerel_metin):
        if taban_metin is None or kayitsiz(yerel_metin) != kayitsiz(taban_metin):
            raise ValueError("Yerelde kayıt dışı değişiklik var; içerik kaybetmemek için elle birleştirme gerekli.")
    if taban_metin is not None:
        taban, taban_idler, _ = sayfa_oku(taban_metin)
        for k in taban:
            for idler, kimlikler in ((uzak_idler, uzak_kimlikler), (yerel_idler, yerel_kimlikler)):
                ayni = kimlikler.get(anahtar(k))
                if ayni is None or icerik(ayni, idler) != icerik(k, taban_idler):
                    raise ValueError(f"{k['id']}: ortak geçmiş değişmiş ya da silinmiş; elle inceleme gerekli.")
    for kimlik in uzak_kimlikler.keys() & yerel_kimlikler.keys():
        if icerik(uzak_kimlikler[kimlik], uzak_idler) != icerik(yerel_kimlikler[kimlik], yerel_idler):
            raise ValueError("Aynı kayıt kimliği farklı içerik taşıyor; elle inceleme gerekli.")

    yalniz_yerel = [k for k in yerel if anahtar(k) not in uzak_kimlikler]
    # Ortak kayıtların numarası da değişmiş olabilir; yanıtları yalnız yeni eklenenler için eşlemek yetmez.
    eslem = {k["id"]: uzak_kimlikler[anahtar(k)]["id"] for k in yerel if anahtar(k) in uzak_kimlikler}
    yeni_eslem = {}
    klasor = os.path.dirname(os.path.abspath(cikti_yolu))
    fd, gecici = tempfile.mkstemp(prefix="kopru-birlestir-", suffix=".html", dir=klasor)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(uzak_metin)
        for k in yalniz_yerel:  # yerel sıra korunur; ileriye yanıt belirsizliğinde yazma yapılmaz
            KayitHTMLKontrol().feed(k["_html"])
            eski_yanit = k.get("yanit") or ""
            if eski_yanit and eski_yanit not in eslem:
                raise ValueError(f"{k['id']}: yanıt henüz eklenmemiş yerel kayda gidiyor.")
            yanit = eslem.get(eski_yanit, "")
            veri = {"kimden": k["kimden"], "kime": k["kime"], "konu": k["konu"], "govde": k.get("govde") or "",
                    "dayanak": k.get("dayanak") or "", "yanit": yanit, "durum": k.get("durum") or "acik", "zaman": k.get("zaman") or ""}
            yeni = ekle(gecici, veri)
            # Ekleyicinin denetimi ve sayaçları kullanılır; yeniden ayrıştırma HTML biçimini bozmasın.
            with open(gecici, encoding="utf-8") as fh:
                metin = fh.read()
            blok = numarala(k["_html"], k["id"], yeni, eski_yanit, yanit)
            metin, sayi = re.subn(r'<article class="kayit" id="' + re.escape(yeni) + r'"[^>]*>.*?</article>',
                                  lambda _: blok, metin, count=1, flags=re.S)
            if sayi != 1:
                raise ValueError("Eklenen kayıt doğrulanamadı; birleştirme yazılmadı.")
            with open(gecici, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(metin)
            eslem[k["id"]] = yeni
            yeni_eslem[k["id"]] = yeni
        denetim = subprocess.run([sys.executable, "-I", "-X", "utf8", os.path.join(BURASI, "kopru_ekle.py"),
                                  gecici, "--kontrol"], capture_output=True, text=True, encoding="utf-8")
        if denetim.returncode != 0:
            raise ValueError("Birleşmiş sayfa denetimden geçmedi: " + (denetim.stdout + denetim.stderr).strip())
        if os.path.exists(cikti_yolu):
            os.chmod(gecici, os.stat(cikti_yolu).st_mode)
        os.replace(gecici, cikti_yolu)
    finally:
        if os.path.exists(gecici):
            os.unlink(gecici)
    print(f"birleşti: uzak {len(uzak)} kayıt + yerel {len(yalniz_yerel)} kayıt → {cikti_yolu}")
    return yeni_eslem


def git_asama(asama, yol):
    s = subprocess.run(["git", "show", f":{asama}:{yol}"], capture_output=True)
    if s.returncode != 0:
        raise SystemExit(f"HATA: git show :{asama}:{yol} başarısız: {s.stderr.decode('utf-8', 'replace')[:300]}")
    return s.stdout.decode("utf-8")


def main():
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    a = sys.argv[1:]
    if any(arg in ("-h", "--help") for arg in a):
        print(__doc__)
        return
    if len(a) == 2 and a[0] == "--rebase":
        yol = a[1]
        birlestir(git_asama(2, yol), git_asama(3, yol), yol, git_asama(1, yol))  # :2 = uzak, :3 = yerel
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
    try:
        main()
    except (OSError, ValueError, RuntimeError) as hata:
        sys.exit(f"HATA: {hata}")
