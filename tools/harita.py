#!/usr/bin/env python3
"""Depo haritasını (docs/harita.json) depoya karşı denetler ve docs/harita.md belgesini ondan üretir.

Harita her dosyanın hangi alana ait olduğunu, ne olduğunu, eski adlarını, nasıl üretildiğini,
nasıl çalıştırılıp denetlendiğini ve yeni belgelerin künyesini taşır. Denetim:
  - sözleşmeye uyum;
  - Git'in izlediği her dosyanın tam bir alanın kapsamında olması;
  - tanımlı her dosyanın var olması, kendi alanının kapsamında durması ve tek kez tanımlanması;
  - "her_dosya_tanimli" alanlarda her dosyanın bir tanımı olması;
  - eski adların tekil olması ve hiçbirinin bugün bir dosya olarak durmaması;
  - üretim kaynağının ve aracının, çalıştırma ve denetim komutlarının gösterdiği dosyaların var olması;
  - künyeli dosyalarda kaynakların var olması; künyeli belgelerin ilk paragrafının sade olması
    (kod biçimi ve dosya adı yok, cümle en çok 30, ortalama en çok 18 kelime) ve klavye
    çizimlerinin tools/cizim.py kurallarına uyması;
  - CITATION.cff'nin var olması ve başlığı ile depo adresinin README ile uyuşması;
  - kaldırılan dosyaların gerçekten kalkmış, sıfırlananların yerinde olması ve önceki sürümde bulunması;
  - giriş sayfası istenen her klasörde (klasor_okur) üretilen README.md'nin kayıtla eşliği;
  - docs/harita.md içindeki üretilen bloğun kayıtla eşliği.

Klasör giriş sayfaları: klasor_okur taşıyan her alanın klasörüne bir README.md yazılır. Sayfa alanın sade
paragraflarıyla açılır, klasördeki dosyaları ne yaptıkları ve nasıl çalıştıklarıyla sayar ve haritaya,
açılışa ve teknik ayrıntılara bağlanır. .github/ klasörüne giriş sayfası yazılmaz: GitHub oradaki README'yi
deponun ön yüzü yapar.

Kullanım:
    python tools/harita.py                 # belgeyi kayıttan yaz ve denetle
    python tools/harita.py --check         # yazmadan denetle; uyumsuzlukta çıkış 1
    python tools/harita.py --ref origin/main   # o sürümdeki her dosya bugün var mı, yoksa eski adı haritada mı
    python tools/harita.py --nerede AD     # bir dosya adının (eski ya da yeni) bugünkü yerini yaz
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

KOK = Path(__file__).resolve().parents[1]
KAYIT = KOK / "docs" / "harita.json"
BELGE = KOK / "docs" / "harita.md"
DEPO = "https://github.com/HalukAINRS/ortak-kopru"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KOK / "tools"))

import acilis  # noqa: E402
import cizim  # noqa: E402
import sema_denetle  # noqa: E402

EN_UZUN_CUMLE = 30
ORTALAMA_CUMLE = 18
KOMUT_YOLU = re.compile(r"(?<![\w./-])([\w.-]+(?:/[\w.-]+)*\.(?:py|ps1|cmd|sh|html|json))(?![\w/-])")


def izlenen_dosyalar() -> list[str]:
    cikti = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=KOK)
    return sorted(ad for ad in set(cikti.decode("utf-8").split("\0")) if ad and (KOK / ad).is_file())


def kapsar(desen: str, yol: str) -> bool:
    if desen.endswith("/**"):
        return yol.startswith(desen[:-2])
    return yol == desen


def alan_bul(harita: dict, yol: str) -> list[str]:
    return [alan["kimlik"] for alan in harita["alanlar"] if any(kapsar(d, yol) for d in alan["kapsam"])]


KLASOR_GIRISI_NE = "Bu klasörün giriş sayfası: ne taşıdığını, dosyalarını ve nasıl çalıştırıldıklarını anlatır."


def klasor_girisleri(harita: dict) -> list[tuple[dict, str]]:
    """Giriş sayfası istenen alanlar ve sayfanın yolu."""
    return [(alan, alan["yol"] + "README.md") for alan in harita["alanlar"] if alan.get("klasor_okur")]


def tanimlar(harita: dict) -> list[tuple[dict, dict]]:
    """Kayıttaki dosya tanımları ve üretilen klasör giriş sayfalarının tanımları."""
    sonuc = [(alan, dosya) for alan in harita["alanlar"] for dosya in alan["dosyalar"]]
    for alan, yol in klasor_girisleri(harita):
        sonuc.append((alan, {"yol": yol, "tur": "belge", "ne": KLASOR_GIRISI_NE,
                             "uretilir": {"kaynak": "docs/harita.json", "arac": "tools/harita.py"},
                             "denetim": "python tools/harita.py --check"}))
    return sonuc


def gerekir(dosya: dict) -> str:
    """Çalıştırma komutunun istediği: kayıtta yazılıysa o, değilse komutun türünden."""
    if "gerekir" in dosya:
        return dosya["gerekir"]
    komut = dosya.get("calistir", "")
    if komut.startswith("python"):
        return "Python 3.12+"
    if komut.startswith("pwsh"):
        return "PowerShell 7"
    return "—"


def kaldirilanlar(harita: dict) -> list[dict]:
    return harita.get("kaldirilanlar", [])


def _git_var(nesne: str) -> bool | None:
    """Git nesnesi bu kopyada var mı; Git yoksa None. Sığ kopyada eski sürümler bulunmayabilir."""
    try:
        sonuc = subprocess.run(["git", "cat-file", "-e", nesne], cwd=KOK, capture_output=True)
    except OSError:
        return None
    return sonuc.returncode == 0


def kaldirilan_denetle(harita: dict, mevcut: set[str]) -> list[str]:
    hatalar, gorulen = [], set()
    canli_eski = {ad for _, d in tanimlar(harita) for ad in d.get("eski_adlar", [])}
    for k in kaldirilanlar(harita):
        yol = k["yol"]
        if yol in gorulen:
            hatalar.append(f"{yol}: kaldırılanlarda iki kez")
        gorulen.add(yol)
        if k["islem"] == "silindi" and yol in mevcut:
            hatalar.append(f"{yol}: silindi diye yazılı ama hâlâ bir dosya")
        if k["islem"] == "sıfırlandı" and yol not in mevcut:
            hatalar.append(f"{yol}: sıfırlandı diye yazılı ama depoda yok")
        for ad in k.get("eski_adlar", []):
            if ad in mevcut:
                hatalar.append(f"{ad}: kaldırılan bir dosyanın eski adı ama hâlâ bir dosya")
            if ad in canli_eski:
                hatalar.append(f"{ad}: hem kaldırılan bir dosyanın hem yaşayan bir dosyanın eski adı")
        surum = k["onceki_surum"]
        if _git_var(surum + "^{commit}") and not _git_var(f"{surum}:{yol}"):
            hatalar.append(f"{yol}: önceki sürümde ({surum[:7]}) bu dosya yok")
    return hatalar


def _baglanti_adi(metin: str) -> str:
    """GitHub'ın başlık bağlantısı: küçük harf, harf ve rakam dışı işaretler atılır, boşluk tire olur."""
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", metin.lower()))


