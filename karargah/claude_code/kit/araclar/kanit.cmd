@echo off
rem ============================================================================
rem  kanit.cmd  -  Karargah tek ortam kuralina uyuyor mu: bakar, sinar, rapor verir
rem ============================================================================
rem  Yeri: <karargah>\araclar\kanit.cmd. Kapi araclar\ klasorunu PATH'e ekler; oturum icinden de calisir.
rem
rem  KULLANIM
rem    kanit.cmd            Cevrimdisi kanit. Oturum acmaz, aga cikmaz:
rem                           - kapiyi KARARGAH_DENEME=1 ile kuru calistirir; komutu ve dizini denetler
rem                           - durum satirini ornek girdiyle calistirir
rem                           - kit dosyalarina ve ayara bakar
rem    kanit.cmd --canli    Ek olarak gercek claude.exe ile tek bir -p cagrisi yapar (hesabinizdan kucuk bir
rem                         kullanim duser; yalniz Read araci acik, oturum kaydi tutulmaz). Claude uc isaret
rem                         dosyasini okumayi dener: kokte, eklenen uzak yerde, ikisinin disinda.
rem
rem  Sonuc sozleri: GECTI . KALDI . ATLANDI (bu ortam sinamaya elvermiyor) . BILGI
rem  Rapor ekrana ve <karargah>\gecici\kanit.son.txt dosyasina yazilir. Cikis kodu: KALDI varsa 1.
rem  Sinama sirasinda uc gecici klasor acilir ve sonunda silinir; onceden varsalar sinama baslamaz:
rem    <ust klasor>\_kanit uzak   eklenen uzak yer
rem    <ust klasor>\_kanit dis    hicbir yere eklenmeyen yer
rem    <karargah>\gecici\kanit    ara dosyalar
rem  Kok yerlesimi icindir. Dosya ASCII + CRLF, BOM'suz.
rem ============================================================================
setlocal EnableExtensions DisableDelayedExpansion

rem ---- [00] Kod sayfasi: sakla, UTF-8'e gec --------------------------------------
set "KANIT_CP="
for /f "tokens=2 delims=:" %%A in ('chcp') do set "KANIT_CP=%%A"
if defined KANIT_CP set "KANIT_CP=%KANIT_CP: =%"
if defined KANIT_CP set "KANIT_CP=%KANIT_CP:.=%"
chcp 65001 >nul 2>&1

rem ---- [01] Yerler ve on kosullar ------------------------------------------------
for %%I in ("%~dp0..") do set "KANIT_KOK=%%~fI"
if "%KANIT_KOK:~-1%"=="\" set "KANIT_KOK=%KANIT_KOK:~0,-1%"
for %%I in ("%KANIT_KOK%\..") do set "KANIT_UST=%%~fI"
if "%KANIT_UST:~-1%"=="\" set "KANIT_UST=%KANIT_UST:~0,-1%"
set "KANIT_KAPI=%KANIT_KOK%\claude_code.cmd"
set "KANIT_GECICI=%KANIT_KOK%\gecici\kanit"
set "KANIT_RAPOR=%KANIT_KOK%\gecici\kanit.son.txt"
set "KANIT_CIKTI=%KANIT_GECICI%\cikti.txt"
set "KANIT_UZAK=%KANIT_UST%\_kanit uzak"
set "KANIT_DIS=%KANIT_UST%\_kanit dis"
set "KANIT_CANLI="
if /i "%~1"=="--canli" set "KANIT_CANLI=1"
set "KANIT_HATA="
set /a KANIT_GECEN=0
set /a KANIT_KALAN=0
set /a KANIT_ATLANAN=0

if not exist "%KANIT_KAPI%" goto :hata_kapi
findstr /c:"KARARGAH_DENEME" "%KANIT_KAPI%" >nul 2>&1
if errorlevel 1 goto :hata_eski
if exist "%KANIT_UZAK%\" goto :hata_kalinti
if exist "%KANIT_DIS%\" goto :hata_kalinti
if exist "%KANIT_GECICI%\" goto :hata_kalinti
if not exist "%KANIT_KOK%\gecici\" mkdir "%KANIT_KOK%\gecici" >nul 2>&1
mkdir "%KANIT_GECICI%" >nul 2>&1
mkdir "%KANIT_UZAK%" >nul 2>&1
mkdir "%KANIT_DIS%" >nul 2>&1
if not exist "%KANIT_GECICI%\" goto :hata_yazilamadi
if not exist "%KANIT_UZAK%\" goto :hata_yazilamadi
if not exist "%KANIT_DIS%\" goto :hata_yazilamadi

