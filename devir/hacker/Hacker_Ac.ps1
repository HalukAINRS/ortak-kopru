# Hacker'ı (Ubuntu VM'deki Claude Code) devir klasöründe (~/hacker-devri) açar. Varsayılan: son oturumdan sürdürür.
# Yer: Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\01_Claude_Code_Hacker\Hacker_Ac.ps1
#
#   Hacker_Ac.ps1                   Devam: ~/hacker-devri'deki son oturum; oturum yoksa yeni oturum
#   Hacker_Ac.ps1 -Mod Yeni         aynı klasörde yeni oturum
#   Hacker_Ac.ps1 -Mod Sec          oturum listesinden seçerek sürdür (claude --resume)
#   Hacker_Ac.ps1 -Mod Kabuk        VM'de kabuk, ~/hacker-devri içinde
#   Hacker_Ac.ps1 -Mod KisayolKur   "01 - Claude Code (Ubuntu VM).lnk" kısayolunu bu betiğe bağlar (bir kez)
#
# VM kapalıysa Hacker_Baslat.ps1 -Mod Kontrol ile başlatılır; QEMU ayarları orada kalır. Bağlantı köprüdeki izleyiciyle
# aynıdır: sabit known_hosts, StrictHostKeyChecking=yes. Çalışma dizini ~/hacker-devri olduğu için Claude Code oradaki
# devir talimatını (CLAUDE.md) yükler ve oradaki oturumu sürdürür. Hacker_Baslat.ps1'in Claude/Devam kipleri ~/HalukAI'de açar.
# Yollar kurulum değişirse aşağıda düzeltilir.
param([ValidateSet("Devam", "Yeni", "Sec", "Kabuk", "KisayolKur")][string]$Mod = "Devam")
$ErrorActionPreference = "Stop"

$Katmanlar = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari"
$HackerKat = "$Katmanlar\01_Claude_Code_Hacker"
$GitBin    = "$Katmanlar\Runtime\Git-Portable-2.56.0.2\usr\bin"
$Anahtar   = "$HackerKat\Home\.ssh\hacker_arm64_035"
$Bilinen   = "$HackerKat\Home\.ssh\known_hosts"
$Baslat    = "$HackerKat\Hacker_Baslat.ps1"
$Kisayol   = "Y:\HalukAI\Masaustu_Kisayollari\01 - Claude Code (Ubuntu VM).lnk"
$Secenek   = @("-i", $Anahtar, "-o", "UserKnownHostsFile=$Bilinen", "-o", "StrictHostKeyChecking=yes",
               "-o", "BatchMode=yes", "-o", "LogLevel=ERROR", "-o", "ConnectTimeout=15")
$Pwsh = @("Y:\Programs\WindowsPowerShell\PowerShell-7.6.8-win-x64\pwsh.exe",
          "$Katmanlar\Runtime\PowerShell-7.6.8-win-x64\pwsh.exe",
          (Get-Process -Id $PID).Path) | Where-Object { $_ -and (Test-Path -LiteralPath $_) } | Select-Object -First 1

# VM içindeki açıcı. Her açılışta ~/bin/hacker-ac olarak yenilenir; değişiklik burada yapılır.
$VmBetik = @'
#!/usr/bin/env bash
# Hacker'ı ~/hacker-devri'de açar. Windows'taki Hacker_Ac.ps1 her açılışta bu dosyayı ~/bin/hacker-ac olarak yeniler.
# Kip: devam (son oturum; yoksa yeni) | yeni | sec (claude --resume) | kabuk
set -u
kip="${1:-devam}"
dizin="$HOME/hacker-devri"
claude="/home/hacker/bin/claude-arm64-035"

cd "$dizin" 2>/dev/null || { echo "[hacker-ac] $dizin yok (devir paketi açılmamış); kabuk açılıyor."; exec bash -l; }
[ -x "$claude" ] || { echo "[hacker-ac] sarmalayıcı yok: $claude; kabuk açılıyor."; exec bash -l; }

