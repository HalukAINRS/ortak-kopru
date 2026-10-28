@echo off
setlocal EnableExtensions DisableDelayedExpansion
rem One local server, one private persistent state directory. Python 3.12+.
if "%~1"=="--help" goto usage
if "%~1"=="/?" goto usage
if not "%~2"=="" goto bad_arguments
if not exist "%~dp0deus.py" goto missing_entry

if "%~1"=="" goto default_state
set "ORTAK_NOKTA_STATE=%~f1"
goto find_python

:default_state
if not defined LOCALAPPDATA goto missing_state
for %%P in ("%LOCALAPPDATA%\OrtakKopru\TekNokta") do set "ORTAK_NOKTA_STATE=%%~fP"

:find_python
python -I -c "import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)" >nul 2>&1
if not errorlevel 1 goto use_python
py -3 -I -c "import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)" >nul 2>&1
if not errorlevel 1 goto use_py
echo Hata: Python 3.12 veya ustu bulunamadi. Python kurulumunu denetleyin. 1>&2
exit /b 1

:use_python
set "ORTAK_NOKTA_PY=python"
set "ORTAK_NOKTA_PY_ARGS="
goto launch

:use_py
set "ORTAK_NOKTA_PY=py"
set "ORTAK_NOKTA_PY_ARGS=-3"

:launch
echo Ortak Nokta, acik portable gelistirme kipinde baslatiliyor.
echo Bu baslatici NT surucusu kurulumu veya cekirdek dogrulamasi yapmaz.
echo Kalici ozel alan: "%ORTAK_NOKTA_STATE%"
echo Asagidaki launch_url baglantisini bu bilgisayarin tarayicisinda acin.
echo Baglanti size ozeldir; sohbet, ortak kayit veya GitHub'a aktarmayin.
echo Sunucuyu durdurmak icin Ctrl+C kullanin.
"%ORTAK_NOKTA_PY%" %ORTAK_NOKTA_PY_ARGS% -I "%~dp0deus.py" --state-dir "%ORTAK_NOKTA_STATE%" --backend portable serve --port 8765
set "ORTAK_NOKTA_EXIT=%errorlevel%"
endlocal & exit /b %ORTAK_NOKTA_EXIT%

:missing_state
echo Hata: LOCALAPPDATA tanimli degil. Git disinda kalici bir ozel dizin belirtin. 1>&2
echo Kullanim: Ortak_Nokta.cmd "D:\OrtakKopruVeri\TekNokta" 1>&2
exit /b 2

:missing_entry
echo Hata: Baslaticinin yaninda deus.py bulunamadi. Depo dosyalarini birlikte tutun. 1>&2
exit /b 2

:bad_arguments
echo Hata: Yalniz bir ozel calisma dizini argumani verilebilir. 1>&2
echo Kullanim: Ortak_Nokta.cmd ["TAM_OZEL_DIZIN_YOLU"] 1>&2
exit /b 2

:usage
echo Kullanim: Ortak_Nokta.cmd ["TAM_OZEL_DIZIN_YOLU"]
echo Varsayilan: LOCALAPPDATA\OrtakKopru\TekNokta
echo Dizin Git disinda olmali. Portable yerel sunucu port 8765'te acilir.
exit /b 0