rem ---- [02] Rapor basligi: ne goruluyor ----------------------------------------
>"%KANIT_RAPOR%" echo Karargah kaniti
call :yaz "BILGI   kok    : %KANIT_KOK%"
set "KANIT_SISTEM="
for /f "delims=" %%V in ('ver') do if not defined KANIT_SISTEM set "KANIT_SISTEM=%%V"
call :yaz "BILGI   sistem : %KANIT_SISTEM%"
set "KANIT_SURUM="
for /f "usebackq delims=" %%V in (`call "%KANIT_KOK%\uygulama\yerel\claude.exe" --version 2^>nul`) do if not defined KANIT_SURUM set "KANIT_SURUM=%%V"
if not defined KANIT_SURUM set "KANIT_SURUM=okunamadi"
call :yaz "BILGI   claude : %KANIT_SURUM%"
call :yaz "BILGI   zaman  : %DATE% %TIME%"

rem ---- [03] Kapi: kuru calistirma -------------------------------------------------
rem Her sinama kapiyi gercek argumanlarla cagirir; KARARGAH_DENEME=1 oldugu icin kapi komutu ve calisma
rem dizinini yazar, Claude Code'u baslatmaz. Ortak kural hazirligi (hazirlik.cmd) cagrilmaz.
set "KARARGAH_DENEME=1"
set "KARARGAH_HAZIRLIK=0"
set "KARARGAH_DIZIN="

set "KANIT_AD=kapi: arguman yok, oturum kokte, ek dizin yok"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :yok "--add-dir"
call :bitir

set "KANIT_AD=kapi: --burada, oturum kokte, klasor eklenir, oturum adi verilir"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --burada <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :var "--add-dir="
call :var "_kanit uzak"
call :var "-n "
call :bitir

set "KANIT_AD=kapi: --burada --continue, klasor yeniden eklenir, ad verilmez"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --burada --continue <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :var "--add-dir="
call :var "--continue"
call :yok " -n "
call :bitir

set "KANIT_AD=kapi: --continue, oturum kokte"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --continue <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :yok "--add-dir"
call :bitir

set "KANIT_AD=kapi: --resume, oturum kokte"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --resume <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :yok "--add-dir"
call :bitir

set "KANIT_AD=kapi: bayraksiz istem yutulmaz (cok degerli bayraklar = ile)"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --burada "bir istem" <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :var "bir istem"
call :var "--add-dir="
call :yok "--add-dir "
call :yok "--mcp-config "
call :bitir

set "KANIT_AD=kapi: remote-control, sunucu kokte, karakter fiilden sonra"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" remote-control <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :var " remote-control"
call :yok "--model"
call :yok "--mcp-config"
call :bitir

set "KANIT_AD=kapi: --burada remote-control reddedilir"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --burada remote-control <nul >"%KANIT_CIKTI%" 2>&1
popd
call :var "remote-control her zaman karargah kokunde"
call :yok "[deneme]"
call :bitir

set "KANIT_AD=kapi: alt komut kokte calisir (doctor)"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" doctor <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :var " doctor"
call :bitir

set "KANIT_AD=kapi: olmayan klasor eklenmez"
set "KARARGAH_DIZIN=%KANIT_UST%\_kanit yok"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --continue <nul >"%KANIT_CIKTI%" 2>&1
popd
set "KARARGAH_DIZIN="
call :dizin
call :var "uzak yer eklenmedi"
call :yok "--add-dir"
call :bitir

set "KANIT_AD=kapi: dokuz arguman reddedilir"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --burada 1 2 3 4 5 6 7 8 9 <nul >"%KANIT_CIKTI%" 2>&1
popd
call :var "en cok sekiz arguman"
call :yok "[deneme]"
call :bitir

set "KANIT_AD=kapi: kokten --burada ek dizin vermez"
pushd "%KANIT_KOK%"
call "%KANIT_KAPI%" --burada <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :yok "--add-dir"
call :bitir

