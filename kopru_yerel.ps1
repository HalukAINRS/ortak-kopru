# Ortak Köprü — senin makinen için ortam ve kapı. Kopru_Izle.cmd bu dosyayı çağırır.
#
#   Kopru_Izle.cmd                 → Izle: beş dakikada bir bekleyenleri CLI'larla yanıtlar, gönderir (pencere açık kalır)
#   Kopru_Izle.cmd Hazirlik        → her parçayı denetler, eksikleri ve ne yapılacağını yazar; model çağırmaz
#   Kopru_Izle.cmd Tek             → bir tur çalışır, çıkar; "Tek Copilot" yalnız o katılımcı
#   Kopru_Izle.cmd Ekle dosya.json → JSON'daki kaydı sayfaya ekler (ör. davet-copilot.json), sonra Gonder gerekir
#   Kopru_Izle.cmd Bolum parca.html → “Yönlendirme dosyası”na alt bölüm ekler/yeniler (ör. bolum-guncel-2026-10-24.html), sonra Gonder
#   Kopru_Izle.cmd Gonder          → sayfayı denetler, değişiklikleri commit edip GitHub'a gönderir
#   Kopru_Izle.cmd VM              → Hacker sanal makinesini başlatır (Hacker_Baslat.ps1 -Mod Kontrol)
#   Kopru_Izle.cmd CopilotKontrol  → Copilot CLI'a Şahit ortamında küçük bir deneme sorusu sorar (giriş sınaması)
#
# Yollar Hacker_Baslat.ps1, Saman_Baslat.ps1, Sahit_Baslat.ps1 ve HalukAI_Ortam.ps1'dekilerle aynı; kurulum değişirse
# burada ve ayarlar-yerel.json'da düzelt. Bu dosya makineye özgüdür; makineden bağımsız izleyici kopru_izle.ps1'dir.
param(
  [ValidateSet("Izle", "Hazirlik", "Tek", "Ekle", "Bolum", "Gonder", "VM", "CopilotKontrol")][string]$Mod = "Izle",
  [string]$Secenek = "",
  [int]$Dakika = 5,
  [string]$Yalniz = ""
)
$ErrorActionPreference = "Continue"
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch {}

# ---- Yollar ----
$Katmanlar    = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari"
$OrtamBetigi  = "Y:\HalukAI\HalukAI_Ortam.ps1"
$PythonExe    = "$Katmanlar\Runtime\Python\python.exe"
$PythonIndir  = "https://www.python.org/ftp/python/3.14.9/python-3.14.9-embed-amd64.zip"
$SshExe       = "$Katmanlar\Runtime\Git-Portable-2.56.0.2\usr\bin\ssh.exe"
$SshAnahtar   = "$Katmanlar\01_Claude_Code_Hacker\Home\.ssh\hacker_arm64_035"
$SshBilinen   = "$Katmanlar\01_Claude_Code_Hacker\Home\.ssh\known_hosts"   # VM sunucu anahtarı burada sabit (Haluk, 24 Eki)
$ClaudeVm     = "/home/hacker/bin/claude-arm64-035"                              # VM içindeki Claude Code sarmalayıcısı
$HackerBaslat = "$Katmanlar\01_Claude_Code_Hacker\Hacker_Baslat.ps1"
$CodexExe     = "$Katmanlar\03_Codex_Saman\npm_global\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\bin\codex.exe"
$SamanHome    = "$Katmanlar\03_Codex_Saman\Home"
$CopilotExe   = "$Katmanlar\Runtime\Copilot-1.0.103-win-x64\copilot.exe"
$SahitHome    = "$Katmanlar\02_Copilot_Sahit\Home"
$DepoYolu     = "Y:/HalukAI/Ortak_Kopru/kopru"      # git safe.directory eğik çizgi ister
$SshOrtak     = @("-p", "2222", "-i", $SshAnahtar, "-o", "BatchMode=yes", "-o", "UserKnownHostsFile=$SshBilinen",
                  "-o", "StrictHostKeyChecking=yes", "-o", "LogLevel=ERROR", "-o", "ConnectTimeout=10", "hacker@127.0.0.1")

