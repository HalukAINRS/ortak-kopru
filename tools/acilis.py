#!/usr/bin/env python3
"""Deponun açılışını (docs/acilis.json) denetler ve dört yüzdeki açılış metnini ondan üretir.

Açılış; kullanıcının niyet sözünü, bu niyetten kurulan tanımı, dokuz soruyu ve altı ana
ilkeyi taşır. Sorular iki gruptadır: kapının kendisini tanımlayan beşli (ne, nerede, nasıl,
ne zaman, ne için) ve içinden geçeni tanımlayan dörtlü (nereden, nereye, ne kadar, neden).

Denetim:
  - sözleşmeye uyum;
  - beşli ve dörtlünün tam, ayrık ve birlikte dokuz soru olması;
  - 5×4 = 20 kesişimin her birinin tam bir kez sorulması;
  - altı ilkenin 1–6 numaralı olması, her ilkenin en az bir kapı ve bir geçiş sorusunu
    bağlaması, ilkelerin birlikte dokuz soruyu kapsaması;
  - "uygulanıyor" olmayan ilkenin eksiğini yazması; dayanak yollarının depoda bulunması;
    bağlı bulguların rafine kayıtlarında açık, bağlı senaryoların senaryo kaydında var olması;
  - dokuz sorunun sade yanıtının açılış belgesinde tam bir kez yer alması ('Niyet' bölümünde ya da
    yanıtı bağlayan ilkenin bölümünde);
  - README.md, docs/web-girisi.md, docs/acilis.md ve docs/teknik/acilis-teknik.md içindeki üretilen
    blokların kayıtla eşliği;
  - yapı: açılış metni önce 'Niyet', sonra sırayla altı ilkenin başlığını taşır; liste, tablo ya da
    alıntı bloğu taşımaz, paragraflardan oluşur (docs/acilis.md, README ve Web açılışı);
  - okunabilirlik: docs/acilis.md, README.md ve Web açılışı ilk kez gelen okuyucu içindir; kod
    biçimi, dosya adı, commit ya da iç kimlik taşımaz, sözlükte açıklanmayan teknik terim kullanmaz,
    cümleleri kısadır; açılış belgesi ve README teknik ayrıntılara (docs/teknik/) ve geçmiş işlere
    (docs/gecmis/) ayrı yerlerden bağlanır.

Kullanım:
    python tools/acilis.py            # blokları kayıttan yaz ve denetle
    python tools/acilis.py --check    # yazmadan denetle; uyumsuzlukta çıkış 1
"""
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
import re
import sys

KOK = Path(__file__).resolve().parents[1]
KAYIT = KOK / "docs" / "acilis.json"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK / "tools"))

import depo_tanimi  # noqa: E402
import sema_denetle  # noqa: E402

BESLI = ("ne", "nerede", "nasil", "ne_zaman", "ne_icin")
DORTLU = ("nereden", "nereye", "ne_kadar", "neden")
BLOK = re.compile(r"(<!-- uretilen:(?P<ad>[a-z_]+) -->\n)(?P<icerik>.*?)(<!-- /uretilen:(?P=ad) -->)", re.S)
DURUM_METNI = {"uygulanıyor": "uygulanıyor", "kısmen": "kısmen uygulanıyor", "henüz yok": "henüz yok"}


def _ad(veri: dict, kok: str) -> str:
    return veri["sorular"][kok]["soru"].rstrip("?")


def _hucre(metin: str) -> str:
    return metin.replace("|", "\\|").replace("\n", " ")


def _rafine_bulgulari() -> dict[str, str]:
    sonuc = {}
    for yol in sorted((KOK / "docs" / "gecmis" / "rafine").glob("*.json")):
        for bulgu in json.loads(yol.read_text(encoding="utf-8"))["findings"]:
            sonuc[bulgu["id"]] = bulgu["resolution"]
    return sonuc


