#!/usr/bin/env python3
"""Deponun bütün çevrimdışı kontrollerini tek komutla, aynı sırayla çalıştırır.

Yerelde ve CI'da aynı liste koşar; böylece "bende geçti" ile "CI'da geçti" aynı
kontrol kümesine dayanır. Sağlayıcı, ağ veya canlı CLI çağrısı yoktur. Bir araç
(node, bash, pwsh) bulunmuyorsa o kontrol ATLANDI olarak yazılır; atlama başarı
sayılmaz ama çıkış kodunu da bozmaz. GitHub Actions altında her kontrol kendi
günlük grubunda açılır ve hatalar satır notu olarak işaretlenir.

Kullanım:
    python tools/dogrula.py              # hepsi
    python tools/dogrula.py --liste      # kontrol adlarını göster
    python tools/dogrula.py --sadece testler,semalar,tanim
    python tools/dogrula.py --ayrintili   # her kontrolün tam çıktısı (testler -v)
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

KOK = Path(__file__).resolve().parents[1]
PWSH_AYRISTIRMA = r"""
$bozuk = $false
Get-ChildItem -LiteralPath . -Filter *.ps1 -Recurse -File | Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' } | ForEach-Object {
  $hatalar = $null; $sozcukler = $null
  [void][System.Management.Automation.Language.Parser]::ParseFile($_.FullName, [ref]$sozcukler, [ref]$hatalar)
  if ($hatalar.Count -gt 0) { $hatalar | ForEach-Object { Write-Host $_ }; $bozuk = $true }
}
if ($bozuk) { exit 1 }
Write-Host 'PowerShell betikleri ayrıştırıldı.'
"""

# (ad, açıklama, komut, gereken araç veya None). Komutlar depo kökünde çalışır.
KONTROLLER: list[tuple[str, str, list[str], str | None]] = [
    ("testler", "Regresyon testleri (canlı sağlayıcı çağrısı yok)",
     [sys.executable, "-m", "unittest", "discover"], None),
    ("depo", "Köprü, ayna, kayıt bağları ve yapılandırma imzaları",
     [sys.executable, str(KOK / "tools/depo_kontrol.py")], None),
    ("okuma", "Statik okuma sayfalarının kaynak metinlerle uyumu",
     [sys.executable, str(KOK / "tools/okuma_yayini_uret.py"), "--check"], None),
    ("semalar", "JSON sözleşmelerinin desteklenen alt kümede kalması",
     [sys.executable, str(KOK / "tools/sema_denetle.py")], None),
    ("tanim", "Dokuz koordinatlı depo tanımının ölçümleri ve dayanakları",
     [sys.executable, str(KOK / "tools/depo_tanimi.py"), "--check"], None),
    ("sorular", "Şimdi ve sonrası kaydı: senaryolar, varyantlar, birleşimler ve belge tabloları",
     [sys.executable, str(KOK / "tools/simdi_ve_sonrasi.py"), "--check"], None),
    ("acilis", "Açılış: niyet ve altı ilke, kayıtla eşlik, yapı ve okunabilirlik",
     [sys.executable, str(KOK / "tools/acilis.py"), "--check"], None),
    ("yol", "Açılıştan gerçeğe yol: ölçütler, ön koşullar, açılışla tutarlılık ve iki belge",
     [sys.executable, str(KOK / "tools/yol.py"), "--check"], None),
    ("harita", "Depo haritası: her dosya tek alanda, eski adlar, künyeler ve harita belgesi",
     [sys.executable, str(KOK / "tools/harita.py"), "--check"], None),
    ("donusum", "Dönüşüm: aşamalar, son ölçüm ve prova, iki belgenin kayıtla eşliği",
     [sys.executable, str(KOK / "tools/donusum.py"), "--check"], None),
    ("arayuz", "Yerel arayüz JavaScript sözdizimi",
     ["node", "--check", str(KOK / "ui/deus/app.js")], "node"),
    ("gonderim", "Bulut gönderim betiğinin Bash sözdizimi",
     ["bash", "-n", str(KOK / ".github/scripts/kopru_gonder.sh")], "bash"),
    ("powershell", "Depodaki bütün PowerShell betiklerinin ayrıştırılması (windows/nt dahil)",
     ["pwsh", "-NoProfile", "-NonInteractive", "-Command", PWSH_AYRISTIRMA], "pwsh"),
]


# Windows'ta `bash` çoğu kez WSL başlatıcısına çıkar ve dağıtım kurulu değilse hata verir; bu kontrolleri
# Linux koşusu denetler (eski iş akışında da Bash sözdizimi yalnız Linux'ta koşuyordu).
YALNIZ_POSIX = {"gonderim"}
WINDOWS = os.name == "nt"


def calistir(ad: str, komut: list[str], gerekli: str | None) -> tuple[str, str, str]:
    """(durum, özet, tam çıktı) döndürür; durum TAMAM, BAŞARISIZ veya ATLANDI."""
    if ad in YALNIZ_POSIX and WINDOWS:
        return "ATLANDI", "Windows'ta atlanır; Linux koşusu denetler", ""
    if gerekli and not shutil.which(gerekli):
        return "ATLANDI", f"{gerekli} bulunamadı", ""
    ortam = {**os.environ, "PYTHONUTF8": "1", "PYTHONDONTWRITEBYTECODE": "1"}
    sonuc = subprocess.run(komut, cwd=KOK, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=ortam)
    cikti = (sonuc.stdout + sonuc.stderr).strip()
    son_satir = next((satir for satir in reversed(cikti.splitlines()) if satir.strip()), "")
    if sonuc.returncode == 0:
        return "TAMAM", son_satir or "sorunsuz (çıktı yok)", cikti
    return "BAŞARISIZ", son_satir or f"çıkış kodu {sonuc.returncode}", cikti


def main() -> int:
    for akis in (sys.stdout, sys.stderr):  # Windows konsolunda Türkçe durum adları için
        if hasattr(akis, "reconfigure"):
            akis.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--liste", action="store_true", help="kontrolleri çalıştırmadan listele")
    parser.add_argument("--sadece", help="virgülle ayrılmış kontrol adları")
    parser.add_argument("--ayrintili", action="store_true", help="her kontrolün tam çıktısını yaz; testler -v")
    args = parser.parse_args()
    secilen = {ad.strip() for ad in args.sadece.split(",")} if args.sadece else None
    bilinmeyen = (secilen or set()) - {ad for ad, *_ in KONTROLLER}
    if bilinmeyen:
        parser.error("bilinmeyen kontrol: " + ", ".join(sorted(bilinmeyen)))
    if args.liste:
        for ad, aciklama, _komut, gerekli in KONTROLLER:
            print(f"{ad:<11} {aciklama}" + (f" [{gerekli}]" if gerekli else ""))
        return 0
    actions = bool(os.environ.get("GITHUB_ACTIONS"))
    sonuclar = []
    for ad, aciklama, komut, gerekli in KONTROLLER:
        if secilen and ad not in secilen:
            continue
        if args.ayrintili and ad == "testler":
            komut = [*komut, "-v"]
        baslangic = time.monotonic()
        durum, ozet, cikti = calistir(ad, komut, gerekli)
        sure = time.monotonic() - baslangic
        sonuclar.append((ad, durum))
        if actions:
            print(f"::group::{ad} — {aciklama}")
        print(f"{durum:<9} {ad:<11} {ozet} ({sure:.1f} sn)")
        if durum == "BAŞARISIZ" or (args.ayrintili and cikti):
            print(cikti)
        if durum == "BAŞARISIZ" and actions:
            print(f"::error title={ad}::{ozet}")
        if actions:
            print("::endgroup::")
        sys.stdout.flush()
    basarisiz = [ad for ad, durum in sonuclar if durum == "BAŞARISIZ"]
    atlanan = [ad for ad, durum in sonuclar if durum == "ATLANDI"]
    print(f"{len(sonuclar) - len(basarisiz) - len(atlanan)} tamam, {len(basarisiz)} başarısız, {len(atlanan)} atlandı"
          + (f" ({', '.join(atlanan)})" if atlanan else ""))
    return 1 if basarisiz else 0


if __name__ == "__main__":
    raise SystemExit(main())
