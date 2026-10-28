param(
    [ValidateSet("Codex","Devam","Sec","PowerShell7","Kontrol")][string]$Mod = "Devam",
    [switch]$Denetle
)
$ErrorActionPreference = "Stop"
$CodexExe = Join-Path $PSScriptRoot "npm_global\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\bin\codex.exe"
$calismaDizini = Join-Path $PSScriptRoot "Workspace"
$ps7Exe = Join-Path (Split-Path $PSScriptRoot -Parent) "Runtime\PowerShell-7.6.8-win-x64\pwsh.exe"
foreach ($gerekliDosya in @($CodexExe, $ps7Exe)) {
    if (-not (Test-Path -LiteralPath $gerekliDosya -PathType Leaf)) { throw "Dosya bulunamadi: $gerekliDosya" }
}
$codexArgumanlari = @()
if ($Mod -eq "Devam") { $codexArgumanlari = @("resume", "--last") }
if ($Mod -eq "Sec") { $codexArgumanlari = @("resume") }
$codexArgumanlari += @("-C", $calismaDizini, "-c", 'model_reasoning_effort="xhigh"', "-c", 'plan_mode_reasoning_effort="xhigh"')
if ($Denetle) {
    [ordered]@{
        Mod = $Mod
        Program = $(if ($Mod -eq "PowerShell7") { $ps7Exe } else { $CodexExe })
        Argumanlar = $(if ($Mod -eq "PowerShell7") { @("-NoLogo", "-NoProfile") } else { $codexArgumanlari })
        CalismaDizini = $calismaDizini
        OturumDizini = (Join-Path $PSScriptRoot "Home\.codex\sessions")
        CodexHome = (Join-Path $PSScriptRoot "Home\.codex")
    } | ConvertTo-Json
    return
}
if ($Mod -eq "Kontrol") {
    & $CodexExe --version
    & (Join-Path (Split-Path $PSScriptRoot -Parent) "Runtime\node-v22.23.3-win-x64\node.exe") --version
    return
}
. "Y:\HalukAI\HalukAI_Ortam.ps1"
$ErrorActionPreference = "Stop"
New-Item -Path "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Workspace" -ItemType Directory -Force | Out-Null
New-Item -Path "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home\.codex\tmp" -ItemType Directory -Force | Out-Null
New-Item -Path "X:\Windows\Temp\Saman_Temp" -ItemType Directory -Force | Out-Null
$env:HOME = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home"
$env:USERPROFILE = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home"
$env:CODEX_HOME = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home\.codex"
$env:APPDATA = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home\AppData\Roaming"
$env:LOCALAPPDATA = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Home\AppData\Local"
$env:TEMP = "X:\Windows\Temp\Saman_Temp"
$env:TMP = "X:\Windows\Temp\Saman_Temp"
Set-Location -LiteralPath $calismaDizini
if ($Mod -eq "PowerShell7") {
    & $ps7Exe -NoLogo -NoProfile
    return
}
Write-Host "Saman | $Mod | $calismaDizini"
& $CodexExe @codexArgumanlari
if ($LASTEXITCODE -ne 0) { throw "Codex cikis kodu: $LASTEXITCODE" }
