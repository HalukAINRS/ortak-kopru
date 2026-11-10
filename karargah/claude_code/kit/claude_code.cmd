@echo off
rem ============================================================================
rem  claude_code.cmd  -  Claude Code karargahinin kapisi (claude.exe)
rem ============================================================================
rem  ENVANTER  .  kok yerlesimi (bu dosya karargah kokunde durur)
rem    <karargah>\                       Claude Code'un calisma koku
rem    |-- claude_code.cmd               kapi (bu dosya)
rem    |-- claude_guncelle.ps1           --guncelle
rem    |-- AGENTS.md                     talimat (CLAUDE.md yokken okunur; varsa kanca ona @AGENTS.md isler)
rem    |-- yapilandirma\                 karakter
rem    |   |-- settings.json             her acilista --settings ile yuklenir
rem    |   `-- settings.tek.json         tek ajanli es karakter (KARARGAH_SUBAGENT=0)
rem    |-- uygulama\yerel\               govde: claude.exe (Windows x64 tek dosya); (varsa) PortableGit\
rem    |-- durum\claude\                 hafiza: CLAUDE_CONFIG_DIR (oturumlar, .credentials.json, .claude.json,
rem    |                                 kullanici ayari); tam izolasyonda ev
rem    |-- gecici\claude\                gecicilik: CLAUDE_CODE_TMPDIR; tam izolasyonda TEMP ve TMP
rem    |-- gecici\onbellek\              LOCALAPPDATA ve APPDATA (tam izolasyonda)
rem    |-- araclar\                      (varsa) karargaha ozel komutlar; PATH'e eklenir
rem    `-- arastirma_tasarim\            dusunce; kapi dokunmaz
rem    <ust kok>\00_araclar\             (varsa) uc karargahin ortak tasinabilir araclari; PATH'e eklenir
rem    <ust kok>\00_araclar\wezterm\wezterm-gui.exe   (varsa) ortak terminal
rem
rem  ENVANTER  .  iskelet yerlesimi (bu dosya claude_code_cli\claude_code_exe\ icinde durur)
rem    00_Uygulama\ govde . 01_Yapilandirma\ karakter . 03_Uygulama_Verileri\ hafiza
rem    claude_code_cli\06_Onbellek\ 07_Gecici_Dosyalar\ 02_Terminal\ ; 00_Yapilandirma\settings.json yuklenmez
rem    Kapi hangi yerlesimde durdugunu kendi konumundan anlar; tasima: karargah_tasi.cmd
rem
rem  ANAHTARLAR  .  cagirmadan once ortam degiskeni; bos birakilani kapi secer (* varsayilan)
rem    .--------------------. .--------------------. .--------------------. .--------------------.
rem    | KARARGAH_IZIN      | | KARARGAH_SUBAGENT  | | KARARGAH_EFOR      | | KARARGAH_MODEL     |
rem    | mutlak*  tam       | | 1*  .  0           | | max*  xhigh  high  | | claude-opus-5-5*   |
rem    | auto  yok          | |                    | | medium  low  ayar  | | opus  best  ayar   |
rem    '--------------------' '--------------------' '--------------------' '--------------------'
rem    .--------------------. .--------------------. .--------------------. .--------------------.
rem    | KARARGAH_          | | KARARGAH_TAM_      | | KARARGAH_WEZTERM   | | KARARGAH_PE_       |
rem    | AUTOCOMPACT        | | IZOLASYON  1 . 0   | | <wezterm-gui.exe>  | | PAGEFILE  <MB>     |
rem    | 200k  500k  1M     | | PE'de 1*           | |                    | |                    |
rem    '--------------------' '--------------------' '--------------------' '--------------------'
rem    mutlak : --permission-mode bypassPermissions + kritik yol silme korumasi ve cmd silme denetimi kapali
rem    tam    : --permission-mode bypassPermissions
rem    auto   : --permission-mode auto --allow-dangerously-skip-permissions
rem    yok    : bayrak yok; settings.json'daki defaultMode gecerli
rem    KARARGAH_MODEL: --model degeri (varsayilan claude-opus-5-5); her acilista acikca verilir, oturumda /model ile degisir.
rem      "ayar" = bayrak yok: /model ile kaydedilmis secim ya da hesabin varsayilani gecerli.
rem    KARARGAH_EFOR: --effort degeri (varsayilan max); "ayar" = bayrak yok, settings.json effortLevel (xhigh) gecerli;
rem      "ultracode" = xhigh + dinamik is akisi orkestrasyonu (en agir isler; token yuku yuksek).
rem    KARARGAH_AUTOCOMPACT: --autocompact; bos = modelin kendi penceresi.
rem    Hizli kip kapalidir (CLAUDE_CODE_DISABLE_FAST_MODE=1); alt ajanlar Opus 4.8 ile calisir (settings.json env).
rem    Tek ortam: her oturum (yeni, --continue, --resume) karargah kokunde acilir. Oturum kayitlari ve otomatik
rem      hafiza hep durum\claude\projects\karargah-claude-code\ altindadir (surucu harfinden bagimsiz).
rem    KARARGAH_DIZIN: oturuma uzak yer olarak eklenecek klasor (--add-dir; --burada cagrilan klasoru verir). Dosya
rem      erisimi verir; o klasorun becerileri, komutlari ve alt ajanlari yuklenir; ayarlari, kancalari ve .mcp.json
rem      dosyasi yuklenmez. Devam eden oturumda kendiliginden geri gelmez; kapi her acilista yeniden verir.
rem      --burada ile acilan yeni etkilesimli oturum klasorun adini alir (-n).
rem    KARARGAH_DENEME=1: her seyi hazirlar, calistirilacak komutu gosterir; Claude Code'u baslatmaz.
rem    KARARGAH_HAZIRLIK=0: <ust kok>\ortak\hazirlik.cmd varsa bile cagrilmaz (ortak kural paketi kancasi).
rem    KARARGAH_ULAK=0: ulak kanali baglanmaz (durum\claude\ulak.mcp.json varsa --mcp-config ile baglanir).
rem    KARARGAH_ULAK_KANAL=0: etkilesimli oturumda --dangerously-load-development-channels server:ulak verilmez
rem      (kanal itmesi kapali; zarflar yine kanca ve ulak_oku ile gelir).
rem
rem  KULLANIM
rem    claude_code.cmd                   etkilesimli oturum; cikista konsol acik kalir
rem    claude_code.cmd --continue        son oturuma ayni karakterle devam
rem    claude_code.cmd --burada [arg...] oturum yine karargah kokunde; cagrildigi klasor uzak yer olarak eklenir
rem                                     (KARARGAH_DIZIN ayni isi yapar); ardindaki en cok sekiz arguman bayrakli
rem                                     cagri gibi claude'a gecer (banner ve WezTerm yok); fazlasi varsa oturum
rem                                     acilmaz; = , ; tasiyan degeri tirnakla yaz
rem    claude_code.cmd -p "soru"         bayrakla baslayan argumanlar karakterle birlikte aktarilir
rem    claude_code.cmd remote-control [secenek...]   Remote Control sunucusu karargah kokunde (rc ayni); karakter ve
rem                                     yetki fiilden sonra verilir; ardindan en cok sekiz secenek gecer
rem    claude_code.cmd doctor            alt komutlar dogrudan aktarilir; karargah kokunde calisir
rem    claude_code.cmd --guncelle [x.y.z]   resmi govdeyi indir, ozetini dogrula, yerine koy
rem    claude_code.cmd --yardim
rem
rem  Dosya ASCII + CRLF, BOM'suz.
rem ============================================================================
setlocal EnableExtensions DisableDelayedExpansion
set "KARARGAH_CAGIRAN=%CD%"

