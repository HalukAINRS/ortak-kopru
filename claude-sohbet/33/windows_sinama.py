# -*- coding: utf-8 -*-
"""33.exe'nin gercek Windows'ta sinanmasi.  Yaninda 33.exe durmalidir.
    python -B windows_sinama.py
Cikti GECTI / KALDI / BILGI satirlaridir; ayni satirlar windows_python_sonucu.txt dosyasina da yazilir.
Uc ayri sey karsilastirilir: sozle yazilmis kuraldan kurulan bagimsiz model, elle yazilmis beklentiler
ve 33.exe'nin kendisi (bu makinede, Windows'un kendi yukleyicisi ve konsoluyla)."""
import sys, os, subprocess, hashlib, random, time, ctypes, platform, threading, queue, traceback
from ctypes import wintypes
BURASI = os.path.dirname(os.path.abspath(__file__)); EXE = os.path.join(BURASI, "33.exe")
BEKLENEN_OZET = "4cc92e7034025c07e60c80d7b37c0adff140c88b4eeb28d7fcc638c5bfa4287f"
satirlar = []; kalanlar = []
def yaz(s):
    print(s, flush=True); satirlar.append(s)
def tamam(ad, kosul, ek=""):
    if not kosul: kalanlar.append(ad)
    yaz(("GECTI  " if kosul else "KALDI  ") + ad + ((" :: " + ascii(ek)[:600]) if (ek != "" and not kosul) else ""))
def bilgi(s): yaz("BILGI  " + s)
def kos(veri=b"", sure=900):
    r = subprocess.run([EXE], input=veri, capture_output=True, timeout=sure); return r.returncode, r.stdout, r.stderr
def dene(ad, f):
    try: f()
    except Exception as h: tamam(ad + " (sinama kosamadi)", False, "".join(traceback.format_exception_only(type(h), h)).strip())

# ---- bagimsiz model: aracin yaptigi is, sozle yazilmis kuraldan ----
EN_BUYUK = 2**63 - 1
def model(s):
    cik = bytearray(); ham = bytearray(); durum = "bos"; deger = 0; sayi = 0
    def sayi_bitti(son):
        nonlocal ham, deger, sayi
        y = 33 + deger if ham[:1] == b"-" else 33 - deger
        cik.extend((bytes(ham) if y > EN_BUYUK else str(y).encode()) + son); ham = bytearray(); deger = 0; sayi = 0
    for b in s:
        c = bytes([b])
        if 48 <= b <= 57:
            if durum == "uzun": cik.extend(c); continue
            ham.extend(c)
            if sayi < 20:
                sayi += 1; deger *= 10
                if deger <= EN_BUYUK:
                    deger += b - 48
                    if deger <= EN_BUYUK: durum = "sayi"; continue
            cik.extend(ham); ham = bytearray(); deger = 0; sayi = 0; durum = "uzun"
        elif durum == "sayi": sayi_bitti(c); durum = "bos"
        elif durum == "uzun": cik.extend(c); durum = "bos"
        elif ham: cik.extend(bytes(ham) + c); ham = bytearray()
        elif b in (43, 45): ham.extend(c)
        else: cik.extend(c)
    if durum == "sayi": sayi_bitti(b"")
    elif ham: cik.extend(ham)
    return bytes(cik)


