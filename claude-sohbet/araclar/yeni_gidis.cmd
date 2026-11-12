@echo off
rem ======================================================================
rem  yeni_gidis.cmd -- bolumleri bir tohuma yerlestirir (yeni nokta).
rem  Kullanim: kendi dosyanizi bu betigin ustune surukleyip birakin
rem            ya da komut isteminde:  yeni_gidis.cmd DOSYA [BOLUMLER]
rem  Yaninda cevrim.exe ve bolumler.txt durmalidir. Verilen dosyaya
rem  dokunmaz; yanina yeni dosya yazar:
rem     AD.nokta.UZANTI          bolumleri yerlesmis metin (nokta)
rem     AD.yerlesmeyen.txt       basligi bu dosyada bulunmayan bolumler
rem     AD.onceki_bolumler.txt   dosyada zaten bolum vardiysa: onlar
rem  Dosyada zaten bolum varsa once onlari ayirir (geri donus); yeni
rem  gidis tohumdan baslar. Ardindan dener: nokta ayrilinca tohum bayt
rem  bayt geri geliyor mu?
rem  Cikis kodu: yerlesmeyen bolumlerin adedi (0: hepsi yerlesti),
rem  -1: olmadi.
rem ======================================================================
setlocal EnableExtensions DisableDelayedExpansion
set "KOD=-1"
if "%~1"=="" goto :kullanim
if not exist "%~1" goto :kullanim
if exist "%~1\*" goto :kullanim
if not exist "%~dp0cevrim.exe" goto :arac_yok
set "B=%~dp0bolumler.txt"
if not "%~2"=="" set "B=%~f2"
if not exist "%B%" goto :bolum_yok
set "A=%~dpn1"
set "U=%~x1"
rem --- 1) geri donus: dosyada zaten bolum varsa ayir; tohumu al
"%~dp0cevrim.exe" <"%~1" >"%A%.t0.tmp" 2>"%A%.o.tmp"
if not "%errorlevel%"=="0" goto :tohum_degil
if not exist "%A%.o.tmp" goto :tohum_degil
set "ONCEKI=0"
for %%F in ("%A%.o.tmp") do set "ONCEKI=%%~zF"
rem --- 2) yeni gidis: bolumler + tohum - nokta
copy /y /b "%B%"+"%A%.t0.tmp" "%A%.g.tmp" >nul
"%~dp0cevrim.exe" <"%A%.g.tmp" >"%A%.n.tmp" 2>"%A%.y.tmp"
set "KOD=%errorlevel%"
if "%KOD%"=="-1" goto :olmadi
rem --- 3) deneme: nokta ayrilinca tohum geri geliyor mu
"%~dp0cevrim.exe" <"%A%.n.tmp" >"%A%.t1.tmp" 2>nul
fc /b "%A%.t1.tmp" "%A%.t0.tmp" >nul 2>nul
set "FARK=%errorlevel%"
move /y "%A%.n.tmp" "%A%.nokta%U%" >nul
if not "%ONCEKI%"=="0" move /y "%A%.o.tmp" "%A%.onceki_bolumler.txt" >nul
if "%KOD%"=="0" del "%A%.yerlesmeyen.txt" 2>nul
if not "%KOD%"=="0" move /y "%A%.y.tmp" "%A%.yerlesmeyen.txt" >nul
for %%F in ("%~1") do echo dosya : %%~zF bayt  %%~nxF
for %%F in ("%A%.nokta%U%") do echo nokta : %%~zF bayt  %%~nxF
if not "%ONCEKI%"=="0" echo Not: verdiginiz dosyada zaten bolum vardi. Once ayrilip
if not "%ONCEKI%"=="0" echo onceki_bolumler.txt dosyasina yazildilar. Yeni gidis tohumdan basladi.
if "%KOD%"=="0" echo Butun bolumler yerlesti.
if not "%KOD%"=="0" echo %KOD% bolum yerlesmedi: basliklari bu dosyada yok. Kaybolmadilar;
if not "%KOD%"=="0" echo yerlesmeyen.txt dosyasinda duruyorlar.
if "%FARK%"=="0" echo Denendi: nokta ayrilinca tohum bayt bayt geri geliyor.
if "%FARK%"=="1" echo UYARI: nokta ayrilinca tohum ayni cikmadi. Bu noktayi kullanmadan
if "%FARK%"=="1" echo once dosyalari karsilastirin.
if not "%FARK%"=="0" if not "%FARK%"=="1" echo Not: deneme yapilamadi; fc komutu calismadi.
goto :son
:olmadi
echo Olmadi: bolumler dosyasi bozuk ya da girdi 8 MiB'tan buyuk.
goto :son
:tohum_degil
echo Olmadi. Verilen dosya tohum degil ya da 8 MiB'tan buyuk.
echo Ilk satiri tek nokta olan dosya bolumler dosyasidir; tohum degildir.
goto :son
:bolum_yok
echo Bolumler dosyasi bulunamadi: bolumler.txt bu betigin yaninda durmali.
goto :son
:arac_yok
echo cevrim.exe bu betigin yaninda yok.
goto :son
:kullanim
echo Kullanim: kendi dosyanizi bu betigin ustune surukleyip birakin.
:son
if defined A del "%A%.t0.tmp" 2>nul
if defined A del "%A%.t1.tmp" 2>nul
if defined A del "%A%.o.tmp" 2>nul
if defined A del "%A%.g.tmp" 2>nul
if defined A del "%A%.n.tmp" 2>nul
if defined A del "%A%.y.tmp" 2>nul
if not defined SINA_BEKLEME pause
endlocal & exit /b %KOD%
