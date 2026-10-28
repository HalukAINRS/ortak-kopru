#!/usr/bin/env python3
"""Şimdi ve sonrası kaydını (docs/gecmis/simdi-ve-sonrasi.json): rafinasyonun dokuz sorusunu hesaplar ve denetler.

Kayıt iki zamanı taşır: "simdi" rafinenin gözlenen hâli, "sonra" rafine sonrası olabilecek
senaryolar. Bu araç kaydın anlatısını yazmaz; şunları yapar:

  hesapla   Çağrı günlüklerinin büyüklüğünü ve inceltilmiş biçimde ne kadar yer tutacağını,
            atlanma günlüğünü, yapılandırılmış hiçbir yolun cevaplayamayacağı açık kayıtları
            ve bulgu sayılarını depodan hesaplar.
  denetle   Sözleşmeye uyumu; her senaryonun dokuz soruyu ve "Nasıl geri alınır?" varyantını
            yanıtlamasını; kullanılan her varyantın tanımlı, tanımlı her varyantın kullanılmış
            olmasını; her birleşimin en az iki kök soru taşımasını ve dokuz kökün de bir
            birleşimde geçmesini; açık her bulgunun bir senaryoya bağlanmasını; ön koşulların
            var ve döngüsüz olmasını; ölçüm anahtarlarının ve depo içi dayanakların varlığını.
  sira      Senaryoların ön koşullara göre uygulanabilir sırasını ("Ne zaman?") verir.
  belge     docs/gecmis/simdi-ve-sonrasi.md içindeki üretilen tabloları (karşılaştırma, senaryolar,
            birleşimler, varyantlar) bu kayıttan yazar; --check belgeyle kaydın eşliğini denetler.

Defter ve günlüklere bağlı hesaplar ana dala yeni kayıt eklendikçe değişir; --check bu
farkları hata değil bilgi olarak yazar, çünkü kayıtlı değerler tarihli gözlemdir.

Kullanım:
    python tools/simdi_ve_sonrasi.py            # hesaplananları yenile ve denetle
    python tools/simdi_ve_sonrasi.py --check    # yazmadan denetle; yapısal hata varsa çıkış 1
    python tools/simdi_ve_sonrasi.py --olc      # hesaplananları JSON olarak yazdır
    python tools/simdi_ve_sonrasi.py --sira     # senaryoların ön koşul sırası
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

KOK = Path(__file__).resolve().parents[1]
KAYIT = KOK / "docs" / "gecmis" / "simdi-ve-sonrasi.json"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK / "defter"))
sys.path.insert(0, str(KOK / "tools"))

import depo_tanimi  # noqa: E402
import kopru_yanitla  # noqa: E402
import sema_denetle  # noqa: E402

KOKLER = depo_tanimi.KOORDINATLAR
ZORUNLU_VARYANT = "nasil.geri_alinir"
# İnceltilmiş günlükte kullanıcı iletisi yerine kalacak kayıt kimlikleri ve sayfa özeti için ayrılan pay.
REFERANS_BAYTI = 200
ILETI = re.compile(r"^## Kullanıcı iletisi\n.*?(?=^## Ham yanıt$)", re.S | re.M)
GUNLUK_ADI = re.compile(r"^(\d{8})-(\d{6})Z-")
INSAN = {"sen", "haluk"}


def gunlukleri_olc(dizin: Path) -> dict[str, int | str]:
    """Çağrı günlüklerini ölçer; kullanıcı iletisi bölümü defterin o anki tam kopyasını taşır."""
    gunlukler = sorted(yol for yol in dizin.glob("*.md") if GUNLUK_ADI.match(yol.name))
    toplam = ileti = 0
    son_toplam = son_ileti = 0
    gunler: Counter[str] = Counter()
    for yol in gunlukler:
        metin = yol.read_bytes().replace(b"\r\n", b"\n").decode("utf-8", errors="replace")
        bayt = len(metin.encode("utf-8"))
        eslesme = ILETI.search(metin)
        ileti_bayti = len(eslesme.group(0).encode("utf-8")) if eslesme else 0
        toplam, ileti = toplam + bayt, ileti + ileti_bayti
        son_toplam, son_ileti = bayt, ileti_bayti
        gunler[GUNLUK_ADI.match(yol.name).group(1)] += 1

    def zaman(yol: Path) -> str:
        tarih, saat = GUNLUK_ADI.match(yol.name).groups()
        return f"{tarih[:4]}-{tarih[4:6]}-{tarih[6:]}T{saat[:2]}:{saat[2:4]}:{saat[4:]}Z"

    sonuc: dict[str, int | str] = {
        "gunluk_sayisi": len(gunlukler),
        "gunluk_bayti": toplam,
        "gunluk_ileti_bayti": ileti,
        "gunluk_ileti_binde": round(1000 * ileti / toplam) if toplam else 0,
        "gunluk_inceltilmis_bayt_tahmini": toplam - ileti + REFERANS_BAYTI * len(gunlukler),
        "son_gunluk_bayti": son_toplam,
        "son_gunluk_inceltilmis_bayt_tahmini": son_toplam - son_ileti + REFERANS_BAYTI if gunlukler else 0,
        "gunluk_yazilan_gun": len(gunler),
    }
    if gunlukler:
        sonuc["ilk_gunluk_zamani"], sonuc["son_gunluk_zamani"] = zaman(gunlukler[0]), zaman(gunlukler[-1])
    atlandi = dizin / "atlandi.log"
    satirlar = atlandi.read_text(encoding="utf-8").splitlines() if atlandi.is_file() else []
    sonuc["atlandi_satiri"] = len(satirlar)
    if satirlar:
        sonuc["son_atlandi_zamani"] = satirlar[-1][:20].replace(" ", "T").rstrip()
    return sonuc


def yapilandirilmis_kimlikler(ayar_dosyalari: list[Path]) -> set[tuple[str, str]]:
    """Ayar dosyalarındaki her çağrı yolunun (asıl ve yedek) hedef kimliği."""
    kimlikler = set()
    for dosya in ayar_dosyalari:
        for kat in json.loads(dosya.read_text(encoding="utf-8"))["katilimcilar"]:
            for yol in [kat] + ([kat["yedek"]] if kat.get("yedek") else []):
                kimlikler.add(kopru_yanitla.hedef_kimligi(kopru_yanitla.yol_kimligi(kat["ad"], kat, yol)))
    return kimlikler


def yetim_kayitlar(kayitlar: list[dict], kimlikler: set[tuple[str, str]]) -> dict[str, set[str]]:
    """Açık kayıtların adreslerinden hiçbir yapılandırılmış yolun cevaplayamayacaklarını bulur.

    Açık katman adresi ancak aynı katmanın yoluyla, yalın üretici adresi o üreticinin herhangi
    bir yoluyla cevaplanabilir. İnsan adresleri (Sen, Haluk) bot hedefi değildir. Sonuç
    adres → bekleyen kayıt kimlikleri; bekleme kuralı kopru_yanitla.bekleyenler ile aynıdır.
    """
    ureticiler = {uretici for uretici, _ in kimlikler}
    adresler = set()
    for kayit in kayitlar:
        if kayit["durum"] != "acik":
            continue
        for uretici, katman in kopru_yanitla.kime_adlari(kayit["kime"]):
            if uretici in INSAN:
                continue
            if ((uretici, katman) not in kimlikler) if katman else (uretici not in ureticiler):
                adresler.add((uretici, katman))
    sonuc = {}
    for uretici, katman in sorted(adresler):
        ad = f"{uretici} ({katman})" if katman else uretici
        # Yalın üretici adresli kayıtlar o üreticinin yapılandırılmış bir yolunca cevaplanabilir;
        # yetim sayılan, yalnız bu adrese açıkça yazılmış bekleyen kayıttır.
        bekleyen = {kayit["id"] for kayit in kopru_yanitla.bekleyenler(kayitlar, ad)
                    if (uretici, katman) in kopru_yanitla.kime_adlari(kayit["kime"])}
        if bekleyen:
            sonuc[ad] = bekleyen
    return sonuc


def hesapla() -> dict[str, int | str]:
    olcum = gunlukleri_olc(KOK / "kayit")
    kayitlar = kopru_yanitla.kayitlari_oku(str(KOK / "kopru.html"))
    kimlikler = yapilandirilmis_kimlikler([KOK / "katilimcilar" / "ayarlar.json", KOK / "katilimcilar" / "ayarlar-yerel.json"])
    yetimler = yetim_kayitlar(kayitlar, kimlikler)
    hepsi = set().union(*yetimler.values()) if yetimler else set()
    sahit = yetimler.get("gemini (şahit)", set())
    olcum.update({
        "yapilandirilmis_yol": len(kimlikler),
        "yetim_acik_kayit": len(hepsi),
        "yetim_dagilimi": "; ".join(f"{ad}={len(kimlik)}" for ad, kimlik in yetimler.items()) or "yok",
        "sahit_yolu_sonrasi_yetim": len(hepsi - sahit),
    })
    bulgular = []
    for yol in sorted((KOK / "docs" / "gecmis" / "rafine").glob("*.json")):
        bulgular.extend(json.loads(yol.read_text(encoding="utf-8"))["findings"])
    olcum["acik_bulgu"] = sum(1 for bulgu in bulgular if bulgu["resolution"] in ("açık", "doğrulanmadı"))
    olcum["duzeltilen_bulgu"] = sum(1 for bulgu in bulgular if bulgu["resolution"] == "düzeltildi")
    return olcum


def bulgulari_oku() -> dict[str, str]:
    """Bulgu kimliği → çözüm durumu, docs/gecmis/rafine/*.json kayıtlarından."""
    sonuc = {}
    for yol in sorted((KOK / "docs" / "gecmis" / "rafine").glob("*.json")):
        for bulgu in json.loads(yol.read_text(encoding="utf-8"))["findings"]:
            sonuc[bulgu["id"]] = bulgu["resolution"]
    return sonuc


def sira(senaryolar: list[dict]) -> tuple[list[str], list[str]]:
    """Ön koşullara göre kararlı topolojik sıra; (sıra, hatalar)."""
    kimlikler = {senaryo["id"] for senaryo in senaryolar}
    hatalar = [f"sonra.{senaryo['id']}.onkosul: tanımsız {onkosul}" for senaryo in senaryolar
               for onkosul in senaryo["onkosul"] if onkosul not in kimlikler]
    if len(kimlikler) != len(senaryolar):
        hatalar.append("sonra.senaryolar: kimlikler tekil değil")
    if hatalar:
        return [], hatalar
    kalan = {senaryo["id"]: set(senaryo["onkosul"]) for senaryo in senaryolar}
    sonuc: list[str] = []
    while kalan:
        hazir = sorted(kimlik for kimlik, onkosul in kalan.items() if onkosul <= set(sonuc))
        if not hazir:
            return sonuc, [f"sonra.onkosul: döngü var ({', '.join(sorted(kalan))})"]
        sonuc.extend(hazir)
        for kimlik in hazir:
            del kalan[kimlik]
    return sonuc, []


def denetle(veri: dict, hesap: dict, bulgular: dict[str, str], olcum_anahtarlari: set[str]) -> list[str]:
    hatalar = [f"sözleşme: {hata}" for hata in sema_denetle.dogrula(sema_denetle.sema_yukle("simdi-ve-sonrasi"), veri)]
    if hatalar:
        return hatalar
    if [soru["kok"] for soru in veri["sorular"]] != list(KOKLER):
        hatalar.append("sorular: dokuz kök bu sırayla bulunmalı: " + ", ".join(KOKLER))
    tanimli = {}
    for soru in veri["sorular"]:
        for varyant in soru["varyantlar"]:
            if not varyant["id"].startswith(soru["kok"] + "."):
                hatalar.append(f"sorular.{soru['kok']}: {varyant['id']} başka köke ait")
            if varyant["id"] in tanimli:
                hatalar.append(f"sorular: {varyant['id']} iki kez tanımlı")
            tanimli[varyant["id"]] = soru["kok"]
    if ZORUNLU_VARYANT not in tanimli:
        hatalar.append(f"sorular: {ZORUNLU_VARYANT} tanımlı olmalı")
    kullanilan: set[str] = set()
    anahtarlar = olcum_anahtarlari | set(hesap)

    def dayanak_denetle(konum: str, dayanak: str | None) -> None:
        yol = depo_tanimi.dayanak_yolu(dayanak) if dayanak else None
        if yol is not None and not yol.exists():
            hatalar.append(f"{konum}.dayanak: depoda yok ({dayanak})")

    for kok in KOKLER:
        for sira_no, oge in enumerate(veri["simdi"][kok]["ogeler"]):
            konum = f"simdi.{kok}.ogeler[{sira_no}]"
            if "varyant" in oge:
                kullanilan.add(oge["varyant"])
                if oge["varyant"] not in tanimli:
                    hatalar.append(f"{konum}.varyant: tanımsız {oge['varyant']}")
                elif tanimli[oge["varyant"]] != kok:
                    hatalar.append(f"{konum}.varyant: {oge['varyant']} bu köke ait değil")
            if "olcum" in oge and oge["olcum"] not in anahtarlar:
                hatalar.append(f"{konum}.olcum: bilinmeyen ölçüm {oge['olcum']}")
            dayanak_denetle(konum, oge.get("dayanak"))
    senaryolar = veri["sonra"]["senaryolar"]
    bagli_bulgular = set()
    for senaryo in senaryolar:
        konum = f"sonra.{senaryo['id']}"
        if ZORUNLU_VARYANT not in senaryo["varyantlar"]:
            hatalar.append(f"{konum}: '{ZORUNLU_VARYANT}' yanıtlanmalı (her öneri geri alınabilir olmalı)")
        for varyant in senaryo["varyantlar"]:
            kullanilan.add(varyant)
            if varyant not in tanimli:
                hatalar.append(f"{konum}.varyantlar: tanımsız {varyant}")
        for bulgu in senaryo["kaynak_bulgu"]:
            bagli_bulgular.add(bulgu)
            if bulgu not in bulgular:
                hatalar.append(f"{konum}.kaynak_bulgu: bulgu kayıtlarında yok {bulgu}")
        for anahtar in senaryo.get("olcumler", []):
            if anahtar not in anahtarlar:
                hatalar.append(f"{konum}.olcumler: bilinmeyen ölçüm {anahtar}")
    for bulgu, cozum in sorted(bulgular.items()):
        if cozum in ("açık", "doğrulanmadı") and bulgu not in bagli_bulgular:
            hatalar.append(f"sonra: açık bulgu {bulgu} hiçbir senaryoya bağlı değil")
    _, sira_hatalari = sira(senaryolar)
    hatalar.extend(sira_hatalari)
    kokler_birlesimde = set()
    for birlesim in veri["birlesimler"]:
        konum = f"birlesimler.{birlesim['id']}"
        if len(set(birlesim["sorular"])) < 2:
            hatalar.append(f"{konum}: en az iki farklı kök soru birleşmeli")
        kokler_birlesimde.update(birlesim["sorular"])
        for varyant in birlesim.get("varyantlar", []):
            kullanilan.add(varyant)
            if varyant not in tanimli:
                hatalar.append(f"{konum}.varyantlar: tanımsız {varyant}")
            elif tanimli[varyant] not in birlesim["sorular"]:
                hatalar.append(f"{konum}.varyantlar: {varyant} birleşimin köklerinden değil")
        for anahtar in birlesim.get("olcumler", []):
            if anahtar not in anahtarlar:
                hatalar.append(f"{konum}.olcumler: bilinmeyen ölçüm {anahtar}")
        dayanak_denetle(konum, birlesim.get("dayanak"))
    for kok in sorted(set(KOKLER) - kokler_birlesimde):
        hatalar.append(f"birlesimler: '{kok}' hiçbir birleşimde geçmiyor")
    for varyant in sorted(set(tanimli) - kullanilan):
        hatalar.append(f"sorular: {varyant} tanımlı ama hiçbir yanıtta kullanılmıyor")
    kimlikler = [birlesim["id"] for birlesim in veri["birlesimler"]]
    if len(kimlikler) != len(set(kimlikler)):
        hatalar.append("birlesimler: kimlikler tekil değil")
    return hatalar


def kapsam(veri: dict) -> dict[str, int]:
    """Birleşimlerin kapsadığı kök çiftleri; 36 olası çiftten kaçının sorulduğu.

    Dokuz kökün hepsini birden taşıyan özet birleşimi her çifti kendiliğinden kapsadığı için
    çift sayımına katılmaz; ayrı sayılır.
    """
    ciftler = set()
    for birlesim in veri["birlesimler"]:
        kokler = sorted(set(birlesim["sorular"]), key=KOKLER.index)
        if len(kokler) == len(KOKLER):
            continue
        ciftler.update((a, b) for i, a in enumerate(kokler) for b in kokler[i + 1:])
    return {"cift": len(ciftler), "olasi_cift": len(KOKLER) * (len(KOKLER) - 1) // 2,
            "birlesim": len(veri["birlesimler"]),
            "uclu_ve_ustu": sum(3 <= len(set(b["sorular"])) < len(KOKLER) for b in veri["birlesimler"]),
            "dokuzlu_ozet": sum(len(set(b["sorular"])) == len(KOKLER) for b in veri["birlesimler"])}


BELGE = KOK / "docs" / "gecmis" / "simdi-ve-sonrasi.md"
BLOK = re.compile(r"(<!-- uretilen:(?P<ad>[a-z_]+) -->\n)(?P<icerik>.*?)(<!-- /uretilen:(?P=ad) -->)", re.S)


def _hucre(metin: str) -> str:
    return metin.replace("|", "\\|").replace("\n", " ")


def tablolar(veri: dict) -> dict[str, str]:
    """Belgedeki üretilen tabloları kayıttan kurar; belge elle değil bu kayıttan güncellenir."""
    sorular = {soru["kok"]: soru["soru"] for soru in veri["sorular"]}
    senaryolar = {senaryo["id"]: senaryo for senaryo in veri["sonra"]["senaryolar"]}
    ilk = veri["sonra"]["senaryolar"][0]
    kisa = veri["kesit"]["temel_commit"][:7]
    satirlar = [f"| Soru | Şimdi: ana dal (`{kisa}`) | Rafine sonrası, {ilk['id']}: {_hucre(ilk['ad'])} |",
                "| --- | --- | --- |"]
    for kok in KOKLER:
        satirlar.append(f"| {sorular[kok]} | {_hucre(veri['simdi'][kok]['yanit'])} | {_hucre(ilk['yanitlar'][kok])} |")
    karsilastirma = "\n".join(satirlar) + "\n"
    sirali, _ = sira(veri["sonra"]["senaryolar"])
    satirlar = ["| Sıra | Senaryo | Durum | Karar | Ön koşul | Bulgular |", "| --- | --- | --- | --- | --- | --- |"]
    for sira_no, kimlik in enumerate(sirali, 1):
        senaryo = senaryolar[kimlik]
        satirlar.append(f"| {sira_no} | {kimlik} {_hucre(senaryo['ad'])} | {senaryo['durum']} | {_hucre(senaryo['karar'])} | "
                        f"{', '.join(senaryo['onkosul']) or '—'} | {', '.join(senaryo['kaynak_bulgu']) or '—'} |")
    senaryo_tablosu = "\n".join(satirlar) + "\n"
    satirlar = ["| Kimlik | Birleşen sorular | Soru | Katman | Durum |", "| --- | --- | --- | --- | --- |"]
    for birlesim in veri["birlesimler"]:
        adlar = " + ".join(sorular[kok] for kok in birlesim["sorular"])
        satirlar.append(f"| {birlesim['id']} | {_hucre(adlar)} | {_hucre(birlesim['soru'])} | {birlesim['katman']} | {birlesim['durum']} |")
    birlesim_tablosu = "\n".join(satirlar) + "\n"
    satirlar = ["| Soru | Varyantlar |", "| --- | --- |"]
    for soru in veri["sorular"]:
        satirlar.append(f"| {soru['soru']} | " + "; ".join(f"{v['soru']} ({_hucre(v['anlam'])})" for v in soru["varyantlar"]) + " |")
    varyant_tablosu = "\n".join(satirlar) + "\n"
    return {"karsilastirma": karsilastirma, "senaryolar": senaryo_tablosu,
            "birlesimler": birlesim_tablosu, "varyantlar": varyant_tablosu}


def belge_guncelle(metin: str, uretilen: dict[str, str]) -> str:
    return BLOK.sub(lambda m: m.group(1) + uretilen.get(m.group("ad"), m.group("icerik")) + m.group(4), metin)


def belge_denetle(metin: str, uretilen: dict[str, str]) -> list[str]:
    bulunan = {m.group("ad"): m.group("icerik") for m in BLOK.finditer(metin)}
    hatalar = [f"belge: '{ad}' tablosunun işaretleri yok" for ad in sorted(set(uretilen) - set(bulunan))]
    hatalar += [f"belge: '{ad}' tablosu kayıtla uyumsuz" for ad in sorted(set(uretilen) & set(bulunan))
                if bulunan[ad] != uretilen[ad]]
    hatalar += [f"belge: bilinmeyen üretilen blok '{ad}'" for ad in sorted(set(bulunan) - set(uretilen))]
    return hatalar


def main() -> int:
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    kip = parser.add_mutually_exclusive_group()
    kip.add_argument("--check", action="store_true", help="yazmadan denetle")
    kip.add_argument("--olc", action="store_true", help="yalnız hesaplananları yazdır")
    kip.add_argument("--sira", action="store_true", help="senaryoların ön koşul sırasını yazdır")
    args = parser.parse_args()
    hesap = hesapla()
    if args.olc:
        print(json.dumps(hesap, ensure_ascii=False, indent=2))
        return 0
    veri = json.loads(KAYIT.read_text(encoding="utf-8"))
    if args.sira:
        sonuc, hatalar = sira(veri["sonra"]["senaryolar"])
        adlar = {senaryo["id"]: senaryo["ad"] for senaryo in veri["sonra"]["senaryolar"]}
        for sira_no, kimlik in enumerate(sonuc, 1):
            print(f"{sira_no:>2}. {kimlik} {adlar[kimlik]}")
        for hata in hatalar:
            print(hata)
        return 1 if hatalar else 0
    if not args.check:
        veri["hesaplanan"] = hesap
        KAYIT.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    olcum_anahtarlari = set(depo_tanimi.olc())
    hatalar = denetle(veri, hesap, bulgulari_oku(), olcum_anahtarlari)
    if not hatalar:
        metin = BELGE.read_text(encoding="utf-8") if BELGE.is_file() else ""
        uretilen = tablolar(veri)
        if not args.check and metin:
            yeni = belge_guncelle(metin, uretilen)
            if yeni != metin:
                BELGE.write_text(yeni, encoding="utf-8", newline="\n")
                metin = yeni
        hatalar.extend(belge_denetle(metin, uretilen))
    for hata in hatalar:
        print(hata)
    for anahtar in sorted(set(veri["hesaplanan"]) | set(hesap)):
        if veri["hesaplanan"].get(anahtar) != hesap.get(anahtar):
            print(f"bilgi: kesitten bu yana değişti, tarihli değer korunuyor: {anahtar}: "
                  f"{veri['hesaplanan'].get(anahtar)!r} → {hesap.get(anahtar)!r}")
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/simdi_ve_sonrasi.py")
        return 1
    k = kapsam(veri)
    print(f"TAMAM: dokuz kök, {sum(len(s['varyantlar']) for s in veri['sorular'])} varyant, "
          f"{len(veri['sonra']['senaryolar'])} senaryo, {k['birlesim']} birleşim "
          f"({k['cift']}/{k['olasi_cift']} kök çifti, {k['uclu_ve_ustu']} üçlü, {k['dokuzlu_ozet']} dokuzlu özet) "
          f"ve belgedeki tablolar tutarlı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