def klasor_girisi(harita: dict, alan: dict, dosyalar: list[str] | None = None) -> str:
    """Bir alanın klasörüne yazılan giriş sayfası (README.md)."""
    yol = alan["yol"]
    kok = "../" * yol.count("/")
    parcalar = [f"# {alan['ad']}"] + list(alan["klasor_okur"])
    tanimli = [d for a, d in tanimlar(harita) if a is alan and d["yol"] != yol + "README.md"]
    parcalar.append("## Bu klasörde")
    if alan["her_dosya_tanimli"] and tanimli:
        satirlar = ["| Dosya | Ne | Nasıl çalışır |", "| --- | --- | --- |"]
        for d in tanimli:
            ic = d["yol"].startswith(yol)
            ad = d["yol"][len(yol):] if ic else d["yol"]
            hedef = ad if ic else kok + d["yol"]
            if "calistir" in d:
                nasil = f"`{d['calistir']}`"
            elif "uretilir" in d:
                nasil = f"`{d['uretilir']['arac']}` üretir"
            else:
                nasil = "—"
            satirlar.append(f"| [`{ad}`]({hedef}) | {_hucre(d['ne'])} | {nasil} |")
        parcalar.append("\n".join(satirlar))
    else:
        dosyalar = izlenen_dosyalar() if dosyalar is None else dosyalar
        klasorler, turler = set(), set()
        for d in dosyalar:
            if alan_bul(harita, d) == [alan["kimlik"]] and d.startswith(yol) and d != yol + "README.md":
                ic = d[len(yol):]
                if "/" in ic:
                    klasorler.add(ic.split("/", 1)[0] + "/")
                else:
                    turler.add("." + ic.rsplit(".", 1)[-1] if "." in ic else ic)
        icerik = [f"[`{k}`]({k})" for k in sorted(klasorler)]
        if turler:
            icerik.append("kökte " + ", ".join(f"`{t}`" for t in sorted(turler)) + " dosyaları")
        parcalar.append("Bu alandaki dosyalar tek tek tanımlanmaz; yukarıdaki açıklama hepsi için geçerlidir. "
                        "Klasörün içinde: " + ", ".join(icerik) + ".")
    parcalar.append(f"Bu sayfa [depo haritasından]({kok}docs/harita.md#{_baglanti_adi(alan['ad'])}) üretilir; değiştirmek için "
                    "haritadaki kayıt düzeltilir ve `python tools/harita.py` çalıştırılır.")
    return "\n\n".join(parcalar) + "\n"


