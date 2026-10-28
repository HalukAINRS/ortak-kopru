#!/usr/bin/env python3
"""Deponun açılışını (docs/acilis.json) denetler ve üç yüzdeki açılış bloklarını ondan üretir.

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
  - README.md, docs/WEB_GIRISI.md ve docs/ACILIS.md içindeki üretilen blokların kayıtla eşliği.

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
    for yol in sorted((KOK / "docs" / "rafine").glob("*.json")):
        for bulgu in json.loads(yol.read_text(encoding="utf-8"))["findings"]:
            sonuc[bulgu["id"]] = bulgu["resolution"]
    return sonuc


def _senaryolar() -> set[str]:
    yol = KOK / "docs" / "rafine-sorulari.json"
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
    return hatalar


AYLAR = ("Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık")


def _tarih(veri: dict) -> str:
    yil, ay, gun = veri["niyet"]["zaman"][:10].split("-")
    return f"{int(gun)} {AYLAR[int(ay) - 1]} {yil}"


def readme_blogu(veri: dict) -> str:
    satirlar = [f"> **Niyet** ({veri['niyet']['sahibi']}, {_tarih(veri)}): “{veri['niyet']['soz']}”", "",
                f"**Tanım.** {veri['tanim']}", "", "**Altı ilke**", ""]
    for ilke in veri["ilkeler"]:
        satirlar.append(f"{ilke['no']}. **{ilke['ad']}.** {ilke['ilke']} *Bugün: {DURUM_METNI[ilke['durum']]}.*")
    satirlar += ["", "Dokuz soruyla ayrıntı, beşli ile dörtlünün yirmi kesişimi ve ilkelerin bugünkü karşılıkları: "
                     "[Açılış: Kapı ve Köprü](docs/ACILIS.md).", ""]
    return "\n".join(satirlar)


def web_blogu(veri: dict) -> str:
    satirlar = [f"**Niyet** ({veri['niyet']['sahibi']}, {_tarih(veri)}): “{veri['niyet']['soz']}”", "",
                veri["tanim"], ""]
    for ilke in veri["ilkeler"]:
        satirlar.append(f"- **{ilke['no']}. {ilke['ad']}.** {ilke['ilke']} Bugün: {DURUM_METNI[ilke['durum']]}.")
    satirlar += ["", "Bu tanımın dokuz soruyla ayrıntısı ve ilkelerin bugün depoda neye karşılık geldiği "
                     "[açılış belgesindedir](ACILIS.md).", ""]
    return "\n".join(satirlar)


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


def _ayir(metin: str) -> str:
    """Bloğu işaretlerden boş satırla ayırır; Web üreticisi ve Markdown işaretleri ayrı paragraf görür."""
    return "\n" + metin.strip("\n") + "\n\n"


def bloklar(veri: dict) -> dict[Path, dict[str, str]]:
    return {yol: {ad: _ayir(metin) for ad, metin in uretilen.items()} for yol, uretilen in _ham_bloklar(veri).items()}


def _ham_bloklar(veri: dict) -> dict[Path, dict[str, str]]:
    return {
        KOK / "README.md": {"acilis": readme_blogu(veri)},
        KOK / "docs" / "WEB_GIRISI.md": {"acilis": web_blogu(veri)},
        KOK / "docs" / "ACILIS.md": {"acilis_sorular": soru_tablosu(veri), "acilis_varyantlar": varyant_tablosu(veri),
                                     "acilis_matris": matris(veri), "acilis_kesisimler": kesisim_tablosu(veri),
                                     "acilis_ilkeler": ilke_tablosu(veri), "acilis_ilke_metinleri": ilke_metinleri(veri)},
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
    for hata in hatalar:
        print(hata)
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/acilis.py")
        return 1
    durumlar = [ilke["durum"] for ilke in veri["ilkeler"]]
    print(f"TAMAM: niyet, tanım, 9 soru ({len(BESLI)}+{len(DORTLU)}), {len(veri['kesisimler'])} kesişim ve 6 ilke "
          f"({durumlar.count('uygulanıyor')} uygulanıyor, {durumlar.count('kısmen')} kısmen, "
          f"{durumlar.count('henüz yok')} henüz yok); README, Web girişi ve açılış belgesi kayıtla uyumlu.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
