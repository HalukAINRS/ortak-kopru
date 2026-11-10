[CmdletBinding()]
param(
    [string]$Headquarters = ('Y:\02_karargahlar\01_codex_karargah' + [char]0x0131),
    [string]$CodexCommand = 'codex',
    [string[]]$CodexArguments = @(),
    [switch]$CheckOnly,
    [switch]$SkipReceive
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'Common.ps1')
$context = Get-DivanContext $Headquarters
$codex = Get-DivanApplication $CodexCommand
foreach ($argument in $CodexArguments) {
    if ($argument -eq '-C' -or $argument -eq '--cd' -or $argument.StartsWith('--cd=')) {
        throw 'The CLI root is the configured headquarters; do not supply a second -C/--cd.'
    }
}
if ($CheckOnly) {
    Write-Output ('CLI root verified: ' + $context.headquarters)
    Write-Output ('Codex executable: ' + $codex)
    Write-Output 'CheckOnly did not start a model or perform network synchronization.'
    return
}
if (-not $SkipReceive) {
    & (Join-Path $PSScriptRoot 'Receive-Divan.ps1') -Headquarters $context.headquarters
}
Push-Location -LiteralPath $context.headquarters
try {
    & $codex -C $context.headquarters @CodexArguments
    if ($LASTEXITCODE -ne 0) { throw ('Codex CLI exited with code ' + $LASTEXITCODE + '.') }
} finally { Pop-Location }
