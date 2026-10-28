param(
    [string]$StateDir='Y:\HalukAI\Ortak_Kopru\DEUS_CLI',
    [string]$Oturum=$env:CODEX_THREAD_ID,
    [string]$Workspace='Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\Workspace',
    [switch]$Denetle
)
$ErrorActionPreference='Stop'
$runtime='Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime'
$python=Join-Path $runtime 'Python\python.exe'
$codex='Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\03_Codex_Saman\npm_global\node_modules\@openai\codex\node_modules\@openai\codex-win32-x64\vendor\x86_64-pc-windows-msvc\bin\codex.exe'
$binding=Join-Path $StateDir 'queue_binding.json'
$pidFile=Join-Path $StateDir 'queue_runtime.json'
$old=$null
if(Test-Path -LiteralPath $binding) {$old=Get-Content -LiteralPath $binding -Raw | ConvertFrom-Json}
if(-not $Oturum -and $old) {$Oturum=$old.target_thread}
$guid=[Guid]::Empty
if(-not [Guid]::TryParse($Oturum,[ref]$guid)) {throw 'Bu açık oturumdan çalıştır veya daha önce kaydedilmiş oturum bağını kullan.'}
if($old -and $old.target_thread -ne $Oturum) {throw 'Kayıtlı kuyruk başka oturuma bağlı; açık işleri denetlemeden hedef değiştirilmez.'}
$running=$false
if(Test-Path -LiteralPath $pidFile) {
    $saved=Get-Content -LiteralPath $pidFile -Raw | ConvertFrom-Json
    $process=Get-CimInstance Win32_Process -Filter ('ProcessId='+[int]$saved.pid) -ErrorAction SilentlyContinue
    $running=$process -and $process.CommandLine.Contains((Join-Path $PSScriptRoot 'queue_consumer.py')) -and $process.CommandLine.Contains($Oturum)
}
if($Denetle) {
    [pscustomobject]@{BindingExists=[bool]$old;ConsumerRunning=[bool]$running;CodexExists=(Test-Path -LiteralPath $codex);WorkspaceExists=(Test-Path -LiteralPath $Workspace)} | ConvertTo-Json
    return
}
New-Item -ItemType Directory -Path $StateDir -Force | Out-Null
if(-not $old) {
    [pscustomobject]@{target_thread=$Oturum;participant='Şaman';new_model_process=$false} | ConvertTo-Json | Set-Content -LiteralPath $binding -Encoding utf8
}
if(-not $running) {
    $args=@('-X','utf8',('"'+(Join-Path $PSScriptRoot 'queue_consumer.py')+'"'),
        '--state-dir',('"'+$StateDir+'"'),'--codex-exe',('"'+$codex+'"'),
        '--workspace',('"'+$Workspace+'"'),'--thread',$Oturum)
    $child=Start-Process -FilePath $python -ArgumentList $args -WorkingDirectory $Workspace -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $StateDir 'queue_stdout.log') -RedirectStandardError (Join-Path $StateDir 'queue_stderr.log')
    Start-Sleep -Milliseconds 700
    if($child.HasExited) {throw ('Kuyruk tüketicisi başlamadı; özel hata günlüğü: '+(Join-Path $StateDir 'queue_stderr.log'))}
    [pscustomobject]@{pid=$child.Id;consumer_script=(Join-Path $PSScriptRoot 'queue_consumer.py');started=[DateTimeOffset]::UtcNow.ToString('o')} | ConvertTo-Json | Set-Content -LiteralPath $pidFile -Encoding utf8
}
[pscustomobject]@{ConsumerRunning=$true;ExistingThread=$true;NewModelProcess=$false;StateDir=$StateDir} | ConvertTo-Json
