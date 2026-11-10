[CmdletBinding()]
param([string]$Headquarters = ('Y:\02_karargahlar\01_codex_karargah' + [char]0x0131))
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'Common.ps1')
$context = Get-DivanContext $Headquarters
# Explicit invocation is the only outbound synchronization step. Receiving and
# launching the CLI never call this script or push to a remote.
Invoke-DivanPython $context @((Join-Path $context.runtime 'bin/divan_git.py'), 'push', '--root', $context.runtime,
    '--repo', $context.repository_path, '--branch', $context.message_branch)