def _senaryolar() -> set[str]:
    yol = KOK / "docs" / "gecmis" / "simdi-ve-sonrasi.json"
    if not yol.is_file():
        return set()
    return {senaryo["id"] for senaryo in json.loads(yol.read_text(encoding="utf-8"))["sonra"]["senaryolar"]}


def denetle(veri: dict, bulgular: dict[str, str] | None = None, senaryolar: set[str] | None = None) -> list[str]:
    hatalar = [f"sözleşme: {hata}" for hata in sema_denetle.dogrula(sema_denetle.sema_yukle("acilis"), veri)]
    if hatalar:
        return hatalar
    bulgular = _rafine_bulgulari() if bulgular is None else bulgular
    senaryolar = _senaryolar() if senaryolar is None else senaryolar
    if tuple(veri["gruplar"]["kapi"]["sorular"]) != BESLI:
        hatalar.append("gruplar.kapi: beşli bu sırayla olmalı: " + ", ".join(BESLI))
    if tuple(veri["gruplar"]["gecis"]["sorular"]) != DORTLU:
        hatalar.append("gruplar.gecis: dörtlü bu sırayla olmalı: " + ", ".join(DORTLU))
    ciftler = [(k["kapi"], k["gecis"]) for k in veri["kesisimler"]]
    for cift in sorted(set(itertools.product(BESLI, DORTLU)) - set(ciftler)):
        hatalar.append(f"kesisimler: {cift[0]} × {cift[1]} sorulmamış")
    for cift in sorted({c for c in ciftler if ciftler.count(c) > 1}):
        hatalar.append(f"kesisimler: {cift[0]} × {cift[1]} birden çok kez sorulmuş")
    ilkeler = veri["ilkeler"]
    if [ilke["no"] for ilke in ilkeler] != list(range(1, 7)):
        hatalar.append("ilkeler: numaralar 1'den 6'ya sırayla olmalı")
    kapsanan: set[str] = set()
    for ilke in ilkeler:
        konum = f"ilkeler[{ilke['no']}]"
        sorular = set(ilke["sorular"])
        kapsanan |= sorular
        if not sorular & set(BESLI) or not sorular & set(DORTLU):
            hatalar.append(f"{konum}: en az bir kapı (beşli) ve bir geçiş (dörtlü) sorusunu bağlamalı")
        if ilke["durum"] != "uygulanıyor" and not ilke.get("eksik"):
            hatalar.append(f"{konum}: '{ilke['durum']}' durumunda eksik yazılmalı")
        if ilke["durum"] == "uygulanıyor" and (ilke.get("bulgular") or ilke.get("senaryolar")):
            hatalar.append(f"{konum}: uygulanan ilke açık bulgu veya senaryoya bağlanmamalı")
        for yol in ilke["dayanaklar"]:
            hedef = depo_tanimi.dayanak_yolu(yol)
            if hedef is not None and not hedef.exists():
                hatalar.append(f"{konum}.dayanaklar: depoda yok ({yol})")
        for bulgu in ilke.get("bulgular", []):
            if bulgu not in bulgular:
                hatalar.append(f"{konum}.bulgular: rafine kayıtlarında yok {bulgu}")
            elif bulgular[bulgu] not in ("açık", "doğrulanmadı"):
                hatalar.append(f"{konum}.bulgular: {bulgu} kapanmış ({bulgular[bulgu]}); ilkenin durumu yeniden yazılmalı")
        for senaryo in ilke.get("senaryolar", []):
            if senaryo not in senaryolar:
                hatalar.append(f"{konum}.senaryolar: senaryo kaydında yok {senaryo}")
    for kok in [k for k in BESLI + DORTLU if k not in kapsanan]:
        hatalar.append(f"ilkeler: '{kok}' hiçbir ilkede geçmiyor")
    # Açılış belgesinde her sorunun sade yanıtı tam bir kez: 'Niyet' bölümünde ya da onu bağlayan ilkede.
    yanitlanan = list(veri["acilis_belgesi"]["niyet"]["sorular"])
    for ilke in ilkeler:
        for kok in ilke["sade_sorular"]:
            if kok not in ilke["sorular"]:
                hatalar.append(f"ilkeler[{ilke['no']}].sade_sorular: '{kok}' bu ilkenin bağladığı sorular arasında değil")
        yanitlanan += ilke["sade_sorular"]
    for kok in BESLI + DORTLU:
        if yanitlanan.count(kok) != 1:
            hatalar.append(f"acilis_belgesi: '{kok}' sorusunun sade yanıtı {yanitlanan.count(kok)} kez yer alıyor (tam bir kez olmalı)")
    return hatalar


