"""Ortak biçim kuralları (out/ORTAK_BICIM_KURALLARI.md): metne uygulanır, kullanıcının sözleri korunur.
normalize(text) -> (yeni_metin, sayac).  Çizimler bu aşamadan sonra eklenir; bu yüzden çizimlere dokunulmaz."""
import re
from collections import Counter

# ---------------------------------------------------------------- korunan kullanıcı metni
KORUMA = [
    re.compile(r"[^.?!\n“”\"*>(]*köken aldığı varlık, mekan, usül, zaman, ve gayeyi[^?\n]*\?(?:\s*Kim değildir\?)?"),
    re.compile(r"Bu soruları ve yanıtları kayıt altına alarak belgele\."),
    re.compile(r"Önce mevcut soru-yanıtlarla 1-5 arası protokol bölümlerini paragraf-ağırlıklı oluştur\."),
    re.compile(r"Sonrasında 0 ve 6'ncı bölüm başlıklarından ne anladığını buraya aktar\."),
    re.compile(r"0'ı Tohum \(Başlangıç\) protokolü, 6'yı Kökleşme \(Bitiş\) protokolüne dönüştür\."),
    re.compile(r"Belgenin son halini oluştur ve masaüstünde gerçekleştirmeye uygun protokollere `\.md` formatında indirmeye hazır hale getir\."),
    re.compile(r"Geçmiş bağlamları buraya taşıma\."),
    re.compile(r"Burası ile sınırlı kalma\."),
]


def korunan_araliklar(text):
    return sorted((m.start(), m.end()) for p in KORUMA for m in p.finditer(text))


def _korunuyor(a, b, spans):
    return any(s < b and a < e for s, e in spans)


def _sub(pat, repl, text, sayac, anahtar, koru=True):
    spans = korunan_araliklar(text) if koru else []
    out, last, n = [], 0, 0
    for m in pat.finditer(text):
        if spans and _korunuyor(m.start(), m.end(), spans):
            sayac[anahtar + " (korundu)"] += 1
            continue
        out.append(text[last:m.start()])
        out.append(repl(m) if callable(repl) else m.expand(repl))
        last = m.end()
        n += 1
    out.append(text[last:])
    if n:
        sayac[anahtar] += n
    return "".join(out)


# ---------------------------------------------------------------- T3 şapka (TDK Güncel Türkçe Sözlük; ORTAK_BICIM_KURALLARI.md)
SAPKA = [
    (r"\b([Dd])ahil", r"\1âhil", "T3 dâhil"),
    (r"\b([Hh])al(e|i|de|den|inde|indeki|ine|ini|iyle|leri|lerde|lerinde|leriyle|ler|in|en)\b", r"\1âl\2", "T3 hâl"),
    (r"\b([İi])nsanî\b", r"\1nsani", "T3 insani"),
    (r"\b([Mm])anevî\b", r"\1anevi", "T3 manevi"),
    (r"\b([Mm])erkezi (iddiaların|sonuçların|sonucu)\b", r"\1erkezî \2", "T3 merkezî (sıfat)"),
    (r"\b([Ff])iili (sonuçlar|yönelim)\b", r"\1iilî \2", "T3 fiilî (sıfat)"),
    (r"\b([Hh])arici disk\b", r"\1aricî disk", "T3 haricî (sıfat)"),
]

EYLEM = {"kaynağı aç", "kaynağa git", "kaynağa erişim", "kaynak bağlantısı", "kaynak belgeyi aç", "önceki belgeyi aç"}
BETIM = {"kaynak metni", "kaynak metin", "makale metni", "makale kaydı", "yazarın metni", "metin"}
KAYNAK_BASLIK = re.compile(r"^#{2,6} (?:Ek [A-Z] —? ?)?(Kaynaklar\b|Kaynakça|Kaynak \d+$|Yöntem kaynakları|Çalışma kaynakları|"
                           r"Konuşma yanıtlarında kullanılan kaynaklar|Birinci yanıtın kaynakları|İkinci yanıtın kaynakları|"
                           r"Kaynak işaretlerinin karşılıkları|Dayanak [Dd]izini|Dayanaklar$|Referanslar)")
