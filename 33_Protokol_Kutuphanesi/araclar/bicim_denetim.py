"""Ortak biçim kuralları denetimi (ORTAK_BICIM_KURALLARI.md).
Kullanım (kütüphane klasöründe): python3 araclar/bicim_denetim.py protokoller [--ornek] [--json çıktı]
Her kural için aykırı yerleri sayar; kullanıcının korunan sözleri ve çizim blokları (~~~text) sayım dışıdır.
"ihlal" sıfır olmalıdır; "okunacak" anlamı bağlama göre değişen sözcüklerdir (iyelik/sıfat) ve elle okunur."""
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bicim  # noqa: E402

SAPKALI = ["dâhil", "hâl", "hâlâ", "hâlen", "hâlihazırda", "hâkim", "imkân", "mekân", "zekâ", "karargâh", "güzergâh",
           "kâğıt", "hikâye", "şikâyet", "fedakâr", "inkâr", "kâmil"]
SAPKASIZ_YANLIS = re.compile(r"\b([İi]nsanî|[Mm]anevî|[İi]lahî|[Aa]slî|[Tt]abî|[Aa]hlakî|[Mm]eslekî|[Tt]icarî|[Hh]ukukî|[İi]darî|[Vv]icdanî)\b")
SAPKASIZ_GEREKEN = [
    (r"\b[Dd]ahil\w*", "dahil"),
    (r"\b[Hh]al(e|i|de|den|inde|indeki|ine|ini|iyle|leri|lerde|lerinde|leriyle|ler|in|en)\b", "hal-"),
    (r"\b[Hh]ala\b", "hala"),
    (r"\b[Hh]alihazır\w*", "halihazır"),
    (r"\b[Hh]akim\w*", "hakim"),
    (r"\b[İi]mkan\w*", "imkan"),
    (r"\bmekan(?!iz|ik)\w*", "mekan (küçük harf)"),
    (r"\b[Zz]eka\w*", "zeka"),
    (r"\b[Kk]arargah\w*", "karargah"),
    (r"\b[Gg]üzergah\w*", "güzergah"),
    (r"\b[Kk]ağıt\w*", "kağıt"),
    (r"\b[Hh]ikaye\w*", "hikaye"),
    (r"\b[Şş]ikayet\w*", "şikayet"),
    (r"\b[Ff]edakar\w*", "fedakar"),
    (r"\b[İi]nkar\w*", "inkar"),
    (r"\bkamil\w*", "kamil"),
    (r"\busül\w*", "usül (küçük harf; kavram usul)"),
]
OKUNACAK = re.compile(r"\b([Aa]skeri|[Rr]esmi|[Ff]iili|[Mm]erkezi|[Hh]arici|[Hh]ayali|[Kk]eyfi|[Ff]ikri|[Hh]issi|[Zz]ihni|[Tt]arihi)\b")
GORUNMEZ = re.compile("[ ​‌‍⁠﻿­\t]")
Y2 = ["## 0 Tohum (Başlangıç) Protokolü", "## 1 Varlık Protokolü", "## 2 Mekan Protokolü", "## 3 Usül Protokolü",
      "## 4 Zaman Protokolü", "## 5 Gaye Protokolü", "## 6 Kökleşme (Bitiş) Protokolü"]


