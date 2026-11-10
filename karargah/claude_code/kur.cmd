@echo off
rem ============================================================================
rem  kur.cmd  -  Kiti Claude Code karargahina kurar (ortak-kopru\karargah\claude_code)
rem ============================================================================
rem  Kit (kit\) hedefin aynasidir: kitteki her dosya karargah kokune gore ayni yola kopyalanir.
rem    kit\claude_code.cmd              kapi: tek ortam, uzak ekleme, oturum adi, remote-control, deneme
rem    kit\araclar\durum_satiri.cmd     durum satiri komutu (statusLine)
rem    kit\araclar\durum_satiri.ps1     durum satirinin asil isi
rem    kit\araclar\kanit.cmd            kanit: kapiyi ve durum satirini sinar, rapor verir
rem    kit\.claude\settings.json        durum satiri + calisma dizini siniri; varsa uzerine yazilmaz
rem    kit\.claude\rules\usul.md        usul: sozluk, kaliplar, ileti bicimi, kanit damgalari
rem
rem  KULLANIM
rem    kur.cmd [karargah koku]
rem    Hedef verilmezse KARARGAH_HEDEF, o da yoksa Y:\02_karargahlar\01_claude_code_karargah* aranir.
rem    KARARGAH_DENEME=1: hicbir sey kopyalamaz; ne yapacagini gosterir.
rem
rem  Kok yerlesimi icindir (kapi karargah kokunde, uygulama\yerel\ yaninda durur). Eski kapi yedeklenir:
rem    claude_code.asil.cmd    ilk kurulumdan onceki kapi; bir kez yazilir, sonra dokunulmaz
rem    claude_code.onceki.cmd  her kurulumda bir onceki kapi
rem  Kurulumdan sonra karargahin kendi kaniti (araclar\kanit.cmd) calistirilir; raporu gecici\kanit.son.txt
rem  dosyasina da yazilir.
rem  Dosya ASCII + CRLF, BOM'suz.
rem ============================================================================
setlocal EnableExtensions DisableDelayedExpansion

rem ---- [00] Kod sayfasi: sakla, UTF-8'e gec --------------------------------------
set "KUR_CP="
for /f "tokens=2 delims=:" %%A in ('chcp') do set "KUR_CP=%%A"
if defined KUR_CP set "KUR_CP=%KUR_CP: =%"
if defined KUR_CP set "KUR_CP=%KUR_CP:.=%"
chcp 65001 >nul 2>&1

rem ---- [01] Kit ve hedef -----------------------------------------------------------
set "KUR_KIT=%~dp0kit"
set "KUR_ONEK="
if "%KARARGAH_DENEME%"=="1" set "KUR_ONEK=1"
set "KUR_HEDEF=%~1"
if not defined KUR_HEDEF set "KUR_HEDEF=%KARARGAH_HEDEF%"
if defined KUR_HEDEF set "KUR_HEDEF=%KUR_HEDEF:"=%"
if not defined KUR_HEDEF for /d %%D in ("Y:\02_karargahlar\01_claude_code_karargah*") do set "KUR_HEDEF=%%~fD"
if not defined KUR_HEDEF goto :hata_hedef
if not "%KUR_HEDEF%"=="\" if "%KUR_HEDEF:~-1%"=="\" set "KUR_HEDEF=%KUR_HEDEF:~0,-1%"
for %%I in ("%KUR_HEDEF%\.") do set "KUR_HEDEF=%%~fI"
if not exist "%KUR_KIT%\claude_code.cmd" goto :hata_kit
if not exist "%KUR_HEDEF%\" goto :hata_hedef_yok
rem Kok yerlesimi: govde ya da hafiza klasoru hedefin kokunde olmali.
if exist "%KUR_HEDEF%\uygulama\yerel\" goto :yerlesim_tamam
if exist "%KUR_HEDEF%\durum\claude\" goto :yerlesim_tamam
goto :hata_yerlesim
:yerlesim_tamam
echo [KARARGAH] BILGI: kit   : "%KUR_KIT%"
echo [KARARGAH] BILGI: hedef : "%KUR_HEDEF%"
if defined KUR_ONEK echo [deneme] KARARGAH_DENEME=1: hicbir dosya kopyalanmaz.

rem ---- [02] Eski kapiyi yedekle ---------------------------------------------------
if not exist "%KUR_HEDEF%\claude_code.cmd" goto :yedek_son
call :yedekle
if errorlevel 1 goto :hata
:yedek_son

rem ---- [03] Kiti kopyala ------------------------------------------------------------
call :kopyala "claude_code.cmd"
if errorlevel 1 goto :hata
call :kopyala "araclar\durum_satiri.cmd"
if errorlevel 1 goto :hata
call :kopyala "araclar\durum_satiri.ps1"
if errorlevel 1 goto :hata
call :kopyala "araclar\kanit.cmd"
if errorlevel 1 goto :hata
call :kopyala ".claude\rules\usul.md"
if errorlevel 1 goto :hata
call :ayar_kur
if errorlevel 1 goto :hata

