@echo off
rem ============================================================================
rem  durum_satiri.cmd  -  Claude Code durum satirini uretir
rem ============================================================================
rem  .claude\settings.json icinde statusLine.command = durum_satiri.cmd olarak cagrilir.
rem  Kapi araclar\ klasorunu PATH'e ekler; komut adiyla bulunur, surucu harfinden bagimsizdir.
rem  Asil is yanindaki durum_satiri.ps1 dosyasindadir. Kapi PowerShell 7 bulduysa (KARARGAH_PWSH)
rem  o, bulmadiysa Windows PowerShell kullanilir. Girdi (JSON) stdin'den aynen gecer.
rem  Dosya ASCII + CRLF, BOM'suz.
rem ============================================================================
if not defined KARARGAH_PWSH goto :ps5
if not exist "%KARARGAH_PWSH%" goto :ps5
"%KARARGAH_PWSH%" -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0durum_satiri.ps1"
exit /b %errorlevel%
:ps5
powershell -NoLogo -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0durum_satiri.ps1"
exit /b %errorlevel%