ELLE = [
 (b"", b""), (b"-33", b"66"), (b"-1", b"34"), (b"0", b"33"), (b"+1", b"32"), (b"+33", b"0"),
 (b"66", b"-33"), (b"34", b"-1"), (b"33", b"0"), (b"32", b"1"), (b"1", b"32"), (b"16", b"17"), (b"17", b"16"),
 (b"-33 para\r\n-1 para\r\n0 para\r\n+1 para\r\n+33 para\r\n", b"66 para\r\n34 para\r\n33 para\r\n32 para\r\n0 para\r\n"),
 (b"66 para\n34 para\n33 para\n32 para\n0 para\n", b"-33 para\n-1 para\n0 para\n1 para\n33 para\n"),
 (b"x token", b"x token"), (b"5 token", b"28 token"), (b"28 para", b"5 para"),
 (b"5-3", b"28-30"), (b"5 -3", b"28 36"), (b"5--3", b"28-36"), (b"--5", b"--28"), (b"---5", b"--38"), (b"+-5", b"+-28"), (b"-+5", b"-+28"),
 (b"a-b", b"a-b"), (b"-", b"-"), (b"+", b"+"), (b"-\n", b"-\n"), (b"x86", b"x-53"), (b"007", b"26"), (b"-0", b"33"), (b"+0", b"33"), (b"00", b"33"),
 (b"16,5", b"17,28"), (b"1.5", b"32.28"), (b"(33 - x)", b"(0 - x)"), (b"1-33", b"32-0"), (b"0-64-128", b"33--31--95"),
 (b"9223372036854775807", b"-9223372036854775774"), (b"-9223372036854775774", b"9223372036854775807"),
 (b"9223372036854775808", b"9223372036854775808"), (b"-9223372036854775775", b"-9223372036854775775"), (b"-9223372036854775807", b"-9223372036854775807"),
 (b"18446744073709551616", b"18446744073709551616"), (b"9" * 20, b"9" * 20), (b"0" * 19 + b"1", b"32"), (b"0" * 20 + b"1", b"0" * 20 + b"1"),
 (b"-" + b"0" * 19 + b"1", b"34"), (b"-" + b"0" * 20 + b"1", b"-" + b"0" * 20 + b"1"),
 (b"7" * 1000, b"7" * 1000), (b"123456789012345678901234567890-5", b"123456789012345678901234567890-28"), (b"123456789012345678901234567890 -5", b"123456789012345678901234567890 38"),
 (b"\x00", b"\x00"), (b"\x00-1\x00", b"\x0034\x00"), (b"\xff5\xfe", b"\xff28\xfe"), ("−1 ş 2".encode(), "−32 ş 31".encode()),
 (bytes(range(256)), bytes(range(0x30)) + b"-123456756" + bytes(range(0x3A, 256))),
]

def rastgele(n):
    p = random.random()
    if p < .5: return bytes(random.choice(b"0123456789+-  \n\r\tax.,") for _ in range(n))
    if p < .8: return bytes(random.choice(b"0123456789-+") for _ in range(n))
    return bytes(random.randrange(256) for _ in range(n))

def duzgun():  # yalin bicimde yazilmis sayilar ve aralarinda isaret olmayan metin
    par = []
    for _ in range(random.randint(0, 12)):
        par.append(random.choice([b" ", b"\n", b" para ", b" token\r\n", b"; ", b"x", b"\x00\xff"]))
        if random.random() < .8: par.append(str(random.choice([random.randint(-50, 80), random.randint(-(2**63 - 34), 2**63 - 1)])).encode())
    return b"".join(par)

AYRAC = b"\n\x01\n"
k32 = ctypes.WinDLL("kernel32", use_last_error=True)

def t_ortam():
    bilgi("ortam: %s | %s | %s | python %s" % (platform.platform(), platform.version(), platform.machine(), platform.python_version()))
    d = open(EXE, "rb").read()
    tamam("dosya: 1536 bayt; ozet beklenenle ayni", len(d) == 1536 and hashlib.sha256(d).hexdigest() == BEKLENEN_OZET, hashlib.sha256(d).hexdigest())
    tur = wintypes.DWORD(99); k32.GetBinaryTypeW.argtypes = [wintypes.LPCWSTR, ctypes.POINTER(wintypes.DWORD)]; k32.GetBinaryTypeW.restype = wintypes.BOOL
    iyi = k32.GetBinaryTypeW(EXE, ctypes.byref(tur))
    tamam("Windows dosyayi 64 bit Windows programi olarak taniyor (GetBinaryType = 6)", bool(iyi) and tur.value == 6, (iyi, tur.value, ctypes.get_last_error()))

def t_elle():
    tamam("model: elle yazilmis %d beklenti" % len(ELLE), all(model(g) == c for g, c in ELLE))
    kotu = []
    for g, c in ELLE:
        r = kos(g)
        if r != (0, c, b""): kotu.append((g, r))
    tamam("33.exe: elle yazilmis %d beklentinin hepsi, cikis kodu 0" % len(ELLE), not kotu, kotu[:2])

def t_sayilar():
    random.seed(33); ornek = [random.randint(-(2**63 - 34), 2**63 - 1) for _ in range(3000)] + list(range(-200, 200)) + [-(2**63 - 34), 2**63 - 1, 10**18, -10**18]
    r = kos(AYRAC.join(str(x).encode() for x in ornek))
    tamam("33.exe: %d sayi icin 33 - x" % len(ornek), r[0] == 0 and r[1] == AYRAC.join(str(33 - x).encode() for x in ornek))