URL = re.compile(r"https?://[^\s<>\"]+")


def url_temiz(u):
    """Metindeki adresin sonuna yapışan noktalama ve dengesiz kapanış ayracı atılır."""
    while u and u[-1] in ".,;:)":
        if u[-1] == ")" and u.count("(") >= u.count(")"):
            break
        u = u[:-1]
    return u


def _tr_lower(s):
    return s.replace("İ", "i").replace("I", "ı").lower()


def _satir_bloklari(text):
    """Her satır için: kod bloğunda mı, kaynak bölümünde mi."""
    lines = text.split("\n")
    fence, kaynak, info = False, False, []
    for l in lines:
        if re.match(r"^(```|~~~)", l):
            info.append(("fence", kaynak))
            fence = not fence
            continue
        if not fence and re.match(r"^#{1,6} ", l):
            kaynak = bool(KAYNAK_BASLIK.match(l))
        info.append(("kod" if fence else "metin", kaynak))
    return lines, info


def _kapanis(s, i, ac, kapa):
    """s[i] == ac; dengeli kapanışın konumu ya da -1 (ters bölüyle kaçırılanlar sayılmaz)."""
    d, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == ac:
            d += 1
        elif c == kapa:
            d -= 1
            if d == 0:
                return j
        j += 1
    return -1


def baglanti_bul(line):
    """Satır içi bağlantılar: (başlangıç, bitiş, metin, hedef, tür) — tür "satir" ([m](h)) ya da "basvuru" ([m][L], [L][])."""
    res, i = [], 0
    while True:
        a = line.find("[", i)
        if a < 0:
            return res
        if a > 0 and line[a - 1] == "!":
            raise ValueError("görsel söz dizimi beklenmiyordu: " + line[a - 1:a + 40])
        j = _kapanis(line, a, "[", "]")
        if j < 0:
            return res
        if j + 1 < len(line) and line[j + 1] == "(":
            k = _kapanis(line, j + 1, "(", ")")
            if k > 0:
                res.append((a, k + 1, line[a + 1:j], line[j + 2:k].strip(), "satir"))
                i = k + 1
                continue
        if j + 1 < len(line) and line[j + 1] == "[":
            k = line.find("]", j + 2)
            if k > 0 and "[" not in line[j + 2:k]:
                res.append((a, k + 1, line[a + 1:j], line[j + 2:k], "basvuru"))
                i = k + 1
                continue
        i = a + 1


def _isaret(metin):
    """"1", "[1]", "K3" -> "[1]", "[K3]"; değilse None."""
    m = re.fullmatch(r"\[?(\d+|K\d+(?:-\d+)?)\]?", metin.strip())
    return f"[{m.group(1)}]" if m else None


def _kunye_bicimi(metin, url):
    """Künyenin yanında adres: bağlantı metni eylem bildiriyorsa "Adres:", betimliyorsa kendi etiketiyle."""
    m = metin.strip()
    k = _tr_lower(m)
    if m == url:
        return url, "M6 adres metinli bağlantı -> adres"
    if k in EYLEM:
        return f"Adres: {url}", "M6 eylem metinli bağlantı -> Adres: adres"
    if k in BETIM:
        return f"{m}: {url}", "M6 betim metinli bağlantı -> etiket: adres"
    i = _isaret(m)
    if i:
        return f"{i} ({url})", "M6 künyede numaralı bağlantı -> [n] (adres)"
    return f"{m} ({url})", "M6 künye bağlantısı -> künye (adres)"


