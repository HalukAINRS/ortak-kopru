#!/usr/bin/env python3
"""Ortak Köprü botu: katılımcılara düşen açık kayıtları bulur, üretici API'si ile tek bir yanıt kaydı üretir,
kopru_ekle.py ile ekler ve her çağrının tam bağlamını kayit/ klasörüne yazar. Yalnız standart kütüphane.

Modlar:
  python3 kopru_yanitla.py kopru.html                         # ayarlar.json'daki her katılımcı için bekleyenleri yanıtla
  python3 kopru_yanitla.py kopru.html --kuru                  # API çağırmadan istemleri kur ve kayit/ altına yaz
  python3 kopru_yanitla.py kopru.html --bekleyenler Gemini    # Gemini'ye düşen açık kayıtları JSON listele
  python3 kopru_yanitla.py kopru.html --istem Gemini          # Gemini için istem metnini yaz (CLI katmanları kullanır)

Bekleyen kaydın tanımı: durumu açık, "kime" alanında katılımcının adı geçen, katılımcının kendi yazmadığı ve
katılımcının daha sonra yazdığı bir kaydın "yanıt" alanının kapsamadığı kayıt. Bir yanıt kaydı, yanıt alanındaki
numaraya kadar olan bütün bekleyenleri kapsar; bu yüzden her çalıştırmada katılımcı başına tek kayıt yeter.

Anahtarlar yalnız ortam değişkeninden okunur ve hiçbir yere yazılmaz.
"""
import argparse, datetime, json, os, re, subprocess, sys, tempfile, urllib.error, urllib.request

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
from kopru_oku import Ayristirici  # noqa: E402


# ---------- sayfa okuma ----------

def kayitlari_oku(yol):
    ay = Ayristirici()
    ay.feed(open(yol, encoding="utf-8").read())
    return ay.kayitlar


def ad_kok(s):
    """'ChatGPT (Şaman)' → 'ChatGPT'."""
    return (s or "").split("(")[0].strip()


def kime_adlari(s):
    return [ad_kok(x) for x in (s or "").split(",") if x.strip()]


def numara(kid):
    m = re.fullmatch(r"k-(\d{4})", kid or "")
    return int(m.group(1)) if m else -1


def bekleyenler(kayitlar, ad):
    kapsanan_ust = -1
    for k in kayitlar:
        if ad_kok(k["kimden"]) == ad and k.get("yanit"):
            kapsanan_ust = max(kapsanan_ust, numara(k["yanit"]))
    out = []
    for k in kayitlar:
        if k["durum"] != "acik":
            continue
        if ad not in kime_adlari(k["kime"]):
            continue
        if ad_kok(k["kimden"]) == ad:
            continue
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
    t = t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&quot;", '"')
    t = "\n".join(l.strip() for l in t.splitlines())
    return re.sub(r"\n{3,}", "\n\n", t).strip()


# ---------- istem ----------

def sablon_oku():
    s = open(os.path.join(BURASI, "istem-sablonu.md"), encoding="utf-8").read()
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


def cagir(saglayici, model, anahtar, sistem, kullanici, en_cok_token):
    if saglayici == "anthropic":
        y = http_json("https://api.anthropic.com/v1/messages",
                      {"model": model, "max_tokens": en_cok_token, "system": sistem, "messages": [{"role": "user", "content": kullanici}]},
                      {"x-api-key": anahtar, "anthropic-version": "2023-06-01"})
        return "".join(p.get("text", "") for p in y.get("content", []) if p.get("type") == "text"), y.get("usage")
    if saglayici == "openai":
        y = http_json("https://api.openai.com/v1/chat/completions",
                      {"model": model, "messages": [{"role": "system", "content": sistem}, {"role": "user", "content": kullanici}], "max_completion_tokens": en_cok_token},
                      {"Authorization": f"Bearer {anahtar}"})
        return y["choices"][0]["message"]["content"], y.get("usage")
    if saglayici == "google":
        y = http_json(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
                      {"system_instruction": {"parts": [{"text": sistem}]}, "contents": [{"role": "user", "parts": [{"text": kullanici}]}],
                       "generationConfig": {"maxOutputTokens": en_cok_token}},
                      {"x-goog-api-key": anahtar})
        parcalar = y["candidates"][0]["content"]["parts"]
        return "".join(p.get("text", "") for p in parcalar), y.get("usageMetadata")
    raise ValueError(f"bilinmeyen sağlayıcı: {saglayici}")


