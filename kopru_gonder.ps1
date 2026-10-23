# Ortak Köprü: son kaydın numarasıyla commit atar ve GitHub'a gönderir.
# Kullanım: pwsh -File kopru_gonder.ps1   (depo kökünde: Y:\HalukAI\Ortak_Kopru\kopru)
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

python kopru_ekle.py kopru.html --kontrol
if ($LASTEXITCODE -ne 0) { Write-Error "Denetim geçmedi; gönderilmedi."; exit 1 }

$son = (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches |
       ForEach-Object { $_.Groups[1].Value } | Select-Object -Last 1
if (-not $son) { $son = "ilk" }

git add -A -- . ":!yanit*.json" ":!istem*.txt"
$degisiklik = git status --porcelain
if (-not $degisiklik) { Write-Host "Değişiklik yok; gönderilecek bir şey yok."; exit 0 }

git commit -m "köprü: $son"
git push
Write-Host "Gönderildi: $son"