rem ---- [00] Kod sayfasi: sakla, UTF-8'e gec --------------------------------------
set "KARARGAH_CP="
for /f "tokens=2 delims=:" %%A in ('chcp') do set "KARARGAH_CP=%%A"
if defined KARARGAH_CP set "KARARGAH_CP=%KARARGAH_CP: =%"
if defined KARARGAH_CP set "KARARGAH_CP=%KARARGAH_CP:.=%"
chcp 65001 >nul 2>&1

rem ---- [01] Konum ve yerlesim --------------------------------------------------------
set "KARARGAH_KAPI=%~dp0"
if "%KARARGAH_KAPI:~-1%"=="\" set "KARARGAH_KAPI=%KARARGAH_KAPI:~0,-1%"
set "KARARGAH_YERLESIM="
if exist "%KARARGAH_KAPI%\uygulama\yerel\" set "KARARGAH_YERLESIM=kok"
if not defined KARARGAH_YERLESIM if exist "%KARARGAH_KAPI%\00_Uygulama\" set "KARARGAH_YERLESIM=iskelet"
if not defined KARARGAH_YERLESIM if exist "%KARARGAH_KAPI%\durum\claude\" set "KARARGAH_YERLESIM=kok"
if not defined KARARGAH_YERLESIM goto :hata_yerlesim
if "%KARARGAH_YERLESIM%"=="kok" goto :yerlesim_kok

set "KARARGAH_EXE_ROOT=%KARARGAH_KAPI%"
for %%I in ("%KARARGAH_KAPI%\..") do set "KARARGAH_CLI_ROOT=%%~fI"
for %%I in ("%KARARGAH_KAPI%\..\..") do set "KARARGAH_ROOT=%%~fI"
set "CLAUDE_APP_DIR=%KARARGAH_KAPI%\00_Uygulama"
set "KARARGAH_CONFIG_DIR=%KARARGAH_KAPI%\01_Yapilandirma"
set "CLAUDE_CONFIG_DIR=%KARARGAH_KAPI%\03_Uygulama_Verileri"
set "KARARGAH_CACHE=%KARARGAH_CLI_ROOT%\06_Onbellek"
set "KARARGAH_TEMP=%KARARGAH_CLI_ROOT%\07_Gecici_Dosyalar"
set "KARARGAH_TERMINAL=%KARARGAH_CLI_ROOT%\02_Terminal"
set "KARARGAH_UST_AYAR=%KARARGAH_CLI_ROOT%\00_Yapilandirma\settings.json"
goto :yerlesim_son

:yerlesim_kok
set "KARARGAH_ROOT=%KARARGAH_KAPI%"
set "KARARGAH_EXE_ROOT=%KARARGAH_KAPI%"
set "CLAUDE_APP_DIR=%KARARGAH_KAPI%\uygulama\yerel"
set "KARARGAH_CONFIG_DIR=%KARARGAH_KAPI%\yapilandirma"
set "CLAUDE_CONFIG_DIR=%KARARGAH_KAPI%\durum\claude"
set "KARARGAH_CACHE=%KARARGAH_KAPI%\gecici\onbellek"
set "KARARGAH_TEMP=%KARARGAH_KAPI%\gecici\claude"
set "KARARGAH_TERMINAL=%KARARGAH_KAPI%\araclar\wezterm"
set "KARARGAH_UST_AYAR="

:yerlesim_son
set "CLAUDE_APP_BIN=%CLAUDE_APP_DIR%\claude.exe"
set "KARARGAH_PROFIL=%KARARGAH_CONFIG_DIR%\settings.json"
set "KARARGAH_PROFIL_TEK=%KARARGAH_CONFIG_DIR%\settings.tek.json"
if not exist "%CLAUDE_APP_BIN%" goto :hata_govde
for %%D in ("%CLAUDE_CONFIG_DIR%" "%KARARGAH_TEMP%") do if not exist "%%~D\" mkdir "%%~D" >nul 2>&1

