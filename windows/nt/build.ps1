[CmdletBinding()]
param(
    [ValidateSet('Debug', 'Release')][string]$Configuration = 'Release',
    [switch]$Restore,
    [string]$NuGet = 'nuget',
    [string]$MSBuild = 'msbuild'
)
$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') { throw 'WDK derlemesi Windows üzerinde çalışır.' }
if ($Restore) {
    & $NuGet restore (Join-Path $PSScriptRoot 'packages.config') `
        -PackagesDirectory (Join-Path $PSScriptRoot 'packages') `
        -Source 'https://api.nuget.org/v3/index.json' -NonInteractive
    if ($LASTEXITCODE -ne 0) { throw "NuGet geri yükleme başarısız: $LASTEXITCODE" }
}
& $MSBuild (Join-Path $PSScriptRoot 'DeusKernel.vcxproj') /m /t:Build `
    "/p:Configuration=$Configuration" /p:Platform=x64 /p:SignMode=Off /v:minimal
if ($LASTEXITCODE -ne 0) { throw "WDK derlemesi başarısız: $LASTEXITCODE" }
$binary = Join-Path $PSScriptRoot "build/x64/$Configuration/deus_kernel.sys"
if (-not (Test-Path -LiteralPath $binary -PathType Leaf)) { throw 'Beklenen sürücü çıktısı bulunamadı.' }
[pscustomobject]@{
    binary = $binary
    sha256 = (Get-FileHash -LiteralPath $binary -Algorithm SHA256).Hash.ToLowerInvariant()
    architecture = 'x64'
    compiled = $true
    signed_by_this_script = $false
    installed_by_this_script = $false
    loaded_by_this_script = $false
} | ConvertTo-Json