AYLAR = ("Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık")


def _tarih(veri: dict) -> str:
    yil, ay, gun = veri["niyet"]["zaman"][:10].split("-")
    return f"{int(gun)} {AYLAR[int(ay) - 1]} {yil}"


SADE_DURUM = {"uygulanıyor": "işliyor", "kısmen": "kısmen işliyor", "henüz yok": "henüz yok"}
SAYI = {0: "hiçbiri", 1: "biri", 2: "ikisi", 3: "üçü", 4: "dördü", 5: "beşi", 6: "altısı"}


def _baslik(ilke: dict) -> str:
    return f"{ilke['no']}. {ilke['ad']}"


def basliklar(veri: dict) -> list[str]:
    """Açılışın başlık sırası: önce 'Niyet', sonra sırayla altı ilke."""
    return ["Niyet"] + [_baslik(ilke) for ilke in veri["ilkeler"]]


def _soru_paragrafi(veri: dict, kok: str) -> str:
    return f"**{veri['sorular'][kok]['soru']}** {veri['sorular'][kok]['sade']}"


def _kucuk(metin: str) -> str:
    return metin.replace("İ", "i").replace("I", "ı").lower()


def _durum_ozeti(veri: dict) -> str:
    durumlar = [ilke["durum"] for ilke in veri["ilkeler"]]
    tam, kismen, yok = durumlar.count("uygulanıyor"), durumlar.count("kısmen"), durumlar.count("henüz yok")
    cumle = f"Bu niyet altı ilkeyle işler. Bugün altısının {SAYI[tam]} tam olarak işliyor, {SAYI[kismen]} kısmen işliyor"
    cumle += f", {SAYI[yok]} henüz yok." if yok else "."
    return cumle + " Her ilke aşağıda kendi başlığında anlatılıyor."


def _kisa_acilis(veri: dict, acilis_yolu: str) -> str:
    """README ve Web girişi için aynı iskelet: 'Niyet', sonra altı ilke; her biri birer paragraf."""
    parcalar = [f"Bu bölüm açılışın kısa hâlidir. İlk kez geliyorsanız uzun ve sade anlatım [açılış sayfasındadır]({acilis_yolu}).",
                "## Niyet",
                f"{veri['niyet']['sahibi']}, {_tarih(veri)}: **“{veri['niyet']['soz']}”**",
                veri["sade_tanim"]]
    for ilke in veri["ilkeler"]:
        parcalar += [f"## {_baslik(ilke)}",
                     f"**{ilke['ilke']}** {ilke['sade']} Bugün {SADE_DURUM[ilke['durum']]}."]
    return "\n\n".join(parcalar) + "\n"


def readme_blogu(veri: dict) -> str:
    return _kisa_acilis(veri, "docs/acilis.md")


def web_blogu(veri: dict) -> str:
    return _kisa_acilis(veri, "acilis.md")


