#!/usr/bin/env python3
"""Steering taramasi: kaynaklari ortak mesaj modeline cevirir, maskeler, txt/json/html uretir,
uc bicimi geri okuyup tam metin ve aday eslesmelerini denetler.

Kullanim: python steering_donustur_tara.py --cikti <dizin> [--vm <dizin>]
Not: desen eslesmesi yonlendirme KANITI degildir; insan incelemesi gereken adaydir."""
import argparse, collections, glob, hashlib, html, json, os, re, sys, time
from html.parser import HTMLParser
from pathlib import Path

K = r'Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari'
ROL = ('user', 'assistant')

# ---------------------------------------------------------------- maskeleme
MASKE = [
    ('BEARER', re.compile(r'(?i)\bBearer\s+[A-Za-z0-9._\-]{12,}')),
    ('CEREZ-SATIRI', re.compile(r'''(?im)\b(?:cookie|set-cookie)\b["']?\s*[:=][^\r\n]+''')),
    ('GIZLI-ATAMA', re.compile(r'''(?i)\b(?:access[_-]?token|refresh[_-]?token|api[_-]?key|authorization|cookie|session[_-]?token|client[_-]?secret|password)\b["']?\s*[:=]\s*["']?[^\s"'<>;,}]+''')),
    ('IMZALI-URL', re.compile(r'(?i)[?&](?:sig|signature|token|key|access_token|x-amz-signature)=[^\s&#"<>]+')),
    ('E-POSTA', re.compile(r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}')),
    ('JWT', re.compile(r'\beyJ[\w\-]{8,}\.[\w\-]{8,}\.[\w\-]{8,}')),
    ('BELIRTEC', re.compile(r'\b(?:sk|pk|rk|ghp|gho|ghs|ghu|github_pat|xox[abp]|AIza|ya29)[\-_A-Za-z0-9.]{16,}')),
    ('UUID', re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b')),
    ('IPV4', re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')),
    ('IPV6', re.compile(r'\b(?:[0-9a-fA-F]{1,4}:){3,7}[0-9a-fA-F]{1,4}\b')),
    ('UZUN-DEGER', re.compile(r'\b(?![0-9a-f]{64}\b)[A-Za-z0-9+/_\-]{44,}={0,2}')),
]

def maskele(metin, sayac):
    for ad, rx in MASKE:
        metin, n = rx.subn('[' + ad + ']', metin)
        if n: sayac[ad] += n
    return metin

# ---------------------------------------------------------------- steering desenleri
def D(*p): return [re.compile(x, re.I | re.U) for x in p]
STEERING = collections.OrderedDict([
    ('ANT-B01', D(r'\b(?:option|seçenek|opsiyon)\s*(?:[ABC]|[0-9])\b', r'\bwhich\b.{0,30}\b(?:prefer|choose|pick)\b',
                  r'hangisini\s+(?:tercih|istersin|istiyorsun|seçersin|seçmek)', r'\b[AB]\s+mı\s+[AB]\s+mi\b',
                  r'(?:ister\s+misin|istersen)[^.\n]{0,120}\b(?:ya\s+da|yoksa|veya)\b',
                  r'\bwould\s+you\s+like\s+(?:me\s+)?to\b[^.?\n]{0,140}\bor\b')),
    ('ANT-B02', D(r"\b(?:great|excellent|fantastic|wonderful|good|sharp|insightful|fascinating|brilliant)\s+(?:question|point|catch|observation|idea|insight)\b",
                  r"\byou(?:'|’)?re\s+(?:absolutely|completely|totally|exactly|quite)\s+right\b",
                  r'\bharika\s+(?:bir\s+)?(?:soru|nokta|tespit|fikir|gözlem)', r'\b(?:çok\s+)?(?:doğru|yerinde|değerli|isabetli)\s+(?:bir\s+)?(?:tespit|soru|gözlem|nokta)\b',
                  r'\bkesinlikle\s+hakl[ıi](?:sın|sınız)', r'\bmükemmel\s+(?:bir\s+)?(?:soru|nokta|tespit)', r'\bçok\s+güzel\s+(?:bir\s+)?(?:soru|nokta|tespit)')),
    ('ANT-B03', D(r'\bas\s+an\s+ai\b', r"\bi(?:'|’)?m\s+(?:just\s+)?an?\s+(?:ai|language\s+model)\b",
                  r"\bi\s+(?:don(?:'|’)?t|do\s+not)\s+have\s+(?:personal\s+)?(?:feelings|opinions|emotions|experiences)",
                  r"\bi(?:'|’)?d\s+be\s+(?:happy|glad|delighted)\s+to\s+help\b", r'\bhope\s+this\s+helps\b', r'\blet\s+me\s+know\s+if\b', r'\bfeel\s+free\s+to\b',
                  r'\byapay\s+zeka\s+olarak\b', r'\byardımcı\s+olmaktan\s+(?:mutluluk|memnuniyet)', r'\bmemnuniyetle\s+yardımcı',
                  r'\bumarım\s+(?:bu\s+)?yardımcı\s+olur', r'\bsize\s+nasıl\s+yardımcı')),
    ('ANT-B04', D(r"\bi\s+can(?:'|’)?t\s+(?:help|assist|comply)\b", r"\bi(?:'|’)?m\s+(?:unable|not\s+able)\s+to\b",
                  r'\bagainst\s+(?:my|our)\s+(?:guidelines|polic(?:y|ies))\b', r"\bi(?:'|’)?m\s+sorry,?\s+(?:but|i\s+can)", r'\b(?:content|usage|safety)\s+polic(?:y|ies)\b',
                  r'\bbu\s+(?:konuda|isteğe|talebe)\s+yardımcı\s+olam', r'\b(?:politika|yönerge)(?:lar)?(?:ım|imiz|ımız)?\s+(?:gereği|nedeniyle|izin\s+vermiyor)',
                  r'\büzgünüm,?\s+(?:ancak|fakat|ama)\b', r'otomatik\s+onay\s+denetimi|yeterli\s+yetki\s+saymadı|kalıcı\s+kayıt\s+tamamlanmadı')),
])
TEKNIK = ['statsigPayload', 'feature_gates', 'dynamic_configs', 'layer_configs', 'can_record_session', 'WIZ_global_data', 'vendor-flags',
          'statsig_hashing_algorithm', 'isolated-segment', 'isRoutingExperimentParticipant', 'marketingEligibility', 'atis-latch',
          'serverClassifierRequest', 'api-request-blob', 'guardian_v2', 'auto_review', 'classifier_instructions']
DEUS = re.compile(r'deus[\s_\-]*ex[\s_\-]*machina', re.I)
KITAP = re.compile(r'\b(?:kitaplık|kitaplik|kütüphane|kutuphane|kitap(?:lar)?)\b', re.I)

def kelime(s): return len(s.split())

def tara(mesajlar):
    """mesajlar: [{i,rol,metin}] -> (sayac{(rol,kat)}, isabetler[], gosterge{})"""
    say = collections.Counter(); hits = []; kapanis = collections.Counter(); asist = 0
    for m in mesajlar:
        rol = m['rol']; t = m['metin']
        for kat, desenler in STEERING.items():
            for ix, rx in enumerate(desenler):
                for mm in rx.finditer(t):
                    say[(rol, kat)] += 1
                    s = max(0, mm.start() - 50); e = min(len(t), mm.end() + 50)
                    hits.append({'i': m['i'], 'rol': rol, 'kat': kat, 'desen': ix, 'parca': re.sub(r'\s+', ' ', t[s:e])})
        if rol == 'assistant':
            asist += 1
            son = [x for x in t.strip().splitlines() if x.strip()]
            if son and son[-1].rstrip().endswith('?'): kapanis['assistant_soru_ile_biter'] += 1
    return say, hits, {'assistant_mesaj': asist, 'assistant_soru_ile_biter': kapanis['assistant_soru_ile_biter']}

# ---------------------------------------------------------------- okuyucular
ROL_ISARET_KULLANICI = re.compile(r'^\s*(?:Şunu söylediniz:|You said:|Sen:|Siz:|Kullanıcı:|Human:)\s*$', re.I)
ROL_ISARET_ASISTAN = re.compile(r'^\s*(?:ChatGPT dedi:|ChatGPT said:|Claude:|Gemini:|Copilot:|Assistant:)\s*$', re.I)

def rolleri_ayir(satirlar):
    """Gorunur metin satirlarindan rol isaretleriyle mesaj uretir; isaret yoksa tek 'metin' mesaji."""
    mes = []; rol = 'metin'; tamp = []
    def kapat():
        nonlocal tamp
        if tamp and rol: mes.append({'rol': rol, 'metin': '\n'.join(tamp).strip()})
        tamp = []
    for s in satirlar:
        if ROL_ISARET_KULLANICI.match(s): kapat(); rol = 'user'; continue
        if ROL_ISARET_ASISTAN.match(s): kapat(); rol = 'assistant'; continue
        if rol: tamp.append(s)
    kapat()
    return mes

class GorunurHTML(HTMLParser):
    """DOM metni; CSS/layout, lazy-loading ve tam geçmiş doğrulanmaz."""
    ATLA = {'script', 'style', 'svg', 'noscript', 'head', 'template'}
    BLOK = {'p', 'div', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'tr', 'article', 'pre'}
    def __init__(self):
        super().__init__(convert_charrefs=True); self.parcalar=[]; self.atlanan=[]
    def handle_starttag(self, tag, attrs):
        if self.atlanan:
            if tag in self.ATLA: self.atlanan.append(tag)
        elif tag in self.ATLA: self.atlanan.append(tag)
        elif tag == 'br' or tag in self.BLOK: self.parcalar.append('\n')
    def handle_endtag(self, tag):
        if self.atlanan:
            if tag == self.atlanan[-1]: self.atlanan.pop()
        elif tag in self.BLOK: self.parcalar.append('\n')
    def handle_data(self, data):
        if not self.atlanan: self.parcalar.append(data)

def html_gorunur_satirlar(ham):
    p=GorunurHTML(); p.feed(ham); p.close()
    sat=[re.sub(r'[ \t\u00a0]+',' ',s).strip() for s in ''.join(p.parcalar).split('\n')]
    return [s for s in sat if s]

def metni_coz(data):
    if data.startswith((b'\xff\xfe', b'\xfe\xff')): return data.decode('utf-16'), 'utf-16-bom'
    if data.startswith(b'\xef\xbb\xbf'): return data.decode('utf-8-sig'), 'utf-8-bom'
    try: return data.decode('utf-8'), 'utf-8'
    except UnicodeDecodeError:
        m=re.search(br'charset\s*=\s*["\x27]?([\w-]+)', data[:4096], re.I)
        if not m: raise ValueError('Kodlama belirsiz; kayıplı decode uygulanmadı.')
        encoding=m[1].decode('ascii'); return data.decode(encoding), encoding

def html_mi(ham):
    return bool(re.match(r'\s*(?:<!--.*?-->\s*)*(?:<!doctype\s+html\b|<html\b)', ham, re.I|re.S))

def oku_html(yol):
    ham, _ = metni_coz(Path(yol).read_bytes())
    return rolleri_ayir(html_gorunur_satirlar(ham)), ham

def oku_txt(yol):
    ham, _ = metni_coz(Path(yol).read_bytes())
    if html_mi(ham): return rolleri_ayir(html_gorunur_satirlar(ham)), ham
    return rolleri_ayir([s.rstrip() for s in ham.splitlines() if s.strip()]), ham

def jsonl(yol):
    with open(yol, 'r', encoding='utf-8', errors='replace') as f:
        for l in f:
            try: yield json.loads(l)
            except Exception: continue

def oku_copilot(yol):
    mes = []
    for o in jsonl(yol):
        t = o.get('type'); d = o.get('data') or {}
        if t in ('user.message', 'assistant.message'):
            c = d.get('content')
            if isinstance(c, str) and c.strip():
                mes.append({'rol': 'user' if t == 'user.message' else 'assistant', 'metin': c, 'zaman': o.get('timestamp')})
    return mes

CTX = re.compile(r'^\s*(?:# AGENTS\.md|<environment_context>|<user_instructions>|<permissions|<INSTRUCTIONS>|<skills_instructions>|<collaboration_mode>)')
def oku_codex(yol):
    mes = []
    for o in jsonl(yol):
        if o.get('type') != 'response_item': continue
        p = o.get('payload') or {}
        if p.get('type') != 'message': continue
        if p.get('channel') not in (None, 'final', 'commentary'): continue
        if p.get('recipient') not in (None, 'all'): continue
        rol = p.get('role')
        if rol not in ROL: continue
        t = '\n'.join(b.get('text', '') for b in (p.get('content') or []) if isinstance(b, dict) and b.get('text'))
        if not t.strip(): continue
        if rol == 'user' and CTX.match(t): rol = 'context'
        mes.append({'rol': rol, 'metin': t, 'zaman': o.get('timestamp')})
    return mes

SR = re.compile(r'(?is)<system-reminder>.*?</system-reminder>')
def oku_claude(yol):
    mes = []
    for o in jsonl(yol):
        t = o.get('type')
        if t not in ROL or o.get('isMeta') or o.get('isSidechain'): continue
        c = (o.get('message') or {}).get('content')
        if isinstance(c, str): tx = c
        elif isinstance(c, list): tx = '\n'.join(b.get('text', '') for b in c if isinstance(b, dict) and b.get('type') == 'text')
        else: continue
        tx = SR.sub('', tx).strip()
        if not tx or tx.startswith(('<command-', '<local-command', 'Caveat:')): continue
        mes.append({'rol': t, 'metin': tx, 'zaman': o.get('timestamp')})
    return mes

def oku_gecmis(yol, tur):
    """Kullanici istem gecmisi (yalniz kullanici sozu)."""
    mes = []
    if tur == 'copilot-gecmis':
        j = json.load(open(yol, 'r', encoding='utf-8'))
        liste = j.get('commandHistory') or j.get('history') or next((v for v in j.values() if isinstance(v, list)), [])
        for x in liste: mes.append({'rol': 'user', 'metin': x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)})
    else:
        for o in jsonl(yol):
            t = o.get('display') or o.get('text') or ''
            if t.strip(): mes.append({'rol': 'user', 'metin': t, 'zaman': str(o.get('timestamp') or o.get('ts') or '')})
    return mes

# ---------------------------------------------------------------- yazicilar / geri okuyucular
BASLIK = re.compile(r'^=== \[(\d+)\] (\S+)(?: (.*))?$')

def txt_yaz(kaynak, mes):
    L = ['# kaynak: %s | katman: %s | tur: %s | sha256: %s | bayt: %d' % (kaynak['ad'], kaynak['katman'], kaynak['tur'], kaynak['sha256'], kaynak['bayt']), '']
    for m in mes:
        L.append('=== [%04d] %s %s' % (m['i'], m['rol'], m.get('zaman') or ''))
        L.extend('|' + x for x in m['metin'].split('\n'))
    return '\n'.join(L)

def txt_oku(s):
    mes = []; cur = None
    for x in s.split('\n'):
        b = BASLIK.match(x)
        if b:
            if cur: cur['metin'] = '\n'.join(cur['_t']); del cur['_t']; mes.append(cur)
            cur = {'i': int(b.group(1)), 'rol': b.group(2), 'zaman': b.group(3) or None, '_t': []}
        elif cur is not None and x.startswith('|'): cur['_t'].append(x[1:])
    if cur: cur['metin'] = '\n'.join(cur['_t']); del cur['_t']; mes.append(cur)
    return mes

def json_yaz(kaynak, mes):
    return json.dumps({'kaynak': kaynak, 'mesajlar': [{'i': m['i'], 'rol': m['rol'], 'zaman': m.get('zaman'), 'metin': m['metin']} for m in mes]}, ensure_ascii=False, indent=1)

def json_oku(s): return json.loads(s)['mesajlar']

def html_yaz(kaynak, mes):
    g = ['<!doctype html>', '<html lang="tr"><head><meta charset="utf-8"><title>%s</title>' % html.escape(kaynak['ad']),
         '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; base-uri \'none\'; form-action \'none\'">',
         '<style>body{font:14px/1.5 sans-serif;max-width:900px;margin:2em auto;padding:0 1em}article{border-top:1px solid #ccc;padding:.4em 0}h3{margin:.2em 0;font-size:12px;color:#555}pre{white-space:pre-wrap;word-wrap:break-word}</style>',
         '</head><body>', '<h1>%s</h1>' % html.escape(kaynak['ad']),
         '<p>katman: %s &middot; tür: %s &middot; sha256: %s &middot; bayt: %d</p>' % (html.escape(kaynak['katman']), html.escape(kaynak['tur']), kaynak['sha256'], kaynak['bayt'])]
    for m in mes:
        g.append('<article data-i="%d" data-rol="%s" data-zaman="%s"><h3>[%04d] %s %s</h3><pre>%s</pre></article>' % (m['i'], html.escape(m['rol']), html.escape(str(m.get('zaman') or '')), m['i'], html.escape(m['rol']), html.escape(str(m.get('zaman') or '')), html.escape(m['metin'])))
    g.append('</body></html>')
    return '\n'.join(g)

class _HP(HTMLParser):
    def __init__(s): super().__init__(convert_charrefs=True); s.mes = []; s.cur = None; s.pre = False
    def handle_starttag(s, tag, a):
        a = dict(a)
        if tag == 'article': s.cur = {'i': int(a.get('data-i', -1)), 'rol': a.get('data-rol', ''), 'zaman': a.get('data-zaman') or None, 'metin': ''}
        if tag == 'pre': s.pre = True
    def handle_endtag(s, tag):
        if tag == 'pre': s.pre = False
        if tag == 'article' and s.cur is not None: s.mes.append(s.cur); s.cur = None
    def handle_data(s, d):
        if s.cur is not None and s.pre: s.cur['metin'] += d

def html_oku(s): p = _HP(); p.feed(s); return p.mes

def html_statik_ihlal(s):
    k = s.lower()
    return [t for t in ('<script', '<link', '<img', '<iframe', '<object', '<embed', '<base', '<form', '<a ') if t in k]

# ---------------------------------------------------------------- ana is
def kaynak_listesi(vm):
    L = []
    Dn = r'X:\Users\Default\Downloads'; Ms = r'X:\Users\Default\Desktop'
    for ad, p in (('web_chatgpt_paylasim_sayfasi', Dn + r'\Yorumları ayrı sayfaya yazma.html'), ('web_chatgpt_bos_kabuk', Dn + r'\6acd2638-a63c-83ed-b994-7baf082ce616.htm')):
        if os.path.exists(p): L.append(('web', 'chatgpt-sayfa', ad, p))
    p = Ms + r'\yeni 1.txt'
    if os.path.exists(p): L.append(('web', 'masaustu-txt', 'web_masaustu_yeni1', p))
    for p in sorted(glob.glob(r'Y:\HalukAI\Ortak_Kopru\Aritilmis_Kaynaklar\*.md')):
        L.append(('web', 'aritilmis-md', 'web_aritilmis_' + re.sub(r'[^A-Za-z0-9]+', '_', os.path.basename(p))[:40], p))
    for p in sorted(glob.glob(K + r'\02_Copilot_Sahit\Home\.copilot\session-state\*\events.jsonl')):
        L.append(('sahit', 'copilot', 'sahit_copilot_' + os.path.basename(os.path.dirname(p))[:8], p))
    p = K + r'\02_Copilot_Sahit\Home\.copilot\command-history-state.json'
    if os.path.exists(p): L.append(('sahit', 'copilot-gecmis', 'sahit_istem_gecmisi', p))
    for p in sorted(glob.glob(K + r'\03_Codex_Saman\Home\.codex\sessions\*\*\*\*.jsonl')):
        L.append(('saman', 'codex', 'saman_codex_' + re.sub(r'^rollout-', '', os.path.basename(p))[:19], p))
    p = K + r'\03_Codex_Saman\Home\.codex\history.jsonl'
    if os.path.exists(p): L.append(('saman', 'codex-gecmis', 'saman_istem_gecmisi', p))
    if vm and os.path.isdir(vm):
        for p in sorted(glob.glob(os.path.join(vm, 'projects', '*', '*.jsonl'))):
            L.append(('hacker', 'claude', 'hacker_claude_' + os.path.basename(os.path.dirname(p))[-12:].strip('-') + '_' + os.path.basename(p)[:8], p))
        p = os.path.join(vm, 'history.jsonl')
        if os.path.exists(p): L.append(('hacker', 'claude-gecmis', 'hacker_istem_gecmisi', p))
    return L

def sha(yol):
    h = hashlib.sha256()
    with open(yol, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--cikti', required=True); ap.add_argument('--vm', default='')
    ap.add_argument('--kaynak-json', help='Açık liste: katman,tur,ad,yol; otomatik geçmiş taranmaz.')
    a = ap.parse_args()
    out = a.cikti
    for d in ('txt', 'json', 'html'): os.makedirs(os.path.join(out, d), exist_ok=True)
    ozet = []; tum_hits = {}; deus = []; kitap = []
    liste = [(x['katman'], x['tur'], x['ad'], x['yol']) for x in json.loads(Path(a.kaynak_json).read_text(encoding='utf-8-sig'))] if a.kaynak_json else kaynak_listesi(a.vm)
    adlar=[x[2] for x in liste]
    if len(adlar)!=len(set(adlar)) or any(not re.fullmatch(r'[\w-]+', ad) for ad in adlar): raise ValueError('Kaynak adları benzersiz ve basit dosya adları olmalı.')
    for katman, tur, ad, yol in liste:
        ham = None
        try:
            if tur == 'chatgpt-sayfa': mes, ham = oku_html(yol)
            elif tur in ('masaustu-txt', 'aritilmis-md', 'kayitli-metin', 'kitaplik-metni'): mes, ham = oku_txt(yol)
            elif tur == 'copilot': mes = oku_copilot(yol)
            elif tur == 'codex': mes = oku_codex(yol)
            elif tur == 'claude': mes = oku_claude(yol)
            else: mes = oku_gecmis(yol, tur)
        except Exception as e:
            ozet.append({'ad': ad, 'katman': katman, 'tur': tur, 'hata': repr(e)[:160]}); continue
        msay = collections.Counter(); sirali = []
        for m in mes:
            m['metin'] = maskele(m['metin'], msay)
            if m['rol'] == 'context' or not m['metin'].strip(): continue
            sirali.append(m)
        for i, m in enumerate(sirali): m['i'] = i + 1
        kaynak = {'ad': ad, 'katman': katman, 'tur': tur, 'dosya_adi': os.path.basename(yol), 'bayt': os.path.getsize(yol), 'sha256': sha(yol),
                  'mesaj': len(sirali), 'maske_sayilari': dict(msay)}
        kaynak['rol_atamasi'] = 'Görünür satır işaretleri; alıntı, arayüz ve gerçek konuşmacı ayrımı doğrulanmadı.' if ham is not None else 'Kaynak kayıt şeması; alıntı ve özgün söz ayrımı ayrıca okunmalı.'
        kaynak['tam_sohbet_dogrulandi'] = False
        kaynak['calisma_zamani_etkinligi_dogrulandi'] = False
        kaynak['tarihsel_yonergeler_veridir'] = True
        if ham is not None:
            _, kaynak['kodlama'] = metni_coz(Path(yol).read_bytes())
            kaynak['html_icerigi'] = html_mi(ham)
            kaynak['gosterim_donusumu'] = 'HTMLParser DOM metni; betik/stil/head/template/svg atlandı; boşluk/satırlar düzenlendi.' if kaynak['html_icerigi'] else 'Metin satırları; boş satırlar ve çevre boşlukları düzenlendi.'
        # teknik imzalar: ozgun ham iceriklerde
        ham_t = ham if ham is not None else None
        if ham_t is None and os.path.getsize(yol) < 40 * 1024 * 1024:
            ham_t, _ = metni_coz(Path(yol).read_bytes())
        kaynak['teknik_imza_ozgun'] = {s: ham_t.count(s) for s in TEKNIK if ham_t and ham_t.count(s)}
        kaynak['teknik_imza_yorumu'] = 'Kaynak içindeki düz dizgeler; alıntı/açıklama da eşleşebilir; etkinlik ölçümü değil.'
        if not sirali:
            kaynak['not'] = 'mesaj cikmadi'; ozet.append(kaynak); continue
        # uc bicim
        t_s = txt_yaz(kaynak, sirali); j_s = json_yaz(kaynak, sirali); h_s = html_yaz(kaynak, sirali)
        for dn, ext, s in (('txt', 'txt', t_s), ('json', 'json', j_s), ('html', 'html', h_s)):
            open(os.path.join(out, dn, ad + '.' + ext), 'w', encoding='utf-8', newline='\n').write(s)
        # bagimsiz tarama: her biciminden geri okuyup
        sonuc = {}
        for bicim, mm in (('txt', txt_oku(t_s)), ('json', json_oku(j_s)), ('html', html_oku(h_s))):
            say, hits, gos = tara(mm)
            ayni = [(m['i'],m['rol'],str(m.get('zaman') or ''),m['metin']) for m in mm] == [(m['i'],m['rol'],str(m.get('zaman') or ''),m['metin']) for m in sirali]
            sonuc[bicim] = {'mesaj': len(mm), 'tam_metin_ayni': ayni, 'sayac': {'%s|%s' % k: v for k, v in sorted(say.items())}, 'gosterge': gos}
            if bicim == 'json': tum_hits[ad] = hits
        sonuc['tutarli'] = all(sonuc[b]['tam_metin_ayni'] for b in ('txt','json','html')) and len({json.dumps(sonuc[b]['sayac'], sort_keys=True) for b in ('txt','json','html')}) == 1
        if not sonuc['tutarli']: raise ValueError('Üç biçim metin veya tarama bakımından tutarsız: '+ad)
        sonuc['html_statik_ihlal'] = html_statik_ihlal(h_s)
        sonuc['kelime'] = {r: sum(kelime(m['metin']) for m in sirali if m['rol'] == r) for r in {m['rol'] for m in sirali}}
        kaynak['tarama'] = sonuc
        ozet.append(kaynak)
        for m in sirali:
            if DEUS.search(m['metin']): deus.append((katman, ad, m))
            if m['rol'] == 'user' and KITAP.search(m['metin']): kitap.append((katman, ad, m))
    json.dump(ozet, open(os.path.join(out, 'ozet.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(tum_hits, open(os.path.join(out, 'isabetler.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # deus_ex_machina dizini
    D_ = collections.defaultdict(lambda: collections.Counter()); ozg = collections.defaultdict(list)
    for katman, ad, m in deus:
        D_[katman][m['rol']] += 1
        if m['rol'] == 'user' and len(ozg[katman]) < 40: ozg[katman].append((ad, m['i'], m.get('zaman') or '', re.sub(r'\s+', ' ', m['metin'])[:500]))
    K_ = collections.defaultdict(lambda: collections.Counter())
    for katman, ad, m in kitap: K_[katman][m['rol']] += 1
    with open(os.path.join(out, 'deus_ex_machina_dizin.json'), 'w', encoding='utf-8') as f:
        json.dump({'deus_ex_machina_anma': {k: dict(v) for k, v in D_.items()}, 'kitaplik_kutuphane_kitap_anma_kullanici': {k: dict(v) for k, v in K_.items()},
                   'ozgun_kullanici_sozu': {k: [{'kaynak': a1, 'mesaj_i': i, 'zaman': z, 'metin': t} for a1, i, z, t in v] for k, v in ozg.items()}}, f, ensure_ascii=False, indent=1)
    print('kaynak:', len(ozet), 'hatali:', sum(1 for o in ozet if 'hata' in o), 'tutarsiz:', sum(1 for o in ozet if o.get('tarama') and not o['tarama']['tutarli']))

if __name__ == '__main__':
    main()