def klasor_denetle(harita: dict, yaz: bool = False) -> list[str]:
    """Klasör giriş sayfaları kayıtla aynı mı; yaz verilirse farklı olanlar yazılır."""
    hatalar = []
    dosyalar = izlenen_dosyalar()
    for alan, yol in klasor_girisleri(harita):
        if yol.startswith(".github/"):
            hatalar.append(f"{yol}: .github/ klasörüne giriş sayfası yazılmaz (GitHub onu deponun ön yüzü yapar)")
            continue
        beklenen = klasor_girisi(harita, alan, dosyalar)
        hedef = KOK / yol
        metin = hedef.read_text(encoding="utf-8") if hedef.is_file() else None
        if metin != beklenen:
            if yaz:
                hedef.write_text(beklenen, encoding="utf-8", newline="\n")
            else:
                hatalar.append(f"{yol}: depo haritasından üretilen hâliyle aynı değil")
        hatalar += sade_paragraf(yol, alan["klasor_okur"][0])
    return hatalar


def ilk_paragraf(metin: str) -> str:
    metin = re.sub(r"<!--.*?-->", "", metin, flags=re.S)
    for blok in re.split(r"\n\s*\n", metin):
        blok = blok.strip()
        if blok and not blok.startswith("#"):
            return blok
    return ""


