#!/usr/bin/env python3
"""Ortak Köprü botu: katılımcılara düşen açık kayıtları bulur, üretici API'si ile tek bir yanıt kaydı üretir,
kopru_ekle.py ile ekler ve her çağrının tam bağlamını kayit/ klasörüne yazar. Yalnız standart kütüphane.

Modlar:
  python3 defter/kopru_yanitla.py kopru.html                         # katilimcilar/ayarlar.json'daki her katılımcı için bekleyenleri yanıtla
  python3 defter/kopru_yanitla.py kopru.html --kuru                  # API çağırmadan istemleri kur ve kayit/ altına yaz
  python3 defter/kopru_yanitla.py kopru.html --bekleyenler Gemini    # Gemini'ye düşen açık kayıtları JSON listele
  python3 defter/kopru_yanitla.py kopru.html --istem Gemini          # Gemini için istem metnini yaz (CLI katmanları kullanır)
  python3 defter/kopru_yanitla.py kopru.html --ayarlar katilimcilar/ayarlar-yerel.json --yalniz Claude   # yalnız bir katılımcıyı çalıştır

Katılımcı ayarları: "saglayici" api adı (anthropic, openai, google) ya da "cli"; cli için "komut" listesi, "istem_nasil"
(dosya | stdin | arg), isteğe bağlı "ortam" (yalnız o komuta verilecek ortam değişkenleri; null değer o değişkeni kaldırır) ve "zaman_asimi" (saniye).
Komut bu makinede yoksa katılımcı sessizce atlanır; atlanan her çalıştırma kayit/atlandi.log'a tek satır düşer.

Bekleyen kaydın tanımı: durumu açık, "kime" alanında katılımcının adı geçen, katılımcının kendi yazmadığı ve
katılımcının daha sonra yazdığı bir kaydın "yanıt" alanının kapsamadığı kayıt. Bir yanıt kaydı, yanıt alanındaki
numaraya kadar aynı hedef kapsamındaki bekleyenleri kapsar. Açık katman adresi
yalnız aynı katmanın yanıtıyla kapsanır; API yedeği CLI imzasını miras alamaz.

Anahtarlar yalnız ortam değişkeninden okunur ve hiçbir yere yazılmaz.
"""
import argparse, datetime, html, json, os, re, shutil, subprocess, sys, tempfile, urllib.error, urllib.request

BURASI = os.path.dirname(os.path.abspath(__file__))          # defter/: kayıt araçları
KOK = os.path.dirname(BURASI)                                 # depo kökü: kopru.html, kayit/, CLI çalışma yeri
KATILIMCILAR = os.path.join(KOK, "katilimcilar")              # ayarlar ve istem şablonu
sys.path.insert(0, BURASI)
from kopru_oku import Ayristirici  # noqa: E402


# ---------- sayfa okuma ----------

def kayitlari_oku(yol):
    ay = Ayristirici()
    with open(yol, encoding="utf-8") as dosya:
        ay.feed(dosya.read())
    ay.close()
    return ay.kayitlar


def ad_kok(s):
    """'ChatGPT (Şaman)' → 'ChatGPT'."""
    return (s or "").split("(")[0].strip()


def kime_adlari(s):
    return [hedef_kimligi(x) for x in (s or "").split(",") if x.strip()]


def hedef_kimligi(s):
    """Üretici ve açık katman ayrı; yalın eski adresler üretici adresidir."""
    s = (s or "").strip().casefold()
    roller = {"saman": "şaman", "şaman": "şaman", "sahit": "şahit", "şahit": "şahit",
              "hacker": "hacker", "cli": "cli", "api": "api"}
    takma = {"şaman": ("chatgpt", "şaman"), "saman": ("chatgpt", "şaman"),
             "şahit": ("copilot", "şahit"), "sahit": ("copilot", "şahit"),
             "hacker": ("claude", "hacker")}
    if s in takma:
        return takma[s]
    m = re.fullmatch(r"([^()]+?)(?:\s*\(([^()]+)\))?", s)
    if not m:
        return (s, "")
    return (m[1].strip(), roller.get((m[2] or "").strip(), (m[2] or "").strip()))


def yol_kimligi(ad, kat, yol):
    """API yedeği üst CLI'ın imzasını miras alamaz."""
    cli = yol["saglayici"] == "cli"
    imza = yol.get("imza")
    if not imza and cli and kat["saglayici"] == "cli":
        imza = kat.get("imza")
    imza = imza or f"{ad} ({'CLI' if cli else 'API'})"
    kok, rol = hedef_kimligi(imza)
    if kok != hedef_kimligi(ad)[0] or (not cli and rol in {"şaman", "şahit", "hacker", "cli", "cli izleyici"}) or (cli and rol == "api"):
        raise ValueError("Yolun sağlayıcısı ile katman imzası uyuşmuyor.")
    return imza