def t_akislar():
    random.seed(34); akislar = [rastgele(random.randint(0, 60)) for _ in range(4000)] + [rastgele(random.randint(200, 3000)) for _ in range(200)]
    tamam("33.exe: 150 rastgele akis ayri ayri, model ile ayni", all(kos(a)[1] == model(a) for a in akislar[:150]))
    butun = AYRAC.join(akislar); t0 = time.time(); r = kos(butun); sure = time.time() - t0
    tamam("33.exe: %d rastgele akis tek seferde (%d bayt, %.1f sn), model ile ayni" % (len(akislar), len(butun), sure), r[0] == 0 and r[1] == model(butun))
    duz = [duzgun() for _ in range(120)]
    tamam("33.exe: 120 yalin akis iki kez gecti, baslangica dondu", all(kos(kos(a)[1])[1] == a for a in duz))
    tamam("33.exe: 60 akista uc gecis = bir gecis", all(kos(kos(kos(a)[1])[1])[1] == kos(a)[1] for a in akislar[150:210]))

def t_uclar():
    r = subprocess.run([EXE], stdin=subprocess.DEVNULL, capture_output=True, timeout=60)
    tamam("bos girise bos cikis (giris NUL aygiti), cikis 0", (r.returncode, r.stdout, r.stderr) == (0, b"", b""), r)
    p = subprocess.Popen([EXE], stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=0); q = queue.Queue()
    def oku():
        while True:
            b = p.stdout.read(1)
            if not b: break
            q.put(b)
    threading.Thread(target=oku, daemon=True).start(); iyi = True; gorulen = []
    for soru, yanit in ((b"-1\n", b"34\n"), (b"-33 para\r\n", b"66 para\r\n"), (b"x\n", b"x\n"), (b"34\n", b"-1\n")):
        p.stdin.write(soru); p.stdin.flush(); al = b""; son = time.time() + 20
        while len(al) < len(yanit) and time.time() < son:
            try: al += q.get(timeout=0.5)
            except queue.Empty: pass
        gorulen.append(al); iyi = iyi and al == yanit
    p.stdin.close(); kod = p.wait(timeout=30)
    tamam("yanit, kaynak kapanmadan gelir (borularda biriktirme yok), cikis 0", iyi and kod == 0, (gorulen, kod))
    p = subprocess.Popen([EXE], stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=0); veri = b"12 abc -7\n" * 20000
    def besle():
        try: p.stdin.write(veri); p.stdin.close()
        except Exception: pass
    threading.Thread(target=besle, daemon=True).start(); ilk = b""
    while len(ilk) < 10:
        parca = p.stdout.read(10 - len(ilk))
        if not parca: break
        ilk += parca
    p.stdout.close()
    try: kod = p.wait(timeout=60)
    except subprocess.TimeoutExpired: p.kill(); kod = "durmadi"
    tamam("cikis ucu kapaninca arac durur, cikis 0", ilk == b"21 abc 40\n" and kod == 0, (ilk, kod))

class STARTUPINFOW(ctypes.Structure):
    _fields_ = [("cb", wintypes.DWORD), ("lpReserved", wintypes.LPWSTR), ("lpDesktop", wintypes.LPWSTR), ("lpTitle", wintypes.LPWSTR),
                ("dwX", wintypes.DWORD), ("dwY", wintypes.DWORD), ("dwXSize", wintypes.DWORD), ("dwYSize", wintypes.DWORD),
                ("dwXCountChars", wintypes.DWORD), ("dwYCountChars", wintypes.DWORD), ("dwFillAttribute", wintypes.DWORD), ("dwFlags", wintypes.DWORD),
                ("wShowWindow", wintypes.WORD), ("cbReserved2", wintypes.WORD), ("lpReserved2", ctypes.c_void_p),
                ("hStdInput", wintypes.HANDLE), ("hStdOutput", wintypes.HANDLE), ("hStdError", wintypes.HANDLE)]
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [("hProcess", wintypes.HANDLE), ("hThread", wintypes.HANDLE), ("dwProcessId", wintypes.DWORD), ("dwThreadId", wintypes.DWORD)]

