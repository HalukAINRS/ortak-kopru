$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$launcher = Join-Path $repoRoot "kopru_yerel.ps1"
$temporary = Join-Path ([System.IO.Path]::GetTempPath()) ("Şahit test " + [guid]::NewGuid().ToString("N"))
$working = Join-Path $temporary "repo yolu boşluk"
$sahitHomePath = Join-Path $temporary "Home Şahit"
$exe = Join-Path $temporary "Copilot CLI sahte.ps1"
$log = Join-Path $temporary "mock.json"
$keys = @("HOME", "USERPROFILE", "COPILOT_HOME", "COPILOT_CACHE_HOME", "NODE_COMPILE_CACHE", "TEMP", "TMP", "COPILOT_AUTO_UPDATE")
$before = @{}
foreach ($key in $keys) { $before[$key] = [Environment]::GetEnvironmentVariable($key, "Process") }
$beforeLocation = (Get-Location).Path
$env:SAHIT_TEST_LOG = $log
New-Item -Path $working -ItemType Directory -Force | Out-Null
New-Item -Path $sahitHomePath -ItemType Directory -Force | Out-Null
@'
$entry = [ordered]@{
  args = @($args)
  cwd = (Get-Location).Path
  home = $env:HOME
  userprofile = $env:USERPROFILE
  copilot_home = $env:COPILOT_HOME
  auto_update = $env:COPILOT_AUTO_UPDATE
}
[System.IO.File]::WriteAllText($env:SAHIT_TEST_LOG, (ConvertTo-Json $entry -Compress))
'@ | Set-Content -LiteralPath $exe -Encoding utf8

try {
  $preview = (& $launcher -Mod SahitDevam -CopilotExePath $exe -SahitHomePath $sahitHomePath -DepoPath $working *>&1 | Out-String)
  if ($preview -notmatch "kuru önizleme" -or $preview -notmatch [regex]::Escape($working) -or $preview -notmatch [regex]::Escape($exe)) {
    throw "Preview did not show dry-run state and paths."
  }
  if (Test-Path -LiteralPath $log) { throw "Dry-run invoked the mock executable." }
  foreach ($key in $keys) {
    if ([Environment]::GetEnvironmentVariable($key, "Process") -ne $before[$key]) { throw "Preview changed $key." }
  }

  $null = & $launcher -Mod SahitDevam -Secenek Surum -CopilotExePath $exe -SahitHomePath $sahitHomePath -DepoPath $working
  $versionRun = Get-Content -LiteralPath $log -Raw | ConvertFrom-Json
  if ($versionRun.args.Count -ne 1 -or $versionRun.args[0] -ne "--version") { throw "Version check arguments were not exact." }
  if ($versionRun.cwd -ne $working -or $versionRun.home -ne $sahitHomePath -or $versionRun.copilot_home -ne (Join-Path $sahitHomePath ".copilot")) {
    throw "Version check did not use the configured repo and Home."
  }
  if ($versionRun.auto_update -ne "false") { throw "Automatic update environment was not disabled for this process." }
  if ((Get-Location).Path -ne $beforeLocation) { throw "Version check did not restore the caller's working directory." }
  foreach ($key in $keys) {
    if ([Environment]::GetEnvironmentVariable($key, "Process") -ne $before[$key]) { throw "Version check failed to restore $key." }
  }
  Remove-Item -LiteralPath $log
  $null = & $launcher -Mod SahitDevam -Secenek Yardim -CopilotExePath $exe -SahitHomePath $sahitHomePath -DepoPath $working
  $helpRun = Get-Content -LiteralPath $log -Raw | ConvertFrom-Json
  if ($helpRun.args.Count -ne 1 -or $helpRun.args[0] -ne "--help") { throw "Help check arguments were not exact." }

  Remove-Item -LiteralPath $log
  $null = & $launcher -Mod SahitDevam -Secenek Baslat -CopilotExePath $exe -SahitHomePath $sahitHomePath -DepoPath $working
  $interactiveRun = Get-Content -LiteralPath $log -Raw | ConvertFrom-Json
  if ($interactiveRun.args.Count -ne 0) { throw "Interactive launch received unrequested CLI arguments." }
  if ($interactiveRun.cwd -ne $working) { throw "Interactive launch used the wrong working directory." }
  if ((Get-Location).Path -ne $beforeLocation) { throw "Interactive launch did not restore the caller's working directory." }
  if (@($interactiveRun.args) -contains "--allow-all-tools") { throw "Broad tool permission flag was passed." }
  foreach ($key in $keys) {
    if ([Environment]::GetEnvironmentVariable($key, "Process") -ne $before[$key]) { throw "Interactive launch failed to restore $key." }
  }

  $failed = $false
  try {
    $null = & $launcher -Mod SahitDevam -CopilotExePath (Join-Path $temporary "missing.exe") -SahitHomePath $sahitHomePath -DepoPath $working
  } catch { $failed = $true }
  if (-not $failed) { throw "Missing executable was not rejected." }

  $failed = $false
  try {
    $null = & $launcher -Mod SahitDevam -Secenek 'Baslat;unexpected' -CopilotExePath $exe -SahitHomePath $sahitHomePath -DepoPath $working
  } catch { $failed = $true }
  if (-not $failed) { throw "Unexpected launch option was not rejected." }
  Write-Output "OK: preview, Unicode/space paths, explicit version/interactive launch, safe args, missing exe, and env restoration."
} finally {
  foreach ($key in $keys) { [Environment]::SetEnvironmentVariable($key, $before[$key], "Process") }
  Remove-Item Env:SAHIT_TEST_LOG -ErrorAction SilentlyContinue
  Remove-Item -LiteralPath $temporary -Recurse -Force -ErrorAction SilentlyContinue
}
