#!/usr/bin/env python3
"""Kişisel içerik aktarımının denetimi. Yalnız okur, rapor yazar; hiçbir dosyayı değiştirmez.

Haluk'un 25 Ekim talimatı: kendisiyle ilgili bütün içerik yalnız rüyalarım.txt'de durur, öteki dosyalar
"rüyalarım.txt / R-0001" biçiminde nötr gönderme yapar, kişisel içerik öteki dosyalardan ancak aktarımın
eksiksizliği doğrulandıktan sonra çıkarılır. Bu araç o doğrulamanın raporunu üretir; kararı Haluk verir.

Denetlenenler:
  1. rüyalarım.txt kayıt kimlikleri (R-0001 …): yinelenen kimlik, boşluk, kimliksiz paragraf.
  2. Öteki dosyalardaki göndermeler: hedefi olmayan kimlik; göndermenin yanına yeniden yazılmış başlık/alıntı.
  3. Kişisel kayıt metninin öteki dosyalarda yinelenmesi (cümle ve 8 kelimelik dizi eşleşmesi).
  4. Aday kişisel içerik: Haluk'un adıyla alıntı taşıyan, birinci tekil kişiyle rüya/görü anlatan satırlar.
     Bunlar adaydır; kişisel olup olmadığına Haluk karar verir.

Kullanım:  ruya_denetim.py [--klasor .] [--rapor Raporlar]
"""
import argparse, datetime, os, re, sys, unicodedata

KISISEL = "rüyalarım.txt"
LISTE_ADI = "dosya_adlari.txt"
KIMLIK = re.compile(r"\bR-(\d{4})\b")
GONDERME = re.compile(r"rüyalarım\.txt\s*/\s*R-(\d{4})", re.I)
ALINTI_ISARETI = re.compile(r"[\"“”„«»]|(?<!\w)['‘’](?=\S)")
ADAY = [
    (re.compile(r"\b(Haluk'un|Haluk’un)\s+(rüya|görü|hayal|ilke|karar|fikir|niyet|tercih|söz|geçmiş)", re.I), "Haluk'un kişisel içeriği"),
    (re.compile(r"\bHaluk(?:'|’)?(?:un|ın|a|ı|la|dan|ta)?\b.*(?:" + ALINTI_ISARETI.pattern + ")"), "Haluk'un adıyla alıntı"),
    (re.compile(r"\bHaluk\b.*\b(dedi|söyledi|yazdı|anlattı|istedi|karar verdi|belirtti|demişti)\b"), "Haluk'a atfedilen söz"),
    (re.compile(r"\b(rüyamda|rüyam|görümde|görüm|hayalim|hayalimde|ilkem|kararım|fikrim)\b", re.I), "birinci tekil kişisel anlatı"),
]


def nfc(s):
    return unicodedata.normalize("NFC", s)


def oku(yol):
    veri = open(yol, "rb").read()
    if veri.startswith(b"\xef\xbb\xbf"):
        veri = veri[3:]
    return veri.decode("utf-8", errors="replace").replace("\r\n", "\n")


def kanonik_adlar(klasor):
    yol = os.path.join(klasor, LISTE_ADI)
    if not os.path.exists(yol):
        return None
    return [nfc(s.strip()) for s in oku(yol).splitlines() if s.strip() and not s.strip().startswith("#")]


def kelimeler(metin):
    return re.findall(r"\w+", metin.lower(), re.UNICODE)


def cumleler(metin):
    for c in re.split(r"(?<=[.!?…])\s+|\n", metin):
        c = c.strip()
        if len(c) >= 40:
            yield c


def kayitlari_ayir(metin):
    """rüyalarım.txt'yi R-xxxx kimliklerine göre bloklara ayırır."""
    kayitlar = {}
    sira = []
    kimliksiz = []
    gecerli = None
    for i, satir in enumerate(metin.splitlines(), 1):
        m = KIMLIK.search(satir)
        if m and (satir.strip().startswith("R-") or satir.strip().startswith("[R-") or satir.strip().startswith("## R-") or satir.strip().startswith("# R-")):
            kid = "R-" + m.group(1)
            if kid in kayitlar:
                kayitlar[kid]["yinelenen"].append(i)
            else:
                kayitlar[kid] = {"satir": i, "metin": [], "yinelenen": []}
                sira.append(kid)
            gecerli = kid
            kalan = satir[m.end():].strip(" :.-—–")
            if kalan:
                kayitlar[kid]["metin"].append(kalan)
        elif gecerli:
            kayitlar[kid]["metin"].append(satir)
        elif satir.strip():
            kimliksiz.append(i)
    return kayitlar, sira, kimliksiz