def acilis_belgesi(veri: dict) -> str:
    """docs/acilis.md'nin bütün gövdesi: giriş, 'Niyet' ve altı ilke; yalnız paragraf."""
    belge = veri["acilis_belgesi"]
    niyet = [f"Ortak Köprü'yü kuran kişi {veri['niyet']['sahibi']}. Bu yerin amacını {_tarih(veri)} günü kendi "
             "sözleriyle şöyle yazdı:", f"**“{veri['niyet']['soz']}”**"]
    niyet += [_soru_paragrafi(veri, kok) for kok in belge["niyet"]["sorular"]]
    niyet += belge["niyet"]["paragraflar"]
    ilkeler = []
    for ilke in veri["ilkeler"]:
        ilkeler += [f"## {_baslik(ilke)}", f"**{ilke['ilke']}**", ilke["sade"]]
        ilkeler += [_soru_paragrafi(veri, kok) for kok in ilke["sade_sorular"]]
        ilkeler += ilke["anlatim"] + [f"**Bugün:** {ilke['bugun_sade']}"]
    # Sözlük yalnız sayfada gerçekten geçen kelimeleri açıklar ve ilkelerden önce gelir.
    gorunen = _kucuk(_gorunen("\n".join(belge["giris"] + niyet + ilkeler)))
    gecenler = [m for m in veri["sozluk"]
                if any(_kucuk(parca) in gorunen for parca in m["terim"].split(" ve "))]
    sozluk = ["Bu sayfada geçen birkaç kelime: " + " ".join(f"**{m['terim']}:** {m['anlam']}" for m in gecenler)] if gecenler else []
    parcalar = belge["giris"] + ["## Niyet"] + niyet + sozluk + [_durum_ozeti(veri)] + ilkeler
    return "\n\n".join(parcalar) + "\n"


def tam_tanim(veri: dict) -> str:
    return veri["tanim"] + "\n"


def soru_tablosu(veri: dict) -> str:
    satirlar = ["| Soru | Grup | Niyete göre | Bugün depoda | Durum |", "| --- | --- | --- | --- | --- |"]
    for grup, kokler in (("kapi", BESLI), ("gecis", DORTLU)):
        for kok in kokler:
            soru = veri["sorular"][kok]
            satirlar.append(f"| {soru['soru']} | {veri['gruplar'][grup]['ad']} | {_hucre(soru['yanit'])} | "
                            f"{_hucre(soru['bugun'])} | {soru['durum']} |")
    return "\n".join(satirlar) + "\n"


def varyant_tablosu(veri: dict) -> str:
    satirlar = ["| Soru | Varyant | Yanıt |", "| --- | --- | --- |"]
    for kok in BESLI + DORTLU:
        for varyant in veri["sorular"][kok]["varyantlar"]:
            satirlar.append(f"| {veri['sorular'][kok]['soru']} | {_hucre(varyant['soru'])} | {_hucre(varyant['yanit'])} |")
    return "\n".join(satirlar) + "\n"


def ilke_metinleri(veri: dict) -> str:
    parcalar = []
    for ilke in veri["ilkeler"]:
        sorular = ", ".join(_ad(veri, k) for k in BESLI + DORTLU if k in ilke["sorular"])
        metin = [f"### {ilke['no']}. {ilke['ad']}", "", f"**{ilke['ilke']}**", "", ilke["aciklama"], "",
                 f"*Bağladığı sorular:* {sorular}. *Bugün:* {DURUM_METNI[ilke['durum']]}."
                 + (f" {ilke['eksik']}" if ilke.get("eksik") else ""), ""]
        parcalar.append("\n".join(metin))
    return "\n".join(parcalar)


def matris(veri: dict) -> str:
    sorular = {(k["kapi"], k["gecis"]): k["soru"] for k in veri["kesisimler"]}
    satirlar = ["| Kapı \\ Geçiş | " + " | ".join(_ad(veri, g) for g in DORTLU) + " |",
                "| --- |" + " --- |" * len(DORTLU)]
    for kapi in BESLI:
        satirlar.append(f"| **{_ad(veri, kapi)}** | " + " | ".join(_hucre(sorular[(kapi, g)]) for g in DORTLU) + " |")
    return "\n".join(satirlar) + "\n"