def t_ucsuz():
    # Hic ucu olmayan arac: konsol yok, uc tutamaci olarak 0 verilir. Okuma basarisiz olur; arac bitmelidir.
    si = STARTUPINFOW(); si.cb = ctypes.sizeof(si); si.dwFlags = 0x100; pi = PROCESS_INFORMATION()
    k32.CreateProcessW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, ctypes.c_void_p, ctypes.c_void_p, wintypes.BOOL, wintypes.DWORD, ctypes.c_void_p, wintypes.LPCWSTR, ctypes.POINTER(STARTUPINFOW), ctypes.POINTER(PROCESS_INFORMATION)]
    k32.CreateProcessW.restype = wintypes.BOOL
    if not k32.CreateProcessW(EXE, None, None, None, False, 0x00000008, None, None, ctypes.byref(si), ctypes.byref(pi)): raise OSError("CreateProcess: %d" % ctypes.get_last_error())
    k32.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]; k32.WaitForSingleObject.restype = wintypes.DWORD
    bekle = k32.WaitForSingleObject(pi.hProcess, 20000); kod = wintypes.DWORD(999)
    k32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]; k32.GetExitCodeProcess(pi.hProcess, ctypes.byref(kod))
    if bekle != 0:
        k32.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]; k32.TerminateProcess(pi.hProcess, 1)
    tamam("uclari olmayan arac (konsolsuz, tutamaclar 0) hemen biter, cikis 0", bekle == 0 and kod.value == 0, (bekle, kod.value))

class COORD(ctypes.Structure): _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]
class SMALL_RECT(ctypes.Structure): _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short), ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]
class CSBI(ctypes.Structure): _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", wintypes.WORD), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]
class KEY_EVENT_RECORD(ctypes.Structure): _fields_ = [("bKeyDown", wintypes.BOOL), ("wRepeatCount", wintypes.WORD), ("wVirtualKeyCode", wintypes.WORD), ("wVirtualScanCode", wintypes.WORD), ("UnicodeChar", wintypes.WCHAR), ("dwControlKeyState", wintypes.DWORD)]
class INPUT_RECORD(ctypes.Structure): _fields_ = [("EventType", wintypes.WORD), ("KeyEvent", KEY_EVENT_RECORD)]