def sade_paragraf(ad: str, paragraf: str) -> list[str]:
    """Künyeli bir belgenin ilk paragrafı, hiç bilmeyen okuyucunun ilk temasıdır."""
    if not paragraf:
        return [f"{ad}: ilk paragraf yok"]
    if paragraf.startswith(("|", "- ", "* ", ">", "```", "<")) or re.match(r"\d+[.)] ", paragraf):
        return [f"{ad}: belge bir paragrafla açılmalı (tablo, liste, alıntı ya da kod değil)"]
    hatalar = []
    if "`" in paragraf:
        hatalar.append(f"{ad}: ilk paragrafta kod biçimi var")
    gorunen = acilis._gorunen(paragraf)
    for bulunan in sorted(set(re.findall(r"\b[\w./-]+\.(?:py|json|md|html|ps1|cmd|ya?ml|sh|cff)\b", gorunen))):
        hatalar.append(f"{ad}: ilk paragrafta dosya adı var: {bulunan}")
    cumleler = [c for c in re.split(r"(?<=[.!?])\s+", " ".join(gorunen.split())) if c.strip()]
    uzunluklar = [len(c.split()) for c in cumleler]
    for cumle, uzunluk in zip(cumleler, uzunluklar):
        if uzunluk > EN_UZUN_CUMLE:
            hatalar.append(f"{ad}: ilk paragrafta {uzunluk} kelimelik cümle (en çok {EN_UZUN_CUMLE}): {cumle[:50]}…")
    if uzunluklar and sum(uzunluklar) / len(uzunluklar) > ORTALAMA_CUMLE:
        hatalar.append(f"{ad}: ilk paragrafta ortalama cümle {sum(uzunluklar) / len(uzunluklar):.1f} kelime (en çok {ORTALAMA_CUMLE})")
    return hatalar


def atif_denetle(harita: dict) -> list[str]:
    yol = KOK / "CITATION.cff"
    if not yol.is_file():
        return ["CITATION.cff: yok; depo kaynak gösterilemez"]
    metin = yol.read_text(encoding="utf-8")
    hatalar = []
    for alan in ("cff-version", "message", "title", "authors", "repository-code", "abstract"):
        if not re.search(rf"(?m)^{re.escape(alan)}:", metin):
            hatalar.append(f"CITATION.cff: '{alan}' alanı yok")
    if f'repository-code: "{DEPO}"' not in metin:
        hatalar.append(f"CITATION.cff: depo adresi {DEPO} değil")
    baslik = re.search(r'(?m)^title: "([^"]+)"', metin)
    readme = (KOK / "README.md").read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
    if not baslik or baslik.group(1) != readme:
        hatalar.append(f"CITATION.cff: başlık README başlığıyla ({readme}) aynı değil")
    return hatalar


def denetle(harita: dict, dosyalar: list[str] | None = None) -> list[str]:
    hatalar = [f"sözleşme: {hata}" for hata in sema_denetle.dogrula(sema_denetle.sema_yukle("harita"), harita)]
    if hatalar:
        return hatalar
    dosyalar = izlenen_dosyalar() if dosyalar is None else dosyalar
    mevcut = set(dosyalar)
    kimlikler = [alan["kimlik"] for alan in harita["alanlar"]]
    for kimlik in sorted({k for k in kimlikler if kimlikler.count(k) > 1}):
        hatalar.append(f"alanlar: '{kimlik}' kimliği birden çok kez")
    for yol in dosyalar:
        bulunan = alan_bul(harita, yol)
        if not bulunan:
            hatalar.append(f"{yol}: hiçbir alanda değil")
        elif len(bulunan) > 1:
            hatalar.append(f"{yol}: birden çok alanda ({', '.join(bulunan)})")
    tanimli: dict[str, str] = {}
    eski: dict[str, str] = {}
    for alan, dosya in tanimlar(harita):
        yol = dosya["yol"]
        if yol in tanimli:
            hatalar.append(f"{yol}: iki kez tanımlı")
        tanimli[yol] = alan["kimlik"]
        if yol not in mevcut:
            hatalar.append(f"{yol}: tanımlı ama depoda yok")
        if not any(kapsar(d, yol) for d in alan["kapsam"]):
            hatalar.append(f"{yol}: '{alan['kimlik']}' alanının kapsamında değil")
        for ad in dosya.get("eski_adlar", []):
            if ad in eski:
                hatalar.append(f"{ad}: eski ad iki dosyada ({eski[ad]}, {yol})")
            eski[ad] = yol
            if ad in mevcut:
                hatalar.append(f"{ad}: eski ad olarak geçiyor ama hâlâ bir dosya")
        gosterilen = list(dosya.get("uretilir", {}).values())
        for alanadi in ("calistir", "denetim"):
            gosterilen += KOMUT_YOLU.findall(dosya.get(alanadi, ""))
        for kunye_kaynagi in dosya.get("kunye", {}).get("kaynaklar", []):
            gosterilen.append(kunye_kaynagi)
        for hedef in gosterilen:
            if not (KOK / hedef).exists():
                hatalar.append(f"{yol}: gösterdiği dosya yok ({hedef})")
        if "kunye" in dosya and dosya["tur"] == "belge" and (KOK / yol).is_file():
            metin = (KOK / yol).read_text(encoding="utf-8")
            hatalar += sade_paragraf(yol, ilk_paragraf(metin)) + cizim.denetle(yol, metin)
    for alan in harita["alanlar"]:
        if alan["her_dosya_tanimli"]:
            for yol in dosyalar:
                if alan_bul(harita, yol) == [alan["kimlik"]] and yol not in tanimli:
                    hatalar.append(f"{yol}: '{alan['kimlik']}' alanında ama tanımı yok")
    hatalar += atif_denetle(harita)
    hatalar += kaldirilan_denetle(harita, mevcut)
    return hatalar