def kesisim_tablosu(veri: dict) -> str:
    sira = {cift: i for i, cift in enumerate(itertools.product(BESLI, DORTLU))}
    satirlar = ["| Kesişim | Soru | Yanıt |", "| --- | --- | --- |"]
    for k in sorted(veri["kesisimler"], key=lambda k: sira[(k["kapi"], k["gecis"])]):
        satirlar.append(f"| {_ad(veri, k['kapi'])} × {_ad(veri, k['gecis'])} | {_hucre(k['soru'])} | {_hucre(k['yanit'])} |")
    return "\n".join(satirlar) + "\n"


def ilke_tablosu(veri: dict) -> str:
    satirlar = ["| İlke | Bağladığı sorular | Bugün | Taşıyan dosyalar | Mesafe |", "| --- | --- | --- | --- | --- |"]
    for ilke in veri["ilkeler"]:
        sorular = ", ".join(_ad(veri, k) for k in BESLI + DORTLU if k in ilke["sorular"])
        dayanaklar = ", ".join(f"`{yol}`" for yol in ilke["dayanaklar"])
        bag = ", ".join(ilke.get("bulgular", []) + ilke.get("senaryolar", []))
        mesafe = _hucre(ilke["eksik"]) + (f" ({bag})" if bag else "") if ilke.get("eksik") else "—"
        satirlar.append(f"| {ilke['no']}. {ilke['ad']} | {sorular} | {DURUM_METNI[ilke['durum']]} | {dayanaklar} | {mesafe} |")
    return "\n".join(satirlar) + "\n"


# İlk kez gelen okuyucunun açılışta karşılaşmaması gereken teknik terimler. Sözlükte açıklanan terim
# kullanılabilir; açıklanmayan terim sade anlatıma giremez. Büyük harfli kısaltmalar büyük/küçük harfe duyarlı.
TEKNIK_TERIMLER = [
    (r"\bAPI\b", "API"), (r"\bCLI\b", "CLI"), (r"\bCI\b", "CI"), (r"\bJSON\b", "JSON"), (r"\bHTML\b", "HTML"),
    (r"\bSHA\b", "SHA"), (r"\bPR\b", "PR"), (r"(?i)\bcommit", "commit"), (r"(?i)\bissue", "issue"),
    (r"(?i)\bpull request", "pull request"), (r"(?i)\bgithub", "github"), (r"(?i)\bpages\b", "pages"),
    (r"(?i)\breadme", "readme"), (r"(?i)\bmarkdown", "markdown"), (r"(?i)\bterminal", "terminal"),
    (r"(?i)\bbetik", "betik"), (r"(?i)\bşema", "şema"), (r"(?i)\bkomut satır", "komut satırı"),
]
EN_UZUN_CUMLE = 30
ORTALAMA_CUMLE = 16


def _gorunen(metin: str) -> str:
    """İşaret satırlarını, bağlantı adreslerini ve vurgu işaretlerini çıkarır; okuyucunun gördüğü metin kalır."""
    metin = re.sub(r"<!--.*?-->", "", metin, flags=re.S)
    metin = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", metin)
    return metin.replace("**", "")


