# Ortak Köprü: yerel değişiklikleri commit eder, uzaktaki yeni kayıtlarla birleştirir ve GitHub'a gönderir.
# Kullanım: pwsh -File kopru_gonder.ps1   (depo kökünde: Y:\HalukAI\Ortak_Kopru\kopru)
# Birden çok yazan olduğu için (GitHub Actions botu, Gemini ve ChatGPT aktarımları, sen) önce uzak alınır:
# kopru.html çakışırsa kopru_birlestir.py uzak sürümü esas alıp yalnız yereldeki kayıtları yeni numarayla ekler;
# kayit/atlandi.log çakışırsa satırlar birleştirilir; diğer kaynak çakışmaları elle çözülmek üzere durdurulur.
# Python: KOPRU_PYTHON ortam değişkeni (tam yol) ya da PATH'teki python / py.
param([string]$Dal = "main", [switch]$Bot)   # -Bot: commit iletisine [skip ci]; bot cevapları Actions botunu tetiklemez
$ErrorActionPreference = "Continue"
Set-Location -LiteralPath $PSScriptRoot

$aktifDal = git symbolic-ref --quiet --short HEAD
if ($LASTEXITCODE -ne 0 -or $aktifDal -ne $Dal) {
  Write-Error "Gönderim için '$Dal' dalında olmalısın; mevcut dal: $aktifDal. Başka dal main'e gönderilmedi."
  exit 1
}
foreach ($durumYolu in @("rebase-merge", "rebase-apply", "MERGE_HEAD", "CHERRY_PICK_HEAD")) {
  $gitYolu = git rev-parse --git-path $durumYolu
  if ($LASTEXITCODE -ne 0 -or (Test-Path -LiteralPath $gitYolu)) {
    Write-Error "Devam eden Git birleştirmesi var; önce 'git status' ile incele."
    exit 1
  }
}

function Bul-Python {
  if ($env:KOPRU_PYTHON -and (Test-Path -LiteralPath $env:KOPRU_PYTHON)) { return @($env:KOPRU_PYTHON) }
  foreach ($aday in @("python3", "python")) {
    $k = Get-Command $aday -ErrorAction SilentlyContinue
    if ($k -and $k.Source -notmatch "WindowsApps") { return @($k.Source) }
  }
  $py = Get-Command py -ErrorAction SilentlyContinue
  if ($py) { return @($py.Source, "-3") }
  throw "Python bulunamadı (bkz. kopru_yerel.ps1)."
}
$python = @(Bul-Python)   # tek öge dönerse de dizi kalsın
$pyExe = $python[0]
$pyArgs = @()
if ($python.Count -gt 1) { $pyArgs = @($python[1..($python.Count-1)]) }

function Son-Kayit {
  $s = (Select-String -LiteralPath kopru.html -Pattern '<article class="kayit" id="(k-\d{4})"' -AllMatches).Matches |
       ForEach-Object { $_.Groups[1].Value } | Select-Object -Last 1
  if ($s) { $s } else { "ilk" }
}

# 1. Denetim ve yerel commit
& $pyExe @pyArgs -I -X utf8 kopru_ekle.py kopru.html --kontrol
if ($LASTEXITCODE -ne 0) { Write-Error "Denetim geçmedi; gönderilmedi."; exit 1 }
& $pyExe @pyArgs -I -X utf8 kopru_ayna_uret.py kopru.html ayna/kopru.html   # ayna kanonik dosyanın gerisinde kalmasın
if ($LASTEXITCODE -ne 0) { Write-Error "Ayna üretilemedi; gönderilmedi."; exit 1 }
git add -A -- . ":!yanit*.json" ":!istem*.txt"
if ($LASTEXITCODE -ne 0) { Write-Error "Değişiklikler hazırlanamıyor; gönderilmedi."; exit 1 }
git diff --cached --quiet
$farkKodu = $LASTEXITCODE
if ($farkKodu -gt 1) { Write-Error "Hazırlanan değişiklikler okunamadı."; exit 1 }
if ($farkKodu -eq 1) {
  $ileti = "köprü: $(Son-Kayit)" + $(if ($Bot) { " [skip ci]" } else { "" })
  git commit -q -m $ileti
  if ($LASTEXITCODE -ne 0) { Write-Error "Commit olmadı (kimlik ayarı? git config user.name / user.email)."; exit 1 }
  Write-Host "Yerel commit: $ileti"
}

