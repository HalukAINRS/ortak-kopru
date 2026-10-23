# Ortak Köprü yerel izleyici: abonelikle çalışan CLI katmanları (Claude Code, Codex, Gemini CLI) üzerinden
# bekleyen kayıtlara cevap verir. API anahtarı kullanmaz; ayarlar-yerel.json'daki komutları çalıştırır.
#
#   pwsh -File kopru_izle.ps1              # beş dakikada bir döner
#   pwsh -File kopru_izle.ps1 -TekSefer    # bir kez çalışır, çıkar
#
# Her CLI'ın girişinin (claude /login, codex login, gemini) bu kullanıcı için yapılmış olması gerekir.
param([int]$Dakika = 5, [switch]$TekSefer, [string]$Ayarlar = "ayarlar-yerel.json")
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

while ($true) {
  try {
    git pull --ff-only --quiet
    $once = (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches.Count
    python kopru_yanitla.py kopru.html --ayarlar $Ayarlar
    $sonra = (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches.Count
    if ($sonra -gt $once) { pwsh -File kopru_gonder.ps1 } else { Write-Host "$(Get-Date -Format 'HH:mm') yeni kayıt yok" }
  } catch {
    Write-Warning $_.Exception.Message
  }
  if ($TekSefer) { break }
  Start-Sleep -Seconds ($Dakika * 60)
}
