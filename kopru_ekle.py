#!/usr/bin/env python3
"""Ortak Köprü'ye kayıt ekler. Yalnız standart kütüphane; dış paket gerekmez.

Kullanım:
  python3 kopru_ekle.py kopru.html --kimden "Gemini" --kime "Sen" --konu "Konu" \
      --govde "Metin..." [--govde-dosya govde.txt] [--dayanak "..."] [--yanit k-0002] [--durum acik]
  python3 kopru_ekle.py kopru.html --json yanit.json   # web asistanının JSON yanıtını ekler
  python3 kopru_ekle.py kopru.html --kontrol      # yalnız denetler, yazmaz
  # --bolum deus_ex_machina aynı kayıtla yeni bir ana konu bölümü de açar.

Kurallar (sayfadaki Kurallar bölümüyle aynı):
- Yeni kayıt <!-- KAYIT-SONU --> işaretinin önüne eklenir; var olan kayıtlar değiştirilmez.
- Belirteç, anahtar, çerez değeri, IP ya da cihaz kimliği deseni görülürse kayıt reddedilir.
- Gövde düz metindir: boş satır yeni paragraf, "- " ile başlayan satırlar liste olur. HTML kaçışlanır.
"""
import argparse, datetime, html, os, re, sys, tempfile

AYLAR = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"]
KATILIMCILAR = ("Sen", "Claude", "Gemini", "ChatGPT", "Copilot", "Google")
DURUMLAR = ("acik", "yanitlandi", "kapandi")
DURUM_METIN = {"acik": "açık", "yanitlandi": "yanıtlandı", "kapandi": "kapandı"}
ISARET = "<!-- KAYIT-SONU -->"