# ---- Ortam ----
if (Test-Path -LiteralPath $OrtamBetigi) { . $OrtamBetigi } else { Write-Warning "Ortam betiği yok: $OrtamBetigi (PATH eksik kalabilir)" }
$env:PYTHONUTF8 = "1"
if (Test-Path -LiteralPath $PythonExe) { $env:KOPRU_PYTHON = $PythonExe }
foreach ($k in @("X:\Windows\Temp\Saman_Temp", "X:\Windows\Temp\Sahit_Temp", "X:\Windows\Temp\Sahit_NodeCache")) {
  try { New-Item -Path $k -ItemType Directory -Force -ErrorAction SilentlyContinue | Out-Null } catch {}
}
Set-Location -LiteralPath $PSScriptRoot
# WinPE her açılışta git'in global ayarını sıfırlar; exFAT'taki depo için safe.directory her seferinde eklenir.
if (Get-Command git -ErrorAction SilentlyContinue) {
  $guvenli = @(git config --global --get-all safe.directory 2>$null)
  if ($guvenli -notcontains $DepoYolu) { git config --global --add safe.directory $DepoYolu }
}

function Port-Acik([int]$Port) {
  try { $s = [System.Net.Sockets.TcpClient]::new("127.0.0.1", $Port); $s.Dispose(); return $true } catch { return $false }
}

function Bul-PyYol {
  if ($env:KOPRU_PYTHON) { return $env:KOPRU_PYTHON }
  $k = Get-Command python -ErrorAction SilentlyContinue
  if ($k -and $k.Source -notmatch "WindowsApps") { return $k.Source }
  return $null
}

function Sahit-Ortami {
  # Sahit_Baslat.ps1 ile aynı değerler; yalnız bu süreç için.
  $env:HOME = $SahitHome; $env:USERPROFILE = $SahitHome
  $env:COPILOT_HOME = "$SahitHome\.copilot"
  $env:COPILOT_CACHE_HOME = "X:\Windows\Temp\Sahit_Temp"; $env:NODE_COMPILE_CACHE = "X:\Windows\Temp\Sahit_NodeCache"
  $env:TEMP = "X:\Windows\Temp\Sahit_Temp"; $env:TMP = "X:\Windows\Temp\Sahit_Temp"
  $env:COPILOT_AUTO_UPDATE = "false"
}