def baglantilar(text, sayac):
    """M6: bağlantı söz dizimi düz metne çevrilir; her adres künyenin yanında ya da cümlenin içinde görünür kalır."""
    url_once = {url_temiz(u) for u in URL.findall(text)}
    lines, info = _satir_bloklari(text)
    tanim, tanim_satir = {}, {}
    for k, l in enumerate(lines):
        m = re.match(r'^\s*\[([^\]]+)\]:\s*<?(https?://[^\s>]+)>?(?:\s+"([^"]*)")?\s*$', l)
        if m and info[k][0] == "metin":
            tanim[m.group(1)] = m.group(2)
            tanim_satir[k] = m.group(1)
    yeni = list(lines)
    # 1) kendiliğinden bağlantılar <U> -> U
    for k, l in enumerate(yeni):
        if info[k][0] != "metin" or k in tanim_satir:
            continue
        yeni[k], n = re.subn(r"<(https?://[^>\s]+)>", r"\1", l)
        if n:
            sayac["M6 <adres> -> adres"] += n

    def hedef_url(h, tur):
        if tur == "basvuru":
            return tanim.get(h or None)
        u = h.split()[0].strip("<>") if h else ""
        return u if u.startswith(("http://", "https://")) else None

    def donustur(k, kaynakta, gor):
        l = yeni[k]
        out, last = [], 0
        for a, b, metin, h, tur in baglanti_bul(l):
            if tur == "basvuru":
                lab = h or metin
                u = tanim.get(lab)
            else:
                u = hedef_url(h, tur)
            if not u:
                continue
            if kaynakta:
                rep, anahtar = _kunye_bicimi(metin, u)
            else:
                m = metin.strip()
                k2 = _tr_lower(m)
                i = _isaret(m)
                if m == u or k2 in EYLEM or k2 in BETIM:
                    rep, anahtar = _kunye_bicimi(metin, u)
                elif i:
                    rep, anahtar = (i, "M6 numaralı gönderme -> [n] (adres künyede)") if u in gor else (f"{i} ({u})", "M6 numaralı gönderme -> [n] (adres)")
                else:
                    # cümleden sonra satır sonunda duran adlı gönderme köşeli ayraçla işaretlenir: [NIST SP 800-160]
                    atif = re.search(r"[.?!]\s*$", l[:a]) and not l[b:].strip()
                    g = f"[{m}]" if atif else m
                    rep, anahtar = (g, "M6 metin içi bağlantı -> metin (adres künyede)") if u in gor else (f"{g} ({u})", "M6 metin içi bağlantı -> metin (adres)")
            gor.add(u)
            sayac[anahtar] += 1
            out.append(l[last:a])
            out.append(rep)
            last = b
        if out:
            out.append(l[last:])
            yeni[k] = "".join(out)

    def gorunur(haric):
        s = set()
        for k, l in enumerate(yeni):
            if k in haric or info[k][0] != "metin":
                continue
            l2 = l
            for a, b, metin, h, tur in reversed(baglanti_bul(l)):
                l2 = l2[:a] + l2[b:]
            s.update(url_temiz(u) for u in URL.findall(l2))
        return s
    # 2) kaynak bölümleri: künye + adres
    gor = set()
    for k in range(len(yeni)):
        if info[k][0] == "metin" and info[k][1] and k not in tanim_satir:
            donustur(k, True, gor)
    # 3) öbür satırlar
    gor = gorunur(set(tanim_satir))
    for k in range(len(yeni)):
        if info[k][0] == "metin" and not info[k][1] and k not in tanim_satir:
            donustur(k, False, gor)
    # 4) başvuru tanımları: adres görünürse satır çıkar; değilse düz satır
    gor = gorunur(set(tanim_satir))
    sil = set()
    for k, lab in tanim_satir.items():
        if tanim[lab] in gor:
            sil.add(k)
            sayac["M6 başvuru tanımı çıktı (adres görünür)"] += 1
        else:
            yeni[k] = f"[{lab}] Adres: {tanim[lab]}"
            gor.add(tanim[lab])
            sayac["M6 başvuru tanımı -> [L] Adres: adres"] += 1
    yeni = [l for k, l in enumerate(yeni) if k not in sil]
    text2 = "\n".join(yeni)
    url_sonra = {url_temiz(u) for u in URL.findall(text2)}
    kayip = url_once - url_sonra
    assert not kayip, f"adres kayboldu: {sorted(kayip)[:3]}"
    return text2