rem ---- [04] Kanit: kurulan karargah kendini sinar --------------------------------
if defined KUR_ONEK goto :son
findstr /c:"KARARGAH_DENEME" "%KUR_HEDEF%\claude_code.cmd" >nul 2>&1
if errorlevel 1 goto :hata_kanit
echo.
echo [KARARGAH] BILGI: kurulum tamam; karargahin kaniti calistiriliyor (araclar\kanit.cmd):
call "%KUR_HEDEF%\araclar\kanit.cmd"
if errorlevel 1 goto :kanit_kaldi
echo.
echo [KARARGAH] BILGI: kanit gecti. Geri almak icin claude_code.onceki.cmd dosyasini claude_code.cmd uzerine kopyalayin.
goto :son
:kanit_kaldi
echo.
echo [KARARGAH] UYARI: kanit KALDI satiri verdi; rapora bakin. Geri almak icin claude_code.onceki.cmd dosyasini claude_code.cmd uzerine kopyalayin.
if defined KUR_CP chcp %KUR_CP% >nul 2>&1
if not defined CI pause
exit /b 1

rem ---- [09] Hatalar ------------------------------------------------------------------
:hata_hedef
echo [KARARGAH] HATA: karargah koku bulunamadi; yolu arguman olarak ya da KARARGAH_HEDEF ile verin.
goto :hata
:hata_hedef_yok
echo [KARARGAH] HATA: hedef klasor yok: "%KUR_HEDEF%"
goto :hata
:hata_kit
echo [KARARGAH] HATA: kit bulunamadi; kur.cmd, kit\ klasorunun yaninda durmali: "%KUR_KIT%"
goto :hata
:hata_yerlesim
echo [KARARGAH] HATA: hedef kok yerlesiminde degil (uygulama\yerel\ ya da durum\claude\ yok): "%KUR_HEDEF%"
echo            Iskelet yerlesiminde kit elle kopyalanir.
goto :hata
:hata_kanit
echo [KARARGAH] HATA: kurulan kapi beklenen dosya degil; kanit calistirilmadi: "%KUR_HEDEF%\claude_code.cmd"
goto :hata
:hata
echo.
echo [KARARGAH] Kurulum tamamlanmadi.
if defined KUR_CP chcp %KUR_CP% >nul 2>&1
if not defined CI pause
exit /b 1

:son
if defined KUR_CP chcp %KUR_CP% >nul 2>&1
if not defined CI pause
exit /b 0

rem ============================== Alt yordamlar ==============================

:yedekle
rem Eski kapi iki yere kopyalanir; claude_code.asil.cmd yalniz ilk kurulumda yazilir.
if defined KUR_ONEK echo [deneme] yedek: claude_code.cmd, claude_code.onceki.cmd olarak kopyalanir; ilk kurulumda claude_code.asil.cmd de yazilir.
if defined KUR_ONEK exit /b 0
if exist "%KUR_HEDEF%\claude_code.asil.cmd" goto :yedek_onceki
copy /y "%KUR_HEDEF%\claude_code.cmd" "%KUR_HEDEF%\claude_code.asil.cmd" >nul
if errorlevel 1 goto :yedek_hata
echo [KARARGAH] BILGI: ilk kapi saklandi: claude_code.asil.cmd
:yedek_onceki
copy /y "%KUR_HEDEF%\claude_code.cmd" "%KUR_HEDEF%\claude_code.onceki.cmd" >nul
if errorlevel 1 goto :yedek_hata
echo [KARARGAH] BILGI: onceki kapi yedeklendi: claude_code.onceki.cmd
exit /b 0
:yedek_hata
echo [KARARGAH] HATA: eski kapi yedeklenemedi; hicbir dosya degistirilmedi: "%KUR_HEDEF%"
exit /b 1

:kopyala
rem %~1: kite ve hedefe gore goreli yol.
if defined KUR_ONEK echo [deneme] kopyala: %~1
if defined KUR_ONEK exit /b 0
if not exist "%KUR_KIT%\%~1" goto :kopyala_hata
for %%F in ("%KUR_HEDEF%\%~1") do if not exist "%%~dpF" mkdir "%%~dpF" >nul 2>&1
copy /y "%KUR_KIT%\%~1" "%KUR_HEDEF%\%~1" >nul
if errorlevel 1 goto :kopyala_hata
echo [KARARGAH] BILGI: kuruldu: %~1
exit /b 0
:kopyala_hata
echo [KARARGAH] HATA: kopyalanamadi: %~1
exit /b 1

:ayar_kur
rem Var olan .claude\settings.json dosyasinin uzerine yazilmaz; kit ayari yanina konur.
if exist "%KUR_HEDEF%\.claude\settings.json" goto :ayar_var
call :kopyala ".claude\settings.json"
exit /b
:ayar_var
rem Var olan ayar durum satirini zaten cagiriyorsa (kit ayari ya da elle birlestirilmis hali) dokunulmaz.
findstr /c:"durum_satiri.cmd" "%KUR_HEDEF%\.claude\settings.json" >nul 2>&1
if errorlevel 1 goto :ayar_farkli
echo [KARARGAH] BILGI: ayar yerinde, dokunulmadi: .claude\settings.json
exit /b 0
:ayar_farkli
if defined KUR_ONEK echo [deneme] .claude\settings.json var ve durum satirini cagirmiyor; kit ayari yanina yazilir: .claude\settings.kit.json
if defined KUR_ONEK exit /b 0
copy /y "%KUR_KIT%\.claude\settings.json" "%KUR_HEDEF%\.claude\settings.kit.json" >nul
if errorlevel 1 goto :ayar_hata
echo [KARARGAH] UYARI: .claude\settings.json var ve durum satirini cagirmiyor, uzerine yazilmadi; kit ayari yanina kondu: .claude\settings.kit.json. Iki dosyayi elle birlestirin.
exit /b 0
:ayar_hata
echo [KARARGAH] HATA: kit ayari yazilamadi: .claude\settings.kit.json
exit /b 1