def okunabilirlik(ad: str, metin: str, sozluk_terimleri: list[str], ayrim_bagi: bool = False) -> list[str]:
    """İlk kez gelen okuyucu için yazılmış metnin sade kalıp kalmadığını denetler."""
    hatalar = []
    if "`" in metin:
        hatalar.append(f"{ad}: kod biçimi (`) kullanılmış")
    gorunen = _gorunen(metin)
    for desen, aciklama in [(r"\b[\w./-]+\.(?:py|json|md|html|ps1|cmd|ya?ml|sh|txt)\b", "dosya adı"),
                            (r"\b(?=[0-9a-f]*\d)[0-9a-f]{7,40}\b", "commit kimliği"),
                            (r"\b(?:R-\d{2}|S\d{2}|B\d{2}|k-\d{4})\b", "iç kimlik")]:
        for bulunan in sorted(set(re.findall(desen, gorunen))):
            hatalar.append(f"{ad}: {aciklama} görünüyor: {bulunan}")
    sozluk = [terim.lower() for terim in sozluk_terimleri]
    for desen, terim in TEKNIK_TERIMLER:
        if re.search(desen, gorunen) and not any(terim in madde for madde in sozluk):
            hatalar.append(f"{ad}: '{terim}' teknik terimi sözlükte açıklanmadan kullanılmış")
    duz = re.sub(r"“[^”]*”", "", gorunen)
    satirlar = [satir.lstrip("-# ").strip() for satir in duz.splitlines() if satir.strip() and not satir.startswith("#")]
    cumleler = [c for c in re.split(r"(?<=[.!?])\s+", " ".join(satirlar)) if c.strip()]
    uzunluklar = [len(c.split()) for c in cumleler]
    for cumle, uzunluk in zip(cumleler, uzunluklar):
        if uzunluk > EN_UZUN_CUMLE:
            hatalar.append(f"{ad}: {uzunluk} kelimelik cümle (en çok {EN_UZUN_CUMLE}): {cumle[:60]}…")
    if uzunluklar and sum(uzunluklar) / len(uzunluklar) > ORTALAMA_CUMLE:
        hatalar.append(f"{ad}: ortalama cümle {sum(uzunluklar) / len(uzunluklar):.1f} kelime (en çok {ORTALAMA_CUMLE})")
    if ayrim_bagi:
        for hedef, adi in (("teknik", "teknik ayrıntılar"), ("gecmis", "geçmiş işler")):
            if not re.search(r"\]\((?:docs/)?" + hedef + r"/(?:README\.md)?(?:#[^)]*)?\)", metin):
                hatalar.append(f"{ad}: {adi} yerine ({hedef}/) bağlantı yok")
    return hatalar


def yapi(ad: str, metin: str, beklenen: list[str]) -> list[str]:
    """Açılış metni paragraflardan oluşur: başlıklar 'Niyet' ve altı ilke, sırayla; liste, tablo, alıntı yok."""
    hatalar = []
    duz = re.sub(r"<!--.*?-->", "", metin, flags=re.S)
    bulunan = [m.group(1) for m in re.finditer(r"(?m)^## (.+)$", duz)]
    if bulunan[:len(beklenen)] != beklenen:
        hatalar.append(f"{ad}: başlık sırası {bulunan} (beklenen: {beklenen})")
    if re.search(r"(?m)^#{3,} ", duz):
        hatalar.append(f"{ad}: alt başlık (###) var; açılış yalnız 'Niyet' ve ilke başlıklarını taşır")
    for desen, aciklama in ((r"(?m)^\s*[-*+] ", "liste"), (r"(?m)^\s*\d+[.)] ", "numaralı liste"),
                            (r"(?m)^\s*\|", "tablo"), (r"(?m)^\s*>", "alıntı bloğu")):
        if re.search(desen, duz):
            hatalar.append(f"{ad}: {aciklama} var; açılış paragraflardan oluşur")
    return hatalar


def okunabilirlik_denetle(veri: dict) -> list[str]:
    terimler = [madde["terim"] for madde in veri["sozluk"]]
    hatalar = []
    acilis = KOK / "docs" / "acilis.md"
    if acilis.is_file():
        metin = acilis.read_text(encoding="utf-8")
        hatalar += okunabilirlik("docs/acilis.md", metin, terimler, ayrim_bagi=True)
        hatalar += yapi("docs/acilis.md", metin, basliklar(veri))
    readme = KOK / "README.md"
    if readme.is_file():
        # README, GitHub'da ilk görülen sayfadır: açılış bloğuyla birlikte bütünü sade kalır ve iki ayrı yere yönlendirir.
        hatalar += okunabilirlik("README.md", readme.read_text(encoding="utf-8"), terimler, ayrim_bagi=True)
        hatalar += yapi("README.md", readme.read_text(encoding="utf-8"), basliklar(veri) + ["Buradan başlayın"])
    for ad, blok in (("README açılışı", readme_blogu(veri)), ("Web açılışı", web_blogu(veri))):
        hatalar += okunabilirlik(ad, blok, terimler) + yapi(ad, blok, basliklar(veri))
    return hatalar