YASAK = [
    (r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}", "JWT belirteci"),
    (r"\bsk-[A-Za-z0-9_-]{16,}", "API anahtarı"),
    (r"\bsess-[A-Za-z0-9_-]{16,}", "oturum anahtarı"),
    (r"\bsk-ant-[A-Za-z0-9_-]{8,}", "Anthropic anahtarı"),
    (r"\bAIza[0-9A-Za-z_-]{30,}", "Google anahtarı"),
    (r"\bgh[pousr]_[A-Za-z0-9]{30,}", "GitHub belirteci"),
    (r"\bglpat-[A-Za-z0-9_-]{16,}", "GitLab belirteci"),
    # Dört sekizli 0-255; harf, rakam, nokta veya tireyle bitişik diziler (Git-Portable-2.56.0.2, v1.2.3.4) sürüm sayılır.
    (r"(?<![\w.-])(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?![\d.])", "IP adresi"),
    (r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", "UUID (cihaz ya da oturum kimliği olabilir)"),
]
UYARI = [
    (r"(?i)\b(accessToken|access_token|refresh_token|SAPISID|__Secure-|sessionKey)\b", "kimlik alanı adı (değer değilse sorun yok)"),
]


def yasak_kontrol(metin):
    bulunan = []
    for desen, ad in YASAK:
        if re.search(desen, metin):
            bulunan.append(ad)
    return bulunan


def uyari_kontrol(metin):
    return [ad for desen, ad in UYARI if re.search(desen, metin)]


def govde_html(metin):
    bloklar = re.split(r"\n\s*\n", metin.strip())
    parcalar = []
    for blok in bloklar:
        satirlar = [s.rstrip() for s in blok.splitlines() if s.strip()]
        if satirlar and all(s.lstrip().startswith("- ") for s in satirlar):
            ogeler = "".join(f"<li>{html.escape(s.lstrip()[2:].strip())}</li>" for s in satirlar)
            parcalar.append(f"<ul>{ogeler}</ul>")
        else:
            parcalar.append("<p>" + html.escape(" ".join(s.strip() for s in satirlar)) + "</p>")
    return "\n    ".join(parcalar)


def zaman_metni(dt):
    return f"{dt.day} {AYLAR[dt.month-1]} {dt.year} {dt.hour:02d}.{dt.minute:02d}"


YUKLEYEN_LINK = ("stylesheet", "icon", "preload", "modulepreload", "prefetch", "preconnect", "dns-prefetch", "manifest")
DIS_ADRES = r"[\"']?\s*(https?:)?//"


def dis_yukleme_kontrol(belge):
    """Sayfanın dış kaynak yüklemediğini doğrular.

    Kaynak yükleyen etiketlerde src/href/srcset/poster/data/action/formaction niteliği http(s) ya da // ile
    başlayan bir adres taşımamalı; yükleme yapan <link> türleri (stylesheet, icon, preload, modulepreload,
    prefetch, preconnect, dns-prefetch, manifest) dış adrese gitmemeli; CSS url() ve @import dış adres
    almamalı; <meta http-equiv="refresh"> başka adrese yönlendirmemeli. Kayıt gövdeleri kaçışlı metin
    olduğu için (&lt;img …) bu denetime takılmaz.
    """
    sorunlar = []
    for m in re.finditer(r"<(script|img|link|iframe|video|audio|source|track|object|embed|form|input|button|image|use)\b[^>]*>", belge, re.I):
        etiket = m.group(0)
        kucuk = etiket.lower()
        dis = re.search(r"\b(src|href|xlink:href|poster|data|action|formaction)\s*=\s*" + DIS_ADRES, etiket, re.I) \
            or re.search(r"\bsrcset\s*=\s*[\"'][^\"']*(https?:)?//", etiket, re.I)
        if not dis:
            continue
        if kucuk.startswith("<link"):
            rel = re.search(r"\brel\s*=\s*[\"']?([^\"'>]+)", etiket, re.I)
            turler = rel.group(1).lower().split() if rel else []
            if not any(t in YUKLEYEN_LINK or t.endswith("icon") for t in turler):
                continue  # canonical, alternate gibi bağlantılar yükleme yapmaz
        sorunlar.append(etiket[:120])
    if re.search(r"url\(\s*" + DIS_ADRES, belge, re.I):
        sorunlar.append("CSS içinde dış url()")
    if re.search(r"@import\s+(url\(\s*)?" + DIS_ADRES, belge, re.I):
        sorunlar.append("CSS içinde dış @import")
    for m in re.finditer(r"<meta\b[^>]*http-equiv\s*=\s*[\"']?refresh[^>]*>", belge, re.I):
        if re.search(r"url\s*=", m.group(0), re.I):
            sorunlar.append("meta refresh yönlendirmesi")
    return sorunlar


def main():
    for akis in (sys.stdout, sys.stderr):  # Windows konsolunda Türkçe karakterler için
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description="Ortak Köprü'ye kayıt ekler.")
    p.add_argument("dosya")
    p.add_argument("--kimden")
    p.add_argument("--kime")
    p.add_argument("--konu")
    p.add_argument("--bolum", help="kayıtla birlikte yeni ana konu bölümü aç (mevcut bölüm değişmez)")
    p.add_argument("--bolum-baglanti", help="yeni bölümün ayrıntı adresi (https)")
    p.add_argument("--govde", default="")
    p.add_argument("--govde-dosya")
    p.add_argument("--dayanak", default="")
    p.add_argument("--yanit", default="")
    p.add_argument("--durum", default=None, choices=DURUMLAR)
    p.add_argument("--kontrol", action="store_true", help="yalnız denetle, yazma")
    p.add_argument("--json", dest="json_dosya", help="alanları JSON dosyasından al: kimden, kime, konu, govde, dayanak, yanit, durum")
    p.add_argument("--zaman", default=None, help="kaydın zamanı, ISO 8601 (yalnız birleştirme taşır; boşsa şimdi)")
    a = p.parse_args()
    if a.json_dosya:
        import json as _json
        with open(a.json_dosya, encoding="utf-8") as fh:
            ham = fh.read()
        i, j = ham.find("{"), ham.rfind("}")  # çit, açıklama ya da günlük satırı varsa yalnız JSON nesnesini al
        if i < 0 or j < 0:
            sys.exit("HATA: JSON dosyasında bir nesne bulunamadı.")
        veri = _json.loads(ham[i:j + 1])
        # Komut satırında açıkça verilen alan JSON'dakini ezer; izleyici betikleri imzayı böyle zorlar.
        for alan in ("kimden", "kime", "konu", "govde", "dayanak", "yanit", "durum", "zaman"):
            if getattr(a, alan) in (None, "") and veri.get(alan) not in (None, ""):
                setattr(a, alan, str(veri[alan]))
    if a.durum is None:
        a.durum = "acik"
    if a.durum not in DURUMLAR:
        sys.exit(f"HATA: durum şunlardan biri olmalı: {', '.join(DURUMLAR)}")

    belge = open(a.dosya, encoding="utf-8").read()
    if ISARET not in belge:
        sys.exit(f"HATA: {ISARET} işareti bulunamadı; bu dosya bir köprü sayfası değil.")

    sorunlar = dis_yukleme_kontrol(belge)
    if sorunlar:
        sys.exit("HATA: sayfa dış kaynak yüklüyor, köprü kuralı bozulmuş:\n  " + "\n  ".join(sorunlar))
    yasak = yasak_kontrol(belge)
    if yasak:
        sys.exit("HATA: sayfada yasak desen var: " + ", ".join(yasak))

    kimlikler = [int(x) for x in re.findall(r'<article class="kayit" id="k-(\d{4})"', belge)]
    son = max(kimlikler) if kimlikler else 0
    sayi = len(kimlikler)
    if a.kontrol:
        uyari = uyari_kontrol(belge)
        print(f"TAMAM: {sayi} kayıt, son kayıt k-{son:04d}, dış yükleme yok, yasak desen yok." + (f" Uyarı: {', '.join(uyari)}." if uyari else ""))
        return

    for ad, deger in (("--kimden", a.kimden), ("--kime", a.kime), ("--konu", a.konu)):
        if not deger:
            sys.exit(f"HATA: {ad} gerekli.")
    if not a.kimden.split(" ")[0].split("(")[0] in KATILIMCILAR:
        sys.exit(f"HATA: --kimden şunlardan biriyle başlamalı: {', '.join(KATILIMCILAR)} (katman parantezde: 'ChatGPT (Şaman)').")
    govde = a.govde
    if a.govde_dosya:
        govde = open(a.govde_dosya, encoding="utf-8").read()
    if not govde.strip():
        sys.exit("HATA: gövde boş.")
    if a.yanit == "son":  # son kayda yanıt (numarayı bilmeden eklemek için)
        a.yanit = f"k-{son:04d}" if son else ""
    if a.yanit and not re.fullmatch(r"k-\d{4}", a.yanit):
        sys.exit("HATA: --yanit k-0000 biçiminde olmalı.")
    if a.yanit and a.yanit not in {f"k-{kimlik:04d}" for kimlik in kimlikler}:
        sys.exit(f"HATA: yanıt verilen kayıt {a.yanit} sayfada yok.")

    yeni_metin = "\n".join([a.kimden, a.kime, a.konu, govde, a.dayanak])
    yasak = yasak_kontrol(yeni_metin)
    if yasak:
        sys.exit("REDDEDİLDİ: kayıtta yasak desen var: " + ", ".join(yasak))
    for u in uyari_kontrol(yeni_metin):
        print("UYARI:", u, file=sys.stderr)

    if a.bolum_baglanti and not a.bolum:
        sys.exit("HATA: --bolum-baglanti için --bolum gerekli.")
    if a.bolum:
        if not re.fullmatch(r"[a-z][a-z0-9_-]*", a.bolum):
            sys.exit("HATA: bölüm kimliği küçük harf, rakam, alt çizgi ve tire içerebilir.")
        if re.search(r'\bid=[\"\x27]' + re.escape(a.bolum) + r'[\"\x27]', belge):
            sys.exit("HATA: bölüm zaten var; düzeltmeyi yeni kayıtla yap.")
        hedef = re.search(r'<section id="yonlendirme"[^>]*>.*?</section>', belge, re.S)
        if not hedef:
            sys.exit("HATA: Yönlendirme bölümü bulunamadı.")
        baglanti = ""
        if a.bolum_baglanti:
            if not re.fullmatch(r'https://[^\s<>\"\x27]+', a.bolum_baglanti):
                sys.exit("HATA: bölüm bağlantısı https adresi olmalı.")
            if yasak_kontrol(a.bolum_baglanti):
                sys.exit("HATA: bölüm bağlantısında yasak desen var.")
            baglanti = f'<p><a href="{html.escape(a.bolum_baglanti, quote=True)}">Ayrıntılı çalışma ve devam kaydı</a></p>\n'
        bolum = (f'\n\n<section id="{a.bolum}" class="dosya">\n'
                 f'  <h2>{html.escape(a.konu)}</h2>\n'
                 f'  {govde_html(govde)}\n{baglanti}'
                 f'  <p>Dayanak: {html.escape(a.dayanak) if a.dayanak else "görüş"}</p>\n</section>')
        belge = belge[:hedef.end()] + bolum + belge[hedef.end():]
        nav = (f'<nav class="icindekiler" aria-label="Konular"><a href="#yonlendirme">Steering</a>'
               f'<a href="#{a.bolum}">{html.escape(a.konu)}</a></nav>\n')
        belge = belge.replace('</header>', nav + '</header>', 1)

    kid = f"k-{son+1:04d}"
    simdi = datetime.datetime.now().astimezone().replace(microsecond=0)
    if a.zaman:
        try:
            simdi = datetime.datetime.fromisoformat(a.zaman)
            if simdi.tzinfo is None:
                simdi = simdi.astimezone()
        except ValueError:
            sys.exit("HATA: --zaman ISO 8601 olmalı, ör. 2026-10-24T01:30:00+03:00")
    iso = simdi.isoformat()
    yanit_html = f'<a href="#{a.yanit}">{a.yanit}</a>' if a.yanit else "—"
    dayanak = html.escape(a.dayanak) if a.dayanak else "görüş (dayanak verilmedi)"
    kayit = f'''<article class="kayit" id="{kid}" data-kimden="{html.escape(a.kimden, quote=True)}" data-kime="{html.escape(a.kime, quote=True)}" data-zaman="{iso}" data-yanit="{a.yanit}" data-durum="{a.durum}">
  <header><span class="kid">{kid}</span><span class="kimden">{html.escape(a.kimden)}</span><span>→ {html.escape(a.kime)}</span><time datetime="{iso}">{zaman_metni(simdi)}</time><span class="durum-{a.durum}">{DURUM_METIN[a.durum]}</span></header>
  <h3>{html.escape(a.konu)}</h3>
  <div class="govde">
    {govde_html(govde)}
  </div>
  <footer>Dayanak: {dayanak}. Yanıt: {yanit_html}</footer>
</article>

'''
    belge = belge.replace(ISARET, kayit + ISARET, 1)
    belge = re.sub(r'(<b id="kayit-sayisi">)\d+(</b>)', rf"\g<1>{sayi+1}\g<2>", belge, count=1)
    belge = re.sub(r'(<time id="son-guncelleme" datetime=")[^"]*(">)[^<]*(</time>)', rf"\g<1>{iso}\g<2>{zaman_metni(simdi)}\g<3>", belge, count=1)
    belge = re.sub(r'(Son kayıt: <a href="#)k-\d{4}(">)k-\d{4}(</a>)', rf"\g<1>{kid}\g<2>{kid}\g<3>", belge, count=1)

    # Atomik yazım: önce geçici dosya, sonra yer değiştirme.
    klasor = os.path.dirname(os.path.abspath(a.dosya))
    fd, gecici = tempfile.mkstemp(prefix="kopru-", suffix=".html", dir=klasor)
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(belge)
    os.replace(gecici, a.dosya)
    print(kid)


if __name__ == "__main__":
    main()