# Oturum dökümleri: CLAUDE_CONFIG_DIR/projects/<çalışma dizini, harf ve rakam dışı karakterler '-'>/*.jsonl
# CLAUDE_CONFIG_DIR'i sarmalayıcı koyuyor (k-0113); değer oradan okunur, okunamazsa Hacker'ın bildirdiği yol kullanılır.
yap="$(sed -n "s/.*CLAUDE_CONFIG_DIR=[\"']\{0,1\}\([^\"' ;]*\).*/\1/p" "$claude" | head -n 1)"
yap="${yap/#\~/$HOME}"; yap="${yap//\$\{HOME\}/$HOME}"; yap="${yap//\$HOME/$HOME}"
case "$yap" in /*) ;; *) yap="" ;; esac
[ -n "$yap" ] || yap="${CLAUDE_CONFIG_DIR:-$HOME/.config/halukai-claude}"
proje="$yap/projects/$(pwd | sed 's/[^A-Za-z0-9]/-/g')"

case "$kip" in
  devam)
    if compgen -G "$proje/*.jsonl" > /dev/null; then
      echo "[hacker-ac] $dizin: son oturum sürdürülüyor (claude --continue)."
      exec "$claude" --continue
    fi
    echo "[hacker-ac] $dizin: sürdürülecek oturum yok ($proje); yeni oturum açılıyor."
    exec "$claude" ;;
  yeni)  exec "$claude" ;;
  sec)   exec "$claude" --resume ;;
  kabuk) exec bash -l ;;
  *)     echo "[hacker-ac] bilinmeyen kip: $kip (devam | yeni | sec | kabuk)"; exit 2 ;;
esac
'@

function Bekle-Kapat([string]$Ileti) {
  if ($Ileti) { Write-Host $Ileti -ForegroundColor Red }
  Read-Host "Kapatmak için Enter" | Out-Null
}

function Ssh-Hazir {
  try {
    $soket = [System.Net.Sockets.TcpClient]::new("127.0.0.1", 2222)
    $akis = $soket.GetStream(); $akis.ReadTimeout = 1500
    $tampon = New-Object byte[] 4
    $okunan = $akis.Read($tampon, 0, 4)
    $soket.Dispose()
    return ($okunan -eq 4 -and [Text.Encoding]::ASCII.GetString($tampon) -eq "SSH-")
  } catch { return $false }
}

if ($Mod -eq "KisayolKur") {
  $wsh = New-Object -ComObject WScript.Shell
  $masaustu = [Environment]::GetFolderPath("Desktop")
  if (-not $masaustu) { $masaustu = "X:\Users\Default\Desktop" }
  $hedefler = @($Kisayol, (Join-Path $masaustu (Split-Path $Kisayol -Leaf))) | Select-Object -Unique
  foreach ($h in $hedefler) {
    if (-not (Test-Path -LiteralPath (Split-Path $h -Parent))) { Write-Host "Klasör yok, atlandı: $(Split-Path $h -Parent)"; continue }
    if (Test-Path -LiteralPath $h) {
      $eski = $wsh.CreateShortcut($h)
      Write-Host "Önceki kısayol: $h"
      Write-Host "  hedef: $($eski.TargetPath) $($eski.Arguments)"
      Write-Host "  klasör: $($eski.WorkingDirectory)"
      if ($h -eq $Kisayol) {
        $yedekDizin = "$HackerKat\Yedek"
        New-Item -ItemType Directory -Force -Path $yedekDizin | Out-Null
        $yedek = Join-Path $yedekDizin ("{0}.{1:yyyyMMdd-HHmmss}.lnk" -f [IO.Path]::GetFileNameWithoutExtension($h), (Get-Date))
        Copy-Item -LiteralPath $h -Destination $yedek
        Write-Host "  yedek: $yedek"
      }
    }
    $k = $wsh.CreateShortcut($h)
    $k.TargetPath = $Pwsh
    $k.Arguments = "-NoLogo -NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" -Mod Devam"
    $k.WorkingDirectory = $HackerKat
    $k.Description = "Hacker: VM'deki Claude Code, ~/hacker-devri, son oturumdan devam"
    $k.Save()
    Write-Host "Kısayol hazır: $h" -ForegroundColor Green
  }
  return
}

$Host.UI.RawUI.WindowTitle = "Hacker (Claude Code) - $Mod"
foreach ($yol in @("$GitBin\ssh.exe", "$GitBin\scp.exe", $Anahtar, $Bilinen)) {
  if (-not (Test-Path -LiteralPath $yol)) { Bekle-Kapat "Bulunamadı: $yol"; exit 1 }
}

if (-not (Ssh-Hazir)) {
  if (-not (Test-Path -LiteralPath $Baslat)) { Bekle-Kapat "VM kapalı ve başlatıcı yok: $Baslat"; exit 1 }
  Write-Host "[Hacker] VM kapalı; Hacker_Baslat.ps1 -Mod Kontrol ile başlatılıyor..." -ForegroundColor Cyan
  & $Pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass -File $Baslat -Mod Kontrol
  Write-Host "[Hacker] SSH bekleniyor (en çok 5 dakika)..." -ForegroundColor Yellow
  $sinir = (Get-Date).AddMinutes(5)
  while (-not (Ssh-Hazir) -and (Get-Date) -lt $sinir) { Start-Sleep -Seconds 2 }
  if (-not (Ssh-Hazir)) { Bekle-Kapat "VM'in SSH'i 5 dakikada açılmadı. Bak: Hacker_Baslat.ps1 -Mod Durum; $HackerKat\Logs\serial.log"; exit 1 }
}

# Açıcıyı VM'e yaz: LF satır sonlarıyla, geçici klasörden ve göreli adla (scp, Y:\ yolundaki iki noktayı uzak makine adı sanar).
$gecici = Join-Path ([IO.Path]::GetTempPath()) "hacker-ac"
New-Item -ItemType Directory -Force -Path $gecici | Out-Null
[IO.File]::WriteAllText((Join-Path $gecici "hacker-ac"), ($VmBetik -replace "`r`n", "`n"), [Text.UTF8Encoding]::new($false))
Push-Location -LiteralPath $gecici
try { & "$GitBin\scp.exe" -q -P 2222 @Secenek hacker-ac hacker@127.0.0.1:bin/hacker-ac } finally { Pop-Location }
if ($LASTEXITCODE -ne 0) { Bekle-Kapat "Açıcı VM'e kopyalanamadı (scp çıkış kodu $LASTEXITCODE)."; exit 1 }

$kip = @{ Devam = "devam"; Yeni = "yeni"; Sec = "sec"; Kabuk = "kabuk" }[$Mod]
& "$GitBin\ssh.exe" -p 2222 @Secenek -t hacker@127.0.0.1 bash bin/hacker-ac $kip
$kod = $LASTEXITCODE
if ($kod -ne 0) { Bekle-Kapat "Hacker oturumu $kod koduyla bitti." }
exit $kod