def eski_ad_denetle(harita: dict, ref: str) -> list[str]:
    """O sürümdeki her dosya bugün aynı yerde mi, değilse eski adı haritada mı?"""
    cikti = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", "-z", ref], cwd=KOK)
    eski = {ad for _, dosya in tanimlar(harita) for ad in dosya.get("eski_adlar", [])}
    eski |= {ad for k in kaldirilanlar(harita) for ad in [k["yol"], *k.get("eski_adlar", [])]}
    bugun = set(izlenen_dosyalar())   # Git'in listesi: büyük/küçük harfe duyarsız dosya sistemlerinde de doğru
    return [f"{ref}:{ad}: bugün yok ve eski adı haritada değil"
            for ad in sorted(set(cikti.decode("utf-8").split("\0")) - {""})
            if ad not in bugun and ad not in eski]


def nerede(harita: dict, ad: str) -> list[str]:
    sonuc = []
    for alan, dosya in tanimlar(harita):
        adlar = [dosya["yol"]] + dosya.get("eski_adlar", [])
        if any(a == ad or a.rsplit("/", 1)[-1] == ad for a in adlar):
            sonuc.append(f"{dosya['yol']}  ({alan['ad']}) — {dosya['ne']}")
    for k in kaldirilanlar(harita):
        adlar = [k["yol"]] + k.get("eski_adlar", [])
        if any(a == ad or a.rsplit("/", 1)[-1] == ad for a in adlar):
            sonuc.append(f"{k['yol']}  ({k['islem']}, {k['tarih']}) — {k['neden']} "
                         f"Önceki hâli: {DEPO}/blob/{k['onceki_surum']}/{k['yol']}")
    return sonuc


def _kok_agaci(harita: dict) -> str:
    """Kökten görünen ağaç: kökteki her dosya ve klasör kendi satırında, alanın adı grubunun ilk satırında;
    iç içe alanlar (docs/teknik/ gibi) üst klasörlerinin altında."""
    gruplar, alt = [], {}
    for alan in harita["alanlar"]:
        parcalar = [d[:-2] if d.endswith("/**") else d for d in alan["kapsam"]]
        if len(parcalar) == 1 and parcalar[0].count("/") >= 2:
            ust = parcalar[0].split("/", 1)[0] + "/"
            alt.setdefault(ust, []).append((parcalar[0][len(ust):], alan["ad"]))
            continue
        ogeler = []
        for oge in parcalar:
            ilk = oge.split("/", 1)[0] + ("/" if "/" in oge else "")
            if ilk not in ogeler:
                ogeler.append(ilk)
        gruplar.append((alan["ad"], ogeler))
    genislik = max(len(o) for _, ogeler in gruplar for o in ogeler) + 2
    satirlar = ["ortak-kopru/"]
    duz = [(o, ad if i == 0 else "") for ad, ogeler in gruplar for i, o in enumerate(ogeler)]
    for i, (oge, ad) in enumerate(duz):
        son = i == len(duz) - 1
        satirlar.append(f"{'└──' if son else '├──'} {oge.ljust(genislik)}{ad}".rstrip())
        cocuklar = alt.get(oge, [])
        for j, (cocuk, cad) in enumerate(cocuklar):
            satirlar.append(f"{'    ' if son else '│   '}{'└──' if j == len(cocuklar) - 1 else '├──'} "
                            f"{cocuk.ljust(genislik - 4)}{cad}".rstrip())
    return "```text\n" + "\n".join(satirlar) + "\n```"


