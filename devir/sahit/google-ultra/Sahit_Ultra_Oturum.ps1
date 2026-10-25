param([ValidateSet('Baslat','Kontrol')][string]$Mod = 'Baslat')
$ErrorActionPreference = 'Stop'
$Katmanlar = 'Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari'
$SahitKok = Join-Path $Katmanlar '02_Copilot_Sahit'
$Calisma = Join-Path $SahitKok 'Workspace'
$DurumYolu = Join-Path $SahitKok 'Sahit_Ultra_Durum.json'
$Agy = Join-Path $Katmanlar 'Runtime\Antigravity-1.4.7-win-x64\agy.exe'
$Profil = Join-Path $Katmanlar '04_Gemini_CLI\Home'
if (-not (Test-Path -LiteralPath $DurumYolu -PathType Leaf)) { throw 'Dogrulanmis Sahit Ultra devam kaydi bulunamadi.' }
$Durum = Get-Content -LiteralPath $DurumYolu -Raw -Encoding utf8 | ConvertFrom-Json -DateKind String
if ($Durum.model -ne 'gemini-4-argon-high' -or $Durum.effort -ne 'high' -or -not $Durum.connection_test_passed) {
    throw 'Model, efor veya Google baglanti dogrulamasi eksik.'
}
if ($Durum.conversation_id -notmatch '^[a-f0-9-]{36}$') { throw 'Belirli Google devam oturumu eksik.' }
if (-not (Test-Path -LiteralPath $Agy -PathType Leaf)) { throw 'Resmi Google CLI bulunamadi.' }
$Bayraklar = @('--conversation', $Durum.conversation_id, '--model', $Durum.model, '--effort', $Durum.effort,
               '--add-dir', 'Y:\HalukAI\Ortak_Kopru')
if ($Mod -eq 'Kontrol') {
    [pscustomobject]@{ Provider = 'Google Antigravity CLI'; Model = $Durum.model; Effort = $Durum.effort;
        GoogleUltraConfirmed = $Durum.ultra_ui_confirmed; ConnectionPassed = $Durum.connection_test_passed;
        UsesSpecificConversation = $true; ProfileOnY = $Profil.StartsWith('Y:'); CredentialCopied = $false;
        NativeDefaultEndpoint = $true; PaidApiKey = $false } | ConvertTo-Json -Compress
    return
}
if ($Durum.ps_pid) {
    $Onceki = Get-Process -Id ([int]$Durum.ps_pid) -ErrorAction SilentlyContinue
    if ($Onceki -and $Onceki.ProcessName -eq 'pwsh' -and $Onceki.StartTime.ToUniversalTime().ToString('o') -eq $Durum.ps_start_utc) {
        Write-Host "Sahit Google Ultra penceresi zaten acik (PID $($Onceki.Id)). O pencereyi kullanin."
        return
    }
}
$EkYollar = @('Runtime\PowerShell-7.6.8-win-x64','Runtime\Git-Portable-2.56.0.2\cmd',
             'Runtime\Git-Portable-2.56.0.2\usr\bin','Runtime\node-v22.23.3-win-x64','Runtime\Python') |
    ForEach-Object { Join-Path $Katmanlar $_ } | Where-Object { Test-Path -LiteralPath $_ -PathType Container }
$env:PATH = (($EkYollar + $env:PATH.Split(';') | Select-Object -Unique) -join ';')
# Only this child process uses the Google profile; existing Copilot files are not migrated over it.
$env:HOME = $Profil; $env:USERPROFILE = $Profil
$env:TEMP = 'X:\Windows\Temp\Antigravity_Temp'; $env:TMP = $env:TEMP
$env:OPENSSL_CONF = Join-Path $Katmanlar 'Runtime\openssl.cnf'
$env:WSL_DISTRO_NAME = 'HalukAI'
foreach ($Anahtar in @('CLOUD_CODE_URL','GEMINI_API_KEY','GOOGLE_API_KEY','GOOGLE_GENAI_USE_VERTEXAI','AGY_ADC_AUTH')) {
    Remove-Item -LiteralPath "Env:$Anahtar" -ErrorAction SilentlyContinue
}
$GitConfig = Join-Path $SahitKok 'Home\.gitconfig'
if (Test-Path -LiteralPath $GitConfig -PathType Leaf) { $env:GIT_CONFIG_GLOBAL = $GitConfig }
New-Item -ItemType Directory -Path $env:TEMP -Force | Out-Null
Set-Location -LiteralPath $Calisma
try { $Host.UI.RawUI.WindowTitle = 'Sahit - Google Ultra - Gemini 4 Argon High' } catch {}
$Ben = Get-Process -Id $PID
$Durum | Add-Member -NotePropertyName ps_pid -NotePropertyValue $PID -Force
$Durum | Add-Member -NotePropertyName ps_start_utc -NotePropertyValue $Ben.StartTime.ToUniversalTime().ToString('o') -Force
$Durum | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $DurumYolu -Encoding utf8
Write-Host 'Sahit: Google AI Ultra / Gemini 4 Argon / desteklenen en yuksek efor high.' -ForegroundColor Cyan
Write-Host 'Belirli Google oturumu surduruluyor. Eski Copilot oturumu kaynak olarak korunuyor.'
& $Agy @Bayraklar
if ($LASTEXITCODE -ne 0) { Write-Host "Google CLI cikis kodu: $LASTEXITCODE" -ForegroundColor Yellow }