rem ---- [02] Anahtarlar ve PE -------------------------------------------------------------
if not defined KARARGAH_IZIN set "KARARGAH_IZIN=mutlak"
if not defined KARARGAH_SUBAGENT set "KARARGAH_SUBAGENT=1"
if not defined KARARGAH_EFOR set "KARARGAH_EFOR=max"
if not defined KARARGAH_MODEL set "KARARGAH_MODEL=claude-opus-5-5"
set "KARARGAH_WEZ_BITTI="
set "KARARGAH_ONEK="
if "%KARARGAH_DENEME%"=="1" set "KARARGAH_ONEK=echo [deneme]"
call :pe_hazirla
if not defined KARARGAH_TAM_IZOLASYON set "KARARGAH_TAM_IZOLASYON=0"
set "KARARGAH_IZIN_ARG="
if /i "%KARARGAH_IZIN%"=="tam" set "KARARGAH_IZIN_ARG=--permission-mode bypassPermissions"
if /i "%KARARGAH_IZIN%"=="mutlak" set "KARARGAH_IZIN_ARG=--permission-mode bypassPermissions"
if /i "%KARARGAH_IZIN%"=="mutlak" set "CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS=1"
if /i "%KARARGAH_IZIN%"=="mutlak" set "CLAUDE_CODE_DISABLE_POWERSHELL_CMD_RM_DENY=1"
if /i "%KARARGAH_IZIN%"=="auto" set "KARARGAH_IZIN_ARG=--permission-mode auto --allow-dangerously-skip-permissions"
set "KARARGAH_PROFIL_SECILI=%KARARGAH_PROFIL%"
if "%KARARGAH_SUBAGENT%"=="0" if exist "%KARARGAH_PROFIL_TEK%" set "KARARGAH_PROFIL_SECILI=%KARARGAH_PROFIL_TEK%"
set "KARARGAH_PROFIL_ARG="
if exist "%KARARGAH_PROFIL_SECILI%" set "KARARGAH_PROFIL_ARG=--settings "%KARARGAH_PROFIL_SECILI%""
set "KARARGAH_EFOR_ARG="
if /i not "%KARARGAH_EFOR%"=="ayar" set "KARARGAH_EFOR_ARG=--effort %KARARGAH_EFOR%"
set "KARARGAH_AC_ARG="
if defined KARARGAH_AUTOCOMPACT set "KARARGAH_AC_ARG=--autocompact %KARARGAH_AUTOCOMPACT%"
set "KARARGAH_MODEL_ARG="
if /i not "%KARARGAH_MODEL%"=="ayar" set "KARARGAH_MODEL_ARG=--model %KARARGAH_MODEL%"

rem ---- [03] Ortam -----------------------------------------------------------------------
set "CLAUDE_CODE_TMPDIR=%KARARGAH_TEMP%"
set "CLAUDE_CODE_USE_POWERSHELL_TOOL=1"
set "CLAUDE_CODE_DISABLE_FAST_MODE=1"
set "DISABLE_AUTOUPDATER=1"
set "DISABLE_UPDATES=1"
set "DISABLE_INSTALLATION_CHECKS=1"
if not defined KARARGAH_KABUK set "PATH=%CLAUDE_APP_DIR%;%PATH%"
call :pwsh_bul
call :git_bash_bul
if not defined GIT_CONFIG_COUNT call :git_ayari
for %%I in ("%KARARGAH_ROOT%\..") do set "KARARGAH_USTKOK=%%~fI"
if not defined KARARGAH_KABUK if exist "%KARARGAH_USTKOK%\00_araclar\" set "PATH=%KARARGAH_USTKOK%\00_araclar;%PATH%"
if not defined KARARGAH_KABUK if exist "%KARARGAH_ROOT%\araclar\" set "PATH=%KARARGAH_ROOT%\araclar;%PATH%"
if not "%KARARGAH_TAM_IZOLASYON%"=="1" goto :izolasyon_son
if not defined KARARGAH_GERCEK_USERPROFILE set "KARARGAH_GERCEK_USERPROFILE=%USERPROFILE%"
for %%D in ("%KARARGAH_CACHE%\Local" "%KARARGAH_CACHE%\Roaming") do if not exist "%%~D\" mkdir "%%~D" >nul 2>&1
set "USERPROFILE=%CLAUDE_CONFIG_DIR%"
set "HOME=%CLAUDE_CONFIG_DIR%"
if exist "%KARARGAH_CACHE%\Local\" set "LOCALAPPDATA=%KARARGAH_CACHE%\Local"
if exist "%KARARGAH_CACHE%\Roaming\" set "APPDATA=%KARARGAH_CACHE%\Roaming"
if not defined KARARGAH_KABUK set "PATH=%APPDATA%\npm;%PATH%"
set "TEMP=%KARARGAH_TEMP%"
set "TMP=%KARARGAH_TEMP%"
if not exist "%CLAUDE_CONFIG_DIR%\.gitconfig" if exist "%KARARGAH_GERCEK_USERPROFILE%\.gitconfig" copy /y "%KARARGAH_GERCEK_USERPROFILE%\.gitconfig" "%CLAUDE_CONFIG_DIR%\.gitconfig" >nul 2>&1
:izolasyon_son