def _hucre(metin: str) -> str:
    return metin.replace("|", "\\|").replace("\n", " ")


def belge(harita: dict) -> str:
    parcalar = list(harita["giris"])
    parcalar += ["Depo kökünden bakınca alanlar şöyle görünür. Sol sütun klasör ya da dosya, sağ sütun alanın adıdır.",
                 _kok_agaci(harita), "## Kurallar"] + list(harita["kurallar"])
    for alan in harita["alanlar"]:
        yer = "depo kökü"
        if alan["yol"]:
            yer = f"`{alan['yol']}`"
            if (KOK / alan["yol"] / "README.md").is_file():
                hedef = alan["yol"][len("docs/"):] if alan["yol"].startswith("docs/") else "../" + alan["yol"]
                yer = f"[`{alan['yol']}`]({hedef}README.md)"
        parcalar += [f"## {alan['ad']}", f"{alan['ne']} Yeri: {yer}."]
        alan_dosyalari = [d for a, d in tanimlar(harita) if a is alan]
        if alan_dosyalari:
            satirlar = ["| Dosya | Tür | Ne | Eski adı |", "| --- | --- | --- | --- |"]
            for dosya in alan_dosyalari:
                eski = ", ".join(f"`{a}`" for a in dosya.get("eski_adlar", [])) or "—"
                satirlar.append(f"| `{dosya['yol']}` | {dosya['tur']} | {_hucre(dosya['ne'])} | {eski} |")
            parcalar.append("\n".join(satirlar))
        else:
            parcalar.append("Bu alandaki dosyalar tek tek tanımlanmaz; alanın açıklaması hepsi için geçerlidir.")
    calisan = [(d["yol"], d["calistir"], d.get("yan_etkisiz", False), gerekir(d)) for _, d in tanimlar(harita) if "calistir" in d]
    parcalar += ["## Çalıştırma",
                 "Aşağıdaki komutlar depo kökünden çalışır. Python komutları Python 3.12 ya da üstünü ve yalnız standart "
                 "kütüphaneyi ister; öteki komutların ne istediği “Gerekir” sütunundadır. Yalnız okuyan komutlar her "
                 "doğrulamada sınanır."]
    satirlar = ["| Dosya | Komut | Yalnız okur | Gerekir |", "| --- | --- | --- | --- |"]
    satirlar += [f"| `{y}` | `{c}` | {'evet' if g else 'hayır'} | {_hucre(r)} |" for y, c, g, r in calisan]
    parcalar.append("\n".join(satirlar))
    if kaldirilanlar(harita):
        parcalar += ["## Kaldırılan ve sıfırlanan dosyalar",
                     "Bazı dosyalar depodan bilerek kaldırıldı ya da içerikleri baştan yazıldı. Eski bir kayıtta "
                     "bunlardan birinin adı geçerse ne olduğu ve önceki hâlinin hangi sürümde durduğu burada yazılıdır."]
        satirlar = ["| Dosya | İşlem | Tarih | Neden | Önceki hâli |", "| --- | --- | --- | --- | --- |"]
        satirlar += [f"| `{k['yol']}` | {k['islem']} | {k['tarih']} | {_hucre(k['neden'])} | "
                     f"[{k['onceki_surum'][:7]}]({DEPO}/blob/{k['onceki_surum']}/{k['yol']}) |" for k in kaldirilanlar(harita)]
        parcalar.append("\n".join(satirlar))
    eski = sorted((ad, d["yol"]) for _, d in tanimlar(harita) for ad in d.get("eski_adlar", []))
    eski = sorted(eski + [(ad, f"{k['yol']} ({k['islem']})") for k in kaldirilanlar(harita)
                          for ad in k.get("eski_adlar", []) if k["islem"] == "silindi"])
    parcalar += ["## Eski adlar",
                 "Eski kayıtlarda ve konuşmalarda geçen bir dosya adını burada bulabilirsiniz. Komutla da sorulabilir: "
                 "`python tools/harita.py --nerede kopru_ekle.py`."]
    satirlar = ["| Eski yol | Bugünkü yol |", "| --- | --- |"] + [f"| `{a}` | `{y}` |" for a, y in eski]
    parcalar.append("\n".join(satirlar))
    kunyeli = [(d["yol"], d["kunye"]) for _, d in tanimlar(harita) if "kunye" in d]
    parcalar += ["## Künyeler",
                 "Yeni belgeler ve kayıtlar künyeleriyle kaynak gösterilebilir. Deponun tamamı için künye kökteki "
                 "kaynak gösterme dosyasındadır."]
    satirlar = ["| Dosya | Sahibi | Hazırlayan | Tarih | Kaynakları | Kimin için |", "| --- | --- | --- | --- | --- | --- |"]
    satirlar += [f"| `{y}` | {k['sahibi']} | {k['hazirlayan']} | {k['tarih']} | "
                 + ", ".join(f"`{s}`" for s in k["kaynaklar"]) + f" | {k['okur']} |" for y, k in kunyeli]
    parcalar.append("\n".join(satirlar))
    return "\n\n".join(parcalar) + "\n"


