#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sina.py -- oran.exe, 128.exe, yuva.exe ve cevrim.exe sinamasi.

Her arac icin bu dosyada, aractan bagimsiz yazilmis bir model vardir.
Sinama uc seyi karsilastirir: elle yazilmis beklenenler, model, arac.

  Linux  : python3 -B sina.py                 (makine kodu kos2 ile, gercek islemcide)
           python3 -B sina.py --wine          (.exe Wine altinda)
  Windows: python -B sina.py                  (.exe dogrudan)
Secenekler: --klasor DIZIN (exe'lerin yeri)   --kos YOL (kos2)
            --isyuku DOSYA (is yuku programlari ve yayimlanmis degerler; yoksa o denetimler atlanir;
                            bu dosyanin yaninda isyuku.json varsa kendiliginden okunur)
            --izler DIZIN  (yayimlanmis adim adim izlerin klasoru; yoksa atlanir)
            oran | 128 | yuva | cevrim | betikler  (yalniz secilenler; betikler: yeni_gidis.cmd ve
                            geri_donus.cmd, yalniz Windows'ta ya da --wine ile)
Cikti ASCII'dir; ayrica exe'lerin yanindaki sina_sonucu.txt dosyasina yazilir.
"""
import json
import os
import random
import re
import struct
import subprocess
import sys
import tempfile

WIN = os.name == 'nt'
BURASI = os.path.dirname(os.path.abspath(__file__))
SEC = {'klasor': BURASI, 'kos': os.path.join(BURASI, 'kos2'), 'wine': False, 'isyuku': None, 'izler': None}
satirlar = []


def yaz(x):
    satirlar.append(x)
    print(x)
    sys.stdout.flush()
gecti = kaldi = 0
bilgi = []


def denet(ad, kosul, ayrinti=''):
    global gecti, kaldi
    if kosul:
        gecti += 1
        yaz('  GECTI  ' + ad)
    else:
        kaldi += 1
        yaz('  KALDI  ' + ad + ('  ' + ayrinti if ayrinti else ''))


def kos(ad, girdi=b'', ortam=None, ikinci=False):
    """Araci calistirir; (cikti baytlari, cikis kodu) verir. ikinci=True ise ikinci cikis (stderr) da gelir."""
    exe = os.path.join(SEC['klasor'], ad)
    if WIN:
        komut = [exe]
    elif SEC['wine']:
        komut = ['wine', exe]
    else:
        komut = [SEC['kos'], exe]
    e = dict(os.environ)
    e.update(ortam or {})
    if SEC['wine']:
        e['WINEDEBUG'] = '-all'
    r = subprocess.run(komut, input=girdi, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                       env=e, timeout=300)
    if ikinci:
        return r.stdout, r.stderr, r.returncode & (0xFFFFFFFF if WIN else 0xFF)
    return r.stdout, r.returncode & (0xFFFFFFFF if WIN else 0xFF)


def adet_sec(linux, windows, wine):
    """Rastgele denemelerin adedi: Linux'ta (kos2) en cok, Wine altinda en az (Wine her kosuda yavas acilir)."""
    return wine if SEC['wine'] else windows if WIN else linux


def kod_esit(gercek, beklenen):
    return gercek == (beklenen & (0xFFFFFFFF if WIN else 0xFF))


# ============================================================ oran
SON63 = (1 << 63) - 1
RAKAM = b'0123456789'


def _isaretli(veri, bas):
    """bas'ta baslayan rakam dizisinin onundeki isaret gecerliyse onu verir (b'-' / b'+'), yoksa None."""
    j = bas
    while j > 0 and veri[j - 1] in b'+-':
        j -= 1
    k = bas - j
    onceki_rakam = 1 if (j > 0 and veri[j - 1] in RAKAM) else 0
    return veri[bas - 1:bas] if (k - onceki_rakam) % 2 == 1 else None


def oran_model(veri):
    diziler = list(re.finditer(rb'[0-9]+', veri))
    if len(diziler) < 2:
        return b'', 0
    sargi, eksi = [], 0
    for m in diziler[:2]:
        r = m.group()
        gecerli = len(r) <= 20 and int(r) <= SON63
        sargi.append(int(r) if gecerli else None)
        if gecerli and _isaretli(veri, m.start()) == b'-':
            eksi ^= 1
    a, b = sargi
    if a is None or b is None:
        a, b = 0, 0
    p = diziler[1].end()
    while p < len(veri) and veri[p] <= 0x20:
        p += 1
    akis = veri[p:]
    cikti, son, kalan = bytearray(), 0, 0
    for m in re.finditer(rb'[0-9]+', akis):
        r = m.group()
        isr = _isaretli(akis, m.start())
        bas = m.start() - (1 if isr else 0)
        yeni = None
        if len(r) <= 20 and int(r) <= SON63 and a != 0:
            pay = int(r) * b
            if pay % a == 0 and pay // a <= SON63:
                q = pay // a
                neg = eksi ^ (1 if isr == b'-' else 0)
                yeni = (b'-' if (neg and q) else b'') + str(q).encode()
        cikti += akis[son:bas]
        if yeni is None:
            kalan += 1
            cikti += akis[bas:m.end()]
        else:
            cikti += yeni
        son = m.end()
    cikti += akis[son:]
    return bytes(cikti), kalan


ORAN_ELLE = [
    (b'8 1 128', b'16', 0),
    (b'8 1 128 bit\r\n', b'16 bit\r\n', 0),
    (b'1 8 16', b'128', 0),
    (b'8 1 12', b'12', 1),
    (b'8 1\r\n128\r\n64\r\n', b'16\r\n8\r\n', 0),
    (b'8 1\r\n\r\n   128\r\n', b'16\r\n', 0),
    (b'1 1073741824 16', b'17179869184', 0),
    (b'1 8 17179869184', b'137438953472', 0),
    (b'64 1 128', b'2', 0),
    (b'1 2 64', b'128', 0),
    (b'-1 1 5 -7 0', b'-5 7 0', 0),
    (b'1 -1 -0', b'0', 0),
    (b'-1 -1 -3', b'-3', 0),
    (b'3 2 9 10 -6', b'6 10 -4', 1),
    (b'0 5 7', b'7', 1),
    (b'5 0 7 -3', b'0 0', 0),
    (b'1 1 9223372036854775807', b'9223372036854775807', 0),
    (b'1 2 9223372036854775807', b'9223372036854775807', 1),
    (b'2 1 9223372036854775807', b'9223372036854775807', 1),
    (b'1 1 9223372036854775808', b'9223372036854775808', 1),
    (b'9223372036854775807 9223372036854775807 5', b'5', 0),
    (b'oran 8:1 128', b'16', 0),
    (b'8 1x128', b'x16', 0),
    (b'8 1-16', b'-2', 0),
    (b'8 1 ', b'', 0),
    (b'8', b'', 0),
    (b'', b'', 0),
    (b'8 1 a 16 b 24 c 3', b'a 2 b 3 c 3', 1),
    (b'1000 1024 1024000', b'1048576', 0),
    (b'8 1 +16', b'2', 0),
    (b'8 1 5-16', b'5-2', 1),
    (b'8 1 --16', b'--2', 0),
    (b'99999999999999999999999 1 5', b'5', 1),
    (b'1 99999999999999999999999 5 6', b'5 6', 2),
    (b'2 1 007', b'007', 1),
    (b'1 1 007', b'7', 0),
    (b'8 1 16,24;32\t40', b'2,3;4\t5', 0),
    (b'1 33 2 token', b'66 token', 0),
]


def oran_rastgele(rs):
    ilginc = [0, 1, 2, 3, 7, 8, 10, 33, 64, 128, 1000, 1024, 1 << 30, SON63, SON63 + 1, 10 ** 22]
    ayrac = [b' ', b' ', b'\r\n', b'\t', b':', b'/', b', ', b' x ', b'-', b'+', b'--', b' -', b' +', b'']

    def sayi(a):
        t = rs.random()
        if t < 0.35:
            v = rs.randrange(0, 200)
        elif t < 0.6:
            v = (a or 1) * rs.randrange(0, 10 ** rs.randrange(1, 12))
        elif t < 0.75:
            v = rs.choice(ilginc)
        elif t < 0.9:
            v = rs.randrange(0, 1 << rs.randrange(1, 70))
        else:
            v = SON63 - rs.randrange(0, 3)
        s = str(v)
        if rs.random() < 0.1:
            s = '0' * rs.randrange(1, 4) + s
        return rs.choice(['', '', '', '-', '+']).encode() + s.encode()

    a = rs.choice(ilginc) if rs.random() < 0.5 else rs.randrange(1, 100)
    b = rs.choice(ilginc) if rs.random() < 0.5 else rs.randrange(0, 100)
    p = rs.choice([b'', b'', b'ab ', b'- ', b'\r\n'])
    p += rs.choice([b'', b'-', b'+']) + str(a).encode() + rs.choice(ayrac[:9] + [b' -', b' +'])
    p += str(b).encode()
    p += rs.choice([b' ', b' ', b'\r\n', b'\r\n\r\n ', b'x', b'-', b'', b'\t '])
    for _ in range(rs.randrange(0, 12)):
        p += sayi(a) + rs.choice(ayrac)
    if rs.random() < 0.15:
        p = p[:rs.randrange(0, len(p) + 1)]
    return p


def sina_oran():
    yaz('oran.exe')
    for g, c, k in ORAN_ELLE:
        mc, mk = oran_model(g)
        ac, ak = kos('oran.exe', g)
        denet('elle %r' % g, mc == c and mk == k and ac == c and kod_esit(ak, k),
              'beklenen %r/%d model %r/%d arac %r/%d' % (c, k, mc, mk, ac, ak))
    rs = random.Random(128)
    adet = adet_sec(3000, 400, 40)
    hata = None
    donusen = donusmeyen = 0
    for _ in range(adet):
        g = oran_rastgele(rs)
        mc, mk = oran_model(g)
        ac, ak = kos('oran.exe', g)
        donusmeyen += mk
        donusen += len(re.findall(rb'[0-9]+', mc)) - mk if mc else 0
        if ac != mc or not kod_esit(ak, mk):
            hata = 'girdi %r model %r/%d arac %r/%d' % (g, mc, mk, ac, ak)
            break
    denet('rastgele %d akis: arac = model' % adet, hata is None, hata or '')
    bilgi.append('oran rastgele: donusen sayi %d, donusmeden gecen %d' % (donusen, donusmeyen))
    # gidis-donus: donusen her sayi, sargilar yer degistirince geri gelir
    hata = None
    for _ in range(adet_sec(300, 60, 10)):
        a, b = rs.randrange(1, 5000), rs.randrange(1, 5000)
        xs = [a * rs.randrange(-10 ** 9, 10 ** 9) for _ in range(5)]
        gidis, k1 = kos('oran.exe', ('%d %d\n' % (a, b)).encode() + ' '.join(map(str, xs)).encode())
        donus, k2 = kos('oran.exe', ('%d %d\n' % (b, a)).encode() + gidis)
        if k1 or k2 or donus != ' '.join(map(str, xs)).encode():
            hata = 'a=%d b=%d xs=%r gidis=%r donus=%r' % (a, b, xs, gidis, donus)
            break
    denet('gidis-donus: (a b) ile giden, (b a) ile geri gelir', hata is None, hata or '')
    if not WIN and not SEC['wine']:
        g = b'8 1 ' + b' '.join(str(8 * i).encode() for i in range(50))
        c1, k1 = kos('oran.exe', g, {'ZOR': '1'})
        denet('ZOR: korunmayan yazmaclar bozulunca sonuc ayni', (c1, k1) == oran_model(g))
        c1, k1 = kos('oran.exe', g, {'YAZ_KES': '3'})
        denet('cikis ucu kapaninca arac durur', len(c1) < len(oran_model(g)[0]))


# ============================================================ 128
M128 = (1 << 128) - 1
ADIM_SINIRI = 100000
KOMUT = {'LD': 1, 'ST': 2, 'ADD': 3, 'AND': 4, 'XOR': 5, 'SHL': 6, 'JZ': 7, 'HALT': 8}


def kodla(k):
    """Acik alanli komut kaydini 5 haneli koda cevirir."""
    op = k['op']
    if op in ('LD',):
        return 0x10000 | k['rd'] << 12 | k['a8']
    if op == 'ST':
        return 0x20000 | k['rs'] << 12 | k['a8']
    if op in ('ADD', 'AND', 'XOR'):
        return KOMUT[op] << 16 | k['rd'] << 12 | k['ra'] << 8 | k['rb']
    if op == 'SHL':
        return 0x60000 | k['rd'] << 12 | k['ra'] << 8 | k['k8']
    if op == 'JZ':
        return 0x70000 | k['ra'] << 12 | k['a8']
    if op == 'HALT':
        return 0x80000
    raise ValueError(op)


def m128_yukle(veri):
    """Girdi metnini {yer: deger} sozlugune cevirir; reddedilirse None."""
    metin = re.sub(rb';[^\n]*', b' ', veri)
    sayilar = []
    for m in re.finditer(rb'[0-9a-fA-FxX]+', metin):
        parcalar = re.split(rb'[xX]', m.group())
        if not any(parcalar):
            continue                                    # yalniz x: sayi degil
        for p in parcalar:
            if p and int(p, 16) > M128:
                return None
        sayilar.append(int(parcalar[-1], 16) if parcalar[-1] else 0)
    if len(sayilar) % 2:
        return None
    bellek = {}
    for yer, deger in zip(sayilar[0::2], sayilar[1::2]):
        if yer > 0x1FF or yer in bellek:
            return None
        bellek[yer] = deger
    return bellek


class Makine:
    def __init__(self, bellek):
        self.M = [bellek.get(i, 0) for i in range(256)]
        self.P = [bellek.get(0x100 + i, 0) for i in range(256)]
        self.R = [0, 0, 0, 0]
        self.pc = 0
        self.adim_sayisi = 0
        self.kod = None                                 # 0 durdu, 1 hata, 2 sinir

    def adim(self):
        """Bir adim. (pc, sonraki_pc, degisim) verir; degisim ('R'|'M', dizin, yeni) ya da None."""
        if self.adim_sayisi >= ADIM_SINIRI:
            self.kod = 2
            return None
        self.adim_sayisi += 1
        pc, c = self.pc, self.P[self.pc]
        op, f1, f2, x = c >> 16, (c >> 12) & 15, (c >> 8) & 15, c & 255
        R, M = self.R, self.M
        gecerli = c <= 0xFFFFF and 1 <= op <= 8 and f1 <= 3 and f2 <= 3
        if gecerli and op in (1, 2, 7):
            gecerli = f2 == 0
        if gecerli and op in (3, 4, 5):
            gecerli = x <= 3
        if gecerli and op == 8:
            gecerli = c == 0x80000
        if not gecerli:
            self.kod = 1
            return (pc, pc, None)
        sonraki, degisim = (pc + 1) % 256, None
        if op == 1:
            degisim = ('R', f1, M[x])
        elif op == 2:
            degisim = ('M', x, R[f1])
        elif op == 3:
            degisim = ('R', f1, (R[f2] + R[x]) & M128)
        elif op == 4:
            degisim = ('R', f1, R[f2] & R[x])
        elif op == 5:
            degisim = ('R', f1, R[f2] ^ R[x])
        elif op == 6:
            degisim = ('R', f1, 0 if x >= 128 else (R[f2] << x) & M128)
        elif op == 7:
            if R[f1] == 0:
                sonraki = x
        else:
            self.kod = 0
            sonraki = pc
        if degisim:
            (R if degisim[0] == 'R' else M)[degisim[1]] = degisim[2]
        self.pc = sonraki
        return (pc, sonraki, degisim)

    def kos(self):
        while self.kod is None:
            self.adim()
        return self

    def cikti(self):
        s = ['%03x %032x' % (i, v) for i, v in enumerate(self.M) if v]
        s += ['%03x %032x' % (0x200 + i, v) for i, v in enumerate(self.R)]
        s += ['204 %032x' % self.pc, '205 %032x' % self.adim_sayisi]
        return ''.join(x + '\r\n' for x in s).encode()


def m128_model(veri):
    bellek = m128_yukle(veri)
    if bellek is None:
        return b'', 3
    m = Makine(bellek).kos()
    return m.cikti(), m.kod


def m128_metin(bellek, rs=None):
    """{yer: deger} sozlugunu girdi metnine cevirir; rs verilirse yazim rastgele cesitlenir."""
    s = []
    for yer, deger in bellek.items():
        if rs is None:
            s.append('%03x %x\r\n' % (yer, deger))
            continue
        a = rs.choice(['%x', '%X', '%03x', '0x%x', '0X%X', '%05x']) % yer
        b = rs.choice(['%x', '%X', '%032x', '0x%x', '0x%032X', '%040x']) % deger
        s.append(a + rs.choice([' ', '\t', ', ', ' = ', '\r\n']) + b +
                 rs.choice(['\r\n', '\n', ' ', ' ; aciklama: abc 123\r\n', ';\n', '\r\n\r\n']))
    return ''.join(s).encode()


def isyuku_oku():
    """Is yuku dosyasi: programlar (acik alanli komut kayitlari), veriler ve yayimlanmis degerler."""
    yol = SEC['isyuku'] or os.path.join(BURASI, 'isyuku.json')
    if not os.path.exists(yol):
        return None
    with open(yol, encoding='utf-8') as f:
        return json.load(f)


def program(kayitlar, veri):
    b = dict(veri)
    for i, k in enumerate(kayitlar):
        b[0x100 + i] = kodla(k)
    return b


def say_girdisi(y, x):
    veri = {int(k): int(v, 16) for k, v in y['sabitler'].items()}
    veri[0] = x
    return program(y['say'], veri)


def m128_rastgele(rs):
    b = {}
    for _ in range(rs.randrange(0, 12)):
        b[rs.randrange(0, 256)] = rs.choice([0, 1, M128, 1 << 127, (1 << 64) - 1, 1 << 64,
                                              rs.getrandbits(128), rs.getrandbits(64)])
    n = rs.randrange(1, 40)
    for i in range(n):
        yer = 0x100 + (i if rs.random() < 0.9 else rs.randrange(0, 256))
        t = rs.random()
        r = lambda: rs.randrange(0, 4)
        a8 = lambda: rs.choice(list(b)[:8] + [rs.randrange(0, 256)]) & 255 if b else rs.randrange(0, 256)
        if t < 0.2:
            c = 0x10000 | r() << 12 | a8()
        elif t < 0.32:
            c = 0x20000 | r() << 12 | a8()
        elif t < 0.62:
            c = rs.choice([3, 4, 5]) << 16 | r() << 12 | r() << 8 | r()
        elif t < 0.77:
            c = 0x60000 | r() << 12 | r() << 8 | rs.choice([0, 1, 4, 63, 64, 65, 127, 128, 200, 255,
                                                             rs.randrange(0, 256)])
        elif t < 0.87:
            c = 0x70000 | r() << 12 | rs.choice([rs.randrange(0, n + 2), rs.randrange(0, 256)])
        elif t < 0.93:
            c = 0x80000
        else:
            c = rs.choice([0, 0x90000, 0x14000, 0x10100, 0x30004, 0x80001, 0x100000, 0xF0000,
                           rs.getrandbits(20), rs.getrandbits(24), rs.getrandbits(128)])
        b[yer] = c
    if rs.random() < 0.6:
        b[0x100 + n] = 0x80000
    return b


def sina_128():
    yaz('128.exe')
    y = isyuku_oku()
    if y is None:
        bilgi.append('128: is yuku dosyasi (isyuku.json) yok; yayimlanmis degerlerle karsilastirma atlandi')
    else:
        veri = {int(k): int(v, 16) for k, v in y['veri'].items()}
        g = m128_metin(program(y['kesisim_fark'], veri))
        ac, ak = kos('128.exe', g)
        satir = dict(l.split() for l in ac.decode().splitlines())
        bek = y['kesisim_sonucu']
        denet('ilk is yuku: kesisim, simetrik fark, birlesim yayimlanan degerlerle ayni (%d adim)' % bek['adim'],
              ak == 0 and (ac, ak) == m128_model(g) and int(satir['205'], 16) == bek['adim']
              and all(int(satir.get('%03x' % int(a), '0'), 16) == int(v, 16) for a, v in bek['bellek'].items()),
              repr(ac[:200]))
        for ad, d in y['yayim'].items():
            x = int(d['girdi'], 16)
            ac, ak = kos('128.exe', m128_metin(say_girdisi(y, x)))
            m = Makine(say_girdisi(y, x)).kos()
            satir = dict(l.split() for l in ac.decode().splitlines())
            denet('sayim %-13s: %d bit, %d adim (yayimlanan degerler)' % (ad, d['bit'], d['adim']),
                  ak == 0 and int(satir.get('001', '0'), 16) == d['bit'] and int(satir['205'], 16) == d['adim']
                  and m.M[1] == d['bit'] and m.adim_sayisi == d['adim'] and ac == m.cikti(), repr(ac[-90:]))
    ELLE = [
        (b'', b'200 %s\r\n201 %s\r\n202 %s\r\n203 %s\r\n204 %s\r\n205 %s\r\n' % (
            (b'0' * 32,) * 5 + (b'0' * 31 + b'1',)), 1),
        (b'100 80000', None, 0), (b'100', b'', 3), (b'200 1', b'', 3), (b'1 2 1 3', b'', 3),
        (b'0 100000000000000000000000000000000', b'', 3),
        (b'0 0x0000000000ffffffffffffffffffffffffffffffff 100 80000', None, 0),
        (b'; aciklama: abc 123\r\n0X0A 0XFF ; q\n100 80000', None, 0),
        (b'100 70000', None, 2), (b'100 90000', None, 1), (b'100 14000', None, 1),
        (b'100 10100', None, 1), (b'100 30004', None, 1), (b'100 80001', None, 1),
        (b'100 100000', None, 1), (b'100 0', None, 1), (b'x 100 x80000', None, 0),
        (b'0 1 100 10000 101 6107f 102 62080 103 63040 104 21001 105 22002 106 23003 107 80000',
         b'000 %s\r\n001 %s\r\n003 %s\r\n200 %s\r\n201 %s\r\n202 %s\r\n203 %s\r\n204 %s\r\n205 %s\r\n' % (
             b'0' * 31 + b'1', b'8' + b'0' * 31, b'0' * 15 + b'1' + b'0' * 16, b'0' * 31 + b'1',
             b'8' + b'0' * 31, b'0' * 32, b'0' * 15 + b'1' + b'0' * 16, b'0' * 31 + b'7',
             b'0' * 31 + b'8'), 0),
        (b'0 ffffffffffffffff 1 1 2 ffffffffffffffffffffffffffffffff '
         b'100 10000 101 11001 102 32001 103 13002 104 33301 105 22005 106 23006 107 80000',
         None, 0),
        (b'1ff 10005 5 7 100 80000 0 0 101 70000', None, 0),
    ]
    for g, c, k in ELLE:
        mc, mk = m128_model(g)
        ac, ak = kos('128.exe', g)
        denet('elle %r' % g[:60], mk == k and ak == k and ac == mc and (c is None or ac == c),
              'beklenen kod %d model %d arac %d cikti %r' % (k, mk, ak, ac[:80]))
    mc, _ = m128_model(ELLE[-2][0])
    denet('toplamada elde alt yaridan uste gecer; 2^128 tasmasi 0 verir',
          b'005 00000000000000010000000000000000\r\n' in mc and b'\r\n006 ' not in mc
          and b'203 ' + b'0' * 32 in mc, repr(mc))
    mc, _ = m128_model(ELLE[-1][0])
    denet('PC 255 ten 0 a sarar (JZ ile 0 a donup 255. yuvayi kosar)', b'204 ' + b'0' * 30 + b'00' in mc)
    rs = random.Random(1280)
    adet = adet_sec(2500, 300, 30)
    hata, kodlar, adimlar = None, {0: 0, 1: 0, 2: 0, 3: 0}, 0
    for i in range(adet):
        b = m128_rastgele(rs)
        g = m128_metin(b, rs)
        if rs.random() < 0.06:
            g += rs.choice([b' 1', b'\r\n300 5\r\n', b' 0 0 0 0', b' 5 1' + b'0' * 32, b'zz 12 fx'])
        mc, mk = m128_model(g)
        ac, ak = kos('128.exe', g)
        kodlar[mk] += 1
        if mk != 3:
            adimlar += int(mc.decode().splitlines()[-1].split()[1], 16)
        if ac != mc or ak != mk:
            hata = 'girdi %r model %d arac %d\n%r\n%r' % (g, mk, ak, mc[-200:], ac[-200:])
            break
    denet('rastgele %d program: arac = model' % adet, hata is None, hata or '')
    bilgi.append('128 rastgele: durdu %d, hata %d, sinir %d, reddedildi %d; toplam %d adim'
                 % (kodlar[0], kodlar[1], kodlar[2], kodlar[3], adimlar))
    if not WIN and not SEC['wine']:
        rs = random.Random(5)
        hata = None
        for _ in range(40):
            g = m128_metin(m128_rastgele(rs))
            if kos('128.exe', g, {'ZOR': '1'}) != m128_model(g):
                hata = repr(g)
                break
        denet('ZOR: korunmayan yazmaclar bozulunca sonuc ayni (40 program)', hata is None, hata or '')
    if SEC['izler'] and y is not None:
        sina_izler(SEC['izler'], y)


def sina_izler(dizin, y):
    """Yayimlanmis adim adim izleri (iz_*.jsonl) bu dosyadaki modelle karsilastirir."""
    def oku(ad):
        with open(os.path.join(dizin, ad), encoding='utf-8') as f:
            return f.read()
    veri = {int(k): int(v, 16) for k, v in y['veri'].items()}
    sabit = {int(k): int(v, 16) for k, v in y['sabitler'].items()}
    isler = [('kesisim_fark', y['kesisim_fark'], veri)]
    for ad, d in y['yayim'].items():
        v = dict(sabit)
        v[0] = int(d['girdi'], 16)
        isler.append(('sayim_' + ad, y['say'], v))
    toplam = 0
    for ad, kayitlar, v in isler:
        m = Makine(program(kayitlar, v))
        hata = None
        izler = oku('iz_%s.jsonl' % ad).splitlines()
        for satir in izler:
            iz = json.loads(satir)
            if kodla(iz['komut']) != m.P[m.pc]:
                hata = 'adim %d: komut farkli' % iz['adim']
                break
            pc, sonraki, d = m.adim()
            bek = None
            if 'degisim' in iz:
                (yer, (_, yeni)), = iz['degisim'].items()
                bek = ('R', int(yer[1:]), int(yeni, 16)) if yer[0] == 'R' else ('M', int(yer[2:-1]), int(yeni, 16))
            if (pc, sonraki, d) != (iz['pc'], iz['sonraki_pc'], bek) or m.adim_sayisi != iz['adim']:
                hata = 'adim %d: model %r iz %r' % (iz['adim'], (pc, sonraki, d), (iz['pc'], iz['sonraki_pc'], bek))
                break
        toplam += len(izler)
        denet('yayimlanan iz %-22s: %4d adim, model her adimda ayni' % (ad, len(izler)),
              hata is None and m.kod == 0, hata or 'durmadi')
    bilgi.append('128 yayimlanan izler: %d adim karsilastirildi' % toplam)


# ============================================================ yuva
def yuva_model(blob):
    if blob is None or len(blob) < 8 or len(blob) > 0x100000:
        return b'', 1
    boy = struct.unpack_from('<I', blob, 4)[0]
    if boy > len(blob) - 8:
        return b'', 1
    t, p, cikti = blob[8:8 + boy], 0, b''
    while p + 4 <= len(t):
        tur, L = t[p], t[p + 1]
        if L < 4 or p + L > len(t):
            break
        if tur == 17 and L >= 0x0E:
            genislik, boyut = struct.unpack_from('<HH', t, p + 0x0A)
            if boyut == 0:
                bayt, genislik = 0, 0
            elif boyut == 0xFFFF:
                bayt = None
            elif boyut == 0x7FFF:
                bayt = (struct.unpack_from('<I', t, p + 0x1C)[0] & 0x7FFFFFFF) << 20 if L >= 0x20 else None
            elif boyut & 0x8000:
                bayt = (boyut & 0x7FFF) << 10
            else:
                bayt = boyut << 20
            cikti += b'%s %s\r\n' % (b'?' if bayt is None else b'%d' % bayt,
                                    b'?' if genislik == 0xFFFF else b'%d' % genislik)
        if tur == 127:
            break
        q = p + L
        while q + 2 <= len(t) and (t[q] or t[q + 1]):
            q += 1
        if q + 2 > len(t):
            break
        p = q + 2
    return cikti, 0


def yapi(tur, govde, yazilar=()):
    """SMBIOS yapisi: baslik (tur, boy, tutamac) + govde + yazilar + cift 0."""
    y = bytes([tur, 4 + len(govde), 0, 0]) + govde
    y += b''.join(s + b'\0' for s in yazilar) + (b'\0' if yazilar else b'\0\0')
    return y


def yuva17(boyut, genislik=64, boy=0x54, genis=0):
    g = bytearray(boy - 4)
    struct.pack_into('<HH', g, 0x0A - 4, genislik, boyut)
    if boy >= 0x20:
        struct.pack_into('<I', g, 0x1C - 4, genis)
    return yapi(17, bytes(g), (b'Yuva 1', b'BANK 0', b'Uretici', b'PARCA-NO-16G'))


def rsmb(tablo):
    return bytes([0, 3, 3, 0]) + struct.pack('<I', len(tablo)) + tablo


def sina_yuva():
    yaz('yuva.exe')
    if WIN:
        import ctypes
        k32 = ctypes.windll.kernel32
        k32.GetSystemFirmwareTable.restype = ctypes.c_uint
        gerek = k32.GetSystemFirmwareTable(0x52534D42, 0, None, 0)
        tampon = ctypes.create_string_buffer(max(gerek, 8))
        alinan = k32.GetSystemFirmwareTable(0x52534D42, 0, tampon, gerek)
        blob = tampon.raw[:alinan] if alinan else None
        mc, mk = yuva_model(blob)
        ac, ak = kos('yuva.exe')
        denet('bu makinenin kaydi: arac = model (%d satir)' % len(mc.splitlines()),
              (ac, ak) == (mc, mk), 'model %r/%d arac %r/%d' % (mc, mk, ac, ak))
        bilgi.append('yuva bu makinede: ' + ' | '.join(ac.decode().split('\r\n')[:-1]) + ' (kod %d)' % ak)
        try:
            r = subprocess.run(['powershell', '-NoProfile', '-Command',
                                '(Get-CimInstance Win32_PhysicalMemory | ForEach-Object { "$($_.Capacity):$($_.DataWidth)" }) -join " "'],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL, timeout=120)
            wmi = sorted(tuple(x.split(':')) for x in r.stdout.decode().split())
            bizim = sorted(tuple(l.split()) for l in ac.decode().splitlines() if l.split()[0] not in ('0', '?'))
            denet('Windows un kendi sayimi (Win32_PhysicalMemory) ile ayni boylar: %r' % ([x[0] for x in wmi],),
                  wmi != [] and [x[0] for x in wmi] == [x[0] for x in bizim], 'arac %r' % (bizim,))
            bilgi.append('yuva: Windows un bildirdigi (boy, veri genisligi) %r; aracin bildirdigi %r' % (wmi, bizim))
        except Exception as e:                      # WMI yoksa bilgi olarak kalir
            bilgi.append('yuva: WMI ile karsilastirilamadi (%s)' % type(e).__name__)
        return
    if SEC['wine']:
        ac, ak = kos('yuva.exe')
        bilgi.append('yuva Wine altinda: cikti %r kod %d (Wine in kaydi; makine kaydi degil)' % (ac, ak))
        denet('Wine altinda calisir ve biter (kod 0 ya da 1)', ak in (0, 1))
        return
    gecici = tempfile.mkdtemp(prefix='yuva_')

    def dene(blob):
        yol = os.path.join(gecici, 'rsmb.bin')
        if blob is None:
            return kos('yuva.exe', b'', {'RSMB': os.path.join(gecici, 'yok')})
        with open(yol, 'wb') as f:
            f.write(blob)
        return kos('yuva.exe', b'', {'RSMB': yol, 'ZOR': '1'})
    bios = yapi(0, bytes(20), (b'Uretici', b'Surum 01.05.00'))
    son = yapi(127, b'')
    hp_once = rsmb(bios + yuva17(0) + yuva17(16384) + son)
    hp_sonra = rsmb(bios + yuva17(16384) + yuva17(16384) + son)
    ELLE = [
        ('bir yuva bos, biri 16 GiB', hp_once, b'0 0\r\n17179869184 64\r\n', 0),
        ('iki yuva 16 GiB', hp_sonra, b'17179869184 64\r\n17179869184 64\r\n', 0),
        ('kayit yok', None, b'', 1),
        ('8 bayttan kisa', b'\0\x03\x03', b'', 1),
        ('basliktaki boy gelenden buyuk', rsmb(bios)[:20], b'', 1),
        ('1 MiB tan buyuk', rsmb(bios + son) + bytes(0x100000), b'', 1),
        ('bos tablo', rsmb(b''), b'', 0),
        ('bilinmeyen boy ve genislik', rsmb(yuva17(0xFFFF, 0xFFFF) + son), b'? ?\r\n', 0),
        ('32 GiB: genis alan', rsmb(yuva17(0x7FFF, 64, genis=32768) + son), b'34359738368 64\r\n', 0),
        ('genis alan yoksa bilinmez', rsmb(yuva17(0x7FFF, 64, boy=0x1C) + son), b'? 64\r\n', 0),
        ('KB birimi', rsmb(yuva17(0x8000 | 512, 8, boy=0x15) + son), b'524288 8\r\n', 0),
        ('ECC: 72/64', rsmb(yuva17(8192, 64) + yuva17(1, 0) + son), b'8589934592 64\r\n1048576 0\r\n', 0),
        ('tur 127 den sonrasi okunmaz', rsmb(son + yuva17(16384)), b'', 0),
        ('kisa tur 17 (boy alani yok) gecilir', rsmb(yapi(17, bytes(6)) + yuva17(4096) + son), b'4294967296 64\r\n', 0),
    ]
    for ad, blob, c, k in ELLE:
        mc, mk = yuva_model(blob)
        ac, ak = dene(blob)
        denet('elle: ' + ad, (mc, mk) == (c, k) and (ac, ak) == (c, k), 'model %r/%d arac %r/%d' % (mc, mk, ac, ak))
    rs = random.Random(17)
    hata = None
    for _ in range(1500):
        t = b''
        for _ in range(rs.randrange(0, 8)):
            sec = rs.random()
            if sec < 0.5:
                t += yuva17(rs.choice([0, 1, 4096, 8192, 16384, 0x7FFF, 0x8000 | 640, 0xFFFF, rs.randrange(0, 65536)]),
                            rs.choice([0, 8, 64, 72, 0xFFFF]), rs.choice([0x0E, 0x15, 0x1B, 0x1C, 0x20, 0x28, 0x54, 0x5C]),
                            rs.choice([0, 32768, 65536, 0x80000000 | 123, rs.getrandbits(32)]))
            elif sec < 0.85:
                t += yapi(rs.choice([0, 1, 2, 4, 16, 19, 126, 130]), bytes(rs.getrandbits(8) for _ in range(rs.randrange(0, 40))),
                          [bytes(rs.randrange(1, 256) for _ in range(rs.randrange(1, 12))) for _ in range(rs.randrange(0, 4))])
            else:
                t += bytes(rs.getrandbits(8) for _ in range(rs.randrange(0, 30)))
        if rs.random() < 0.7:
            t += yapi(127, b'')
        if rs.random() < 0.3:
            t = t[:rs.randrange(0, len(t) + 1)]
        blob = rsmb(t)
        if rs.random() < 0.05:
            blob = blob[:4] + struct.pack('<I', rs.randrange(0, len(t) + 40)) + blob[8:]
        if yuva_model(blob) != dene(blob):
            hata = 'kayit %s model %r arac %r' % (blob.hex(), yuva_model(blob), dene(blob))
            break
    denet('rastgele 1500 kayit (bozuk ve kesik olanlar dahil): arac = model', hata is None, hata or '')


# ============================================================ cevrim
CEVRIM_SIGA = 0x800000


def _satir(d, p):
    """p'de baslayan satir: (icerik sonu, sonraki satirin basi). Icerik CR LF'yi kapsamaz."""
    i = d.find(b'\n', p)
    if i < 0:
        return len(d), len(d)
    return (i - 1 if i > p and d[i - 1] == 13 else i), i + 1


def cevrim_model(d):
    """(birinci cikis, ikinci cikis, cikis kodu). Reddedilirse (b'', b'', 0xFFFFFFFF)."""
    n, RET = len(d), (b'', b'', 0xFFFFFFFF)
    if n >= CEVRIM_SIGA:
        return RET
    ce, nx = _satir(d, 0) if n else (0, 0)
    if n and d[:ce] == b'.':                                    # birlestirme (yeni gidis)
        kayitlar, p = [], nx
        while True:
            if p >= n:
                return RET
            ce, nx = _satir(d, p)
            if ce == p:
                return RET
            if d[p] == 0x2E:
                if ce - p != 1:
                    return RET
                tohum = nx
                break
            if d[p] != 0x23 or len(kayitlar) >= 256:
                return RET
            anahtar, p = d[p:ce], nx
            if p >= n:
                return RET
            ce, nx = _satir(d, p)
            if ce - p < 2 or d[p] != 0x2E:
                return RET
            bas, p = p, nx
            while True:
                if p >= n:
                    return RET
                ce, nx = _satir(d, p)
                if ce - p == 1 and d[p] == 0x2E:
                    break
                if ce - p >= 2 and d[p] == 0x2E and d[p - 4:p] == b'\r\n\r\n':
                    return RET                                  # bolumun icinde ikinci bir bolum basi
                p = nx
            kayitlar.append([anahtar, d[bas:ce], False])
            p = nx
        c1, s, p = bytearray(), tohum, tohum
        while p < n:
            ce, nx = _satir(d, p)
            baslik = d[p:ce]
            if ce > p and d[p] == 0x23 and any(not k[2] and k[0] == baslik for k in kayitlar):
                capa, q = ce, nx
                while q < n:
                    qce, qnx = _satir(d, q)
                    if qce > q and d[q] == 0x23:
                        break
                    if qce > q:
                        capa = qce
                    q = qnx
                c1 += d[s:capa]
                s = capa
                for k in kayitlar:
                    if not k[2] and k[0] == baslik:
                        k[2] = True
                        c1 += b'\r\n\r\n' + k[1]
                p = q
            else:
                p = nx
        c1 += d[s:]
        kalan = [k for k in kayitlar if not k[2]]
        c2 = b''.join(k[0] + b'\r\n' + k[1] + b'\r\n' for k in kalan)
        return bytes(c1), (b'.\r\n' + c2 + b'.\r\n' if kalan else b''), len(kalan)
    c1, c2, s, p, anahtar, adet = bytearray(), bytearray(), 0, 0, None, 0   # ayirma (geri donus)
    while p < n:
        ce, nx = _satir(d, p)
        if ce > p and d[p] == 0x23:
            anahtar = d[p:ce]
        elif ce - p >= 2 and d[p] == 0x2E and anahtar is not None and p >= 4 and d[p - 4:p] == b'\r\n\r\n':
            q, son = nx, None
            while q < n:
                qce, qnx = _satir(d, q)
                if qce - q == 1 and d[q] == 0x2E:
                    son = (qce, qnx)
                    break
                if qce - q >= 2 and d[q] == 0x2E and d[q - 4:q] == b'\r\n\r\n':
                    break                                       # ic ice olmaz: ilki bolum degildi
                q = qnx
            if son:
                c1 += d[s:p - 4]
                if adet == 0:
                    c2 += b'.\r\n'
                adet += 1
                c2 += anahtar + b'\r\n' + d[p:son[0]] + b'\r\n'
                s, p = son
                continue
        p = nx
    c1 += d[s:]
    if adet:
        c2 += b'.\r\n'
    return bytes(c1), bytes(c2), 0


def cevrim_rastgele_tohum(rs, blok_olabilir=True):
    basliklar = [b'### A', b'### B', b'### C', b'#', b'# uzun bir baslik satiri:', b'###']
    s = bytearray()
    for _ in range(rs.randrange(0, 14)):
        t = rs.random()
        if t < 0.22:
            satir = rs.choice(basliklar)
        elif t < 0.45:
            satir = b''
        elif t < 0.75:
            satir = rs.choice([b'metin', b'iki kelime', b'x', b' bosluklu ', b'33 - x', b'a.b', b'..', b'#degil'[1:]])
        elif t < 0.85 and blok_olabilir:
            satir = rs.choice([b'.c:', b'.claude, 1:', b'.x'])
        elif t < 0.93 and blok_olabilir:
            satir = b'.'
        else:
            satir = b'son satir'
        s += satir + rs.choice([b'\r\n'] * 6 + [b'\n', b'\r\n\r\n'])
    if s and rs.random() < 0.4:
        s = s.rstrip(b'\r\n')
    return bytes(s)


def cevrim_rastgele_baslik(rs, bozuk=False):
    basliklar = [b'### A', b'### B', b'### C', b'#', b'# uzun bir baslik satiri:', b'### yok']
    s = bytearray(b'.\r\n')
    for _ in range(rs.randrange(0, 5)):
        s += rs.choice(basliklar) + b'\r\n' + rs.choice([b'.c:', b'.claude, 2026:', b'.x']) + b'\r\n'
        for _ in range(rs.randrange(0, 5)):
            s += rs.choice([b'bolum satiri', b'', b'# bolum icinde kare', b'.nokta ile baslayan', b'33 - x', b' . ', b'bolum satiri']) + b'\r\n'
        s += b'.\r\n'
    s += b'.\r\n'
    if bozuk:
        i = rs.randrange(0, len(s))
        s = rs.choice([s[:i], s[:i] + b'yabanci\r\n' + s[i:], s[:-3], s.replace(b'.\r\n', b'', 1) if rs.random() < 0.5 else s[:i] + b'\r\n' + s[i:]])
    return bytes(s)


def sina_cevrim():
    yaz('cevrim.exe')
    RET = 0xFFFFFFFF
    T = b'bas\r\n### H\r\nx\r\n\r\n### G\r\ny'
    H = b'.\r\n### H\r\n.c:\r\nmetin\r\n.\r\n.\r\n'
    N = b'bas\r\n### H\r\nx\r\n\r\n.c:\r\nmetin\r\n.\r\n\r\n### G\r\ny'
    ELLE = [
        ('yeni gidis: bolum, basliginin bolgesindeki son dolu satirin ardina girer', H + T, N, b'', 0),
        ('geri donus: bolum ayrilir, tohum bayt bayt geri gelir', N, T, H, 0),
        ('bos akis', b'', b'', b'', 0),
        ('bolumu olmayan metin aynen gecer', T, T, b'', 0),
        ('bos baslik: tohum aynen gecer', b'.\r\n.\r\n' + T, T, b'', 0),
        ('basligi olmayan bolum yerlesmez, sayilir ve ikinci cikistan geri gelir',
         b'.\r\n### Z\r\n.c:\r\nm\r\n.\r\n.\r\n' + T, T, b'.\r\n### Z\r\n.c:\r\nm\r\n.\r\n.\r\n', 1),
        ('ayni basliga iki bolum sirayla girer',
         b'.\r\n### G\r\n.a:\r\n1\r\n.\r\n### G\r\n.b:\r\n2\r\n.\r\n.\r\n' + T,
         b'bas\r\n### H\r\nx\r\n\r\n### G\r\ny\r\n\r\n.a:\r\n1\r\n.\r\n\r\n.b:\r\n2\r\n.', b'', 0),
        ('iki bolum art arda ayrilir',
         b'bas\r\n### H\r\nx\r\n\r\n### G\r\ny\r\n\r\n.a:\r\n1\r\n.\r\n\r\n.b:\r\n2\r\n.', T,
         b'.\r\n### G\r\n.a:\r\n1\r\n.\r\n### G\r\n.b:\r\n2\r\n.\r\n.\r\n', 0),
        ('basliktaki sira tohumdaki siradan farkli olabilir',
         b'.\r\n### G\r\n.g:\r\n.\r\n### H\r\n.h:\r\n.\r\n.\r\n' + T,
         b'bas\r\n### H\r\nx\r\n\r\n.h:\r\n.\r\n\r\n### G\r\ny\r\n\r\n.g:\r\n.', b'', 0),
        ('bolgesi bos basligin capasi basligin kendisidir',
         b'.\r\n### H\r\n.c:\r\n.\r\n.\r\n### H\r\n\r\n\r\n### G\r\n', b'### H\r\n\r\n.c:\r\n.\r\n\r\n\r\n### G\r\n', b'', 0),
        ('basliksiz bolum ayrilmaz', b'x\r\n\r\n.c:\r\nm\r\n.\r\n', b'x\r\n\r\n.c:\r\nm\r\n.\r\n', b'', 0),
        ('kapanisi olmayan bolum ayrilmaz', b'### H\r\nx\r\n\r\n.c:\r\nm\r\n', b'### H\r\nx\r\n\r\n.c:\r\nm\r\n', b'', 0),
        ('iki satir sonunun ardinda durmayan bolum ayrilmaz', b'### H\r\nx\r\n.c:\r\nm\r\n.\r\n', b'### H\r\nx\r\n.c:\r\nm\r\n.\r\n', b'', 0),
        ('LF ile ayrilmis bos satir yetmez (CR LF CR LF gerekir)', b'### H\nx\n\n.c:\nm\n.\n', b'### H\nx\n\n.c:\nm\n.\n', b'', 0),
        ('tek noktali satirlar tek basina bolum degildir', b'### H\r\n\r\n.\r\n.\r\n', b'### H\r\n\r\n.\r\n.\r\n', b'', 0),
        ('bozuk baslik: bolum basi yok', b'.\r\n### H\r\nx\r\n.\r\n.\r\n' + T, b'', b'', RET),
        ('bozuk baslik: bolum kapanmamis', b'.\r\n### H\r\n.c:\r\nmetin\r\n', b'', b'', RET),
        ('bozuk baslik: kapanis yok', b'.\r\n### H\r\n.c:\r\n.\r\n', b'', b'', RET),
        ('bozuk baslik: bos satir', b'.\r\n\r\n.\r\n' + T, b'', b'', RET),
        ('bozuk baslik: yabanci satir', b'.\r\nabc\r\n.\r\n' + T, b'', b'', RET),
        ('yalniz acilis', b'.', b'', b'', RET),
        ('bozuk baslik: bolumun icinde ikinci bir bolum basi', b'.\r\n### H\r\n.c:\r\n\r\n.d:\r\n.\r\n.\r\n' + T, b'', b'', RET),
        ('ic ice olmaz: bos satirdan sonra nokta ile baslayan satir, gercek bolumu yutmaz',
         b'### H\r\n\r\n..\r\nx\r\n\r\n.c:\r\nm\r\n.\r\ny', b'### H\r\n\r\n..\r\nx\r\ny',
         b'.\r\n### H\r\n.c:\r\nm\r\n.\r\n.\r\n', 0),
    ]
    for ad, g, c1, c2, k in ELLE:
        m = cevrim_model(g)
        a = kos('cevrim.exe', g, ikinci=True)
        denet('elle: ' + ad, m == (c1, c2, k) and a[:2] == (c1, c2) and kod_esit(a[2], k),
              'model %r arac %r' % (m, a))
    rs = random.Random(2)
    adet = adet_sec(4000, 500, 40)
    hata, sayac = None, {'ayir': 0, 'birlestir': 0, 'ret': 0, 'donen': 0, 'bolum': 0}
    for i in range(adet):
        t = cevrim_rastgele_tohum(rs)
        h = cevrim_rastgele_baslik(rs, bozuk=rs.random() < 0.12)
        g = rs.choice([t, h + t, h + t, h])
        m = cevrim_model(g)
        a = kos('cevrim.exe', g, ikinci=True)
        if a[:2] != m[:2] or not kod_esit(a[2], m[2]):
            hata = 'girdi %r model %r arac %r' % (g, m, a)
            break
        sayac['ret' if m[2] == RET else 'birlestir' if g[:1] == b'.' and _satir(g, 0)[0] == 1 else 'ayir'] += 1
        if m[2] != RET and g is not t and m[0]:
            # donus: aracin kurdugu nokta yine araca verilir
            m2 = cevrim_model(m[0])
            a2 = kos('cevrim.exe', m[0], ikinci=True)
            if a2[:2] != m2[:2] or not kod_esit(a2[2], m2[2]):
                hata = 'donus girdisi %r model %r arac %r' % (m[0], m2, a2)
                break
            sayac['donen'] += 1
            sayac['bolum'] += m2[1].count(b'\r\n.\r\n')
    denet('rastgele %d akis (ayirma, birlestirme, bozuk baslik): arac = model' % adet, hata is None, hata or '')
    bilgi.append('cevrim rastgele: ayirma %(ayir)d, birlestirme %(birlestir)d, reddedilen %(ret)d; kurulan %(donen)d nokta yeniden ayrildi' % sayac)
    # yasa: bolumsuz tohum + baslik -> nokta -> (tohum, baslik) -> ayni nokta
    hata, tur = None, 0
    for i in range(adet_sec(1500, 200, 20)):
        t = cevrim_rastgele_tohum(rs, blok_olabilir=False)
        h = cevrim_rastgele_baslik(rs)
        n1, kalan, k1 = kos('cevrim.exe', h + t, ikinci=True)
        if kod_esit(k1, RET):
            continue                                            # bu baslik bozuk sayildi (ic ice bolum)
        t2, h2, k2 = kos('cevrim.exe', n1, ikinci=True)
        n2, kalan2, k3 = kos('cevrim.exe', h2 + t2, ikinci=True)
        if t2 != t or n2 != n1 or k2 != 0 or k3 != 0 or kalan2 != b'':
            hata = 'tohum %r baslik %r nokta %r donen tohum %r ikinci nokta %r' % (t, h, n1, t2, n2)
            break
        tur += 1
    denet('yasa: %d kez gidis, donus, yeni gidis: tohum bayt bayt doner, ikinci nokta ilkiyle ayni' % tur, hata is None, hata or '')
    buyuk = b'### B\r\nx\r\n\r\n.c:\r\n' + b'0123456789abcdef\r\n' * 150000 + b'.\r\n' + b'y\r\n' * 100000
    m = cevrim_model(buyuk)
    a = kos('cevrim.exe', buyuk, ikinci=True)
    denet('buyuk akis (%d bayt, 2,7 MB lik bolum): arac = model' % len(buyuk), a[:2] == m[:2] and kod_esit(a[2], m[2]) and len(m[1]) > 2000000)
    a = kos('cevrim.exe', b'a' * CEVRIM_SIGA, ikinci=True)
    denet('8 MiB a sigmayan akis reddedilir, hicbir sey verilmez', a[:2] == (b'', b'') and kod_esit(a[2], RET))
    a = kos('cevrim.exe', b'a' * (CEVRIM_SIGA - 1), ikinci=True)
    denet('8 MiB tan bir bayt kisa akis islenir', a[0] == b'a' * (CEVRIM_SIGA - 1) and a[2] == 0)
    if not WIN and not SEC['wine']:
        g = H + T
        denet('ZOR: korunmayan yazmaclar bozulunca sonuc ayni',
              kos('cevrim.exe', g, {'ZOR': '1'}, ikinci=True)[:2] == cevrim_model(g)[:2]
              and kos('cevrim.exe', N, {'ZOR': '1'}, ikinci=True)[:2] == cevrim_model(N)[:2])
        a = kos('cevrim.exe', g, {'YAZ_KES': '1'}, ikinci=True)
        denet('cikis ucu kapaninca arac durur (kod -1)', a[2] == 255 and len(a[0]) < len(N))


# ============================================================ betikler
def cevrim_ornek(rs):
    """Yapay bir tohum ile alti bolumlu bir baslik. Gercek kullanima benzer: UTF-8, CR LF,
    yinelenen basliklar, son satirda satir sonu yok, ilk ve son basliga ikiser bolum."""
    hece = ['ara', 'bağ', 'çık', 'dön', 'göz', 'ışık', 'öz', 'şu', 'üç', 'yol', 'zemin', 'nokta', 'kod', '33', 'x']

    def tumce(n):
        return ' '.join(rs.choice(hece) for _ in range(n))
    basliklar = ['### BİRİNCİ BAŞLIK: ' + tumce(6).upper(), '### İKİNCİ BAŞLIK:', '### ÜÇÜNCÜ BAŞLIK:', '### SON BAŞLIK:']
    s = ['İlk satır: ' + tumce(5), '']
    for _ in range(6):
        s += ['### YİNELENEN BAŞLIK AŞAĞIDA:', '']
        s += [tumce(rs.randrange(3, 12)) if rs.random() < 0.8 else '' for _ in range(rs.randrange(40, 100))]
        s.append('')
    s += [basliklar[0]] + [''] * 15
    s += [basliklar[1], '', tumce(20), '', '']
    s += [basliklar[2], '', tumce(18), '']
    s += [basliklar[3], '', 'Son satır.']
    tohum = '\r\n'.join(s).encode('utf-8')

    def bolum(ad, n):
        g = ['.' + ad + ':', '']
        g += ['│ ' + tumce(rs.randrange(2, 9)) + ' │' if rs.random() < 0.5 else tumce(rs.randrange(1, 10)) for _ in range(n)]
        return '\r\n'.join(g + ['', 'son satır', '.']).encode('utf-8')
    sira = [(0, bolum('uye, 1', 40)), (0, bolum('uye, 2', 12)), (1, bolum('uye, 3', 25)),
            (2, bolum('uye, 4', 9)), (3, bolum('uye, 5', 14)), (3, bolum('uye, 6', 6))]
    baslik = b'.\r\n' + b''.join(basliklar[i].encode('utf-8') + b'\r\n' + b + b'\r\n' for i, b in sira) + b'.\r\n'
    eski = tohum[:tohum.index(basliklar[1].encode('utf-8'))].rstrip(b'\r\n')
    return tohum, baslik, eski


def betik_kos(dizin, betik, *dosyalar):
    """Bir .cmd betigini calistirir: (cikis kodu, konsola yazdigi). Windows'ta surukle birakta oldugu gibi
    betik de dosya da tam yoluyla ve tirnak icinde verilir."""
    e = dict(os.environ, SINA_BEKLEME='1')
    if WIN:
        komut = 'cmd /d /s /c "' + ' '.join('"%s"' % os.path.join(dizin, x) for x in (betik,) + dosyalar) + '"'
    else:
        e['WINEDEBUG'] = '-all'
        komut = ['wine', 'cmd', '/c', betik] + list(dosyalar)
    r = subprocess.run(komut, env=e, cwd=dizin, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, timeout=600)
    return r.returncode & (0xFFFFFFFF if WIN else 0xFF), r.stdout.decode('ascii', 'replace').replace('\r', '')


def sina_betikler():
    """yeni_gidis.cmd ve geri_donus.cmd: yalniz Windows'ta (ya da --wine ile). Urettikleri dosyalar
    burada, betiklerden bagimsiz olarak modelle bayt bayt karsilastirilir."""
    yaz('betikler: yeni_gidis.cmd, geri_donus.cmd')
    gerek = ('cevrim.exe', 'yeni_gidis.cmd', 'geri_donus.cmd')
    eksik = [x for x in gerek if not os.path.exists(os.path.join(SEC['klasor'], x))]
    if eksik:
        bilgi.append('betikler sinanmadi; yok: ' + ', '.join(eksik))
        return
    RET = 0xFFFFFFFF
    tohum, baslik, eski = cevrim_ornek(random.Random(5))
    nokta, kalan, k = cevrim_model(baslik + tohum)
    denet('ornek (%d baytlik tohum, 6 bolum): modelde hepsi yerlesiyor, donuste tohum ve baslik geri geliyor' % len(tohum),
          k == 0 and kalan == b'' and cevrim_model(nokta) == (tohum, baslik, 0))
    dizin = tempfile.mkdtemp(prefix='deneme klasörü (2) ', dir=SEC['klasor'])
    for x in gerek:
        with open(os.path.join(SEC['klasor'], x), 'rb') as f, open(os.path.join(dizin, x), 'wb') as g:
            g.write(f.read())

    def oku(x):
        y = os.path.join(dizin, x)
        return open(y, 'rb').read() if os.path.exists(y) else None

    def koy(x, d):
        with open(os.path.join(dizin, x), 'wb') as f:
            f.write(d)
    ad = 'çalışma dosyası (deneme)'
    koy(ad + '.html', tohum)
    koy('bolumler.txt', baslik)
    kod, yazi = betik_kos(dizin, 'yeni_gidis.cmd', ad + '.html')
    denet('yeni_gidis.cmd: adi Turkce harfli, bosluklu, parantezli dosya ve klasor; nokta = model (kod 0)',
          kod == 0 and oku(ad + '.nokta.html') == nokta, 'kod %d yazi %r' % (kod, yazi))
    denet('yeni_gidis.cmd: verilen dosyaya dokunmadi; gecici dosya ve yerlesmeyen dosyasi birakmadi',
          oku(ad + '.html') == tohum and sorted(os.listdir(dizin)) == sorted(gerek + ('bolumler.txt', ad + '.html', ad + '.nokta.html')),
          repr(sorted(os.listdir(dizin))))
    if WIN:
        denet('yeni_gidis.cmd kendi denemesini yapti (fc): nokta ayrilinca tohum bayt bayt geri geliyor',
              'Denendi: nokta ayrilinca tohum bayt bayt geri geliyor.' in yazi and 'Butun bolumler yerlesti.' in yazi, repr(yazi))
    kod, yazi = betik_kos(dizin, 'geri_donus.cmd', ad + '.nokta.html')
    denet('geri_donus.cmd: tohum bayt bayt, bolumler basliklariyla geri geldi (kod 0)',
          kod == 0 and oku(ad + '.nokta.tohum.html') == tohum and oku(ad + '.nokta.bolumler.txt') == baslik,
          'kod %d yazi %r' % (kod, yazi))
    if WIN:
        denet('geri_donus.cmd kendi denemesini yapti (fc): yeniden birlestirince ayni nokta',
              'Denendi: tohum ile bolumler yeniden birlestirilince ayni nokta cikti.' in yazi, repr(yazi))
    kod, yazi = betik_kos(dizin, 'yeni_gidis.cmd', ad + '.nokta.tohum.html', ad + '.nokta.bolumler.txt')
    denet('yeni_gidis.cmd: donen tohum ile donen bolumlerden kurulan ikinci nokta ilkiyle ayni',
          kod == 0 and oku(ad + '.nokta.tohum.nokta.html') == nokta, 'kod %d yazi %r' % (kod, yazi))
    kod, yazi = betik_kos(dizin, 'yeni_gidis.cmd', ad + '.nokta.html')
    denet('yeni_gidis.cmd: icinde bolum olan dosyada bolumler iki kez girmedi; oncekiler ayri dosyaya yazildi',
          kod == 0 and oku(ad + '.nokta.nokta.html') == nokta and oku(ad + '.nokta.onceki_bolumler.txt') == baslik,
          'kod %d yazi %r' % (kod, yazi))
    m = cevrim_model(baslik + eski)
    koy('eski sürüm.html', eski)
    kod, yazi = betik_kos(dizin, 'yeni_gidis.cmd', 'eski sürüm.html')
    denet('yeni_gidis.cmd: eski tohumda basligi duran 2 bolum yerlesti; 4 bolum yerlesmeyen dosyasinda (kod 4)',
          kod == 4 == m[2] and oku('eski sürüm.nokta.html') == m[0] and oku('eski sürüm.yerlesmeyen.txt') == m[1],
          'kod %d yazi %r' % (kod, yazi))
    kod, yazi = betik_kos(dizin, 'geri_donus.cmd', 'eski sürüm.nokta.html')
    denet('geri_donus.cmd: eski tohum bayt bayt geri geldi',
          kod == 0 and oku('eski sürüm.nokta.tohum.html') == eski, 'kod %d yazi %r' % (kod, yazi))
    kod, yazi = betik_kos(dizin, 'geri_donus.cmd', ad + '.html')
    denet('geri_donus.cmd: bolumu olmayan dosyada bir sey yazmadi (kod 1)',
          kod == 1 and oku(ad + '.tohum.html') is None and oku(ad + '.bolumler.txt') is None, 'kod %d yazi %r' % (kod, yazi))
    kod, yazi = betik_kos(dizin, 'geri_donus.cmd', 'bolumler.txt')
    denet('geri_donus.cmd: bolumler dosyasi verilince reddetti, bir sey yazmadi (kod -1)',
          kod_esit(kod, RET) and oku('bolumler.tohum.txt') is None and oku('bolumler.bolumler.txt') is None, 'kod %d yazi %r' % (kod, yazi))
    koy('bozuk.txt', b'.\r\nyabanci\r\n')
    kod, yazi = betik_kos(dizin, 'yeni_gidis.cmd', ad + '.html', 'bozuk.txt')
    denet('yeni_gidis.cmd: bozuk bolumler dosyasinda nokta yazmadi (kod -1)',
          kod_esit(kod, RET) and oku(ad + '.nokta.html') == nokta, 'kod %d yazi %r' % (kod, yazi))
    denet('betikler gecici dosya birakmadi', not any(x.endswith('.tmp') for x in os.listdir(dizin)), repr(sorted(os.listdir(dizin))))
    if WIN:
        import shutil
        shutil.rmtree(dizin, ignore_errors=True)


def sina_windows():
    """Yalniz Windows: dosya turu ve Defender taramasi."""
    import ctypes
    from ctypes import wintypes
    yaz('windows')
    k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    k32.GetBinaryTypeW.argtypes = [wintypes.LPCWSTR, ctypes.POINTER(wintypes.DWORD)]
    k32.GetBinaryTypeW.restype = wintypes.BOOL
    mp = os.path.join(os.environ.get('ProgramFiles', r'C:\Program Files'), 'Windows Defender', 'MpCmdRun.exe')
    for ad in ('oran.exe', '128.exe', 'yuva.exe', 'cevrim.exe'):
        yol = os.path.join(SEC['klasor'], ad)
        tur = wintypes.DWORD(99)
        iyi = k32.GetBinaryTypeW(yol, ctypes.byref(tur))
        denet('%s: Windows 64 bit program olarak taniyor (GetBinaryType = 6)' % ad, bool(iyi) and tur.value == 6)
        if not os.path.exists(mp):
            bilgi.append('Defender: MpCmdRun.exe yok; %s taranmadi' % ad)
            continue
        r = subprocess.run([mp, '-Scan', '-ScanType', '3', '-File', yol, '-DisableRemediation'],
                           stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=900)
        metin = ' | '.join(x.strip() for x in (r.stdout + r.stderr).decode('mbcs', 'replace').splitlines() if x.strip())[:300]
        if r.returncode in (0, 2):
            denet('%s: Defender taradi ve tehdit bulmadi (cikis kodu %d)' % (ad, r.returncode), r.returncode == 0, ascii(metin))
        bilgi.append('Defender %s: cikis kodu %d; %s' % (ad, r.returncode, ascii(metin)))


def ana():
    a = sys.argv[1:]
    secim = []
    while a:
        x = a.pop(0)
        if x == '--wine':
            SEC['wine'] = True
        elif x in ('--klasor', '--kos', '--isyuku', '--izler'):
            SEC[x[2:]] = a.pop(0)
        else:
            secim.append(x)
    for ad, f in (('oran', sina_oran), ('128', sina_128), ('yuva', sina_yuva), ('cevrim', sina_cevrim)):
        if not secim or ad in secim:
            f()
    if (WIN or SEC['wine']) and (not secim or 'betikler' in secim):
        sina_betikler()
    if WIN and not secim:
        sina_windows()
    for b in bilgi:
        yaz('  BILGI  ' + b)
    yaz('%d GECTI, %d KALDI' % (gecti, kaldi))
    with open(os.path.join(SEC['klasor'], 'sina_sonucu.txt'), 'w', encoding='ascii', errors='replace', newline='\r\n') as f:
        f.write('\n'.join(satirlar) + '\n')
    return 1 if kaldi else 0


if __name__ == '__main__':
    sys.exit(ana())
