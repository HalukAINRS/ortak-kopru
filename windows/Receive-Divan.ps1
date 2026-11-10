[CmdletBinding()]
param(
    [string]$Headquarters = ('Y:\02_karargahlar\01_codex_karargah' + [char]0x0131),
    [switch]$Watch,
    [ValidateRange(1, 3600)][int]$IntervalSeconds = 15,
    [ValidateRange(0, 2147483647)][int]$MaxCycles = 0
)
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'Common.ps1')
$context = Get-DivanContext $Headquarters
$cycle = 0
do {
    $cycle += 1
    Invoke-DivanPython $context @((Join-Path $context.runtime 'bin/divan_git.py'), 'pull', '--root', $context.runtime,
        '--repo', $context.repository_path, '--branch', $context.message_branch)
    Invoke-DivanPython $context @((Join-Path $context.runtime 'bin/divan.py'), '--root', $context.runtime,
        'inbox', '--member', $context.member)
    if (-not $Watch -or ($MaxCycles -gt 0 -and $cycle -ge $MaxCycles)) { break }
    Start-Sleep -Seconds $IntervalSeconds
} while ($true)