switch ($Mod) {

  "VM" {
    & pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File $HackerBaslat -Mod Kontrol
  }

  "Gonder" {
    & "$PSScriptRoot\kopru_gonder.ps1"
  }

  "Ekle" {
    $py = Bul-PyYol
    if (-not $py) { Write-Error "Python yok (bkz. Hazirlik)."; return }
    if (-not $Secenek -or -not (Test-Path -LiteralPath $Secenek)) { Write-Error "Eklenecek JSON dosyasını ver: Kopru_Izle.cmd Ekle davet-copilot.json"; return }
    $kid = (& $py -I -X utf8 kopru_ekle.py kopru.html --json $Secenek 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) { Write-Error "Eklenmedi: $kid"; return }
    Write-Host "Eklendi: $kid" -ForegroundColor Green
    & $py -I -X utf8 kopru_ekle.py kopru.html --kontrol
    Write-Host "Göndermek için: Kopru_Izle.cmd Gonder" -ForegroundColor Cyan
  }

  "Bolum" {
    $py = Bul-PyYol
    if (-not $py) { Write-Error "Python yok (bkz. Hazirlik)."; return }
    if (-not $Secenek -or -not (Test-Path -LiteralPath $Secenek)) { Write-Error "Parça dosyasını ver: Kopru_Izle.cmd Bolum bolum-guncel-2026-10-24.html"; return }
    & $py -I -X utf8 kopru_bolum_ekle.py kopru.html $Secenek
    if ($LASTEXITCODE -ne 0) { return }
    & $py -I -X utf8 kopru_ekle.py kopru.html --kontrol
    Write-Host "Göndermek için: Kopru_Izle.cmd Gonder (ayna da yenilenmeli; Claude bu sohbette yapar)" -ForegroundColor Cyan
  }

  "CopilotKontrol" {
    if (-not (Test-Path -LiteralPath $CopilotExe)) { Write-Error "copilot.exe yok: $CopilotExe"; return }
    Sahit-Ortami
    Write-Host "Copilot CLI'a Şahit ortamında soruluyor (tek kısa çağrı)..." -ForegroundColor Cyan
    $cevap = ("Yalniz OK yaz, baska hicbir sey yazma." | & $CopilotExe -s --no-color --no-auto-update --disable-client-telemetry --disable-builtin-mcps --no-custom-instructions --no-ask-user --sync-session off --allow-all-tools --deny-tool "shell,write" 2>&1 | Out-String).Trim()
    Write-Host "Çıkış kodu: $LASTEXITCODE" -ForegroundColor $(if ($LASTEXITCODE -eq 0) { "Green" } else { "Yellow" })
    Write-Host "Cevap: $cevap"
    if ($cevap -match "(?i)login|authenticat|token") { Write-Host "Giriş gerekiyor: Sahit_Baslat.ps1 ile Copilot'u aç, içinde /login yaz; sonra bu kontrolü yinele." -ForegroundColor Yellow }
  }

  "Hazirlik" {
    $satirlar = New-Object System.Collections.Generic.List[object]
    function Ekle($bilesen, $durum, $not) { $satirlar.Add([PSCustomObject]@{ Bilesen = $bilesen; Durum = $durum; Not = $not }) }

    # 1. Depo
    $gitVar = [bool](Get-Command git -ErrorAction SilentlyContinue)
    if (-not $gitVar) { Ekle "Depo" "EKSİK" "git PATH'te yok; HalukAI_Ortam.ps1 yüklenmedi mi?" }
    else {
      $icerde = (git rev-parse --is-inside-work-tree 2>$null)
      if ($icerde -ne "true") { Ekle "Depo" "EKSİK" "Bu klasör git deposu değil: $PSScriptRoot" }
      else {
        $uzak = (git remote get-url origin 2>$null)
        $kirli = @(git status --porcelain 2>$null).Count
        $dal = (git rev-parse --abbrev-ref HEAD 2>$null)
        Ekle "Depo" "TAMAM" "$uzak · dal $dal · gönderilmemiş değişiklik: $kirli dosya"
      }
    }

    # 2. Python
    $pyYol = Bul-PyYol
    if ($pyYol) { $surum = (& $pyYol --version 2>&1); Ekle "Python" "TAMAM" "$surum · $pyYol" }
    else { Ekle "Python" "EKSİK" "Chrome'da indir: $PythonIndir → 7-Zip ile şuraya aç (içinde doğrudan python.exe olacak): $Katmanlar\Runtime\Python\" }

    # 3. Codex (Şaman)
    if (Test-Path -LiteralPath $CodexExe) {
      $cv = (& $CodexExe --version 2>&1 | Select-Object -First 1)
      $giris = Test-Path -LiteralPath "$SamanHome\.codex\auth.json"
      Ekle "Codex (ChatGPT)" $(if ($giris) { "TAMAM" } else { "GİRİŞ YOK" }) "$cv · giriş dosyası: $(if ($giris) { 'var' } else { 'yok → Saman_Baslat.ps1 ile açıp codex login' })"
    } else { Ekle "Codex (ChatGPT)" "EKSİK" "codex.exe yok: $CodexExe" }

    # 4. Copilot CLI (Şahit)
    if (Test-Path -LiteralPath $CopilotExe) {
      $cpv = (& $CopilotExe --version 2>&1 | Select-Object -First 1)
      $cfg = Test-Path -LiteralPath "$SahitHome\.copilot"
      Ekle "Copilot (Şahit)" $(if ($cfg) { "TAMAM" } else { "KLASÖR YOK" }) "$cpv · Home: $(if ($cfg) { 'var' } else { "yok: $SahitHome\.copilot" }) · giriş sınaması: Kopru_Izle.cmd CopilotKontrol"
    } else { Ekle "Copilot (Şahit)" "EKSİK" "copilot.exe yok: $CopilotExe" }

    # 5. Hacker VM (Claude)
    if (Port-Acik 2222) {
      $cl = (& $SshExe @SshOrtak "$ClaudeVm --version" 2>&1 | Select-Object -Last 1)
      if ($LASTEXITCODE -eq 0) { Ekle "Claude (Hacker VM)" "TAMAM" "ssh tamam · $cl" }
      else { Ekle "Claude (Hacker VM)" "SORUN" "ssh/claude cevap vermedi: $cl (known_hosts yoksa: Hacker_Baslat.ps1 ile bir kez elle bağlanıp anahtarı kaydet)" }
    } else { Ekle "Claude (Hacker VM)" "KAPALI" "2222 kapalı → Kopru_Izle.cmd VM (QEMU açılır, 1-2 dk). VM kapalıyken Claude sessiz kalır." }

    # 6. Sayfa denetimi ve bekleyenler
    if ($pyYol) {
      $den = (& $pyYol -I -X utf8 kopru_ekle.py kopru.html --kontrol 2>&1 | Out-String).Trim()
      Ekle "Sayfa denetimi" $(if ($LASTEXITCODE -eq 0) { "TAMAM" } else { "SORUN" }) $den
      foreach ($ad in @("Claude", "ChatGPT", "Copilot")) {
        $j = (& $pyYol -I -X utf8 kopru_yanitla.py kopru.html --bekleyenler $ad 2>&1 | Out-String)
        try { $n = @((ConvertFrom-Json $j)).Count } catch { $n = "?" }
        $ipucu = if ($ad -eq "Copilot" -and $n -eq 0) { "henüz ona yazılmış kayıt yok → Kopru_Izle.cmd Ekle davet-copilot.json" } else { "ilk turda bu kayıtlara tek yanıt yazar" }
        Ekle "Bekleyen → $ad" "$n kayıt" $ipucu
      }
    } else { Ekle "Sayfa denetimi" "ATLANDI" "Python yok" }

    $satirlar | Format-Table -AutoSize -Wrap | Out-String -Width 170 | Write-Host
    Write-Host "Her satır TAMAM ise:  Kopru_Izle.cmd Tek   (bir tur)   →   Kopru_Izle.cmd   (sürekli)" -ForegroundColor Cyan
  }

  "Tek" {
    if (-not $Yalniz -and $Secenek) { $Yalniz = $Secenek }
    if (-not (Port-Acik 2222)) { Write-Warning "Hacker VM kapalı (2222); Claude bu turda sessiz kalır. Açmak için: Kopru_Izle.cmd VM" }
    & "$PSScriptRoot\kopru_izle.ps1" -TekSefer -Yalniz $Yalniz
  }

  default {   # Izle
    if (-not $Yalniz -and $Secenek) { $Yalniz = $Secenek }
    if (-not (Port-Acik 2222)) { Write-Warning "Hacker VM kapalı (2222); Claude açılana kadar sessiz kalır. Açmak için ayrı pencerede: Kopru_Izle.cmd VM" }
    Write-Host "İzleyici başladı: $Dakika dakikada bir. Durdurmak için Ctrl+C." -ForegroundColor Cyan
    & "$PSScriptRoot\kopru_izle.ps1" -Dakika $Dakika -Yalniz $Yalniz
  }
}
