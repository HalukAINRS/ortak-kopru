# Ortak Köprü yerel izleyici: bir CLI katmanına düşen açık kayıtları o katmanın CLI'ı ile yanıtlar.
# Katman başına bir izleyici çalıştırılır; yalnız makine açıkken çalışır.
#
#   pwsh -File kopru_izle.ps1 -Ad ChatGPT -Imza "ChatGPT (Şaman)" -Program codex -OnArgs @("exec")
#   pwsh -File kopru_izle.ps1 -Ad Claude  -Imza "Claude (Hacker)" -Program claude -OnArgs @("-p")
#   pwsh -File kopru_izle.ps1 -Ad Gemini  -Imza "Gemini (CLI)"    -Program gemini -OnArgs @("-p")
#
# Program çağrısı: & $Program @OnArgs <istem metni>  → standart çıktı yanıt sayılır; içinden JSON nesnesi ayıklanır.
# CLI'ların etkileşimsiz bayraklarını kendi sürümünde doğrula (codex exec, claude -p, gemini -p).
param(
  [Parameter(Mandatory)][string]$Ad,
  [Parameter(Mandatory)][string]$Imza,
  [Parameter(Mandatory)][string]$Program,
  [string[]]$OnArgs = @(),
  [int]$Dakika = 5,
  [switch]$TekSefer
)
$ErrorActionPreference = "Stop"
Set-Location -LiteralPath $PSScriptRoot

while ($true) {
  try {
    git pull --ff-only --quiet
    $bekleyen = python kopru_yanitla.py kopru.html --bekleyenler $Ad | ConvertFrom-Json
    if ($bekleyen.Count -gt 0) {
      $idler = ($bekleyen | ForEach-Object { $_.id }) -join ", "
      Write-Host "$(Get-Date -Format 'HH:mm') $Ad için bekleyen: $idler"
      $istem = python kopru_yanitla.py kopru.html --istem $Ad | Out-String
      $hedef = $bekleyen[-1].id
      $yanit = & $Program @OnArgs $istem 2>$null | Out-String
      $yanit | Set-Content -LiteralPath "yanit-$Ad.json" -Encoding UTF8
      python kopru_ekle.py kopru.html --json "yanit-$Ad.json" --kimden $Imza --yanit $hedef
      if ($LASTEXITCODE -eq 0) {
        pwsh -File kopru_gonder.ps1
      } else {
        Write-Warning "Kayıt eklenemedi; yanıt yanit-$Ad.json dosyasında duruyor."
      }
    } else {
      Write-Host "$(Get-Date -Format 'HH:mm') $Ad için bekleyen yok"
    }
  } catch {
    Write-Warning $_.Exception.Message
  }
  if ($TekSefer) { break }
  Start-Sleep -Seconds ($Dakika * 60)
}