rem ---- [0h] Ortak kurallar hazirligi (varsa) ----------------------------------------------
rem <ust kok>\ortak\hazirlik.cmd <ajan> "<hafiza koku>" "<karargah koku>": ortak kural paketi varsa kendi
rem girislerini burada tazeler; sifirdan farkli cikis acilisi durdurur. KARARGAH_HAZIRLIK=0 atlar.
if /i "%KARARGAH_HAZIRLIK%"=="0" goto :hazirlik_son
if not exist "%KARARGAH_USTKOK%\ortak\hazirlik.cmd" goto :hazirlik_son
call "%KARARGAH_USTKOK%\ortak\hazirlik.cmd" claude "%CLAUDE_CONFIG_DIR%" "%KARARGAH_ROOT%"
if errorlevel 1 echo [KARARGAH] HATA: ortak kural hazirligi basarisiz, kod %errorlevel%. KARARGAH_HAZIRLIK=0 ile atlanir. & goto :hata
:hazirlik_son

rem ---- [0u] Ulak: uc kol arasinda kapali kanal (varsa) --------------------------------------------
rem hazirlik.ps1, ortak\ulak\ulak.js varsa durum\claude\ulak.mcp.json dosyasini yazar; kapi onu --mcp-config ile baglar.
rem Etkilesimli oturumda kanal itmesi de acilir: baska kolun zarfi oturuma aninda duser (Claude Code kanallari,
rem arastirma onizlemesi; ilk acilista onay sorabilir). -p kipinde yalniz araclar baglanir.
set "KARARGAH_ULAK_ARG="
set "KARARGAH_KANAL_ARG="
if /i "%KARARGAH_ULAK%"=="0" goto :ulak_son
if not exist "%CLAUDE_CONFIG_DIR%\ulak.mcp.json" goto :ulak_son
rem --mcp-config cok degerlidir: bosluklu yazilirsa ardindaki bayraksiz argumani da dosya sanar; deger "=" ile verilir.
set "KARARGAH_ULAK_ARG=--mcp-config="%CLAUDE_CONFIG_DIR%\ulak.mcp.json""
if /i not "%KARARGAH_ULAK_KANAL%"=="0" set "KARARGAH_KANAL_ARG=--dangerously-load-development-channels server:ulak"
:ulak_son

rem ---- [0d] Tek ortam: calisma dizini her oturumda karargah koku; baska yer uzak olarak eklenir ------
rem Oturum hicbir kosulda baska klasorde acilmaz: profil, hafiza, oturum kayitlari ve proje kimligi karargahta
rem kalir. --burada cagrilan klasoru, KARARGAH_DIZIN verilen klasoru oturuma ek dizin olarak katar (--add-dir).
set "KARARGAH_IS=%KARARGAH_ROOT%"
set "CLAUDE_CODE_PROJECT_DIR_NAME=karargah-claude-code"
if /i "%~1"=="--burada" set "KARARGAH_DIZIN=%KARARGAH_CAGIRAN%"
set "KARARGAH_UZAK="
set "KARARGAH_UZAK_ARG="
set "KARARGAH_UZAK_AD="
set "KARARGAH_AD_ARG="
if defined KARARGAH_DIZIN call :uzak_hazirla

rem ---- [04] Dallanma ------------------------------------------------------------------------
set "KARARGAH_ARG1=%~1"
set "KARARGAH_EK="
if /i "%KARARGAH_ARG1%"=="--burada" if not "%~2"=="" set "KARARGAH_EK=1"
if defined KARARGAH_EK call :ek_sinir %*
if defined KARARGAH_EK if errorlevel 1 (call :kodsayfasi_geri & exit /b 1)
if /i "%KARARGAH_ARG1%"=="--yardim" goto :yardim
if "%KARARGAH_ARG1%"=="/?" goto :yardim
if /i "%KARARGAH_ARG1%"=="--guncelle" goto :guncelle
set "KARARGAH_RC="
if /i "%KARARGAH_ARG1%"=="remote-control" set "KARARGAH_RC=1"
if /i "%KARARGAH_ARG1%"=="rc" set "KARARGAH_RC=1"
if defined KARARGAH_RC call :ek_sinir %*
if defined KARARGAH_RC if errorlevel 1 (call :kodsayfasi_geri & exit /b 1)
if defined KARARGAH_RC goto :uzaktan_kumanda
if /i "%KARARGAH_ARG1%"=="--burada" if /i "%~2"=="remote-control" goto :hata_burada_rc
if /i "%KARARGAH_ARG1%"=="--burada" if /i "%~2"=="rc" goto :hata_burada_rc
if /i "%KARARGAH_ARG1%"=="--burada" if defined KARARGAH_EK goto :burada_argumanli
if /i "%KARARGAH_ARG1%"=="--burada" goto :etkilesimli
if "%KARARGAH_ARG1%"=="" goto :etkilesimli
if /i "%KARARGAH_ARG1%"=="--version" goto :aktar
if /i "%KARARGAH_ARG1%"=="-v" goto :aktar
if /i "%KARARGAH_ARG1%"=="--help" goto :aktar
if /i "%KARARGAH_ARG1%"=="-h" goto :aktar
for %%S in (agents auth doctor install mcp migrate-installer plugin setup-token update) do if /i "%KARARGAH_ARG1%"=="%%S" goto :aktar
goto :etkilesimli_argumanli

rem ---- [05] Dogrudan aktarim (alt komutlar; karargah kokunde) ----------------------------------
rem mcp, plugin, agents ve doctor bulunulan klasore gore kayit tutar ya da okur; baska klasorde calisirlarsa o
rem klasor ayri bir proje olarak kaydedilir. Goreli yol tasiyan arguman karargah kokune gore cozulur.
:aktar
pushd "%KARARGAH_IS%" 2>nul
if defined KARARGAH_ONEK echo [deneme] dizin: "%CD%"
%KARARGAH_ONEK% "%CLAUDE_APP_BIN%" %*
set "KARARGAH_CIKIS=%errorlevel%"
popd 2>nul
call :kodsayfasi_geri
exit /b %KARARGAH_CIKIS%