def _ayir(metin: str) -> str:
    """Bloğu işaretlerden boş satırla ayırır; Web üreticisi ve Markdown işaretleri ayrı paragraf görür."""
    return "\n" + metin.strip("\n") + "\n\n"


def bloklar(veri: dict) -> dict[Path, dict[str, str]]:
    return {yol: {ad: _ayir(metin) for ad, metin in uretilen.items()} for yol, uretilen in _ham_bloklar(veri).items()}


def _ham_bloklar(veri: dict) -> dict[Path, dict[str, str]]:
    return {
        KOK / "README.md": {"acilis": readme_blogu(veri)},
        KOK / "docs" / "web-girisi.md": {"acilis": web_blogu(veri)},
        KOK / "docs" / "acilis.md": {"acilis_belgesi": acilis_belgesi(veri)},
        KOK / "docs" / "teknik" / "acilis-teknik.md": {"acilis_tanim": tam_tanim(veri), "acilis_sorular": soru_tablosu(veri),
                                                       "acilis_varyantlar": varyant_tablosu(veri), "acilis_matris": matris(veri),
                                                       "acilis_kesisimler": kesisim_tablosu(veri), "acilis_ilkeler": ilke_tablosu(veri),
                                                       "acilis_ilke_metinleri": ilke_metinleri(veri)},
    }


def belge_guncelle(metin: str, uretilen: dict[str, str]) -> str:
    return BLOK.sub(lambda m: m.group(1) + uretilen.get(m.group("ad"), m.group("icerik")) + m.group(4), metin)


def belge_denetle(ad: str, metin: str, uretilen: dict[str, str]) -> list[str]:
    bulunan = {m.group("ad"): m.group("icerik") for m in BLOK.finditer(metin)}
    hatalar = [f"{ad}: '{blok}' bloğunun işaretleri yok" for blok in sorted(set(uretilen) - set(bulunan))]
    hatalar += [f"{ad}: '{blok}' bloğu açılış kaydıyla uyumsuz" for blok in sorted(set(uretilen) & set(bulunan))
                if bulunan[blok] != uretilen[blok]]
    return hatalar


def main() -> int:
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="yazmadan denetle")
    args = parser.parse_args()
    veri = json.loads(KAYIT.read_text(encoding="utf-8"))
    hatalar = denetle(veri)
    if not hatalar:
        for yol, uretilen in bloklar(veri).items():
            metin = yol.read_text(encoding="utf-8") if yol.is_file() else ""
            if not args.check and metin:
                yeni = belge_guncelle(metin, uretilen)
                if yeni != metin:
                    yol.write_text(yeni, encoding="utf-8", newline="\n")
                    metin = yeni
            hatalar.extend(belge_denetle(yol.relative_to(KOK).as_posix(), metin, uretilen))
        hatalar.extend(okunabilirlik_denetle(veri))
    for hata in hatalar:
        print(hata)
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/acilis.py")
        return 1
    durumlar = [ilke["durum"] for ilke in veri["ilkeler"]]
    print(f"TAMAM: niyet, tanım, 9 soru ({len(BESLI)}+{len(DORTLU)}), {len(veri['kesisimler'])} kesişim ve 6 ilke "
          f"({durumlar.count('uygulanıyor')} uygulanıyor, {durumlar.count('kısmen')} kısmen, "
          f"{durumlar.count('henüz yok')} henüz yok); README, Web girişi, açılış belgesi ve teknik ek kayıtla uyumlu; ilk temas metinleri sade.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