def main() -> int:
    for akis in (sys.stdout, sys.stderr):
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="yazmadan denetle")
    parser.add_argument("--ref", help="o Git sürümündeki her dosyanın bugünkü karşılığını denetle")
    parser.add_argument("--nerede", metavar="AD", help="bir dosya adının bugünkü yerini yaz")
    args = parser.parse_args()
    harita = json.loads(KAYIT.read_text(encoding="utf-8"))
    if args.nerede:
        sonuc = nerede(harita, args.nerede)
        print("\n".join(sonuc) if sonuc else f"{args.nerede}: haritada yok")
        return 0 if sonuc else 1
    hatalar = [f"sözleşme: {hata}" for hata in sema_denetle.dogrula(sema_denetle.sema_yukle("harita"), harita)]
    if not hatalar:
        # Önce belge yazılır (--check değilse); sonra belge dahil her şey denetlenir.
        uretilen = {"harita": acilis._ayir(belge(harita))}
        metin = BELGE.read_text(encoding="utf-8") if BELGE.is_file() else ""
        if not args.check and metin:
            yeni = acilis.belge_guncelle(metin, uretilen)
            if yeni != metin:
                BELGE.write_text(yeni, encoding="utf-8", newline="\n")
                metin = yeni
        hatalar = klasor_denetle(harita, yaz=not args.check)
        hatalar += denetle(harita) + acilis.belge_denetle("docs/harita.md", metin, uretilen)
    if args.ref:
        hatalar += eski_ad_denetle(harita, args.ref)
    for hata in hatalar:
        print(hata)
    if hatalar:
        if args.check:
            print("Yenilemek için: python tools/harita.py")
        return 1
    tanimli = len(tanimlar(harita))
    eski = sum(len(d.get("eski_adlar", [])) for _, d in tanimlar(harita))
    print(f"TAMAM: {len(izlenen_dosyalar())} dosya {len(harita['alanlar'])} alanda, {tanimli} tanım, {eski} eski ad; "
          "künyeler, komutlar ve harita belgesi tutarlı.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
