# Ortak Köprü yerel izleyici: abonelikle çalışan CLI katmanları (Claude Code, Codex, Gemini CLI) üzerinden
# bekleyen kayıtlara cevap verir. API anahtarı kullanmaz; ayarlar-yerel.json'daki komutları çalıştırır.
#
#   pwsh -File kopru_izle.ps1              # beş dakikada bir döner
#   pwsh -File kopru_izle.ps1 -TekSefer    # bir kez çalışır, çıkar
#   pwsh -File kopru_izle.ps1 -Yalniz Claude   # yalnız bir katılımcı
#
# Bu dosya makineden bağımsızdır; makineye özgü ortam (PATH, Python yolu, katman Home'ları) kopru_yerel.ps1'de
# ve ayarlar-yerel.json'dadır. Windows'ta Kopru_Izle.cmd bu dosyayı o ortamla çağırır.
# Python: KOPRU_PYTHON ortam değişkeni (tam yol) ya da PATH'teki python / py.
param([int]$Dakika = 5, [switch]$TekSefer, [string]$Ayarlar = "ayarlar-yerel.json", [string]$Yalniz = "", [string]$Dal = "main")
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

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
  try {
    $zaman = Get-Date -Format 'HH:mm'
    # Önce eşitle: yerelde gönderilmemiş commit ya da değişiklik varsa kopru_gonder.ps1 birleştirip gönderir; yoksa düz ileri sarılır.
    git fetch -q origin $Dal
    $ileride = [int](git rev-list --count "origin/$Dal..HEAD")
    $kirli = @(git status --porcelain -- . ":!yanit*.json" ":!istem*.txt").Count
    if ($ileride -gt 0 -or $kirli -gt 0) {
      pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File kopru_gonder.ps1 -Dal $Dal
    } elseif ([int](git rev-list --count "HEAD..origin/$Dal") -gt 0) {
      git merge -q --ff-only "origin/$Dal"
    }
    $once = Kayit-Sayisi
    & $pyExe @pyArgs -I -X utf8 kopru_yanitla.py kopru.html --ayarlar $Ayarlar @ekArg
    if ($LASTEXITCODE -ne 0) { Write-Warning "$zaman bot hata ile bitti (çıkış kodu $LASTEXITCODE)" }
    $sonra = Kayit-Sayisi
    if ($sonra -gt $once) {
      pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File kopru_gonder.ps1 -Dal $Dal -Bot   # [skip ci]: botlar birbirini tetiklemez, saatlik zamanlayıcı toplar
    } else {
      Write-Host "$zaman yeni kayıt yok ($once kayıt)"
    }
  } catch {
    Write-Warning $_.Exception.Message
  }
  if ($TekSefer) { break }
  Start-Sleep -Seconds ($Dakika * 60)
}
