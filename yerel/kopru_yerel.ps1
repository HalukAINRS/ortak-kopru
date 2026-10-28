# Ortak Köprü — senin makinen için ortam ve kapı. Kopru_Izle.cmd bu dosyayı çağırır.
#
#   Kopru_Izle.cmd                 → Izle: beş dakikada bir bekleyenleri CLI'larla yanıtlar, gönderir (pencere açık kalır)
#   Kopru_Izle.cmd Hazirlik        → her parçayı denetler, eksikleri ve ne yapılacağını yazar; model çağırmaz
#   Kopru_Izle.cmd Tek             → bir tur çalışır, çıkar; "Tek Copilot" yalnız o katılımcı
#   Kopru_Izle.cmd Ekle kayit.json → JSON'daki kaydı deftere ekler (biçim: katilimcilar/yanit-sablonu.json), sonra Gonder gerekir
#   Kopru_Izle.cmd Gonder          → sayfayı denetler, değişiklikleri commit edip GitHub'a gönderir
#   Kopru_Izle.cmd VM              → Hacker sanal makinesini başlatır (Hacker_Baslat.ps1 -Mod Kontrol)
#   Kopru_Izle.cmd CopilotKontrol  → Copilot CLI'a Şahit ortamında küçük bir deneme sorusu sorar (giriş sınaması)
#   Kopru_Izle.cmd CodexGiris      → Şaman ortamında `codex login` (tarayıcı); "CodexGiris Cihaz" cihaz kodu akışı; "CodexGiris Durum" yalnız durum
#   Kopru_Izle.cmd CopilotGiris    → Şahit ortamında `copilot login` (tarayıcı); "CopilotGiris Cihaz" cihaz kodu akışı
#   Kopru_Izle.cmd CodexTani       → Codex tanısı: ortam, config.toml yetki satırları, auth.json alan adları, arg0 geçici klasörleri, kısa deneme çağrısı (değer yazmaz)
#   Kopru_Izle.cmd Arg0Temizle     → Codex'in silemediği eski arg0 klasörlerini kilidi tutulmayanlardan başlayarak siler (önce kilit dosyası kapatılır)
#   Parametreler: -Dakika N (izleme aralığı, varsayılan 5), -Yalniz AD (Tek ve Izle'de yalnız bir katılımcı), -Secenek (kipin argümanı)
#
# Gerekenler: Windows, PowerShell 7, Git, Python 3.12+. Bu dosya makineye özgüdür; makineden bağımsız izleyici kopru_izle.ps1'dir.
# Yollar ilk kurulan makinenin düzenine göredir ve katilimcilar/ayarlar-yerel.json'daki yollarla AYNI DEĞİLDİR (biri
# Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari, öbürü Y:\archive\… altını gösterir); yeniden kurarken ikisi aynı yere bağlanır.
# Köprü klasörü (Haluk, 28 Ekim 2026 19.53 UTC): Y:\HalukAI\ortak-kopru. Depo yolu sabit yazılmaz, betiğin konumundan
# türer. Kurulum ve bilinen uyuşmazlıklar: docs/teknik/yerel-taraf.md
param(
  [ValidateSet("Izle", "Hazirlik", "Tek", "Ekle", "Gonder", "VM", "CopilotKontrol", "CodexGiris", "CopilotGiris", "CodexTani", "Arg0Temizle")][string]$Mod = "Izle",
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
$SshOrtak     = @("-p", "2222", "-i", $SshAnahtar, "-o", "BatchMode=yes", "-o", "UserKnownHostsFile=$SshBilinen",
                  "-o", "StrictHostKeyChecking=yes", "-o", "LogLevel=ERROR", "-o", "ConnectTimeout=10", "hacker@127.0.0.1")

# ---- Ortam ----
if (Test-Path -LiteralPath $OrtamBetigi) { . $OrtamBetigi } else { Write-Warning "Ortam betiği yok: $OrtamBetigi (PATH eksik kalabilir)" }
$env:PYTHONUTF8 = "1"
if (Test-Path -LiteralPath $PythonExe) { $env:KOPRU_PYTHON = $PythonExe }
foreach ($k in @("X:\Windows\Temp\Saman_Temp", "X:\Windows\Temp\Sahit_Temp", "X:\Windows\Temp\Sahit_NodeCache")) {
  try { New-Item -Path $k -ItemType Directory -Force -ErrorAction SilentlyContinue | Out-Null } catch {}
}
$DepoKoku = Split-Path -Parent $PSScriptRoot   # betikler yerel/ altında; çalışma yeri depo köküdür
$DepoYolu = $DepoKoku -replace '\\', '/'      # git safe.directory eğik çizgi ister; yol betiğin konumundan türer
Set-Location -LiteralPath $DepoKoku
# WinPE her açılışta git'in global ayarını sıfırlar; exFAT'taki depo için safe.directory her seferinde eklenir.
# Yan etki: $DepoYolu Git'in GENEL ayarına eklenir. Geri almak için: git config --global --unset-all safe.directory $DepoYolu
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

function Saman-Ortami {
  # Saman_Baslat.ps1 ile aynı değerler; yalnız bu süreç için.
  $env:HOME = $SamanHome; $env:USERPROFILE = $SamanHome
  $env:CODEX_HOME = "$SamanHome\.codex"
  $env:APPDATA = "$SamanHome\AppData\Roaming"; $env:LOCALAPPDATA = "$SamanHome\AppData\Local"
  $env:TEMP = "X:\Windows\Temp\Saman_Temp"; $env:TMP = "X:\Windows\Temp\Saman_Temp"
  foreach ($k in @($env:CODEX_HOME, $env:APPDATA, $env:LOCALAPPDATA)) { New-Item -Path $k -ItemType Directory -Force -ErrorAction SilentlyContinue | Out-Null }
}

function Arg0-Listele {
  $kok = Join-Path $env:CODEX_HOME "tmp\arg0-windows"
  if (-not (Test-Path -LiteralPath $kok)) { Write-Host "  yok: $kok"; return }
  $dirs = @(Get-ChildItem -LiteralPath $kok -Directory | Sort-Object LastWriteTime)
  Write-Host "  $($dirs.Count) klasör; en eski: $(if ($dirs) { $dirs[0].LastWriteTime } else { '-' }) · en yeni: $(if ($dirs) { $dirs[-1].LastWriteTime } else { '-' })"
  foreach ($d in $dirs | Select-Object -Last 3) {
    $dosyalar = (Get-ChildItem -LiteralPath $d.FullName -Force | ForEach-Object { "$($_.Name) ($($_.Length) B)" }) -join ", "
    Write-Host "  $($d.Name) [$($d.LastWriteTime.ToString('HH:mm:ss'))]: $dosyalar"
  }
  $bat = Get-ChildItem -LiteralPath $kok -Recurse -Filter "apply_patch.bat" -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($bat) { Write-Host "  örnek apply_patch.bat içeriği:"; Get-Content -LiteralPath $bat.FullName | ForEach-Object { "    $_" } }
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
    if (-not $Secenek -or -not (Test-Path -LiteralPath $Secenek)) { Write-Error "Eklenecek JSON dosyasını ver: Kopru_Izle.cmd Ekle kayit.json (biçim: katilimcilar/yanit-sablonu.json)"; return }
    $kid = (& $py -I -X utf8 defter/kopru_ekle.py kopru.html --json $Secenek 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) { Write-Error "Eklenmedi: $kid"; return }
    Write-Host "Eklendi: $kid" -ForegroundColor Green
    & $py -I -X utf8 defter/kopru_ekle.py kopru.html --kontrol
    Write-Host "Göndermek için: Kopru_Izle.cmd Gonder" -ForegroundColor Cyan
  }

  "CodexGiris" {
    if (-not (Test-Path -LiteralPath $CodexExe)) { Write-Error "codex.exe yok: $CodexExe"; return }
    Saman-Ortami
    & $CodexExe --version
    # WinPE'de Windows kimlik deposu süreçler/açılışlar arasında kalmıyor; giriş dosyaya (auth.json) yazılsın.
    $cfg = Join-Path $env:CODEX_HOME "config.toml"
    $icerik = if (Test-Path -LiteralPath $cfg) { Get-Content -LiteralPath $cfg -Raw } else { "" }
    if ($icerik -notmatch '(?m)^\s*cli_auth_credentials_store\s*=') {
      Set-Content -LiteralPath $cfg -Value ('cli_auth_credentials_store = "file"' + "`n" + $icerik) -Encoding utf8NoBOM -NoNewline
      Write-Host "config.toml: cli_auth_credentials_store = `"file`" eklendi (giriş $env:CODEX_HOME\auth.json dosyasına yazılacak)." -ForegroundColor Yellow
    } elseif ($icerik -match '(?m)^\s*cli_auth_credentials_store\s*=\s*"(?!file")') {
      Write-Warning "config.toml'da cli_auth_credentials_store 'file' değil; WinPE'de giriş kalıcı olmaz. Satırı 'file' yap."
    }
    if ($Secenek -eq "Durum") { & $CodexExe login status; return }
    if ($Secenek -eq "Cihaz") {
      Write-Host "Cihaz kodu akışı: yazılan adresi Chrome'da aç, kodu gir, ChatGPT Pro hesabınla onayla." -ForegroundColor Cyan
      & $CodexExe login --device-auth
    } else {
      Write-Host "Tarayıcı açılacak; açılmazsa terminaldeki adresi Chrome'a kopyala. 'Sign in with ChatGPT' → Pro hesabınla onayla → buraya dön." -ForegroundColor Cyan
      Write-Host "Giriş $env:CODEX_HOME\auth.json dosyasına yazılır (izleyici Şaman'ı katilimcilar/ayarlar-yerel.json'daki Home ile çağırır; ikisinin aynı olduğunu denetleyin)." -ForegroundColor Cyan
      & $CodexExe login
    }
    Write-Host "--- durum ---" -ForegroundColor Cyan
    & $CodexExe login status
    Write-Host "Sonraki: Kopru_Izle.cmd Tek ChatGPT" -ForegroundColor Cyan
  }

  "CodexTani" {
    if (-not (Test-Path -LiteralPath $CodexExe)) { Write-Error "codex.exe yok: $CodexExe"; return }
    Saman-Ortami
    Write-Host "--- ortam ---" -ForegroundColor Cyan
    foreach ($d in @("OPENAI_API_KEY", "CODEX_API_KEY", "OPENAI_BASE_URL", "CODEX_HOME", "HOME", "USERPROFILE")) {
      $v = [Environment]::GetEnvironmentVariable($d)
      if ($d -like "*KEY*") { Write-Host ("  {0}: {1}" -f $d, $(if ($v) { "VAR ($($v.Length) karakter) ← Codex'i API yoluna saptırır" } else { "yok" })) }
      else { Write-Host ("  {0}: {1}" -f $d, $v) }
    }
    foreach ($kapsam in @("User", "Machine")) {
      $v = [Environment]::GetEnvironmentVariable("OPENAI_API_KEY", $kapsam)
      if ($v) { Write-Host "  OPENAI_API_KEY $kapsam kapsamında kayıtlı (VAR)" -ForegroundColor Yellow }
    }
    $cfg = Join-Path $env:CODEX_HOME "config.toml"
    Write-Host "--- $cfg ---" -ForegroundColor Cyan
    if (Test-Path -LiteralPath $cfg) {
      $satirlar = Select-String -LiteralPath $cfg -Pattern '^\s*(model_provider|preferred_auth_method|model|model_reasoning_effort|wire_api|base_url|env_key|chatgpt_base_url|openai_api_key|name|requires_openai_auth)\s*=|^\s*\[' 
      if ($satirlar) { $satirlar | ForEach-Object { "  {0}: {1}" -f $_.LineNumber, ($_.Line -replace '(?i)((?:openai_)?api_key\s*=\s*").*?(")', '$1<gizli>$2') } } else { "  (yetki/sağlayıcı satırı yok)" }
    } else { "  yok" }
    $auth = Join-Path $env:CODEX_HOME "auth.json"
    Write-Host "--- $auth ---" -ForegroundColor Cyan
    if (Test-Path -LiteralPath $auth) {
      try {
        $j = Get-Content -LiteralPath $auth -Raw | ConvertFrom-Json
        $alanlar = $j.PSObject.Properties.Name
        Write-Host "  alanlar: $($alanlar -join ', ')"
        if ($alanlar -contains "auth_mode") { Write-Host "  auth_mode: $($j.auth_mode)" }
        if ($alanlar -contains "OPENAI_API_KEY") { Write-Host "  OPENAI_API_KEY alanı: $(if ($j.OPENAI_API_KEY) { 'DOLU ← API yoluna saptırabilir' } else { 'boş' })" }
        if ($alanlar -contains "tokens") { Write-Host "  tokens alanları: $(($j.tokens.PSObject.Properties.Name) -join ', ')" }
        if ($alanlar -contains "last_refresh") { Write-Host "  last_refresh: $($j.last_refresh)" }
        Write-Host "  dosya zamanı: $((Get-Item -LiteralPath $auth).LastWriteTime)"
      } catch { Write-Host "  okunamadı: $($_.Exception.Message)" }
    } else { Write-Host '  yok (giriş kimlik deposunda olabilir; config.toml''a cli_auth_credentials_store = "file" ekleyip CodexGiris yinele)' }
    Write-Host "--- arg0 geçici klasörleri ($env:CODEX_HOME\tmp\arg0-windows) ---" -ForegroundColor Cyan
    Arg0-Listele
    try { $v = Get-Volume -DriveLetter ($SamanHome.Substring(0,1)) -ErrorAction Stop; Write-Host "  sürücü $($SamanHome.Substring(0,2)) dosya sistemi: $($v.FileSystemType)" } catch { Write-Host "  dosya sistemi okunamadı: $($_.Exception.Message)" }
    Write-Host "--- codex login status ---" -ForegroundColor Cyan
    & $CodexExe login status 2>&1 | Select-Object -Last 3
    Write-Host "--- deneme: codex exec ---" -ForegroundColor Cyan
    $env:OPENAI_API_KEY = $null; $env:CODEX_API_KEY = $null
    "Yalniz OK yaz, baska hicbir sey yazma." | & $CodexExe exec --skip-git-repo-check - 2>&1 | Select-Object -Last 12
    Write-Host "çıkış kodu: $LASTEXITCODE"
  }

  "Arg0Temizle" {
    Saman-Ortami
    Arg0-Listele
    $kok = Join-Path $env:CODEX_HOME "tmp\arg0-windows"
    if (-not (Test-Path -LiteralPath $kok)) { Write-Host "Klasör yok, silinecek bir şey yok."; return }
    $silinen = 0; $atlanan = 0
    foreach ($d in Get-ChildItem -LiteralPath $kok -Directory) {
      $kilit = Join-Path $d.FullName ".lock"
      $bos = $true
      if (Test-Path -LiteralPath $kilit) {
        try { $fs = [System.IO.File]::Open($kilit, 'Open', 'ReadWrite', 'None'); $fs.Close() } catch { $bos = $false }   # açılamıyorsa canlı bir Codex tutuyor
      }
      if (-not $bos) { $atlanan++; Write-Host "  atlandı (kilit tutuluyor): $($d.Name)"; continue }
      try { Remove-Item -LiteralPath $d.FullName -Recurse -Force -ErrorAction Stop; $silinen++ } catch { Write-Warning "  silinemedi: $($d.Name): $($_.Exception.Message)" }
    }
    Write-Host "Silinen: $silinen · atlanan (canlı): $atlanan" -ForegroundColor Green
  }

  "CopilotGiris" {
    if (-not (Test-Path -LiteralPath $CopilotExe)) { Write-Error "copilot.exe yok: $CopilotExe"; return }
    Sahit-Ortami
    & $CopilotExe --version
    if ($Secenek -eq "Cihaz") {
      Write-Host "Cihaz kodu akışı: yazılan adresi Chrome'da aç, kodu gir, GitHub hesabınla onayla." -ForegroundColor Cyan
      & $CopilotExe login --device-code
    } else {
      Write-Host "Tarayıcı açılacak; açılmazsa 'CopilotGiris Cihaz' dene. GitHub hesabınla onayla → buraya dön." -ForegroundColor Cyan
      Write-Host "Giriş sistem kimlik deposuna, o yoksa $env:COPILOT_HOME altına yazılır; WinPE'de her açılışta yinelemek gerekebilir." -ForegroundColor Cyan
      & $CopilotExe login
    }
    Write-Host "Sonraki: Kopru_Izle.cmd CopilotKontrol" -ForegroundColor Cyan
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
      if ($icerde -ne "true") { Ekle "Depo" "EKSİK" "Bu klasör git deposu değil: $DepoKoku" }
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
      $den = (& $pyYol -I -X utf8 defter/kopru_ekle.py kopru.html --kontrol 2>&1 | Out-String).Trim()
      Ekle "Sayfa denetimi" $(if ($LASTEXITCODE -eq 0) { "TAMAM" } else { "SORUN" }) $den
      foreach ($ad in @("Claude", "ChatGPT", "Copilot")) {
        $j = (& $pyYol -I -X utf8 defter/kopru_yanitla.py kopru.html --bekleyenler $ad 2>&1 | Out-String)
        try { $n = @((ConvertFrom-Json $j)).Count } catch { $n = "?" }
        $ipucu = if ($ad -eq "Copilot" -and $n -eq 0) { "henüz ona yazılmış kayıt yok → Kopru_Izle.cmd Ekle kayit.json" } else { "ilk turda bu kayıtlara tek yanıt yazar" }
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
