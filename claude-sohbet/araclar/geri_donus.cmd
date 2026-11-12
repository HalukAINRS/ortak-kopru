@echo off
rem ======================================================================
rem  geri_donus.cmd -- noktadan tohumu ve bolumleri geri alir.
rem  Kullanim: nokta dosyasini bu betigin ustune surukleyip birakin
rem            ya da komut isteminde:  geri_donus.cmd DOSYA
rem  Yaninda cevrim.exe durmalidir. Verilen dosyaya dokunmaz; yanina iki
rem  yeni dosya yazar:
rem     AD.tohum.UZANTI    bolumleri cikarilmis metin (tohum)
rem     AD.bolumler.txt    cikarilan bolumler, basliklariyla
rem  Ardindan dener: tohum ile bolumler yeniden birlestirilince ayni
rem  nokta cikiyor mu?
rem  Cikis kodu: 0 ayrildi, 1 ayrilacak bolum yok, -1 olmadi.
rem ======================================================================
setlocal EnableExtensions DisableDelayedExpansion
set "KOD=-1"
if "%~1"=="" goto :kullanim
if not exist "%~1" goto :kullanim
if exist "%~1\*" goto :kullanim
if not exist "%~dp0cevrim.exe" goto :arac_yok
set "A=%~dpn1"
set "U=%~x1"
"%~dp0cevrim.exe" <"%~1" >"%A%.c1.tmp" 2>"%A%.c2.tmp"
if not "%errorlevel%"=="0" goto :olmadi
if not exist "%A%.c2.tmp" goto :olmadi
set "BOY=?"
for %%F in ("%A%.c2.tmp") do set "BOY=%%~zF"
if "%BOY%"=="0" goto :bolum_yok
rem --- deneme: bolumler + tohum yeniden ayni noktayi veriyor mu
copy /y /b "%A%.c2.tmp"+"%A%.c1.tmp" "%A%.g.tmp" >nul
"%~dp0cevrim.exe" <"%A%.g.tmp" >"%A%.d.tmp" 2>nul
fc /b "%A%.d.tmp" "%~1" >nul 2>nul
set "FARK=%errorlevel%"
move /y "%A%.c1.tmp" "%A%.tohum%U%" >nul
move /y "%A%.c2.tmp" "%A%.bolumler.txt" >nul
set "KOD=0"
for %%F in ("%~1") do echo nokta    : %%~zF bayt  %%~nxF
for %%F in ("%A%.tohum%U%") do echo tohum    : %%~zF bayt  %%~nxF
for %%F in ("%A%.bolumler.txt") do echo bolumler : %%~zF bayt  %%~nxF
if "%FARK%"=="0" echo Denendi: tohum ile bolumler yeniden birlestirilince ayni nokta cikti.
if "%FARK%"=="1" echo UYARI: yeniden birlestirince ayni nokta cikmadi. Bolumlerden biri
if "%FARK%"=="1" echo kendi basliginin altinda durmuyor olabilir. Dosyalar yine de yazildi.
if not "%FARK%"=="0" if not "%FARK%"=="1" echo Not: deneme yapilamadi; fc komutu calismadi.
goto :son
:bolum_yok
set "KOD=1"
echo Bu dosyada ayrilacak bolum yok: dosya zaten tohum. Hicbir sey yazilmadi.
goto :son
:olmadi
echo Olmadi. Dosya bir nokta degil ya da 8 MiB'tan buyuk.
echo Ilk satiri tek nokta olan dosya bolumler dosyasidir; nokta degildir.
goto :son
:arac_yok
echo cevrim.exe bu betigin yaninda yok.
goto :son
:kullanim
echo Kullanim: nokta dosyasini bu betigin ustune surukleyip birakin.
:son
if defined A del "%A%.c1.tmp" 2>nul
if defined A del "%A%.c2.tmp" 2>nul
if defined A del "%A%.g.tmp" 2>nul
if defined A del "%A%.d.tmp" 2>nul
if not defined SINA_BEKLEME pause
endlocal & exit /b %KOD%