def denetle(path):
    raw = open(path, "rb").read()
    ihlal, okun, ornek = Counter(), Counter(), defaultdict(list)

    def say(sayac, kural, metin, n=1):
        sayac[kural] += n
        if len(ornek[kural]) < 4:
            ornek[kural].append(metin[:140])

    if raw.startswith(b"\xef\xbb\xbf"):
        say(ihlal, "M1 BOM", "BOM")
    text = raw.decode("utf-8")
    if "\r" in text:
        say(ihlal, "M1 CR satır sonu", "CR", text.count("\r"))
    if unicodedata.normalize("NFC", text) != text:
        say(ihlal, "M1 NFC değil", "NFC")
    if not text.endswith("\n") or text.endswith("\n\n"):
        say(ihlal, "M1 dosya sonu tek satır sonuyla bitmeli", repr(text[-5:]))
    if not re.fullmatch(r"\d\d[_.][A-Za-z0-9_.-]+\.md", os.path.basename(path)):
        say(ihlal, "M8 dosya adı", os.path.basename(path))
    # çizim bloklarını ayır; M7 denetimi
    cizimler = re.findall(r"\n~~~text\n(.*?)\n~~~\n\n(\*Çizim (\d+) — [^\n]*\*)", text, flags=re.S)
    for no, (blk, alt, n) in enumerate(cizimler, 1):
        if int(n) != no:
            say(ihlal, "M7 çizim numarası sırası", alt)
        for l in blk.split("\n"):
            if len(l) > 72:
                say(ihlal, "M7 çizim 72 sütunu aşıyor", l)
            if any(ord(c) > 126 or (ord(c) < 32) for c in l):
                say(ihlal, "M7 çizimde ASCII dışı", l)
    if text.count("~~~text") != len(cizimler):
        say(ihlal, "M7 alt yazısız çizim bloğu", str(text.count("~~~text") - len(cizimler)))
    govde = re.sub(r"\n\n~~~text\n.*?\n~~~\n\n\*Çizim \d+ — [^\n]*\*(?=\n|$)", "", text.rstrip("\n"), flags=re.S)
    spans = bicim.korunan_araliklar(govde)

    def korunuyor(a, b):
        return any(s < b and a < e for s, e in spans)

    def bul(pat, kural, sayac=ihlal, metin=govde):
        for m in re.finditer(pat, metin):
            if not korunuyor(m.start(), m.end()):
                say(sayac, kural, metin[max(0, m.start() - 40):m.end() + 40].replace("\n", "⏎"))

    lines, info = bicim._satir_bloklari(govde)
    # satır düzeyi kurallar
    h1, onceki, fence = 0, 0, False
    for k, l in enumerate(lines):
        if re.match(r"^(```|~~~)", l):
            if l.startswith("~~~") and not fence:
                say(ihlal, "M5 ~~~ ile açılan kod/şablon bloğu", l)
            fence = not fence
            continue
        if l != l.rstrip(" \t"):
            say(ihlal, "M2 satır sonu boşluğu", repr(l[-30:]))
        if GORUNMEZ.search(l):
            say(ihlal, "M1 sekme/görünmez karakter", repr(GORUNMEZ.search(l).group(0)) + " " + l[:60])
        if fence:
            continue
        if re.search(r"\S  +\S", l):
            say(ihlal, "M2 satır içinde art arda boşluk", l)
        if l == "" and k and lines[k - 1] == "":
            say(ihlal, "M2 art arda boş satır", f"satır {k + 1}")
        m = re.match(r"^(#{1,6}) (.*)$", l)
        if m:
            lv = len(m.group(1))
            h1 += lv == 1
            if onceki and lv > onceki + 1:
                say(ihlal, "M3 başlık düzeyi atlıyor", l)
            onceki = lv
            if re.search(r"[.,;:]$", m.group(2)):
                say(ihlal, "M3 başlık noktalama ile bitiyor", l)
        if re.match(r"^\s*[*+] ", l):
            say(ihlal, "M4 liste imi - olmalı", l)
        if re.match(r"^\s*\d+\) ", l):
            say(ihlal, "M4 numaralı liste '1. ' olmalı", l)
        if re.match(r"^\s*(?:[-+*]|\d+\.)?\s*\*\*[^*\n]+\*\*:", l):
            say(ihlal, "M4 iki nokta kalın etiketin dışında", l)
        # M6 bağlantılar ve HTML
        l2 = re.sub(r"`[^`\n]*`", "", l)
        for a, b, metin, h, tur in bicim.baglanti_bul(l2):
            if tur == "satir":
                say(ihlal, "M6 bağlantı söz dizimi [..](..)", l2[a:b])
        if re.match(r"^\s*\[[^\]]+\]:\s*\S", l2):
            say(ihlal, "M6 başvuru tanımı", l2)
        if re.search(r"<https?://", l2):
            say(ihlal, "M6 <adres>", l2)
        if re.search(r"</?[a-zA-Z][a-zA-Z0-9]*(\s[^>]*)?>", l2):
            say(ihlal, "M6 HTML etiketi", l2)
        # T2 düz çift tırnak (satır içi kod dışında, yazı içinde)
        if '"' in l2:
            say(ihlal, "T2 düz çift tırnak", l2)
        # T5 yüzde
        for mm in re.finditer(r"\b\d+(?:[.,]\d+)?\s?%|%\s\d", l2):
            if not re.search(r"https?://\S*$", l2[:mm.start()]):
                say(ihlal, "T5 yüzde işareti sayıdan önce", l2[max(0, mm.start() - 30):mm.end() + 10])
        # T6 sayısal tarih
        for mm in re.finditer(r"\b\d{1,2}[./]\d{1,2}[./]\d{4}\b|\b\d{4}-\d{2}-\d{2}\b", l2):
            if not re.search(r"https?://\S*$", l2[:mm.start()]):
                say(ihlal, "T6 sayısal tarih", l2[max(0, mm.start() - 30):mm.end() + 10])
    if h1 != 1:
        say(ihlal, "M3 tek birinci düzey başlık", f"{h1} adet")
    # T1 kelime içi kıvrık kesme
    bul(r"(?<=[\w)”%.])’(?=\w)", "T1 kelime içinde ’")
    # T3
    bul(SAPKASIZ_YANLIS, "T3 şapkasız yazılmalı")
    for pat, ad in SAPKASIZ_GEREKEN:
        bul(pat, f"T3 şapkalı yazılmalı: {ad}")
    bul(OKUNACAK, "T3 bağlama göre (iyelik mi sıfat mı?)", okun)
    # T4 aralık kısa çizgiyle (adres ve standart numarası dışında)
    for mm in re.finditer(r"(?<![\w/.:#-])(\d{1,3})-(\d{1,3})(?![\w-])", govde):
        satir = govde[govde.rfind("\n", 0, mm.start()) + 1:mm.start()]
        if re.search(r"https?://\S*$", satir) or korunuyor(mm.start(), mm.end()):
            continue
        if re.search(r"\b(SP|ISO|IEC|RFC|TR|IEEE|EN|TS|Std\.?|No\.?)\s$", satir) or re.search(r"\d{4}-$", satir):
            continue  # standart ve belge numaraları değişmez
        say(ihlal, "T4 aralık – ile yazılmalı", govde[max(0, mm.start() - 40):mm.end() + 20].replace("\n", "⏎"))
    # Y1 başlık bloğu
    L = govde.split("\n")
    i = 1
    while i < len(L) and L[i] == "":
        i += 1
    if i < len(L) and re.fullmatch(r"\*\*[^*]+\*\*", L[i]) and not re.match(r"\*\*[^*]+:\*\*", L[i]):
        i += 2
    alan = []
    while i < len(L) and L[i]:
        alan.append(L[i])
        i += 1
    if not alan or not alan[0].startswith("**Sürüm:** 1.0"):
        say(ihlal, "Y1 ilk alan **Sürüm:** 1.0", alan[0] if alan else "(alan yok)")
    tarihli = [j for j, a in enumerate(alan) if a.startswith("**Tarih:** ")]
    if tarihli != ([1] if tarihli else []):
        say(ihlal, "Y1 Tarih varsa ikinci alan ve tek", " / ".join(alan[:3]))
    for j, a in enumerate(alan):
        if not re.match(r"^\*\*[^*]+:\*\* \S", a):
            say(ihlal, "Y1 alan biçimi **Ad:** değer", a)
        if (j < len(alan) - 1) != a.endswith("\\"):
            say(ihlal, "Y1 satır kırma (son alan dışında \\)", a)
    # Y2 (kod ve şablon blokları dışında)
    disari = [l for k, l in enumerate(lines) if info[k][0] == "metin"]
    for h in Y2:
        if disari.count(h) != 1:
            say(ihlal, "Y2 bölüm başlığı tam bir kez", h)
    return ihlal, okun, ornek


def main():
    hedef = sys.argv[1]
    files = [os.path.join(hedef, f) for f in sorted(os.listdir(hedef)) if f.endswith(".md")] if os.path.isdir(hedef) else [hedef]
    ozet, toplam = {}, Counter()
    for f in files:
        ihlal, okun, ornek = denetle(f)
        toplam.update(ihlal)
        ozet[os.path.basename(f)] = {"ihlal": dict(ihlal), "okunacak": dict(okun), "ornek": {k: v for k, v in ornek.items()}}
        print(os.path.basename(f)[:40], "ihlal:", sum(ihlal.values()), dict(ihlal) if ihlal else "", "| okunacak:", sum(okun.values()))
        if "--ornek" in sys.argv:
            for k, v in ornek.items():
                for x in v:
                    print("    ", k, "→", x)
    print("TOPLAM ihlal:", sum(toplam.values()), dict(toplam))
    if "--json" in sys.argv:
        json.dump(ozet, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
