param([string]$Config='Y:\HalukAI\Ortak_Kopru\DEUS_CLI\feedback\config.json',[switch]$Denetle)
$ErrorActionPreference='Stop'
if(-not (Test-Path -LiteralPath $Config -PathType Leaf)){
    if($Denetle){[ordered]@{Configured=$false;Running=$false}|ConvertTo-Json;return}
    throw 'Geri donus icin belirli oturum ve kaynak kaydi gerekli.'
}
$settings=Get-Content -LiteralPath $Config -Raw | ConvertFrom-Json
$guid=[Guid]::Empty
if(-not [Guid]::TryParse($settings.target_thread,[ref]$guid)){throw 'Gecerli belirli oturum gerekli.'}
$binding=Get-Content -LiteralPath 'Y:\HalukAI\Ortak_Kopru\DEUS_CLI\queue_binding.json' -Raw | ConvertFrom-Json
if($binding.target_thread -ne $settings.target_thread){throw 'Mevcut Deus oturum bagi ile uyusmuyor.'}
$script=Join-Path $PSScriptRoot 'feedback_watch.py'
$stateDir=Split-Path -Parent $Config
$pidFile=Join-Path $stateDir 'runtime.json'
$running=$false
if(Test-Path -LiteralPath $pidFile){
    $saved=Get-Content -LiteralPath $pidFile -Raw | ConvertFrom-Json -DateKind String
    $proc=Get-CimInstance Win32_Process -Filter ('ProcessId='+[int]$saved.pid) -ErrorAction SilentlyContinue
    $running=$proc -and $proc.CommandLine.Contains($script) -and $proc.CommandLine.Contains($Config) -and
        $proc.CreationDate.ToUniversalTime().ToString('o') -eq $saved.process_start_utc
}
if($Denetle){[ordered]@{Configured=$true;Running=[bool]$running;BoundToExistingSession=$true;RegisteredSources=@($settings.sources).Count;LoadedCodeMatchesDisk=($running -and $saved.script_sha256 -eq (Get-FileHash -LiteralPath $script -Algorithm SHA256).Hash)}|ConvertTo-Json;return}
if(-not $running){
    $python='Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime\Python\python.exe'
    $args=@('-I','-B','-X','utf8',('"'+$script+'"'),'watch','--config',('"'+$Config+'"'))
    $child=Start-Process -FilePath $python -ArgumentList $args -WorkingDirectory $settings.workspace -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $stateDir 'stdout.log') -RedirectStandardError (Join-Path $stateDir 'stderr_ozel.log')
    Start-Sleep -Milliseconds 700
    if($child.HasExited){throw 'Geri donus izleyicisi baslamadi; ozel gunlugu denetle.'}
    $actual=Get-CimInstance Win32_Process -Filter ('ProcessId='+$child.Id)
    [ordered]@{pid=$child.Id;process_start_utc=$actual.CreationDate.ToUniversalTime().ToString('o');script=$script;config=$Config;script_sha256=(Get-FileHash -LiteralPath $script -Algorithm SHA256).Hash}|ConvertTo-Json|Set-Content -LiteralPath $pidFile -Encoding utf8
}
[ordered]@{Running=$true;ExistingSession=$true;NewModelProcess=$false;PollSeconds=10}|ConvertTo-Json