def dosya_ici(text, sayac):
    """M6: dosya içi bağlantılar düz metin; HTML çapaları çıkar."""
    lines, info = _satir_bloklari(text)
    for k, l in enumerate(lines):
        if info[k][0] != "metin":
            continue
        out, last = [], 0
        for a, b, metin, h, tur in baglanti_bul(l):
            if tur != "satir" or not h.startswith("#"):
                continue
            i = _isaret(metin)
            out += [l[last:a], i if i else metin.strip()]
            last = b
            sayac["M6 dosya içi bağlantı -> düz"] += 1
        if out:
            out.append(l[last:])
            lines[k] = "".join(out)
    text = "\n".join(lines)
    text, n = re.subn(r'(?m)^<a id="[^"]+"></a>\n', "", text)
    if n:
        sayac["M6 HTML çapası çıktı"] += n
    return text


def satir_sonlari(text, sayac):
    """M2: satır sonu boşluğu yok; zorunlu satır kırma ters bölüyle."""
    lines = text.split("\n")
    out, fence = [], False
    for k, l in enumerate(lines):
        if re.match(r"^(```|~~~)", l):
            fence = not fence
            out.append(l.rstrip())
            continue
        s = l.rstrip(" \t")
        if s != l:
            sonraki = lines[k + 1] if k + 1 < len(lines) else ""
            if (not fence and l.endswith("  ") and s and sonraki.strip() and not sonraki.lstrip().startswith(("#", "|", "```", "~~~"))
                    and not s.startswith("|") and not s.endswith("\\")):
                s += "\\"
                sayac["M2 iki boşluk -> ters bölü"] += 1
            else:
                sayac["M2 satır sonu boşluğu silindi"] += 1
        out.append(s)
    return "\n".join(out)


def tilde_bloklari(text, sayac):
    """M5: çizim dışı ~~~ blokları üç ters tırnakla açılır (içlerinde ``` yoksa)."""
    def r(m):
        govde = m.group(2)
        if "```" in govde:
            return m.group(0)
        sayac["M5 ~~~ blok -> ```"] += 1
        return "```" + m.group(1) + "\n" + govde + "\n```"
    return re.sub(r"(?ms)^~{3,}(?!text)([\w-]*)\n(.*?)\n~{3,}$", r, text)


def bolum_basliklari(text, sayac):
    """Y2: 0–6 bölüm başlıkları tek biçimde."""
    for a, b in [(r"(?m)^## (\d) — ", r"## \1 "),
                 (r"(?m)^## 0 Tohum Protokolü — Başlangıç$", "## 0 Tohum (Başlangıç) Protokolü"),
                 (r"(?m)^## 6 Kökleşme Protokolü — Bitiş$", "## 6 Kökleşme (Bitiş) Protokolü")]:
        text, n = re.subn(a, b, text)
        if n:
            sayac["Y2 bölüm başlığı"] += n
    return text


def bos_satirlar(text, sayac):
    """M2: kod blokları dışında art arda iki boş satır bulunmaz; dosya sonunda boş satır kalmaz."""
    lines = text.split("\n")
    out, fence = [], False
    for l in lines:
        if re.match(r"^(```|~~~)", l):
            fence = not fence
        if not fence and l == "" and out and out[-1] == "" and not re.match(r"^(```|~~~)", l):
            sayac["M2 çift boş satır teke indi"] += 1
            continue
        out.append(l)
    while out and out[-1] == "":
        out.pop()
    return "\n".join(out)


def normalize(text):
    sayac = Counter()
    text = baglantilar(text, sayac)
    text = dosya_ici(text, sayac)
    text = _sub(re.compile(r"(?<=\w)’(?=\w)"), "'", text, sayac, "T1 kesme ’ -> '")
    for p, r, k in SAPKA:
        text = _sub(re.compile(p), r, text, sayac, k)
    text = tilde_bloklari(text, sayac)
    text = bolum_basliklari(text, sayac)
    text = satir_sonlari(text, sayac)
    text = bos_satirlar(text, sayac)
    return text, sayac


def normalize_parca(s):
    """Çapa ve alt yazı gibi kısa parçalar için metne uygulanan yazım ve başlık kuralları (korunan metin parçanın içinde aranır)."""
    sayac = Counter()
    s = _sub(re.compile(r"(?<=\w)’(?=\w)"), "'", s, sayac, "T1")
    for p, r, k in SAPKA:
        s = _sub(re.compile(p), r, s, sayac, k)
    return bolum_basliklari(s, sayac)
