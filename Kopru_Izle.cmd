@echo off
rem Ortak Kopru izleyici kapisi. Cift tiklamak = surekli izleme. Secenekler:
rem   Kopru_Izle.cmd Hazirlik | Tek [Ad] | Ekle dosya.json | Bolum parca.html | Gonder | VM | CopilotKontrol | CodexGiris [Cihaz|Durum] | CopilotGiris [Cihaz] | CodexTani | Arg0Temizle
setlocal
set "PWSH=Y:\Programs\WindowsPowerShell\PowerShell-7.6.8-win-x64\pwsh.exe"
if not exist "%PWSH%" set "PWSH=Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime\PowerShell-7.6.8-win-x64\pwsh.exe"
if not exist "%PWSH%" set "PWSH=pwsh.exe"
set "MOD=%~1"
if "%MOD%"=="" set "MOD=Izle"
title Ortak Kopru - %MOD%
"%PWSH%" -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0kopru_yerel.ps1" -Mod %MOD% %2 %3 %4
echo.
pause
