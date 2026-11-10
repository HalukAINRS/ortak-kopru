Set-StrictMode -Version 2.0

function Get-DivanDefaultHeadquarters {
    return ('Y:\02_karargahlar\01_codex_karargah' + [char]0x0131)
}

function Get-DivanFullPath {
    param([Parameter(Mandatory = $true)][string]$Path)
    if (-not [System.IO.Path]::IsPathRooted($Path)) {
        throw 'An absolute, environment-native path is required. The Windows Y: drive must be mounted on Windows.'
    }
    return [System.IO.Path]::GetFullPath($Path)
}

function Test-DivanSamePath {
    param([string]$First, [string]$Second)
    $a = (Get-DivanFullPath $First).TrimEnd([char[]]@('/', '\'))
    $b = (Get-DivanFullPath $Second).TrimEnd([char[]]@('/', '\'))
    $comparison = [System.StringComparison]::Ordinal
    if ($env:OS -eq 'Windows_NT') { $comparison = [System.StringComparison]::OrdinalIgnoreCase }
    return [string]::Equals($a, $b, $comparison)
}

function Get-DivanApplication {
    param([string]$Command)
    $application = Get-Command -Name $Command -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($null -eq $application) { throw ('Required executable not found: ' + $Command) }
    return $application.Source
}

function Get-DivanPython {
    param([string]$Command)
    $candidates = @('python', 'python3', 'py')
    if (-not [string]::IsNullOrWhiteSpace($Command)) { $candidates = @($Command) }
    foreach ($candidate in $candidates) {
        $application = Get-Command -Name $candidate -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -eq $application) { continue }
        $prefix = @()
        if ([System.IO.Path]::GetFileNameWithoutExtension($application.Source) -eq 'py') { $prefix = @('-3') }
        $oldPreference = $ErrorActionPreference
        try {
            $ErrorActionPreference = 'Continue'
            & $application.Source @prefix -c 'import sys; sys.exit(0 if sys.version_info >= (3,11) else 2)' 2>$null | Out-Null
            $code = $LASTEXITCODE
        } finally { $ErrorActionPreference = $oldPreference }
        if ($code -eq 0) { return [pscustomobject]@{ Command = $application.Source; Arguments = @($prefix) } }
    }
    throw 'Python 3.11 or newer is required. Install it through its official installer or select -PythonCommand.'
}

function Invoke-DivanGit {
    param([string]$GitCommand, [string[]]$Arguments)
    $oldPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = 'Continue'
        $result = @(& $GitCommand @Arguments 2>$null)
        $code = $LASTEXITCODE
    } finally { $ErrorActionPreference = $oldPreference }
    if ($code -ne 0) { throw ('Git operation failed (exit ' + $code + '). Check repository access; credentials were not printed.') }
    return $result
}

function Get-DivanRepositoryIdentity {
    param([string]$Address)
    $value = $Address.Trim()
    if ($value -match '^[^@/:]+@([^/:]+):(.+)$') {
        return ($Matches[1].ToLowerInvariant() + '/' + $Matches[2].TrimEnd('/').Replace('\', '/').ToLowerInvariant() -replace '\.git$', '')
    }
    $uri = $null
    if ([System.Uri]::TryCreate($value, [System.UriKind]::Absolute, [ref]$uri) -and $uri.Scheme -in @('https', 'ssh')) {
        $port = ''
        if (-not $uri.IsDefaultPort -and -not ($uri.Scheme -eq 'ssh' -and $uri.Port -eq 22)) { $port = ':' + $uri.Port }
        return ($uri.DnsSafeHost.ToLowerInvariant() + $port + '/' + $uri.AbsolutePath.Trim('/').ToLowerInvariant() -replace '\.git$', '')
    }
    if ($null -ne $uri -and $uri.Scheme -eq 'file') { $value = $uri.LocalPath }
    return (Get-DivanFullPath $value).TrimEnd([char[]]@('/', '\'))
}

function Assert-DivanRepository {
    param([string]$GitCommand, [string]$RepositoryPath, [string]$ExpectedIdentity)
    if (-not (Test-Path -LiteralPath $RepositoryPath -PathType Container)) { throw 'Repository directory is missing.' }
    $top = (@(Invoke-DivanGit $GitCommand @('-C', $RepositoryPath, 'rev-parse', '--show-toplevel')) -join "`n").Trim()
    if (-not (Test-DivanSamePath $top $RepositoryPath)) { throw 'RepositoryPath must be the existing checkout root, not its subdirectory.' }
    $origin = (@(Invoke-DivanGit $GitCommand @('-C', $RepositoryPath, 'remote', 'get-url', 'origin')) -join "`n").Trim()
    $actual = Get-DivanRepositoryIdentity $origin
    if ($actual -ne $ExpectedIdentity) { throw 'Existing origin does not identify the expected repository. It was preserved; no reset or remote rewrite was performed.' }
}

function Invoke-DivanPython {
    param($Context, [string[]]$Arguments)
    $prefix = @($Context.python_arguments)
    & $Context.python_command @prefix @Arguments
    if ($LASTEXITCODE -ne 0) { throw ('Divan command failed (exit ' + $LASTEXITCODE + ').') }
}

function Get-DivanContext {
    param([string]$Headquarters)
    $hq = Get-DivanFullPath $Headquarters
    $runtime = Join-Path $hq '.divan'
    $configPath = Join-Path $runtime '00_yonetim/windows.json'
    if (-not (Test-Path -LiteralPath $configPath -PathType Leaf)) { throw 'Run Setup-Divan.ps1 for this headquarters first.' }
    $config = Get-Content -LiteralPath $configPath -Raw -Encoding UTF8 | ConvertFrom-Json
    if ($config.surum -ne 1 -or -not (Test-DivanSamePath $config.headquarters $hq)) { throw 'Existing Windows configuration is inconsistent; it was preserved.' }
    $python = Get-DivanPython $config.python_command
    $gitCommand = Get-DivanApplication 'git'
    Assert-DivanRepository $gitCommand $config.repository_path $config.expected_origin_identity
    return [pscustomobject]@{
        headquarters = $hq
        runtime = $runtime
        repository_path = $config.repository_path
        python_command = $python.Command
        python_arguments = @($python.Arguments)
        member = $config.member
        message_branch = $config.message_branch
    }
}

function Write-DivanNewUtf8File {
    param([string]$Path, [string]$Text)
    $bytes = (New-Object System.Text.UTF8Encoding($false)).GetBytes($Text)
    $stream = New-Object System.IO.FileStream($Path, [System.IO.FileMode]::CreateNew, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)
    try { $stream.Write($bytes, 0, $bytes.Length); $stream.Flush() } finally { $stream.Dispose() }
}