rem ---- [06] Etkilesimli oturum ------------------------------------------------------------------
rem Bayrak sirasi: cok degerli bayraklar (--add-dir, --mcp-config) once, tek degerliler sonra; kullanicinin
rem argumanlari en sonda. Boylece ardindan gelen bayraksiz arguman (istem, alt komut) yutulmaz.
:etkilesimli_argumanli
pushd "%KARARGAH_IS%" 2>nul
if defined KARARGAH_ONEK echo [deneme] dizin: "%CD%"
%KARARGAH_ONEK% "%CLAUDE_APP_BIN%" %KARARGAH_UZAK_ARG% %KARARGAH_ULAK_ARG% %KARARGAH_PROFIL_ARG% %KARARGAH_MODEL_ARG% %KARARGAH_IZIN_ARG% %KARARGAH_EFOR_ARG% %KARARGAH_AC_ARG% %*
set "KARARGAH_CIKIS=%errorlevel%"
popd 2>nul
call :kodsayfasi_geri
exit /b %KARARGAH_CIKIS%

:burada_argumanli
rem --burada ve ardindaki argumanlar bayrakli cagri gibi; oturum karargah kokunde, cagrilan klasor uzak yer olarak
rem ekli. --burada claude'a gecmez.
pushd "%KARARGAH_IS%" 2>nul
if defined KARARGAH_ONEK echo [deneme] dizin: "%CD%"
%KARARGAH_ONEK% "%CLAUDE_APP_BIN%" %KARARGAH_UZAK_ARG% %KARARGAH_ULAK_ARG% %KARARGAH_PROFIL_ARG% %KARARGAH_MODEL_ARG% %KARARGAH_IZIN_ARG% %KARARGAH_EFOR_ARG% %KARARGAH_AC_ARG% %2 %3 %4 %5 %6 %7 %8 %9
set "KARARGAH_CIKIS=%errorlevel%"
popd 2>nul
call :kodsayfasi_geri
exit /b %KARARGAH_CIKIS%

rem ---- [06u] Remote Control sunucusu: ortam karargah, claude.ai ve telefon uzak ekran -------------------
rem Karakter bayraklari fiilden once verilirse claude.exe acilmayi reddeder; --settings ve --permission-mode
rem fiilden sonra verilir. --model, --effort, --autocompact ve --mcp-config sunucu kipinde yoktur; actigi
rem oturumlar karakter dosyasini (--settings) ve karargahin kullanici ayarini okur. Tam giris gerekir:
rem claude_code.cmd auth login (setup-token yetmez).
:uzaktan_kumanda
set "KARARGAH_RC_IZIN="
if /i "%KARARGAH_IZIN%"=="tam" set "KARARGAH_RC_IZIN=--permission-mode bypassPermissions"
if /i "%KARARGAH_IZIN%"=="mutlak" set "KARARGAH_RC_IZIN=--permission-mode bypassPermissions"
if /i "%KARARGAH_IZIN%"=="auto" set "KARARGAH_RC_IZIN=--permission-mode auto"
if defined KARARGAH_UZAK echo [KARARGAH] BILGI: Remote Control sunucusuna uzak yer bayrakla eklenmez; permissions.additionalDirectories ayari kullanilir.
pushd "%KARARGAH_IS%" 2>nul
if defined KARARGAH_ONEK echo [deneme] dizin: "%CD%"
%KARARGAH_ONEK% "%CLAUDE_APP_BIN%" remote-control %KARARGAH_PROFIL_ARG% %KARARGAH_RC_IZIN% %2 %3 %4 %5 %6 %7 %8 %9
set "KARARGAH_CIKIS=%errorlevel%"
popd 2>nul
call :kodsayfasi_geri
exit /b %KARARGAH_CIKIS%