set "KANIT_AD=kapi: surucu koku eklenir"
if not exist "%SystemDrive%\" goto :kok_surucu_atla
pushd "%SystemDrive%\"
call "%KANIT_KAPI%" --burada --continue <nul >"%KANIT_CIKTI%" 2>&1
popd
call :dizin
call :var "--add-dir="
call :var ":\."
call :bitir
goto :kok_surucu_son
:kok_surucu_atla
call :atla "bu ortam surucu kokunu klasor olarak gormuyor"
:kok_surucu_son

rem ---- [04] Durum satiri: ornek girdi --------------------------------------------
rem Girdi, Claude Code'un verdigi JSON'un ayni bicimidir; kok ve uzak yer bu karargahin gercek yollaridir.
rem Beklenen: satir "karargah" ile baslar, eklenen yeri ve oturum adini gosterir.
set "KANIT_KOK_J=%KANIT_KOK:\=\\%"
set "KANIT_UZAK_J=%KANIT_UZAK:\=\\%"
>"%KANIT_GECICI%\durum.json" echo {"workspace":{"current_dir":"%KANIT_KOK_J%","project_dir":"%KANIT_KOK_J%","added_dirs":["%KANIT_UZAK_J%"]},"session_name":"kanit","version":"0"}
set "KANIT_PWSH_ASIL=%KARARGAH_PWSH%"
set "KARARGAH_ROOT=%KANIT_KOK%"

set "KANIT_AD=durum satiri: Windows PowerShell"
set "KARARGAH_PWSH="
rem Adinin bulunmasi yetmez; calistigi sinanir (cikis kodu 7 beklenir).
powershell -NoLogo -NoProfile -NonInteractive -Command "exit 7" >nul 2>&1
if not "%errorlevel%"=="7" goto :ps5_atla
call "%~dp0durum_satiri.cmd" <"%KANIT_GECICI%\durum.json" >"%KANIT_CIKTI%" 2>&1
call :durum_denetle
call :bitir
goto :ps5_son
:ps5_atla
call :atla "powershell calismiyor ya da yok"
:ps5_son

set "KANIT_AD=durum satiri: PowerShell 7"
set "KARARGAH_PWSH=%KANIT_PWSH_ASIL%"
if not defined KARARGAH_PWSH for %%P in (pwsh.exe) do if not "%%~$PATH:P"=="" set "KARARGAH_PWSH=%%~$PATH:P"
if not defined KARARGAH_PWSH goto :ps7_atla
if not exist "%KARARGAH_PWSH%" goto :ps7_atla
"%KARARGAH_PWSH%" -NoLogo -NoProfile -NonInteractive -Command "exit 7" >nul 2>&1
if not "%errorlevel%"=="7" goto :ps7_atla
call "%~dp0durum_satiri.cmd" <"%KANIT_GECICI%\durum.json" >"%KANIT_CIKTI%" 2>&1
call :durum_denetle
call :bitir
goto :ps7_son
:ps7_atla
call :atla "pwsh calismiyor ya da yok"
:ps7_son

rem ---- [05] Kit: dosyalar ve ayar --------------------------------------------------
set "KANIT_AD=kit: dosyalar yerinde"
>"%KANIT_CIKTI%" echo kit dosyalari
if not exist "%KANIT_KOK%\araclar\durum_satiri.cmd" set "KANIT_HATA=%KANIT_HATA% [yok: araclar\durum_satiri.cmd]"
if not exist "%KANIT_KOK%\araclar\durum_satiri.ps1" set "KANIT_HATA=%KANIT_HATA% [yok: araclar\durum_satiri.ps1]"
if not exist "%KANIT_KOK%\.claude\rules\usul.md" set "KANIT_HATA=%KANIT_HATA% [yok: .claude\rules\usul.md]"
call :bitir