def main():
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="Kişisel içerik aktarımı denetimi (yalnız okur).")
    p.add_argument("--klasor", default=".")
    p.add_argument("--rapor", default=None, help="rapor klasörü (varsayılan: <klasor>/Raporlar)")
    a = p.parse_args()
    klasor = a.klasor
    rapor_dizin = a.rapor or os.path.join(klasor, "Raporlar")
    R = []
    sorun = {"kritik": 0, "uyari": 0, "aday": 0}

    def yaz(s=""):
        R.append(s)

    yaz("Kişisel içerik aktarımı denetimi · %s · %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), os.path.abspath(klasor)))
    yaz("Yalnız okur. Bulgular aday ve denetim niteliğindedir; karar Haluk'un.")
    adlar = kanonik_adlar(klasor)
    if adlar is None:
        yaz("UYARI: %s yok; klasördeki bütün .txt dosyaları denetlendi." % LISTE_ADI)
        adlar = sorted(nfc(x) for x in os.listdir(klasor) if x.lower().endswith(".txt") and x != LISTE_ADI)
        sorun["uyari"] += 1
    mevcut = {nfc(x): x for x in os.listdir(klasor)}
    kisisel_yol = os.path.join(klasor, mevcut.get(nfc(KISISEL), KISISEL))

    # 1. rüyalarım.txt kimlikleri
    yaz(""); yaz("== 1. %s kayıt kimlikleri ==" % KISISEL)
    kayitlar, sira, kimliksiz = {}, [], []
    if not os.path.exists(kisisel_yol):
        yaz("%s yok. Kişisel içerik henüz tek yere toplanmamış; göndermeler ve yinelemeler bu yüzden denetlenemedi." % KISISEL)
        sorun["kritik"] += 1
    else:
        kmetin = oku(kisisel_yol)
        kayitlar, sira, kimliksiz = kayitlari_ayir(kmetin)
        yaz("%d kayıt: %s" % (len(sira), (", ".join(sira[:5]) + (" …" if len(sira) > 5 else "")) if sira else "yok"))
        for kid in sira:
            if kayitlar[kid]["yinelenen"]:
                yaz("KRİTİK: %s birden çok kez tanımlı (satır %d ve %s)." % (kid, kayitlar[kid]["satir"], ", ".join(map(str, kayitlar[kid]["yinelenen"]))))
                sorun["kritik"] += 1
        sayilar = sorted(int(k[2:]) for k in sira)
        if sayilar:
            eksik = [n for n in range(sayilar[0], sayilar[-1] + 1) if n not in sayilar]
            if eksik:
                yaz("UYARI: numara boşlukları: %s (kayıt silinmiş ya da başka dosyada kalmış olabilir)." % ", ".join("R-%04d" % n for n in eksik[:20]))
                sorun["uyari"] += 1
        if kimliksiz:
            yaz("UYARI: ilk kimlikten önce %d kimliksiz dolu satır var (satır %s); kimliksiz içerik gönderme alamaz." % (len(kimliksiz), ", ".join(map(str, kimliksiz[:10]))))
            sorun["uyari"] += 1
        bos = [k for k in sira if not "".join(kayitlar[k]["metin"]).strip()]
        if bos:
            yaz("UYARI: içeriği boş kayıtlar: %s" % ", ".join(bos))
            sorun["uyari"] += 1

    # Öteki dosyalar
    digerleri = [ad for ad in adlar if nfc(ad) != nfc(KISISEL)]
    yaz(""); yaz("== 2. Göndermeler (öteki dosyalardan rüyalarım.txt'ye) ==")
    gonderme_toplam = 0
    for ad in digerleri:
        yol = os.path.join(klasor, mevcut.get(nfc(ad), ad))
        if not os.path.exists(yol):
            yaz("%s: yok (henüz oluşturulmamış)." % ad)
            continue
        metin = oku(yol)
        for i, satir in enumerate(metin.splitlines(), 1):
            for m in GONDERME.finditer(satir):
                gonderme_toplam += 1
                kid = "R-" + m.group(1)
                if kayitlar and kid not in kayitlar:
                    yaz("KRİTİK: %s satır %d → %s, hedef kayıt yok." % (ad, i, kid))
                    sorun["kritik"] += 1
                kalan = satir[m.end():].strip()
                if len(kalan) > 20 and (ALINTI_ISARETI.search(kalan) or kalan.startswith((":", "—", "–", "-"))):
                    yaz("UYARI: %s satır %d: %s göndermesinin yanında metin yeniden yazılmış görünüyor: «%s»" % (ad, i, kid, kalan[:90]))
                    sorun["uyari"] += 1
            for m in KIMLIK.finditer(satir):
                if not GONDERME.search(satir):
                    kid = "R-" + m.group(1)
                    if kayitlar and kid in kayitlar:
                        yaz("UYARI: %s satır %d: %s dosya adı olmadan anılıyor; biçim 'rüyalarım.txt / %s' olmalı." % (ad, i, kid, kid))
                        sorun["uyari"] += 1
    yaz("%d gönderme bulundu." % gonderme_toplam)

    # 3. Yinelemeler
    yaz(""); yaz("== 3. Kişisel kayıt metninin öteki dosyalarda yinelenmesi ==")
    yineleme = 0
    if kayitlar:
        cumle_indeks = {}
        shingle_indeks = {}
        for kid in sira:
            govde = "\n".join(kayitlar[kid]["metin"])
            for c in cumleler(govde):
                cumle_indeks.setdefault(re.sub(r"\s+", " ", c.lower()), kid)
            k = kelimeler(govde)
            for j in range(0, max(0, len(k) - 7)):
                shingle_indeks.setdefault(" ".join(k[j:j + 8]), kid)
        for ad in digerleri:
            yol = os.path.join(klasor, mevcut.get(nfc(ad), ad))
            if not os.path.exists(yol):
                continue
            metin = oku(yol)
            bulunan = {}
            for i, satir in enumerate(metin.splitlines(), 1):
                for c in cumleler(satir):
                    kid = cumle_indeks.get(re.sub(r"\s+", " ", c.lower()))
                    if kid:
                        bulunan.setdefault((kid, i), "cümle")
                k = kelimeler(satir)
                for j in range(0, max(0, len(k) - 7)):
                    kid = shingle_indeks.get(" ".join(k[j:j + 8]))
                    if kid:
                        bulunan.setdefault((kid, i), "8 kelime")
            for (kid, i), tur in sorted(bulunan.items(), key=lambda x: (x[0][1], x[0][0])):
                yaz("UYARI: %s satır %d, %s ile örtüşüyor (%s). Gönderme yeter; metin burada kalmamalı." % (ad, i, kid, tur))
                yineleme += 1
        sorun["uyari"] += yineleme
    yaz("%d yineleme." % yineleme)

    # 4. Aday kişisel içerik
    yaz(""); yaz("== 4. Aday kişisel içerik (karar Haluk'un) ==")
    for ad in digerleri:
        yol = os.path.join(klasor, mevcut.get(nfc(ad), ad))
        if not os.path.exists(yol):
            continue
        metin = oku(yol)
        adaylar = []
        for i, satir in enumerate(metin.splitlines(), 1):
            if GONDERME.search(satir):
                continue
            for desen, ad_ in ADAY:
                if desen.search(satir):
                    adaylar.append((i, ad_, satir.strip()))
                    break
        if adaylar:
            yaz("%s: %d aday" % (ad, len(adaylar)))
            for i, tur, satir in adaylar[:40]:
                yaz("  satır %d [%s]: %s" % (i, tur, satir[:140] + ("…" if len(satir) > 140 else "")))
            if len(adaylar) > 40:
                yaz("  … %d aday daha" % (len(adaylar) - 40))
            sorun["aday"] += len(adaylar)

    yaz(""); yaz("== Özet ==")
    yaz("Kritik %d · uyarı %d · aday %d." % (sorun["kritik"], sorun["uyari"], sorun["aday"]))
    if sorun["kritik"] == 0 and sorun["uyari"] == 0 and sorun["aday"] == 0 and kayitlar:
        yaz("Araç bir sorun bulmadı. Bu, aktarımın eksiksiz olduğunun kanıtı değil; adayların ve kayıtların okunarak doğrulanması Haluk'un.")
    else:
        yaz("Kişisel içerik öteki dosyalardan ancak kritik ve uyarı sayısı sıfırlanıp adaylar Haluk tarafından görüldükten sonra çıkarılmalı.")
    os.makedirs(rapor_dizin, exist_ok=True)
    dosya = os.path.join(rapor_dizin, "RuyaDenetim-%s.txt" % datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    with open(dosya, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(R) + "\n")
    print("\n".join(R))
    print("\nRapor: %s" % dosya)


if __name__ == "__main__":
    main()
