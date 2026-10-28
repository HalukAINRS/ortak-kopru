@echo off
rem Hacker VM'deki Claude Code CLI ile uzaktan kontrol oturumu acar (claude remote-control).
rem Oturum Claude Code uygulamasinda gorunur; bu pencere acik kaldikca surer.
rem Kullanim: Hacker_Uzak_Kontrol.cmd [VM_DIZINI]   (varsayilan: /home/hacker/Uzak_Oturum)
rem VM'yi baslatmaz (once: Kopru_Izle.cmd VM), kimlik dosyasi kopyalamaz, ayar degistirmez.
rem VM, Y: surucusunu gormez; oturum yalniz VM'deki dosyalarla calisir.
rem SSH yollari ayarlar-yerel.json ve kopru_yerel.ps1'deki Hacker yoluyla aynidir.
setlocal
set "SSH=Y:\archive\30_Govde_Sistem\Calisma_Zamani\2026-10-25_Canli\Git-Portable-2.56.0.2\usr\bin\ssh.exe"
if not exist "%SSH%" set "SSH=Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime\Git-Portable-2.56.0.2\usr\bin\ssh.exe"
if not exist "%SSH%" set "SSH=ssh.exe"
set "ANAHTARLAR=Y:\archive\10_Katmanlar\Hacker_Claude_Code\2026-10-25_Canli\Home\.ssh"
if not exist "%ANAHTARLAR%\hacker_arm64_035" set "ANAHTARLAR=Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\01_Claude_Code_Hacker\Home\.ssh"
set "CLAUDE_VM=/home/hacker/bin/claude-arm64-035"
set "DIZIN=%~1"
if "%DIZIN%"=="" set "DIZIN=/home/hacker/Uzak_Oturum"
title Hacker - Claude uzaktan kontrol
if not exist "%ANAHTARLAR%\hacker_arm64_035" (
  echo Hacker SSH anahtari bulunamadi; ayarlar-yerel.json'daki yolu denetleyin.
  pause
  exit /b 1
)
echo VM'deki Claude Code denetleniyor...
"%SSH%" -p 2222 -i "%ANAHTARLAR%\hacker_arm64_035" -o BatchMode=yes -o "UserKnownHostsFile=%ANAHTARLAR%\known_hosts" -o StrictHostKeyChecking=yes -o LogLevel=ERROR -o ConnectTimeout=15 hacker@127.0.0.1 "%CLAUDE_VM% --version"
if errorlevel 1 (
  echo VM'ye baglanilamadi ya da Claude Code calismadi. VM kapaliysa ayri pencerede: Kopru_Izle.cmd VM
  pause
  exit /b 1
)
echo Uzaktan kontrol aciliyor: %DIZIN%
echo Oturum Claude Code uygulamasinda gorunur. Bu pencereyi kapatmak oturumu bitirir.
"%SSH%" -tt -p 2222 -i "%ANAHTARLAR%\hacker_arm64_035" -o BatchMode=yes -o "UserKnownHostsFile=%ANAHTARLAR%\known_hosts" -o StrictHostKeyChecking=yes -o LogLevel=ERROR -o ConnectTimeout=15 hacker@127.0.0.1 "mkdir -p '%DIZIN%' && cd '%DIZIN%' && exec %CLAUDE_VM% remote-control"
echo.
echo Oturum kapandi (cikis kodu %errorlevel%).
pause