def numara(kid):
    m = re.fullmatch(r"k-(\d{4})", kid or "")
    return int(m.group(1)) if m else -1


def bekleyenler(kayitlar, ad):
    hedef = hedef_kimligi(ad)
    genel = (hedef[0], "")
    kapsanan = {}
    for y in kayitlar:
        if not y.get("yanit"):
            continue
        kimden = hedef_kimligi(y["kimden"])
        for kapsam in {kimden, (kimden[0], "")}:
            kapsanan[kapsam] = max(kapsanan.get(kapsam, -1), numara(y["yanit"]))
    out = []
    for k in kayitlar:
        if k["durum"] != "acik":
            continue
        adresler = kime_adlari(k["kime"])
        kapsam = hedef if hedef in adresler else genel if genel in adresler else None
        if kapsam is None:
            continue
        kimden = hedef_kimligi(k["kimden"])
        if kimden == kapsam or (not kapsam[1] and kimden[0] == kapsam[0]):
            continue
        # Eski yalın üretici adreslerinin kapsama davranışı korunur.
        # Açık katman adresini yalnız aynı katmanın yanıtı kapsar.
        kapsanan_ust = kapsanan.get(kapsam, -1)
        if numara(k["id"]) <= kapsanan_ust:
            continue
        out.append(k)
    return out


def bolum_metni(belge, bolum_id):
    m = re.search(r'<section id="%s"[^>]*>(.*?)</section>' % re.escape(bolum_id), belge, re.S)
    if not m:
        return ""
    t = re.sub(r"<style.*?</style>", "", m.group(1), flags=re.S)
    t = re.sub(r"</(p|li|h[1-6]|tr|div|details|summary)>", "\n", t)
    t = re.sub(r"</t[dh]>", " | ", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)   # &#x27; ve diğer bütün HTML varlıkları istemde düz metin olur
    t = "\n".join(l.strip() for l in t.splitlines())
    return re.sub(r"\n{3,}", "\n\n", t).strip()


# ---------- istem ----------

def sablon_oku():
    s = open(os.path.join(KATILIMCILAR, "istem-sablonu.md"), encoding="utf-8").read()
    sistem = re.search(r"## Sistem\n(.*?)\n## Kullanıcı\n", s, re.S).group(1).strip()
    kullanici = s.split("## Kullanıcı\n", 1)[1].strip()
    return sistem, kullanici


def istem_kur(yol, ad, bek):
    belge = open(yol, encoding="utf-8").read()
    kayitlar = kayitlari_oku(yol)
    sistem, kullanici = sablon_oku()
    degerler = {
        "ad": ad,
        "bekleyen_idler": ", ".join(k["id"] for k in bek),
        "hedef_id": bek[-1]["id"],
        "kurallar_metni": bolum_metni(belge, "kurallar"),
        "dosya_metni": bolum_metni(belge, "yonlendirme"),
        "kayitlar_json": json.dumps(kayitlar, ensure_ascii=False, indent=1),
        "bekleyen_json": json.dumps(bek, ensure_ascii=False, indent=1),
    }
    for k, v in degerler.items():
        sistem = sistem.replace("{" + k + "}", v)
        kullanici = kullanici.replace("{" + k + "}", v)
    return sistem, kullanici


# ---------- üretici çağrıları ----------