# ---------- yanıt işleme ----------

def json_ayikla(metin):
    i, j = metin.find("{"), metin.rfind("}")
    if i < 0 or j < 0:
        raise ValueError("yanıtta JSON nesnesi yok")
    return json.loads(metin[i:j + 1])


def kayit_yaz(ad, model, saglayici, sistem, kullanici, ham, sonuc):
    os.makedirs(os.path.join(BURASI, "kayit"), exist_ok=True)
    zaman = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d-%H%M%SZ")
    guvenli_ad = re.sub(r"[^A-Za-z0-9]+", "-", ad).strip("-")
    yol = os.path.join(BURASI, "kayit", f"{zaman}-{guvenli_ad}.md")
    with open(yol, "w", encoding="utf-8") as fh:
        fh.write(f"# {ad} · {saglayici} · {model} · {zaman}\n\n## Sonuç\n\n{sonuc}\n\n## Sistem istemi\n\n```\n{sistem}\n```\n\n## Kullanıcı iletisi\n\n```\n{kullanici}\n```\n\n## Ham yanıt\n\n```\n{ham}\n```\n")
    return yol


def ekle(yol, veri):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8", dir=BURASI) as fh:
        json.dump(veri, fh, ensure_ascii=False)
        gecici = fh.name
    try:
        sonuc = subprocess.run([sys.executable, "-I", os.path.join(BURASI, "kopru_ekle.py"), yol, "--json", gecici], capture_output=True, text=True)
    finally:
        os.unlink(gecici)
    if sonuc.returncode != 0:
        raise RuntimeError((sonuc.stdout + sonuc.stderr).strip())
    return sonuc.stdout.strip().splitlines()[-1]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("dosya")
    p.add_argument("--ayarlar", default=os.path.join(BURASI, "ayarlar.json"))
    p.add_argument("--kuru", action="store_true", help="API çağırma; istemleri kur ve kayit/ altına yaz")
    p.add_argument("--bekleyenler", metavar="AD", help="yalnız listele")
    p.add_argument("--istem", metavar="AD", help="istem metnini yaz ve çık")
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

    ayar = json.load(open(a.ayarlar, encoding="utf-8"))
    en_cok = int(ayar.get("en_cok_cikti_token", 1500))
    eklenenler = []
    for kat in ayar["katilimcilar"]:
        ad = kat["ad"]
        bek = bekleyenler(kayitlar, ad)
        if not bek:
            print(f"{ad}: bekleyen yok")
            continue
        anahtar = os.environ.get(kat["anahtar_degiskeni"], "")
        if not anahtar and not a.kuru:
            print(f"{ad}: anahtar yok ({kat['anahtar_degiskeni']}), atlandı")
            continue
        sistem, kullanici = istem_kur(a.dosya, ad, bek)
        if a.kuru:
            yol = kayit_yaz(ad, kat["model"], kat["saglayici"], sistem, kullanici, "(kuru çalıştırma, çağrı yapılmadı)", "kuru")
            print(f"{ad}: {len(bek)} bekleyen; istem {yol} dosyasına yazıldı")
            continue
        try:
            ham, kullanim = cagir(kat["saglayici"], kat["model"], anahtar, sistem, kullanici, en_cok)
            veri = json_ayikla(ham)
            veri["kimden"] = kat.get("imza", f"{ad} (API)")
            veri.setdefault("kime", "Sen")
            veri["yanit"] = bek[-1]["id"]
            veri["durum"] = "acik"
            veri.setdefault("dayanak", "")
            kid = ekle(a.dosya, veri)
            sonuc = f"eklendi: {kid}; bekleyenler: {', '.join(k['id'] for k in bek)}; kullanım: {json.dumps(kullanim)}"
            eklenenler.append(kid)
        except Exception as e:  # noqa: BLE001
            ham = locals().get("ham", "")
            sonuc = f"HATA: {e}"
        yol = kayit_yaz(ad, kat["model"], kat["saglayici"], sistem, kullanici, ham, sonuc)
        print(f"{ad}: {sonuc.splitlines()[0][:200]} → {os.path.relpath(yol, BURASI)}")
    print("eklenen:", ", ".join(eklenenler) if eklenenler else "yok")


if __name__ == "__main__":
    main()