:etkilesimli
if not defined WEZTERM_PANE if not defined KARARGAH_KABUK if not defined KARARGAH_EK if not defined KARARGAH_ONEK call :wezterm_dene
if defined KARARGAH_WEZ_BITTI call :kodsayfasi_geri & exit /b 0
set "KARARGAH_SURUM="
for /f "usebackq delims=" %%V in (`call "%CLAUDE_APP_BIN%" --version 2^>nul`) do if not defined KARARGAH_SURUM set "KARARGAH_SURUM=%%V"
if not defined KARARGAH_SURUM set "KARARGAH_SURUM=claude"
set "KARARGAH_MODEL_BILGI=%KARARGAH_MODEL% (--model)"
if /i "%KARARGAH_MODEL%"=="ayar" set "KARARGAH_MODEL_BILGI=ayar (bayrak yok; /model kaydi ya da hesap varsayilani)"
set "KARARGAH_EFOR_BILGI=%KARARGAH_EFOR% (--effort); oturumda /effort"
if /i "%KARARGAH_EFOR%"=="ayar" set "KARARGAH_EFOR_BILGI=settings.json effortLevel; oturumda /effort"
set "KARARGAH_SUBAGENT_BILGI=acik; alt ajan modeli Opus 4.8, eforu xhigh"
if "%KARARGAH_SUBAGENT%"=="0" set "KARARGAH_SUBAGENT_BILGI=kapali (settings.tek.json; Agent araci yasakli)"
set "KARARGAH_YETKI_BILGI=%KARARGAH_IZIN%: %KARARGAH_IZIN_ARG%"
if /i "%KARARGAH_IZIN%"=="yok" set "KARARGAH_YETKI_BILGI=settings.json defaultMode gecerli"
title Claude Code Karargahi [%KARARGAH_MODEL% / %KARARGAH_IZIN%]
cd /d "%KARARGAH_IS%"
echo ============================================================================
echo   Claude Code Karargahi                           %KARARGAH_SURUM%
echo   Kok    : "%KARARGAH_ROOT%"   [%KARARGAH_YERLESIM% yerlesimi]
if defined KARARGAH_UZAK echo   Uzak   : "%KARARGAH_UZAK%"   ek dizin, oturuma adini verir; ortam kokte kalir. Cikarmak icin: set KARARGAH_DIZIN=
echo   Hafiza : "%CLAUDE_CONFIG_DIR%"
echo   Model  : %KARARGAH_MODEL_BILGI%   efor: %KARARGAH_EFOR_BILGI%   hizli kip: kapali
echo   Yetki  : %KARARGAH_YETKI_BILGI%
echo   Alt ajan: %KARARGAH_SUBAGENT_BILGI%
echo   Kabuk  : %KARARGAH_KABUK_BILGI%
if defined KARARGAH_ULAK_ARG if defined KARARGAH_KANAL_ARG echo   Ulak   : acik; kanal itmesi acik; araclar: ulak_gonder ulak_oku ulak_bekle ulak_defter ulak_kollar ulak_cagir
if defined KARARGAH_ULAK_ARG if not defined KARARGAH_KANAL_ARG echo   Ulak   : acik; kanal itmesi kapali; zarflar kanca ve ulak_oku ile gelir
if not defined KARARGAH_ULAK_ARG echo   Ulak   : yok; ortak\ulak kurulu degil ya da KARARGAH_ULAK=0
if not defined KARARGAH_PROFIL_ARG echo   UYARI  : karakter dosyasi yok, varsayilan ayarlar: "%KARARGAH_PROFIL_SECILI%"
if defined KARARGAH_UST_AYAR if exist "%KARARGAH_UST_AYAR%" echo   Bilgi  : "%KARARGAH_UST_AYAR%" yuklenmez; etkin karakter 01_Yapilandirma\settings.json
if defined KARARGAH_PE echo   Makine : Windows PE; hafiza ve gecicilik karargahta, oturum klasoru surucu harfinden bagimsiz
if "%KARARGAH_TAM_IZOLASYON%"=="1" echo   Ev     : USERPROFILE, HOME, LOCALAPPDATA, APPDATA, TEMP karargahta
echo   Icerde : /model  /effort  /fast  /autocompact  /permissions  /status ; Alt+M kip, Alt+V gorsel
echo   Cikista bu konsol acik kalir; claude yazinca ayni kapidan yeniden acilir (claude --continue gibi).
echo ============================================================================
if defined KARARGAH_ONEK echo [deneme] dizin: "%CD%"
%KARARGAH_ONEK% "%CLAUDE_APP_BIN%" %KARARGAH_UZAK_ARG% %KARARGAH_ULAK_ARG% %KARARGAH_PROFIL_ARG% %KARARGAH_MODEL_ARG% %KARARGAH_IZIN_ARG% %KARARGAH_EFOR_ARG% %KARARGAH_AC_ARG% %KARARGAH_AD_ARG% %KARARGAH_KANAL_ARG%
set "KARARGAH_CIKIS=%errorlevel%"
if defined KARARGAH_ONEK call :kodsayfasi_geri & exit /b 0
title Claude Code Karargahi [konsol]
echo.
echo [KARARGAH] Claude Code kapandi (cikis kodu %KARARGAH_CIKIS%). Yeniden: claude   Son oturum: claude --continue
if defined KARARGAH_KABUK call :kodsayfasi_geri & exit /b %KARARGAH_CIKIS%
set "KARARGAH_KABUK=1"
set "PROMPT=[Karargah] $P$G"
doskey claude="%~f0" $*
cmd.exe /k
exit /b

rem ---- [07] Guncelleme -----------------------------------------------------------------------------
:guncelle
if defined KARARGAH_ONEK echo [deneme] guncelleme calistirilmadi. & call :kodsayfasi_geri & exit /b 0
set "KARARGAH_PS=%KARARGAH_PWSH%"
if not defined KARARGAH_PS for %%P in (pwsh.cmd) do if not "%%~$PATH:P"=="" set "KARARGAH_PS=%%~$PATH:P"
if not defined KARARGAH_PS set "KARARGAH_PS=powershell.exe"
if not exist "%KARARGAH_KAPI%\claude_guncelle.ps1" echo [KARARGAH] HATA: claude_guncelle.ps1 yok: "%KARARGAH_KAPI%" & goto :hata
set "KARARGAH_HEDEF_SURUM=%~2"
call "%KARARGAH_PS%" -NoProfile -ExecutionPolicy Bypass -File "%KARARGAH_KAPI%\claude_guncelle.ps1" -Govde "%CLAUDE_APP_BIN%" -Surum "%KARARGAH_HEDEF_SURUM%" -Gecici "%KARARGAH_TEMP%"
set "KARARGAH_CIKIS=%errorlevel%"
call :kodsayfasi_geri
if not defined KARARGAH_KABUK pause
exit /b %KARARGAH_CIKIS%