def http_json(url, veri, basliklar, zaman_asimi=180):
    istek = urllib.request.Request(url, data=json.dumps(veri).encode("utf-8"), headers={"Content-Type": "application/json", **basliklar}, method="POST")
    try:
        with urllib.request.urlopen(istek, timeout=zaman_asimi) as y:
            return json.loads(y.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        govde = e.read().decode("utf-8", errors="replace")[:2000]
        raise RuntimeError(f"HTTP {e.code}: {govde}") from None


class KomutYok(Exception):
    """CLI komutu bu makinede yok (kurulmamış ya da yol yanlış). Sessiz atlanır, kayıt dosyası yazılmaz."""


def komut_var_mi(komut):
    """Komutun ilk ögesi tam yolsa dosya var mı, değilse PATH'te bulunuyor mu bakar."""
    exe = komut[0]
    if os.sep in exe or (os.altsep and os.altsep in exe) or (len(exe) > 1 and exe[1] == ":"):
        return os.path.isfile(exe)
    return shutil.which(exe) is not None


def cli_cagir(komut, sistem, kullanici, istem_nasil="dosya", ad="bot", zaman_asimi=1800, ortam=None):
    """Abonelikle çalışan bir CLI'ı (claude -p, codex exec, gemini -p) etkileşimsiz çalıştırır; standart çıktı yanıttır.
    istem_nasil: "dosya" → istem istem-<ad>.txt dosyasına yazılır, komuttaki {dosya} yer tutucusu adıyla değiştirilir
                 (Windows komut satırı sınırını aşmaz; CLI dosyayı kendi okur);
                 "stdin" → istem standart girdiden verilir (ssh üzerinden uzak makinedeki CLI için de);
                 "arg"   → istem son argüman olur (yalnız kısa istemler, Linux/macOS).
    ortam: yalnız bu komut için eklenecek ortam değişkenleri (ör. CLI'ın kendi HOME'u); süreç ortamının üstüne yazılır.
    Çıktı her zaman UTF-8 okunur (Windows'ta konsol kod sayfasına bağlı kalmaz)."""
    istem = sistem + "\n\n---\n\n" + kullanici
    komut = list(komut)
    if not komut_var_mi(komut):
        raise KomutYok(komut[0])
    cevre = dict(os.environ)
    for k, v in (ortam or {}).items():   # null → değişken kaldırılır (ör. OPENAI_API_KEY: Codex API yoluna sapmasın)
        if v is None:
            cevre.pop(k, None)
        else:
            cevre[k] = str(v)
    secenek = dict(capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=zaman_asimi, cwd=KOK, env=cevre)
    if istem_nasil == "dosya":
        dosya = f"istem-{re.sub(r'[^A-Za-z0-9]+', '-', ad).strip('-')}.txt"
        open(os.path.join(KOK, dosya), "w", encoding="utf-8").write(istem)
        komut = [c.replace("{dosya}", dosya) for c in komut]
        sonuc = subprocess.run(komut, **secenek)
    elif istem_nasil == "stdin":
        sonuc = subprocess.run(komut, input=istem, **secenek)
    else:
        sonuc = subprocess.run(komut + [istem], **secenek)
    if sonuc.returncode != 0:
        raise RuntimeError(f"CLI çıkış kodu {sonuc.returncode}: {(sonuc.stderr or sonuc.stdout)[-1500:]}")
    return sonuc.stdout, {"cli": " ".join(komut), "stderr_son": (sonuc.stderr or "")[-300:]}


def cagir(saglayici, model, anahtar, sistem, kullanici, en_cok_token, caba=None):
    """Üretici API'sini çağırır. Derin düşünme ayarı (caba) 400 verirse bir alt düzeyle, sonra ayarsız yeniden dener."""
    denemeler = [caba, "high", None] if caba and caba != "high" else ([caba, None] if caba else [None])
    son_hata = None
    for c in denemeler:
        try:
            if saglayici == "anthropic":
                govde = {"model": model, "max_tokens": en_cok_token, "system": sistem, "messages": [{"role": "user", "content": kullanici}]}
                y = http_json("https://api.anthropic.com/v1/messages", govde, {"x-api-key": anahtar, "anthropic-version": "2023-06-01"})
                return "".join(p.get("text", "") for p in y.get("content", []) if p.get("type") == "text"), y.get("usage")
            if saglayici == "openai":
                govde = {"model": model, "instructions": sistem, "input": kullanici, "max_output_tokens": en_cok_token}
                if c:
                    govde["reasoning"] = {"effort": c}
                y = http_json("https://api.openai.com/v1/responses", govde, {"Authorization": f"Bearer {anahtar}"})
                metin = []
                for oge in y.get("output", []):
                    if oge.get("type") == "message":
                        for par in oge.get("content", []):
                            if par.get("type") == "output_text":
                                metin.append(par.get("text", ""))
                return "".join(metin), y.get("usage")
            if saglayici == "google":
                uretim = {"maxOutputTokens": en_cok_token}
                if c:
                    uretim["thinkingConfig"] = {"thinkingLevel": c}
                govde = {"system_instruction": {"parts": [{"text": sistem}]}, "contents": [{"role": "user", "parts": [{"text": kullanici}]}], "generationConfig": uretim}
                y = http_json(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent", govde, {"x-goog-api-key": anahtar})
                parcalar = y["candidates"][0]["content"]["parts"]
                return "".join(p.get("text", "") for p in parcalar if not p.get("thought")), y.get("usageMetadata")
            raise ValueError(f"bilinmeyen sağlayıcı: {saglayici}")
        except RuntimeError as e:
            son_hata = e
            if c is None or not str(e).startswith("HTTP 400"):
                raise
            print(f"  {saglayici}: düşünme ayarı '{c}' kabul edilmedi, bir alt düzey deneniyor")
    raise son_hata


# ---------- yanıt işleme ----------

def json_ayikla(metin):
    i, j = metin.find("{"), metin.rfind("}")
    if i < 0 or j < 0:
        raise ValueError("yanıtta JSON nesnesi yok")
    return json.loads(metin[i:j + 1])


def kayit_yaz(ad, model, saglayici, sistem, kullanici, ham, sonuc):
    os.makedirs(os.path.join(KOK, "kayit"), exist_ok=True)
    zaman = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d-%H%M%SZ")
    guvenli_ad = re.sub(r"[^A-Za-z0-9]+", "-", ad).strip("-")
    # Aynı saniyedeki iki çağrı eski makbuzu ezemez; eşzamanlı süreçlerde de
    # dosya oluşturma atomik olsun (var olan ada 'w' ile yazma).
    sira = 0
    while True:
        ek = f"-{sira:03d}" if sira else ""
        yol = os.path.join(KOK, "kayit", f"{zaman}-{guvenli_ad}{ek}.md")
        try:
            fh = open(yol, "x", encoding="utf-8")
            break
        except FileExistsError:
            sira += 1
    with fh:
        fh.write(f"# {ad} · {saglayici} · {model} · {zaman}\n\n## Sonuç\n\n{sonuc}\n\n## Sistem istemi\n\n```\n{sistem}\n```\n\n## Kullanıcı iletisi\n\n```\n{kullanici}\n```\n\n## Ham yanıt\n\n```\n{ham}\n```\n")
    return yol


def atlandi_yaz(ad, hatalar):
    """Yol bulunamayınca her çalıştırmada koca bir kayıt dosyası yerine kayit/atlandi.log'a tek satır düşer."""
    os.makedirs(os.path.join(KOK, "kayit"), exist_ok=True)
    zaman = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%SZ")
    with open(os.path.join(KOK, "kayit", "atlandi.log"), "a", encoding="utf-8") as fh:
        fh.write(f"{zaman} {ad}: {' | '.join(hatalar)}\n")


def ekle(yol, veri):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8", dir=KOK) as fh:
        json.dump(veri, fh, ensure_ascii=False)
        gecici = fh.name
    try:
        sonuc = subprocess.run([sys.executable, "-I", "-X", "utf8", os.path.join(BURASI, "kopru_ekle.py"), yol, "--json", gecici],
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
    finally:
        os.unlink(gecici)
    if sonuc.returncode != 0:
        raise RuntimeError((sonuc.stdout + sonuc.stderr).strip())
    return sonuc.stdout.strip().splitlines()[-1]


def main():
    for akis in (sys.stdout, sys.stderr):  # Windows konsolunda Türkçe karakterler için
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser()
    p.add_argument("dosya")
    p.add_argument("--ayarlar", default=os.path.join(KATILIMCILAR, "ayarlar.json"))
    p.add_argument("--kuru", action="store_true", help="API çağırma; istemleri kur ve kayit/ altına yaz")
    p.add_argument("--bekleyenler", metavar="AD", help="yalnız listele")
    p.add_argument("--istem", metavar="AD", help="istem metnini yaz ve çık")
    p.add_argument("--yalniz", metavar="AD", help="ayarlardaki katılımcılardan yalnız bunu çalıştır")
    a = p.parse_args()

    kayitlar = kayitlari_oku(a.dosya)
    if a.bekleyenler:
        print(json.dumps(bekleyenler(kayitlar, a.bekleyenler), ensure_ascii=False, indent=1))
        return
    if a.istem:
        bek = bekleyenler(kayitlar, a.istem)
        if not bek:
            print("", end="")
            return
        sistem, kullanici = istem_kur(a.dosya, a.istem, bek)
        print(sistem + "\n\n---\n\n" + kullanici)
        return

    with open(a.ayarlar, encoding="utf-8") as dosya_ayar:
        ayar = json.load(dosya_ayar)
    en_cok = int(ayar.get("en_cok_cikti_token", 1500))
    eklenenler = []
    hata_sayisi = 0
    if a.yalniz and a.yalniz not in {kat["ad"] for kat in ayar["katilimcilar"]}:
        adlar = ", ".join(kat["ad"] for kat in ayar["katilimcilar"])
        sys.exit(f"HATA: --yalniz {a.yalniz!r} bu ayar dosyasında yok; geçerli adlar: {adlar}")
    for kat in ayar["katilimcilar"]:
        ad = kat["ad"]
        if a.yalniz and ad != a.yalniz:
            continue
        # Yollar: asıl yol, sonra varsa "yedek". Her yol için gereken ortam değişkeni (anahtar ya da abonelik belirteci) yoksa o yol atlanır.
        yollar = [kat] + ([kat["yedek"]] if kat.get("yedek") else [])
        ham, kullanim, kullanilan, hatalar = "", None, None, []
        bek_goruldu, kuru_yazildi = False, False
        yol_hatasi = False
        for yol_ayar in yollar:
            try:
                hedef = yol_kimligi(ad, kat, yol_ayar)
            except ValueError as e:
                hatalar.append(str(e))
                yol_hatasi = True
                continue
            bek = bekleyenler(kayitlar, hedef)
            if not bek:
                continue
            bek_goruldu = True
            sistem, kullanici = istem_kur(a.dosya, hedef, bek)
            if a.kuru:
                yol = kayit_yaz(ad, yol_ayar.get("model", "-"), yol_ayar["saglayici"], sistem, kullanici, "(kuru çalıştırma, çağrı yapılmadı)", "kuru")
                print(f"{hedef}: {len(bek)} bekleyen; istem {yol} dosyasına yazıldı")
                kuru_yazildi = True
                break
            degisken = yol_ayar.get("anahtar_degiskeni")
            anahtar = (os.environ.get(degisken, "") or "").strip() if degisken else ""   # boş ya da boşluk değer = yok
            if degisken and not anahtar:
                hatalar.append(f"{yol_ayar['saglayici']}: {degisken} yok")
                continue
            try:
                if yol_ayar["saglayici"] == "cli":
                    ham, kullanim = cli_cagir(yol_ayar["komut"], sistem, kullanici, yol_ayar.get("istem_nasil", "dosya"), ad,
                                              int(yol_ayar.get("zaman_asimi", 1800)), yol_ayar.get("ortam"))
                else:
                    ham, kullanim = cagir(yol_ayar["saglayici"], yol_ayar["model"], anahtar, sistem, kullanici, en_cok, yol_ayar.get("dusunme"))
                kullanilan = yol_ayar
                kullanilan_imza = hedef
                break
            except KomutYok as e:
                hatalar.append(f"{yol_ayar['saglayici']}: komut yok: {e}")
            except Exception as e:  # noqa: BLE001
                hatalar.append(f"{yol_ayar['saglayici']}: {str(e)[:300]}")
                yol_hatasi = True
        if kuru_yazildi:
            continue
        if not bek_goruldu and not hatalar:
            print(f"{ad}: bekleyen yok")
            continue
        if kullanilan is None:
            atlandi_yaz(ad, hatalar)
            print(f"{ad}: atlandı ({' | '.join(hatalar)[:200]}) → kayit/atlandi.log")
            if yol_hatasi:
                hata_sayisi += 1
            continue
        try:
            veri = json_ayikla(ham)
            veri["kimden"] = kullanilan_imza
            veri.setdefault("kime", "Sen")
            veri["yanit"] = bek[-1]["id"]
            veri["durum"] = "acik"
            veri.setdefault("dayanak", "")
            kid = ekle(a.dosya, veri)
            sonuc = f"eklendi: {kid}; yol: {kullanilan['saglayici']} {kullanilan.get('model', '')}; bekleyenler: {', '.join(k['id'] for k in bek)}; kullanım: {json.dumps(kullanim, ensure_ascii=False)}"
            eklenenler.append(kid)
        except Exception as e:  # noqa: BLE001
            sonuc = f"HATA: {e}"
            hata_sayisi += 1
        yol = kayit_yaz(ad, kullanilan.get("model", "-"), kullanilan["saglayici"], sistem, kullanici, ham, sonuc)
        print(f"{ad}: {sonuc.splitlines()[0][:200]} → {os.path.relpath(yol, KOK)}")
    print("eklenen:", ", ".join(eklenenler) if eklenenler else "yok")
    if hata_sayisi:
        print(f"HATA: {hata_sayisi} katılımcının yanıtı tamamlanamadı; günlükleri inceleyin.", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
