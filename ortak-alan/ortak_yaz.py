#!/usr/bin/env python3
"""Ortak anlatı dosyaları için korumalı yazma. Yalnız standart kütüphane; Windows (FAT32) ve Linux'ta aynı.

Üç katman aynı dosyaları yazıyor. Bu araç, bir katılımcının görmediği sürümün üstüne yazmasını engeller:
okurken dosyanın özeti (SHA-256) alınır, yazarken aynı özet "temel" olarak verilir; dosya o arada değiştiyse
yazım reddedilir ve değişiklik gösterilir. Her yazımdan önce eski sürüm Yedekler/ altına alınır, her yazım
DEGISIKLIK.log'a işlenir. FAT32'de Türkçe harfli adların ASCII ikizleri (S-041) denetlenir.

Kullanım (ortak klasörde ya da --klasor ile):
  ortak_yaz.py durum                                   dosyaların özeti, kilitleri, ad çakışmaları
  ortak_yaz.py oku  "An.txt"                           içeriği yazdırır, sonda TEMEL=<özet> satırı
  ortak_yaz.py yaz  "An.txt" --temel <özet> --yeni yeni.txt --yazar "Şahit" --dayanak "k-0130"
  ortak_yaz.py ekle "An.txt" --parca ek.txt --yazar "Hacker" --dayanak "..."   (sona ekler; temel gerekmez)
  ortak_yaz.py kilit-kaldir "An.txt" --yazar "Şaman"   (10 dakikadan eski bayat kilit)
Yazım modlarında --yazar ve --dayanak zorunludur. Dosya adı dosya_adlari.txt'deki listede değilse uyarır.
"""
import argparse, datetime, hashlib, os, sys, tempfile, time, unicodedata, difflib

KILIT_SURESI_SN = 600
LISTE_ADI = "dosya_adlari.txt"
YEDEK_DIZIN = "Yedekler"
GUNLUK = "DEGISIKLIK.log"


def nfc(s):
    return unicodedata.normalize("NFC", s)


def ascii_anahtar(ad):
    """Türkçe harfleri ASCII karşılığına indirip küçültür: FAT32 OEM eşlemesinin gördüğü ad (S-041)."""
    tablo = str.maketrans("çğıöşüÇĞİÖŞÜâîûÂÎÛ", "cgiosuCGIOSUaiuAIU")
    return nfc(ad).translate(tablo).casefold()


def ozet(veri):
    return hashlib.sha256(veri).hexdigest()


def oku_bayt(yol):
    with open(yol, "rb") as f:
        return f.read()


def coz(veri):
    bom = veri.startswith(b"\xef\xbb\xbf")
    metin = veri[3:].decode("utf-8") if bom else veri.decode("utf-8")
    crlf = "\r\n" in metin
    return metin.replace("\r\n", "\n"), bom, crlf


def kodla(metin, bom, crlf):
    if crlf:
        metin = metin.replace("\n", "\r\n")
    veri = metin.encode("utf-8")
    return (b"\xef\xbb\xbf" + veri) if bom else veri


def kanonik_adlar(klasor):
    yol = os.path.join(klasor, LISTE_ADI)
    if not os.path.exists(yol):
        return None
    adlar = []
    for satir in coz(oku_bayt(yol))[0].splitlines():
        s = satir.strip()
        if s and not s.startswith("#"):
            adlar.append(nfc(s))
    return adlar


def ikiz_denetimi(klasor, ad):
    """Aynı klasörde ASCII anahtarı aynı, adı farklı dosya var mı (S-041)."""
    anahtar = ascii_anahtar(ad)
    ikizler = []
    for mevcut in os.listdir(klasor):
        if nfc(mevcut) != nfc(ad) and ascii_anahtar(mevcut) == anahtar and os.path.isfile(os.path.join(klasor, mevcut)):
            ikizler.append(mevcut)
    return ikizler


def kilit_yolu(klasor, ad):
    return os.path.join(klasor, "." + nfc(ad) + ".kilit")


