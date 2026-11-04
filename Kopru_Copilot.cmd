@echo off
rem ==========================================================================
rem  Kopru_Copilot.cmd
rem  GitHub Copilot CLI'yi ortak-kopru deposuna bagli olarak su ayarlarla acar:
rem    Mod: autopilot   Model: claude-opus-5.5   Akil yurutme eforu: max
rem
rem  Kullanim: cift tiklayin ya da komut isteminde calistirin.
rem    Kopru_Copilot.cmd [ek copilot secenekleri]
rem    Ornek: Kopru_Copilot.cmd --continue
rem
rem  Istege bagli ortam degiskenleri:
rem    KOPRU_KLASOR=yol   Deponun yerel klasoru. Verilmezse bu dosya bir
rem                       ortak-kopru klonunun icindeyse o klasor, degilse
rem                       %USERPROFILE%\ortak-kopru kullanilir.
rem    KOPRU_TAM_IZIN=1   --allow-all ekler; izin onay penceresi cikmaz.
rem    KOPRU_DENEME=1     Her seyi denetler ve komutu gosterir, baslatmaz.
rem
rem  Gerekenler: Git ve GitHub Copilot CLI. Eksikse winget ile kurmayi onerir.
rem  Kaynak: https://github.com/HalukAINRS/ortak-kopru
rem ==========================================================================
setlocal EnableExtensions DisableDelayedExpansion
title Kopru Copilot - ortak-kopru
rem Programlar yalnizca PATH'te aranir; gecerli klasordeki git.cmd gibi
rem ayni adli dosyalar calistirilmaz.
set "NoDefaultCurrentDirectoryInExePath=1"

set "MODEL=claude-opus-5.5"
set "EFOR=max"
set "DEPO_URL=https://github.com/HalukAINRS/ortak-kopru.git"
for %%I in ("%~dp0.") do set "BETIK_KLASORU=%%~fI"