# 2. Uzakla birleştir, gönder (yarış olursa üç deneme)
$env:GIT_EDITOR = "true"
for ($deneme = 1; $deneme -le 3; $deneme++) {
  git fetch -q origin $Dal
  if ($LASTEXITCODE -ne 0) { Write-Error "origin'den alınamadı (ağ? uzak adı?)."; exit 1 }
  $geride = git rev-list --count "HEAD..origin/$Dal"
  if ($LASTEXITCODE -ne 0) { Write-Error "Uzak dal karşılaştırılamadı."; exit 1 }
  $ileride = git rev-list --count "origin/$Dal..HEAD"
  if ($LASTEXITCODE -ne 0) { Write-Error "Yerel dal karşılaştırılamadı."; exit 1 }
  $geride = [int]$geride
  $ileride = [int]$ileride
  if ($geride -gt 0) {
    Write-Host "Uzakta $geride yeni commit var; yerel $ileride commit üzerine alınıyor."
    git rebase -q "origin/$Dal" 2>&1 | Out-Null
    $rebaseKodu = $LASTEXITCODE
    $tur = 0
    while ($rebaseKodu -ne 0 -and $tur -lt 20) {
      $tur++
      $cakisan = @(git diff --name-only --diff-filter=U)
      if ($LASTEXITCODE -ne 0) { Write-Error "Çakışma listesi okunamadı."; git rebase --abort; exit 1 }
      if ($cakisan.Count -eq 0) { Write-Error "Rebase durdu ama çakışan dosya yok; 'git status' ile bak."; git rebase --abort; exit 1 }
      $elle = @($cakisan | Where-Object { $_ -notin @("kopru.html", "ayna/kopru.html", "kayit/atlandi.log") })
      if ($elle.Count -gt 0) {
        Write-Error "Kaynak çakışması elle çözülmeli: $($elle -join ', '). Rebase geri alınıyor."
        git rebase --abort
        exit 1
      }
      foreach ($f in @($cakisan | Where-Object { $_ -ne "ayna/kopru.html" })) {
        if ($f -eq "kopru.html") {
          & $pyExe @pyArgs -I -X utf8 kopru_birlestir.py --rebase kopru.html
          if ($LASTEXITCODE -ne 0) { Write-Error "kopru.html birleştirilemedi; rebase geri alındı."; git rebase --abort; exit 1 }
        } elseif ($f -eq "kayit/atlandi.log") {
          & $pyExe @pyArgs -I -X utf8 kopru_birlestir.py --rebase-metin $f
          if ($LASTEXITCODE -ne 0) { Write-Error "Günlük birleştirilemedi."; git rebase --abort; exit 1 }
        }
        git add -- $f
        if ($LASTEXITCODE -ne 0) { Write-Error "Birleşmiş dosya hazırlanamadı."; git rebase --abort; exit 1 }
      }
      if ($cakisan -contains "kopru.html" -or $cakisan -contains "ayna/kopru.html") {
        & $pyExe @pyArgs -I -X utf8 kopru_ayna_uret.py kopru.html ayna/kopru.html
        if ($LASTEXITCODE -ne 0) { Write-Error "Birleşmiş sayfanın aynası üretilemedi."; git rebase --abort; exit 1 }
        git add -- ayna/kopru.html
        if ($LASTEXITCODE -ne 0) { Write-Error "Birleşmiş ayna hazırlanamadı."; git rebase --abort; exit 1 }
      }
      git -c core.editor=true rebase --continue 2>&1 | Out-Null
      $rebaseKodu = $LASTEXITCODE
    }
    if ($rebaseKodu -ne 0) { Write-Error "Rebase bitmedi; geri alınıyor."; git rebase --abort; exit 1 }
  }
  # Çakışmasız rebase de sayfayı değiştirebilir; son birleşmiş sürümü denetle ve aynasını üret.
  & $pyExe @pyArgs -I -X utf8 kopru_ekle.py kopru.html --kontrol
  if ($LASTEXITCODE -ne 0) { Write-Error "Birleşmiş sayfa denetimden geçmedi; gönderilmedi."; exit 1 }
  & $pyExe @pyArgs -I -X utf8 kopru_ayna_uret.py kopru.html ayna/kopru.html
  if ($LASTEXITCODE -ne 0) { Write-Error "Son ayna üretilemedi; gönderilmedi."; exit 1 }
  git add -- ayna/kopru.html
  if ($LASTEXITCODE -ne 0) { Write-Error "Son ayna hazırlanamadı."; exit 1 }
  git diff --cached --quiet
  $farkKodu = $LASTEXITCODE
  if ($farkKodu -gt 1) { Write-Error "Ayna farkı okunamadı."; exit 1 }
  if ($farkKodu -eq 1) {
    $ileti = "köprü: $(Son-Kayit) ayna eşitle" + $(if ($Bot) { " [skip ci]" } else { "" })
    git commit -q -m $ileti
    if ($LASTEXITCODE -ne 0) { Write-Error "Ayna commit'i oluşturulamadı."; exit 1 }
  }
  $ileride = git rev-list --count "origin/$Dal..HEAD"
  if ($LASTEXITCODE -ne 0) { Write-Error "Gönderilecek commit'ler okunamadı."; exit 1 }
  if ($ileride -eq "0") { Write-Host "Gönderilecek yeni commit yok; yerel güncel."; exit 0 }
  git push -q origin "HEAD:$Dal"
  if ($LASTEXITCODE -eq 0) { Write-Host "Gönderildi: $(Son-Kayit)"; exit 0 }
  Write-Warning "Gönderim reddedildi (bu arada başka gönderim oldu); yeniden deneniyor ($deneme/3)."
}
Write-Error "Üç denemede gönderilemedi."
exit 1