set "KANIT_AYAR=%KANIT_KOK%\.claude\settings.json"
if not exist "%KANIT_AYAR%" goto :ayar_yok
rem call :yaz hata kodunu sifirlar; findstr sonucu once degiskene alinir.
findstr /c:"durum_satiri.cmd" "%KANIT_AYAR%" >nul 2>&1
set "KANIT_E=%errorlevel%"
if "%KANIT_E%"=="0" call :yaz "BILGI   ayar: durum satiri bagli"
if not "%KANIT_E%"=="0" call :yaz "BILGI   ayar: durum satiri bagli degil (.claude\settings.json)"
findstr /c:"blockReadsOutsideWorkingDirectories" "%KANIT_AYAR%" >nul 2>&1
set "KANIT_E=%errorlevel%"
if "%KANIT_E%"=="0" call :yaz "BILGI   ayar: okuma siniri yazili"
if not "%KANIT_E%"=="0" call :yaz "BILGI   ayar: okuma siniri yok"
findstr /c:"blockWritesOutsideWorkingDirectories" "%KANIT_AYAR%" >nul 2>&1
set "KANIT_E=%errorlevel%"
if "%KANIT_E%"=="0" call :yaz "BILGI   ayar: yazma siniri yazili"
if not "%KANIT_E%"=="0" call :yaz "BILGI   ayar: yazma siniri yok"
goto :ayar_son
:ayar_yok
call :yaz "BILGI   ayar: .claude\settings.json yok; durum satiri ve sinir bagli degil"
:ayar_son

rem ---- [06] Canli kanit: gercek claude.exe, tek -p cagrisi --------------------
rem Claude'a uc isaret dosyasi gosterilir. Kokteki dosya goreli yolla verilir: okunabiliyorsa oturum kokte
rem acilmistir. Uzak yerdeki dosya okunabiliyorsa klasor eklenmistir. Disaridaki dosya icin sonuc bilgidir:
rem sinir ayari aciksa okunamaz. Yalniz Read araci acik oldugu icin kabuk komutuyla dolanilamaz.
if not defined KANIT_CANLI goto :canli_son
set "KANIT_T1=KOK-%RANDOM%-%RANDOM%"
set "KANIT_T2=UZAK-%RANDOM%-%RANDOM%"
set "KANIT_T3=DIS-%RANDOM%-%RANDOM%"
>"%KANIT_GECICI%\kok_isaret.txt" echo %KANIT_T1%
>"%KANIT_UZAK%\uzak_isaret.txt" echo %KANIT_T2%
>"%KANIT_DIS%\dis_isaret.txt" echo %KANIT_T3%
set "KANIT_ISTEM=Uc dosyayi Read araciyla okumayi dene. Her dosya icin tek satir yaz: okuyabildiysen icerigini aynen, okuyamadiysan RED. Baska hicbir sey yazma. Dosyalar: gecici\kanit\kok_isaret.txt ve %KANIT_UZAK%\uzak_isaret.txt ve %KANIT_DIS%\dis_isaret.txt"
set "KARARGAH_DENEME="
set "KARARGAH_EFOR=low"
pushd "%KANIT_UZAK%"
call "%KANIT_KAPI%" --burada --tools Read -p "%KANIT_ISTEM%" --no-session-persistence <nul >"%KANIT_CIKTI%" 2>&1
popd
set "KARARGAH_DENEME=1"

set "KANIT_AD=canli: oturum kokte (goreli yoldaki isaret okundu)"
call :var "%KANIT_T1%"
set "KANIT_CANLI_KOK=1"
if defined KANIT_HATA set "KANIT_CANLI_KOK="
call :bitir

set "KANIT_AD=canli: uzak yer ekli (isaret okundu)"
call :var "%KANIT_T2%"
call :bitir

if not defined KANIT_CANLI_KOK goto :canli_son
findstr /c:"%KANIT_T3%" "%KANIT_CIKTI%" >nul 2>&1
set "KANIT_E=%errorlevel%"
if "%KANIT_E%"=="0" call :yaz "BILGI   canli: disaridaki dosya okundu; okuma siniri kapali"
if not "%KANIT_E%"=="0" call :yaz "BILGI   canli: disaridaki dosya okunamadi; okuma siniri gecerli"
:canli_son

rem ---- [07] Sonuc ------------------------------------------------------------------
call :temizle
call :yaz "SONUC   %KANIT_GECEN% gecti, %KANIT_KALAN% kaldi, %KANIT_ATLANAN% atlandi"
echo BILGI   rapor  : "%KANIT_RAPOR%"
if defined KANIT_CP chcp %KANIT_CP% >nul 2>&1
if %KANIT_KALAN% GTR 0 exit /b 1
exit /b 0

