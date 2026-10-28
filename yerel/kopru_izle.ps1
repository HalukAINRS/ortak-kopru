# Ortak Köprü yerel izleyici: abonelikle çalışan CLI katmanları (Claude Code, Codex, Google CLI izleyicisi) üzerinden
# bekleyen kayıtlara cevap verir. API anahtarı kullanmaz; katilimcilar/ayarlar-yerel.json'daki komutları çalıştırır.
#
#   pwsh -File yerel/kopru_izle.ps1              # beş dakikada bir döner
#   pwsh -File yerel/kopru_izle.ps1 -TekSefer    # bir kez çalışır, çıkar
#   pwsh -File yerel/kopru_izle.ps1 -Yalniz Claude   # yalnız bir katılımcı
#   -Ayarlar YOL (varsayılan katilimcilar/ayarlar-yerel.json), -Dal AD (izleyicinin çalışacağı dal, varsayılan main)
#
# Bu dosya makineden bağımsızdır; makineye özgü ortam (PATH, Python yolu, katman Home'ları) kopru_yerel.ps1'de
# ve katilimcilar/ayarlar-yerel.json'dadır. Windows'ta Kopru_Izle.cmd bu dosyayı o ortamla çağırır.
# Python: KOPRU_PYTHON ortam değişkeni (tam yol) ya da PATH'teki python / py.
param([int]$Dakika = 5, [switch]$TekSefer, [string]$Ayarlar = "katilimcilar/ayarlar-yerel.json", [string]$Yalniz = "", [string]$Dal = "main")
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath (Split-Path -Parent $PSScriptRoot)   # betikler yerel/ altında; çalışma yeri depo köküdür

$aktifDal = git symbolic-ref --quiet --short HEAD
if ($LASTEXITCODE -ne 0 -or $aktifDal -ne $Dal) { throw "İzleyici '$Dal' dalında çalışmalı; mevcut dal: $aktifDal." }

function Bul-Python {
  if ($env:KOPRU_PYTHON -and (Test-Path -LiteralPath $env:KOPRU_PYTHON)) { return @($env:KOPRU_PYTHON) }
  foreach ($aday in @("python3", "python")) {
    $k = Get-Command $aday -ErrorAction SilentlyContinue
    if ($k -and $k.Source -notmatch "WindowsApps") { return @($k.Source) }   # Microsoft Store yer tutucusunu atla
  }
  $py = Get-Command py -ErrorAction SilentlyContinue
  if ($py) { return @($py.Source, "-3") }
  throw "Python bulunamadı. Taşınabilir Python'u Runtime\Python altına aç ya da KOPRU_PYTHON değişkenini ayarla (bkz. kopru_yerel.ps1)."
}
$python = @(Bul-Python)   # tek öge dönerse de dizi kalsın
$pyExe = $python[0]
$pyArgs = @()
if ($python.Count -gt 1) { $pyArgs = @($python[1..($python.Count-1)]) }
if (-not (Test-Path -LiteralPath $Ayarlar)) { throw "Ayar dosyası yok: $Ayarlar" }

function Kayit-Sayisi { (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches.Count }

$ekArg = @()
if ($Yalniz) { $ekArg = @("--yalniz", $Yalniz) }

while ($true) {
  $turHata = $false
  try {
    $zaman = Get-Date -Format 'HH:mm'
    $aktifDal = git symbolic-ref --quiet --short HEAD
    if ($LASTEXITCODE -ne 0 -or $aktifDal -ne $Dal) { throw "İzleyici '$Dal' dalında çalışmalı; bu tur katılımcı çağrılmadı." }
    # Önce eşitle: yerelde gönderilmemiş commit ya da gönderim kapsamında değişiklik varsa kopru_gonder.ps1 birleştirip gönderir; yoksa düz ileri sarılır.
    git fetch -q origin $Dal
    if ($LASTEXITCODE -ne 0) { throw "Uzak depo alınamadı; bu tur katılımcı çağrılmadı." }
    $ileride = git rev-list --count "origin/$Dal..HEAD"
    if ($LASTEXITCODE -ne 0) { throw "Yerel/uzak dal karşılaştırılamadı." }
    $geride = git rev-list --count "HEAD..origin/$Dal"
    if ($LASTEXITCODE -ne 0) { throw "Uzak/yerel dal karşılaştırılamadı." }
    # Yalnız gönderim kapsamındaki değişiklikler (defter, ayna, çağrı kayıtları) göndericiyi çağırır; başka yerel değişiklikler yerelde kalır.
    $kirli = @(git status --porcelain -- kopru.html ayna/kopru.html kayit).Count
    if ($LASTEXITCODE -ne 0) { throw "Çalışma ağacının durumu okunamadı." }
    if ([int]$ileride -gt 0 -or $kirli -gt 0) {
      pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot "kopru_gonder.ps1") -Dal $Dal
      if ($LASTEXITCODE -ne 0) { throw "Eşitleme başarısız; bu tur katılımcı çağrılmadı." }
    } elseif ([int]$geride -gt 0) {
      git merge -q --ff-only "origin/$Dal"
      if ($LASTEXITCODE -ne 0) { throw "Uzak değişiklikler alınamadı; bu tur katılımcı çağrılmadı." }
    }
    $once = Kayit-Sayisi
    & $pyExe @pyArgs -I -X utf8 defter/kopru_yanitla.py kopru.html --ayarlar $Ayarlar @ekArg
    if ($LASTEXITCODE -ne 0) { $turHata = $true; Write-Warning "$zaman bot hata ile bitti (çıkış kodu $LASTEXITCODE)" }
    $sonra = Kayit-Sayisi
    $yeniDosyalar = @(git status --porcelain -- kopru.html kayit ayna/kopru.html)
    if ($LASTEXITCODE -ne 0) { throw "Tur çıktılarının durumu okunamadı." }
    if ($sonra -gt $once -or $yeniDosyalar.Count -gt 0) {
      pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot "kopru_gonder.ps1") -Dal $Dal -Bot   # [skip ci]: botlar birbirini tetiklemez, saatlik zamanlayıcı toplar
      if ($LASTEXITCODE -ne 0) { throw "Yeni kayıtlar gönderilemedi; yerel kopyada korunuyor." }
    } else {
      Write-Host "$zaman yeni kayıt yok ($once kayıt)"
    }
  } catch {
    $turHata = $true
    Write-Warning $_.Exception.Message
  }
  if ($TekSefer) { if ($turHata) { exit 1 }; exit 0 }
  Start-Sleep -Seconds ($Dakika * 60)
}