rem ---- [08] Yardim ---------------------------------------------------------------------------------
:yardim
echo.
echo  claude_code.cmd                   etkilesimli oturum (kok: "%KARARGAH_ROOT%")
echo  claude_code.cmd --continue        son oturuma ayni karakterle devam
echo  claude_code.cmd --burada [arg...] oturum karargah kokunde; cagrildigi klasor uzak yer olarak eklenir
echo  claude_code.cmd -p "soru"         bayraklar karakterle birlikte aktarilir
echo  claude_code.cmd remote-control    Remote Control sunucusu karargah kokunde (rc ayni)
echo  claude_code.cmd doctor            alt komutlar dogrudan aktarilir; karargah kokunde calisir
echo  claude_code.cmd --guncelle [x.y.z]   resmi govdeyi indir, ozetini dogrula, yerine koy
echo.
echo  Anahtarlar: KARARGAH_IZIN=mutlak^|tam^|auto^|yok  KARARGAH_SUBAGENT=1^|0  KARARGAH_MODEL=claude-opus-5-5^|opus^|best^|ayar
echo              KARARGAH_EFOR=max^|ultracode^|xhigh^|high^|medium^|low^|ayar  KARARGAH_AUTOCOMPACT=200k^|500k^|1M  KARARGAH_TAM_IZOLASYON=1^|0
echo              KARARGAH_WEZTERM=^<wezterm-gui.exe^>  KARARGAH_PE_PAGEFILE=^<MB^>
echo              KARARGAH_DIZIN=^<uzak yer olarak eklenecek klasor^>  KARARGAH_DENEME=1
call :kodsayfasi_geri
exit /b 0

rem ---- [09] Hatalar ----------------------------------------------------------------------------------
:hata_yerlesim
echo [KARARGAH] HATA: yerlesim taninmadi. Bu dosya ya karargah kokunde (uygulama\yerel\ yaninda)
echo            ya da claude_code_cli\claude_code_exe\ icinde (00_Uygulama\ yaninda) durmali: "%KARARGAH_KAPI%"
goto :hata
:hata_burada_rc
echo [KARARGAH] HATA: remote-control her zaman karargah kokunde calisir; --burada olmadan cagirin.
goto :hata
:hata_govde
echo [KARARGAH] HATA: claude.exe yok: "%CLAUDE_APP_BIN%"
echo            Resmi tek dosya: https://downloads.claude.ai/claude-code-releases/^<x.y.z^>/win32-x64/claude.exe
echo            uygulama\yerel\ icine kopyalanir ya da claude_code.cmd --guncelle calistirilir.
goto :hata
:hata
echo.
echo [KARARGAH] Kapi acilmadi.
call :kodsayfasi_geri
if "%~1"=="" pause
exit /b 1

rem ============================== Alt yordamlar ==============================

:pe_hazirla
rem MiniNT anahtari = Windows PE. Ev karargaha doner; uzun yol acilir; istenirse sayfalama dosyasi.
set "KARARGAH_PE="
reg query "HKLM\SYSTEM\CurrentControlSet\Control\MiniNT" >nul 2>&1 && set "KARARGAH_PE=1"
if not defined KARARGAH_PE exit /b 0
if not defined KARARGAH_TAM_IZOLASYON set "KARARGAH_TAM_IZOLASYON=1"
reg add "HKLM\SYSTEM\CurrentControlSet\Control\FileSystem" /v LongPathsEnabled /t REG_DWORD /d 1 /f >nul 2>&1
if not defined KARARGAH_PE_PAGEFILE exit /b 0
if not exist "%KARARGAH_ROOT:~0,2%\pagefile.sys" wpeutil CreatePageFile /path=%KARARGAH_ROOT:~0,2%\pagefile.sys /size=%KARARGAH_PE_PAGEFILE% >nul 2>&1
exit /b 0

:git_bash_bul
rem Bash araci icin bash.exe: tasinabilir Git, sistem Git, PATH'teki git. Yoksa PowerShell araci yeter.
set "KARARGAH_GIT_BASH="
if exist "%CLAUDE_APP_DIR%\PortableGit\bin\bash.exe" set "KARARGAH_GIT_BASH=%CLAUDE_APP_DIR%\PortableGit\bin\bash.exe"
if defined KARARGAH_GIT_BASH if not defined KARARGAH_KABUK set "PATH=%CLAUDE_APP_DIR%\PortableGit\cmd;%PATH%"
if not defined KARARGAH_GIT_BASH if exist "%ProgramFiles%\Git\bin\bash.exe" set "KARARGAH_GIT_BASH=%ProgramFiles%\Git\bin\bash.exe"
if not defined KARARGAH_GIT_BASH if defined ProgramFiles(x86) if exist "%ProgramFiles(x86)%\Git\bin\bash.exe" set "KARARGAH_GIT_BASH=%ProgramFiles(x86)%\Git\bin\bash.exe"
if not defined KARARGAH_GIT_BASH if exist "%LocalAppData%\Programs\Git\bin\bash.exe" set "KARARGAH_GIT_BASH=%LocalAppData%\Programs\Git\bin\bash.exe"
if not defined KARARGAH_GIT_BASH for %%G in (git.exe) do if not "%%~$PATH:G"=="" for %%I in ("%%~dp$PATH:G..") do if exist "%%~fI\bin\bash.exe" set "KARARGAH_GIT_BASH=%%~fI\bin\bash.exe"
if defined KARARGAH_GIT_BASH if not defined CLAUDE_CODE_GIT_BASH_PATH set "CLAUDE_CODE_GIT_BASH_PATH=%KARARGAH_GIT_BASH%"
set "KARARGAH_KABUK_BILGI=PowerShell araci (Git Bash yok)"
if defined KARARGAH_GIT_BASH set "KARARGAH_KABUK_BILGI=Git Bash + PowerShell araci"
exit /b 0

:wezterm_dene
rem Tasinabilir WezTerm varsa oturum onun penceresinde acilir; bu pencere kapanir.
set "KARARGAH_WEZ="
if defined KARARGAH_WEZTERM if exist "%KARARGAH_WEZTERM%" set "KARARGAH_WEZ=%KARARGAH_WEZTERM%"
if not defined KARARGAH_WEZ if exist "%KARARGAH_TERMINAL%\wezterm-gui.exe" set "KARARGAH_WEZ=%KARARGAH_TERMINAL%\wezterm-gui.exe"
if not defined KARARGAH_WEZ if exist "%KARARGAH_USTKOK%\00_araclar\wezterm\wezterm-gui.exe" set "KARARGAH_WEZ=%KARARGAH_USTKOK%\00_araclar\wezterm\wezterm-gui.exe"
if not defined KARARGAH_WEZ exit /b 0
start "" "%KARARGAH_WEZ%" start --cwd "%KARARGAH_IS%" -- cmd.exe /d /k call "%~f0"
if errorlevel 1 exit /b 0
set "KARARGAH_WEZ_BITTI=1"
exit /b 0