def t_konsol():
    # Cift tiklamadaki durum: arac kendi yeni konsoluyla acilir; tuslar konsolun giris kuyruguna yazilir, ekran konsoldan okunur.
    assert ctypes.sizeof(INPUT_RECORD) == 20
    u32 = ctypes.WinDLL("user32", use_last_error=True)
    k32.CreateFileW.restype = wintypes.HANDLE; k32.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
    k32.AttachConsole.argtypes = [wintypes.DWORD]; k32.AttachConsole.restype = wintypes.BOOL
    k32.WriteConsoleInputW.argtypes = [wintypes.HANDLE, ctypes.POINTER(INPUT_RECORD), wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]; k32.WriteConsoleInputW.restype = wintypes.BOOL
    k32.ReadConsoleOutputCharacterW.argtypes = [wintypes.HANDLE, wintypes.LPWSTR, wintypes.DWORD, COORD, ctypes.POINTER(wintypes.DWORD)]; k32.ReadConsoleOutputCharacterW.restype = wintypes.BOOL
    k32.GetConsoleScreenBufferInfo.argtypes = [wintypes.HANDLE, ctypes.POINTER(CSBI)]; k32.GetConsoleScreenBufferInfo.restype = wintypes.BOOL
    k32.GetConsoleMode.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
    p = subprocess.Popen([EXE], creationflags=0x00000010)   # CREATE_NEW_CONSOLE
    try:
        time.sleep(3)
        if p.poll() is not None: raise OSError("arac yeni konsolda hemen kapandi, cikis %r" % p.returncode)
        k32.FreeConsole()
        if not k32.AttachConsole(p.pid): raise OSError("AttachConsole: %d" % ctypes.get_last_error())
        hin = k32.CreateFileW("CONIN$", 0xC0000000, 3, None, 3, 0, None); hout = k32.CreateFileW("CONOUT$", 0xC0000000, 3, None, 3, 0, None)
        if hin in (None, wintypes.HANDLE(-1).value) or hout in (None, wintypes.HANDLE(-1).value): raise OSError("CONIN$/CONOUT$: %d" % ctypes.get_last_error())
        kip = wintypes.DWORD(0); k32.GetConsoleMode(hin, ctypes.byref(kip)); bilgi("konsol giris kipi: 0x%04X (satir: %s, yanki: %s, islenmis: %s); giris kod sayfasi %d, cikis %d" % (kip.value, bool(kip.value & 2), bool(kip.value & 4), bool(kip.value & 1), k32.GetConsoleCP(), k32.GetConsoleOutputCP()))
        def tus(ch, vk=None, ctrl=0):
            if vk is None: vk = u32.VkKeyScanW(ord(ch)) & 0xFF
            kayit = (INPUT_RECORD * 2)()
            for i, asagi in enumerate((1, 0)):
                kayit[i].EventType = 1; e = kayit[i].KeyEvent
                e.bKeyDown = asagi; e.wRepeatCount = 1; e.wVirtualKeyCode = vk; e.wVirtualScanCode = u32.MapVirtualKeyW(vk, 0) & 0xFFFF; e.UnicodeChar = ch; e.dwControlKeyState = ctrl
            n = wintypes.DWORD(0)
            if not k32.WriteConsoleInputW(hin, kayit, 2, ctypes.byref(n)) or n.value != 2: raise OSError("WriteConsoleInput: %d" % ctypes.get_last_error())
        def satir(s):
            for c in s: tus(c)
            tus("\r", 0x0D); time.sleep(2)
        def ekran(kac=10):
            b = CSBI()
            if not k32.GetConsoleScreenBufferInfo(hout, ctypes.byref(b)): raise OSError("GetConsoleScreenBufferInfo: %d" % ctypes.get_last_error())
            cik = []
            for y in range(kac):
                t = ctypes.create_unicode_buffer(b.dwSize.X + 1); n = wintypes.DWORD(0)
                k32.ReadConsoleOutputCharacterW(hout, t, b.dwSize.X, COORD(0, y), ctypes.byref(n)); cik.append(t[:n.value].rstrip())
            return cik
        bos = ekran(); tamam("konsol: pencere bos acilir (arac kendiliginden bir sey yazmaz)", all(x == "" for x in bos), bos)
        satir("-1"); e = ekran(); tamam("konsol: -1 yazilinca alt satira 34 gelir", e[:2] == ["-1", "34"], e)
        satir("-33 para"); e = ekran(); tamam("konsol: -33 para yazilinca 66 para gelir", e[2:4] == ["-33 para", "66 para"], e)
        satir("66 34 33 32 0"); e = ekran(); tamam("konsol: bes sayi tek satirda aynadan gecer", e[4:6] == ["66 34 33 32 0", "-33 -1 0 1 33"], e)
        satir("merhaba"); e = ekran(); tamam("konsol: sayi olmayan yazi oldugu gibi doner", e[6:8] == ["merhaba", "merhaba"], e)
        tus("\x1a", 0x5A, 0x0008); tus("\r", 0x0D)
        try: kod = p.wait(timeout=10); bilgi("konsol: Ctrl+Z ve Enter aracin bitmesini sagladi, cikis %r; ekran: %s" % (kod, ascii(ekran()[8:10])))
        except subprocess.TimeoutExpired: bilgi("konsol: Ctrl+Z ve Enter araci BITIRMEDI; ekran: %s" % ascii(ekran()[8:10]))
    finally:
        if p.poll() is None: p.kill()
        k32.FreeConsole()

def t_defender():
    mp = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"), "Windows Defender", "MpCmdRun.exe")
    if not os.path.exists(mp): bilgi("Defender: MpCmdRun.exe bu makinede yok; tarama yapilmadi"); return
    r = subprocess.run([mp, "-Scan", "-ScanType", "3", "-File", EXE, "-DisableRemediation"], capture_output=True, timeout=900)
    metin = " | ".join(x.strip() for x in (r.stdout + r.stderr).decode("mbcs", "replace").splitlines() if x.strip())[:500]
    if r.returncode in (0, 2): tamam("Defender dosyayi taradi ve tehdit bulmadi (cikis kodu %d)" % r.returncode, r.returncode == 0, metin)
    bilgi("Defender taramasi: cikis kodu %d; %s" % (r.returncode, ascii(metin)))

for ad, f in (("ortam", t_ortam), ("elle yazilmis beklentiler", t_elle), ("sayilar", t_sayilar), ("rastgele akislar", t_akislar), ("uclar", t_uclar), ("ucsuz arac", t_ucsuz), ("konsol", t_konsol), ("defender", t_defender)):
    dene(ad, f)
yaz("")
yaz("toplam: %d gecti, %d kaldi" % (sum(1 for s in satirlar if s.startswith("GECTI")), len(kalanlar)))
open(os.path.join(BURASI, "windows_python_sonucu.txt"), "w", encoding="ascii", errors="replace").write("\n".join(satirlar) + "\n")
sys.exit(1 if kalanlar else 0)