echo ==========================================================
echo  Kopru Copilot: GitHub Copilot CLI + ortak-kopru
echo  Model: %MODEL%   Efor: %EFOR%   Mod: autopilot
echo ==========================================================
echo(

echo [1/4] Git denetleniyor...
call :git_bul
if not errorlevel 1 goto :git_hazir
call :kur Git.Git "Git"
call :git_bul
if not errorlevel 1 goto :git_hazir
set "HATA=Git bulunamadi. Kurmak icin: winget install --id Git.Git -e"
goto :hata
:git_hazir
echo       "%BULUNAN%"

echo [2/4] GitHub Copilot CLI denetleniyor...
call :copilot_bul
if not errorlevel 1 goto :copilot_hazir
call :kur GitHub.Copilot "GitHub Copilot CLI"
call :copilot_bul
if not errorlevel 1 goto :copilot_hazir
set "HATA=GitHub Copilot CLI bulunamadi. Kurmak icin: winget install --id GitHub.Copilot -e"
goto :hata
:copilot_hazir
echo       "%BULUNAN%"
call :pwsh_bul
if errorlevel 1 goto :pwsh_yok
echo       PowerShell 7: "%BULUNAN%"
goto :pwsh_hazir
:pwsh_yok
echo       Not: PowerShell 7 bulunamadi; Copilot Windows PowerShell 5.1 kullanacak.
echo       Kurmak icin: winget install --id Microsoft.PowerShell -e
:pwsh_hazir

if not defined KOPRU_KLASOR goto :klasor_otomatik
set "KOPRU_KLASOR=%KOPRU_KLASOR:"=%"
if not defined KOPRU_KLASOR goto :klasor_otomatik
for %%I in ("%KOPRU_KLASOR%\.") do set "KLASOR=%%~fI"
goto :klasor_secildi
:klasor_otomatik
call :depo_mu "%BETIK_KLASORU%"
if errorlevel 1 goto :klasor_varsayilan
set "KLASOR=%BETIK_KLASORU%"
goto :klasor_secildi
:klasor_varsayilan
set "KLASOR=%USERPROFILE%\ortak-kopru"
:klasor_secildi

echo [3/4] Depo hazirlaniyor: "%KLASOR%"
set "GUNCELLE="
if exist "%KLASOR%\.git" goto :depo_var
git clone "%DEPO_URL%" "%KLASOR%"
if not errorlevel 1 goto :baslat
set "HATA=Depo klonlanamadi. Internet baglantisini, GitHub oturumunu ve klasoru denetleyin."
goto :hata
:depo_var
call :depo_mu "%KLASOR%"
if errorlevel 1 goto :depo_yanlis
set "GUNCELLE=1"
goto :baslat
:depo_yanlis
if defined UZAK echo       Bu klasorun origin adresi: "%UZAK%"
if not defined UZAK echo       Bu klasorde origin adresi tanimli degil.
set "HATA=Klasor ortak-kopru deposunun klonu degil. KOPRU_KLASOR ile baska bir klasor secin."
goto :hata

:baslat
set "SECENEKLER=--model %MODEL% --reasoning-effort %EFOR% --autopilot"
if "%KOPRU_TAM_IZIN%"=="1" set "SECENEKLER=%SECENEKLER% --allow-all"
rem Asagidaki blok bir kerede okunur; git pull ya da Copilot bu dosyayi
rem degistirse bile calismakta olan komutlar etkilenmez.
(
  if defined GUNCELLE (
    git -C "%KLASOR%" pull --ff-only --quiet || echo       Uyari: Depo guncellenemedi; yerel hali ile devam ediliyor.
  )
  echo [4/4] Copilot baslatiliyor: copilot %SECENEKLER% %*
  if "%KOPRU_DENEME%"=="1" (
    echo(
    echo [deneme] KOPRU_DENEME=1 oldugu icin Copilot baslatilmadi.
    exit /b 0
  )
  echo(
  cd /d "%KLASOR%" && call copilot %SECENEKLER% %* && exit /b 0
  call set "CIKIS=%%ERRORLEVEL%%"
  echo(
  call echo [uyari] Copilot %%CIKIS%% cikis koduyla kapandi.
  echo         Oturum acmak icin Copilot icinde /login yazin. Surum eskiyse: copilot update
  if not defined CI pause
  exit /b 1
)

:hata
echo(
echo [hata] %HATA%
if not defined CI pause
exit /b 1

:git_bul
call :bul git "%ProgramFiles%\Git\cmd" "%LOCALAPPDATA%\Programs\Git\cmd"
exit /b

:copilot_bul
call :bul copilot "%LOCALAPPDATA%\Microsoft\WinGet\Links" "%ProgramFiles%\WinGet\Links" "%APPDATA%\npm"
exit /b

:pwsh_bul
set "PWSH_KLASORU="
(for /d %%D in ("Y:\Programs\WindowsPowerShell\PowerShell-*") do if exist "%%~fD\pwsh.exe" set "PWSH_KLASORU=%%~fD") 2>nul
call :bul pwsh "%ProgramFiles%\PowerShell\7" "%PWSH_KLASORU%"
exit /b

:bul
rem Komutun tam yolunu BULUNAN degiskenine yazar. Once PATH, sonra verilen
rem klasorler aranir; komut bir klasorde bulunursa o klasor PATH'e eklenir.
set "BUL_KOMUT=%~1"
set "BULUNAN="
for %%X in (%BUL_KOMUT%.exe %BUL_KOMUT%.cmd) do if not defined BULUNAN set "BULUNAN=%%~$PATH:X"
if defined BULUNAN exit /b 0
:bul_sonraki
shift
if "%~1"=="" exit /b 1
set "BULUNAN=%~1\%BUL_KOMUT%.exe"
if exist "%BULUNAN%" goto :bul_ekle
set "BULUNAN=%~1\%BUL_KOMUT%.cmd"
if exist "%BULUNAN%" goto :bul_ekle
set "BULUNAN="
goto :bul_sonraki
:bul_ekle
set "PATH=%~1;%PATH%"
exit /b 0

:kur
rem Eksik araci kullanici onaylarsa winget ile kurar. CI ortaminda sormaz.
if defined CI exit /b 1
set "WINGET="
for %%X in (winget.exe) do set "WINGET=%%~$PATH:X"
if not defined WINGET exit /b 1
echo(
echo       %~2 bulunamadi. winget ile simdi kurulsun mu?
choice /c EH /n /m "      [E]vet / [H]ayir: "
if errorlevel 2 exit /b 1
if not errorlevel 1 exit /b 1
winget install --id %~1 -e --source winget --accept-package-agreements --accept-source-agreements
exit /b

:depo_mu
rem Klasor GitHub'daki HalukAINRS/ortak-kopru deposunun klonuysa 0 dondurur.
set "UZAK="
if not exist "%~1\.git" exit /b 1
for /f "usebackq delims=" %%U in (`git -C "%~1" remote get-url origin 2^>nul`) do set "UZAK=%%U"
if not defined UZAK exit /b 1
set "UZAK=%UZAK:"=%"
if not defined UZAK exit /b 1
if "%UZAK:~-1%"=="/" set "UZAK=%UZAK:~0,-1%"
if /i "%UZAK:~-4%"==".git" set "UZAK=%UZAK:~0,-4%"
set "UZAK_SON=%UZAK:~-34%"
if /i "%UZAK_SON%"=="/github.com/HalukAINRS/ortak-kopru" exit /b 0
if /i "%UZAK_SON%"=="@github.com/HalukAINRS/ortak-kopru" exit /b 0
if /i "%UZAK_SON%"=="@github.com:HalukAINRS/ortak-kopru" exit /b 0
exit /b 1
