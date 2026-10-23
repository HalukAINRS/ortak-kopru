param([int]$Dakika = 5, [switch]$TekSefer, [string]$Ayarlar = "ayarlar-yerel.json", [string]$Yalniz = "")
$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot
. "Y:\HalukAI\HalukAI_Ortam.ps1"
$env:PYTHONUTF8 = "1"
$env:COPILOT_HOME = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\02_Copilot_Sahit\Home\.copilot"
$env:COPILOT_CACHE_HOME = "X:\Windows\Temp\Sahit_Temp"
$env:NODE_COMPILE_CACHE = "X:\Windows\Temp\Sahit_NodeCache"
$env:COPILOT_AUTO_UPDATE = "false"
$env:CODEX_HOME = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home\.codex"
$env:HOME = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home"
$env:USERPROFILE = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home"
$pyExe = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime\Python\python.exe"
while ($true) {
  try {
    git pull --rebase origin main
    $once = (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches.Count
    & $pyExe -I -X utf8 kopru_yanitla.py kopru.html --ayarlar $Ayarlar
    $sonra = (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches.Count
    if ($sonra -gt $once) {
      git add kopru.html kayit
      git commit -m "kopru: yerel CLI yanitlari [skip ci]"
      git pull --rebase origin main
      git push origin main
    } else {
      Write-Host "Yeni kayit eklenmedi."
    }
  } catch {
    Write-Warning $_.Exception.Message
  }
  if ($TekSefer) { break }
  Start-Sleep -Seconds ($Dakika * 60)
}