def kilitle(klasor, ad, yazar):
    yol = kilit_yolu(klasor, ad)
    for _ in range(20):
        try:
            fd = os.open(yol, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write("%s|%s|%d\n" % (yazar, datetime.datetime.now().isoformat(timespec="seconds"), os.getpid()))
            return yol
        except FileExistsError:
            try:
                yas = time.time() - os.path.getmtime(yol)
                sahip = open(yol, encoding="utf-8").read().strip()
            except OSError:
                yas, sahip = 0, "?"
            if yas > KILIT_SURESI_SN:
                sys.exit("HATA: %s bayat kilitli (%s, %d sn). Sahibi yazmıyorsa: kilit-kaldir" % (ad, sahip, yas))
            time.sleep(0.5)
    sys.exit("HATA: %s kilitli (%s); 10 saniyede açılmadı, sonra yeniden dene." % (ad, sahip))


def kilit_ac(yol):
    try:
        os.remove(yol)
    except OSError:
        pass


def yedekle(klasor, ad, veri):
    dizin = os.path.join(klasor, YEDEK_DIZIN)
    os.makedirs(dizin, exist_ok=True)
    kok, uz = os.path.splitext(nfc(ad))
    hedef = os.path.join(dizin, "%s.%s%s" % (kok, ozet(veri)[:12], uz or ".txt"))
    if not os.path.exists(hedef):
        with open(hedef, "wb") as f:
            f.write(veri)
    return hedef


def gunluk(klasor, yazar, ad, eski, yeni, dayanak, islem, not_=""):
    satir = "%s | %s | %s | %s | %s → %s | %s%s\n" % (
        datetime.datetime.now().astimezone().isoformat(timespec="seconds"), yazar, islem, nfc(ad),
        eski[:12] if eski else "yok", yeni[:12], dayanak, (" | " + not_) if not_ else "")
    with open(os.path.join(klasor, GUNLUK), "a", encoding="utf-8") as f:
        f.write(satir)


def atomik_yaz(yol, veri):
    klasor = os.path.dirname(os.path.abspath(yol))
    fd, gecici = tempfile.mkstemp(prefix=".yaz-", suffix=".tmp", dir=klasor)
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(veri)
            f.flush()
            os.fsync(f.fileno())
        os.replace(gecici, yol)
    finally:
        if os.path.exists(gecici):
            os.remove(gecici)


def ad_uyarilari(klasor, ad):
    adlar = kanonik_adlar(klasor)
    if adlar is not None and nfc(ad) not in adlar:
        print("UYARI: '%s' %s listesinde yok; ortak dosya adları listeyle sınırlı tutulmalı." % (ad, LISTE_ADI), file=sys.stderr)
    ikiz = ikiz_denetimi(klasor, ad)
    if ikiz:
        sys.exit("HATA: '%s' için ASCII ikizi var: %s. FAT32'de yazım yanlış dosyaya gidebilir (S-041). "
                 "Önce ikizi birleştirip kaldırın." % (ad, ", ".join(ikiz)))


def komut_durum(a):
    klasor = a.klasor
    adlar = kanonik_adlar(klasor)
    mevcut = sorted(x for x in os.listdir(klasor) if os.path.isfile(os.path.join(klasor, x)) and not x.startswith("."))
    print("Klasör: %s" % os.path.abspath(klasor))
    if adlar is None:
        print("UYARI: %s yok; kanonik ad listesi denetlenemedi." % LISTE_ADI)
    print("%-32s %-13s %9s  %-19s %s" % ("Dosya", "Özet", "Bayt", "Değişti", "Durum"))
    gorulen = set()
    for ad in (adlar or []) + [x for x in mevcut if adlar is None or nfc(x) not in adlar]:
        if nfc(ad) in gorulen or ad in (LISTE_ADI, GUNLUK):
            continue
        gorulen.add(nfc(ad))
        yol = os.path.join(klasor, ad)
        notlar = []
        if os.path.exists(kilit_yolu(klasor, ad)):
            notlar.append("KİLİTLİ")
        ikiz = ikiz_denetimi(klasor, ad)
        if ikiz:
            notlar.append("İKİZ: " + ", ".join(ikiz))
        if adlar is not None and nfc(ad) not in adlar:
            notlar.append("listede yok")
        if os.path.exists(yol):
            veri = oku_bayt(yol)
            z = datetime.datetime.fromtimestamp(os.path.getmtime(yol)).strftime("%Y-%m-%d %H:%M:%S")
            print("%-32s %-13s %9d  %-19s %s" % (ad, ozet(veri)[:12], len(veri), z, "; ".join(notlar)))
        else:
            print("%-32s %-13s %9s  %-19s %s" % (ad, "-", "-", "-", "; ".join(["YOK"] + notlar)))
    kilitler = [x for x in os.listdir(klasor) if x.endswith(".kilit")]
    if kilitler:
        print("Kilitler: " + ", ".join(kilitler))


def komut_oku(a):
    yol = os.path.join(a.klasor, a.dosya)
    if not os.path.exists(yol):
        sys.exit("HATA: %s yok." % a.dosya)
    veri = oku_bayt(yol)
    metin, _, _ = coz(veri)
    sys.stdout.write(metin)
    if not metin.endswith("\n"):
        sys.stdout.write("\n")
    print("TEMEL=%s" % ozet(veri))


def komut_yaz(a):
    ad_uyarilari(a.klasor, a.dosya)
    yol = os.path.join(a.klasor, a.dosya)
    yeni_veri = oku_bayt(a.yeni)
    yeni_metin, _, _ = coz(yeni_veri)
    kilit = kilitle(a.klasor, a.dosya, a.yazar)
    try:
        var = os.path.exists(yol)
        eski_veri = oku_bayt(yol) if var else b""
        eski_ozet = ozet(eski_veri) if var else ""
        if var:
            if not a.temel:
                sys.exit("HATA: dosya var; önce 'oku' ile TEMEL alın ve --temel verin (görmeden üzerine yazılmaz).")
            if a.temel != eski_ozet:
                eski_metin = coz(eski_veri)[0]
                temel_yolu = None
                for x in os.listdir(os.path.join(a.klasor, YEDEK_DIZIN)) if os.path.isdir(os.path.join(a.klasor, YEDEK_DIZIN)) else []:
                    if a.temel[:12] in x and x.startswith(os.path.splitext(nfc(a.dosya))[0] + "."):
                        temel_yolu = os.path.join(a.klasor, YEDEK_DIZIN, x)
                print("REDDEDİLDİ: %s siz okuduktan sonra değişti (temel %s, şimdi %s)." % (a.dosya, a.temel[:12], eski_ozet[:12]), file=sys.stderr)
                if temel_yolu:
                    fark = difflib.unified_diff(coz(oku_bayt(temel_yolu))[0].splitlines(), eski_metin.splitlines(),
                                                "okuduğunuz sürüm", "şimdiki sürüm", lineterm="", n=1)
                    print("Bu arada yapılan değişiklik:", file=sys.stderr)
                    for s in fark:
                        print("  " + s, file=sys.stderr)
                else:
                    print("Okuduğunuz sürümün yedeği bulunamadı; şimdiki sürümü yeniden okuyup birleştirin.", file=sys.stderr)
                bekleyen = os.path.join(a.klasor, YEDEK_DIZIN, "%s.BEKLEYEN-%s-%s.txt" % (
                    os.path.splitext(nfc(a.dosya))[0], datetime.datetime.now().strftime("%Y%m%d-%H%M%S"), ascii_anahtar(a.yazar)))
                os.makedirs(os.path.dirname(bekleyen), exist_ok=True)
                with open(bekleyen, "wb") as f:
                    f.write(yeni_veri)
                print("Yazmak istediğiniz içerik kaybolmadı: %s" % bekleyen, file=sys.stderr)
                sys.exit(3)
            yedek = yedekle(a.klasor, a.dosya, eski_veri)
            _, bom, crlf = coz(eski_veri)
        else:
            yedek, bom, crlf = None, False, os.name == "nt"
        cikti = kodla(yeni_metin, bom, crlf)
        atomik_yaz(yol, cikti)
        yeni_ozet = ozet(cikti)
        gunluk(a.klasor, a.yazar, a.dosya, eski_ozet, yeni_ozet, a.dayanak, "yaz", a.not_ or "")
        print("Yazıldı: %s · %s → %s%s" % (a.dosya, eski_ozet[:12] or "yok", yeni_ozet[:12], (" · yedek: " + os.path.basename(yedek)) if yedek else ""))
        print("TEMEL=%s" % yeni_ozet)
    finally:
        kilit_ac(kilit)


def komut_ekle(a):
    ad_uyarilari(a.klasor, a.dosya)
    yol = os.path.join(a.klasor, a.dosya)
    parca, _, _ = coz(oku_bayt(a.parca))
    if not parca.strip():
        sys.exit("HATA: eklenecek parça boş.")
    kilit = kilitle(a.klasor, a.dosya, a.yazar)
    try:
        var = os.path.exists(yol)
        eski_veri = oku_bayt(yol) if var else b""
        eski_ozet = ozet(eski_veri) if var else ""
        if var:
            eski_metin, bom, crlf = coz(eski_veri)
            yedek = yedekle(a.klasor, a.dosya, eski_veri)
        else:
            eski_metin, bom, crlf, yedek = "", False, os.name == "nt", None
        govde = eski_metin.rstrip("\n")
        yeni_metin = (govde + "\n\n" if govde else "") + parca.strip("\n") + "\n"
        cikti = kodla(yeni_metin, bom, crlf)
        atomik_yaz(yol, cikti)
        yeni_ozet = ozet(cikti)
        gunluk(a.klasor, a.yazar, a.dosya, eski_ozet, yeni_ozet, a.dayanak, "ekle", a.not_ or "")
        print("Eklendi: %s · %s → %s%s" % (a.dosya, eski_ozet[:12] or "yok", yeni_ozet[:12], (" · yedek: " + os.path.basename(yedek)) if yedek else ""))
        print("TEMEL=%s" % yeni_ozet)
    finally:
        kilit_ac(kilit)


def komut_kilit_kaldir(a):
    yol = kilit_yolu(a.klasor, a.dosya)
    if not os.path.exists(yol):
        print("Kilit yok.")
        return
    yas = time.time() - os.path.getmtime(yol)
    sahip = open(yol, encoding="utf-8").read().strip()
    if yas < KILIT_SURESI_SN and not a.zorla:
        sys.exit("HATA: kilit %d saniyelik (%s); bayat değil. Sahibi gerçekten yazmıyorsa --zorla." % (yas, sahip))
    os.remove(yol)
    gunluk(a.klasor, a.yazar, a.dosya, "", "kilit", "kilit kaldırıldı: " + sahip, "kilit")
    print("Kilit kaldırıldı (%s)." % sahip)


def main():
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="Ortak anlatı dosyaları için korumalı yazma.")
    p.add_argument("--klasor", default=".", help="ortak klasör (varsayılan: bulunulan)")
    alt = p.add_subparsers(dest="komut", required=True)
    alt.add_parser("durum")
    k = alt.add_parser("oku"); k.add_argument("dosya")
    k = alt.add_parser("yaz"); k.add_argument("dosya"); k.add_argument("--temel", default=""); k.add_argument("--yeni", required=True)
    k.add_argument("--yazar", required=True); k.add_argument("--dayanak", required=True); k.add_argument("--not", dest="not_")
    k = alt.add_parser("ekle"); k.add_argument("dosya"); k.add_argument("--parca", required=True)
    k.add_argument("--yazar", required=True); k.add_argument("--dayanak", required=True); k.add_argument("--not", dest="not_")
    k = alt.add_parser("kilit-kaldir"); k.add_argument("dosya"); k.add_argument("--yazar", required=True); k.add_argument("--zorla", action="store_true")
    a = p.parse_args()
    if not os.path.isdir(a.klasor):
        sys.exit("HATA: klasör yok: %s" % a.klasor)
    {"durum": komut_durum, "oku": komut_oku, "yaz": komut_yaz, "ekle": komut_ekle, "kilit-kaldir": komut_kilit_kaldir}[a.komut](a)


if __name__ == "__main__":
    main()