rem ---- [09] Hatalar ------------------------------------------------------------------
:hata_kapi
echo [KARARGAH] HATA: kapi bulunamadi; kanit.cmd karargahin araclar\ klasorunde durmali: "%KANIT_KAPI%"
goto :hata
:hata_eski
echo [KARARGAH] HATA: kapi kuru calistirmayi tanimiyor (eski kapi); once kiti kurun: "%KANIT_KAPI%"
goto :hata
:hata_kalinti
echo [KARARGAH] HATA: onceki sinamadan kalan gecici klasor var; silip yeniden deneyin:
echo            "%KANIT_UZAK%"
echo            "%KANIT_DIS%"
echo            "%KANIT_GECICI%"
goto :hata
:hata_yazilamadi
echo [KARARGAH] HATA: gecici klasorler acilamadi; ust klasore ve gecici\ klasorune yazilabilmeli.
call :temizle
goto :hata
:hata
if defined KANIT_CP chcp %KANIT_CP% >nul 2>&1
exit /b 1

rem ============================== Alt yordamlar ==============================

:yaz
rem Bir satiri hem ekrana hem rapora yazar.
echo %~1
>>"%KANIT_RAPOR%" echo %~1
exit /b 0

:var
rem %1 (tirnakli parca) son ciktida gecmeli.
findstr /c:%1 "%KANIT_CIKTI%" >nul 2>&1
if errorlevel 1 set "KANIT_HATA=%KANIT_HATA% [yok: %~1]"
exit /b 0

:yok
rem %1 (tirnakli parca) son ciktida gecmemeli.
findstr /c:%1 "%KANIT_CIKTI%" >nul 2>&1
if not errorlevel 1 set "KANIT_HATA=%KANIT_HATA% [olmamali: %~1]"
exit /b 0

:dizin
rem Kapinin yazdigi calisma dizini karargah koku olmali.
set "KANIT_SATIR="
for /f "usebackq delims=" %%L in (`findstr /c:"[deneme] dizin:" "%KANIT_CIKTI%" 2^>nul`) do set "KANIT_SATIR=%%L"
if not defined KANIT_SATIR set "KANIT_HATA=%KANIT_HATA% [dizin satiri yok]"
if not defined KANIT_SATIR exit /b 0
set "KANIT_SATIR=%KANIT_SATIR:"=%"
if /i not "%KANIT_SATIR%"=="[deneme] dizin: %KANIT_KOK%" set "KANIT_HATA=%KANIT_HATA% [dizin kok degil]"
exit /b 0

:durum_denetle
call :var "karargah"
call :var "uzak: "
call :var "_kanit uzak"
call :var "ad: kanit"
call :yok "ORTAM KAYDI"
call :yok "KAPI DISI"
call :yok "okunamadi"
exit /b 0

:bitir
rem KANIT_HATA bossa GECTI, doluysa KALDI yazar; KALDI durumunda son cikti rapora eklenir.
if defined KANIT_HATA goto :bitir_kaldi
set /a KANIT_GECEN+=1
call :yaz "GECTI   %KANIT_AD%"
exit /b 0
:bitir_kaldi
set /a KANIT_KALAN+=1
call :yaz "KALDI   %KANIT_AD% %KANIT_HATA%"
>>"%KANIT_RAPOR%" echo ---- son cikti ----
type "%KANIT_CIKTI%" >>"%KANIT_RAPOR%" 2>nul
>>"%KANIT_RAPOR%" echo ----
set "KANIT_HATA="
exit /b 0

:atla
rem %~1: neden. KANIT_AD sinamasini atlanmis sayar.
set /a KANIT_ATLANAN+=1
call :yaz "ATLANDI %KANIT_AD% (%~1)"
exit /b 0

:temizle
rem Yalniz bu sinamanin actigi klasorler silinir (on kosul: baslarken yoktular).
if exist "%KANIT_UZAK%\" rd /s /q "%KANIT_UZAK%" >nul 2>&1
if exist "%KANIT_DIS%\" rd /s /q "%KANIT_DIS%" >nul 2>&1
if exist "%KANIT_GECICI%\" rd /s /q "%KANIT_GECICI%" >nul 2>&1
exit /b 0