:git_ayari
rem Karargah surucusu (FAT32) izin biti ve sembolik bag tasimaz; derin yollar git'te uzun yol ister. Ortam degiskeniyle
rem verilen ayar depo ve kullanici ayarinin ustundedir; hicbir dosyaya yazilmaz.
set "GIT_CONFIG_COUNT=3"
set "GIT_CONFIG_KEY_0=core.longpaths"
set "GIT_CONFIG_VALUE_0=true"
set "GIT_CONFIG_KEY_1=core.symlinks"
set "GIT_CONFIG_VALUE_1=false"
set "GIT_CONFIG_KEY_2=core.filemode"
set "GIT_CONFIG_VALUE_2=false"
exit /b 0

:pwsh_bul
rem PowerShell 7: bilinen klasor, PATH'teki pwsh.exe, sonra pwsh.cmd yonlendiricisine PSHOME sorulur.
set "KARARGAH_PWSH="
if exist "%ProgramFiles%\PowerShell\7\pwsh.exe" set "KARARGAH_PWSH=%ProgramFiles%\PowerShell\7\pwsh.exe"
if not defined KARARGAH_PWSH for %%P in (pwsh.exe) do if not "%%~$PATH:P"=="" set "KARARGAH_PWSH=%%~$PATH:P"
if not defined KARARGAH_PWSH for %%P in (pwsh.cmd) do if not "%%~$PATH:P"=="" for /f "usebackq delims=" %%H in (`call "%%~$PATH:P" -NoProfile -NonInteractive -Command "$PSHOME" 2^>nul`) do if not defined KARARGAH_PWSH if exist "%%~H\pwsh.exe" set "KARARGAH_PWSH=%%~H\pwsh.exe"
if not defined KARARGAH_PWSH exit /b 0
for %%I in ("%KARARGAH_PWSH%") do set "KARARGAH_PWSH_DIR=%%~dpI"
if "%KARARGAH_PWSH_DIR:~-1%"=="\" set "KARARGAH_PWSH_DIR=%KARARGAH_PWSH_DIR:~0,-1%"
if not defined KARARGAH_KABUK set "PATH=%KARARGAH_PWSH_DIR%;%PATH%"
exit /b 0

:ek_sinir
rem --burada kapinin argumanidir ve CLI'a gecmez; remote-control kapida yeniden yazilir. Ikisinde de ilk
rem argumanin ardindan ikinci ile dokuzuncu arasi en cok sekiz arguman tirnaklari ve sirasiyla gecer. Fazlasi
rem sessizce dusmesin diye oturum acilmaz.
shift & shift & shift & shift & shift & shift & shift & shift & shift
if "%~1"=="" exit /b 0
echo [KARARGAH] HATA: ilk argumanin ardindan en cok sekiz arguman gecer; fazlasi dusmesin diye oturum acilmadi.
exit /b 1

:uzak_hazirla
rem KARARGAH_DIZIN'i tam yola cevirir ve --add-dir bayragini kurar. Olmayan klasor ve karargah kokunun kendisi
rem eklenmez. --add-dir cok degerlidir: bosluklu yazilirsa ardindaki bayraksiz argumani da klasor sanar; deger
rem "=" ile verilir. Yol sonunda ters bolu tutulmaz (tirnagi bozar); surucu koku C:\. olarak yazilir.
set "KARARGAH_DIZIN=%KARARGAH_DIZIN:"=%"
if not defined KARARGAH_DIZIN exit /b 0
if not "%KARARGAH_DIZIN%"=="\" if "%KARARGAH_DIZIN:~-1%"=="\" set "KARARGAH_DIZIN=%KARARGAH_DIZIN:~0,-1%"
for %%I in ("%KARARGAH_DIZIN%\.") do set "KARARGAH_UZAK=%%~fI"
if "%KARARGAH_UZAK:~-1%"=="\" set "KARARGAH_UZAK=%KARARGAH_UZAK:~0,-1%"
if exist "%KARARGAH_UZAK%\" goto :uzak_var
echo [KARARGAH] UYARI: eklenecek klasor bulunamadi, uzak yer eklenmedi: "%KARARGAH_DIZIN%"
set "KARARGAH_UZAK="
exit /b 0
:uzak_var
if /i "%KARARGAH_UZAK%"=="%KARARGAH_ROOT%" set "KARARGAH_UZAK="
if not defined KARARGAH_UZAK exit /b 0
rem Oturum adi: eklenen klasorun adi (surucu kokunde ad verilmez). Yalniz yeni etkilesimli oturuma verilir;
rem /resume secicisinde, ucbirim basliginda ve Remote Control listesinde gorunur.
if not "%KARARGAH_UZAK:~-1%"==":" for %%I in ("%KARARGAH_UZAK%") do set "KARARGAH_UZAK_AD=%%~nxI"
if defined KARARGAH_UZAK_AD set "KARARGAH_AD_ARG=-n "%KARARGAH_UZAK_AD%""
if "%KARARGAH_UZAK:~-1%"==":" set "KARARGAH_UZAK=%KARARGAH_UZAK%\."
set "KARARGAH_UZAK_ARG=--add-dir="%KARARGAH_UZAK%""
exit /b 0

:kodsayfasi_geri
if defined KARARGAH_CP chcp %KARARGAH_CP% >nul 2>&1
exit /b 0
