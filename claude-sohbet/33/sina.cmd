@echo off
rem ======================================================================
rem  sina.cmd -- 33.exe'yi Windows'ta sinar.
rem  Bu dosyanin yaninda 33.exe durmalidir (33.hex.txt ve 33.b64.txt de
rem  varsa metinden kurma yolu da denenir).
rem  Cift tiklayin ya da komut isteminde calistirin.
rem  Sonuc ayni klasordeki windows_sonucu.txt dosyasina yazilir.
rem  Yalniz komut isteminin kendi komutlarini kullanir. certutil varsa
rem  dosya ozetine de bakar. Baska hicbir seye dokunmaz, aga cikmaz.
rem ======================================================================
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
set "S=windows_sonucu.txt"
set "BEKLENEN_OZET=4cc92e7034025c07e60c80d7b37c0adff140c88b4eeb28d7fcc638c5bfa4287f"
set /a GECEN=0
set /a KALAN=0
>"%S%" echo 33.exe Windows sinamasi
>>"%S%" echo isaret: CLS-004-P6X3
>>"%S%" echo zaman: %DATE% %TIME%
ver >>"%S%"
if not exist "33.exe" goto :dosya_yok

rem --- noktadaki cizelge: gidis ve donus
call :dene 33.exe "-33 para" "66 para"
call :dene 33.exe "-1 para" "34 para"
call :dene 33.exe "0 para" "33 para"
call :dene 33.exe "+1 para" "32 para"
call :dene 33.exe "+33 para" "0 para"
call :dene 33.exe "66 para" "-33 para"
call :dene 33.exe "34 para" "-1 para"
call :dene 33.exe "33 para" "0 para"
call :dene 33.exe "32 para" "1 para"
rem --- tek sayi, cok sayi, sayi olmayan
call :dene 33.exe "-1" "34"
call :dene 33.exe "66 34 33 32 0" "-33 -1 0 1 33"
call :dene 33.exe "merhaba" "merhaba"
call :dene 33.exe "5-3" "28-30"
call :dene 33.exe "16,5" "17,28"
rem --- sinirlar
call :dene 33.exe "9223372036854775807" "-9223372036854775774"
call :dene 33.exe "-9223372036854775774" "9223372036854775807"
call :dene 33.exe "9223372036854775808" "9223372036854775808"
call :dene 33.exe "000000000000000000001" "000000000000000000001"

rem --- iki arac art arda: gidis ve donus
>giren.tmp echo -33 para
33.exe <giren.tmp | 33.exe >cikan.tmp
set "CIKAN="
set /p CIKAN=<cikan.tmp
if "%CIKAN%"=="-33 para" goto :cift_gecti
set /a KALAN+=1
>>"%S%" echo KALDI  iki gecis: [%CIKAN%]
goto :bos
:cift_gecti
set /a GECEN+=1
>>"%S%" echo GECTI  iki gecis baslangica dondu: [%CIKAN%]

:bos
rem --- bos girise bos cikis
33.exe <nul >cikan.tmp
set "BOY=?"
for %%F in (cikan.tmp) do set "BOY=%%~zF"
if "%BOY%"=="0" goto :bos_gecti
set /a KALAN+=1
>>"%S%" echo KALDI  bos giris: %BOY% bayt cikti
goto :ozet
:bos_gecti
set /a GECEN+=1
>>"%S%" echo GECTI  bos girise bos cikis

:ozet
rem --- dosya ozeti ve metinden kurma (certutil varsa)
certutil -? >nul 2>nul
if errorlevel 1 goto :certutil_yok
call :ozet_al 33.exe
if not defined OZET goto :certutil_yok
if /i "%OZET%"=="%BEKLENEN_OZET%" goto :ozet_gecti
set /a KALAN+=1
>>"%S%" echo KALDI  ozet: [%OZET%]
goto :hex
:ozet_gecti
set /a GECEN+=1
>>"%S%" echo GECTI  33.exe ozeti beklenenle ayni

:hex
if not exist "33.hex.txt" goto :b64
if exist hex_kurulan.exe del hex_kurulan.exe
certutil -f -decodehex 33.hex.txt hex_kurulan.exe >nul 2>nul
call :kurulan hex_kurulan.exe "onaltilik yazimdan"

:b64
if not exist "33.b64.txt" goto :bitti
if exist b64_kurulan.exe del b64_kurulan.exe
certutil -f -decode 33.b64.txt b64_kurulan.exe >nul 2>nul
call :kurulan b64_kurulan.exe "32 satirdan"
goto :bitti

:certutil_yok
>>"%S%" echo NOT    certutil yok ya da calismiyor: ozet ve metinden kurma denenmedi
goto :bitti

:dosya_yok
set /a KALAN+=1
>>"%S%" echo KALDI  33.exe bu klasorde yok
goto :bitti

:bitti
>>"%S%" echo toplam: %GECEN% gecti, %KALAN% kaldi
if exist giren.tmp del giren.tmp
if exist cikan.tmp del cikan.tmp
if exist ozet.tmp del ozet.tmp
if exist hex_kurulan.exe del hex_kurulan.exe
if exist b64_kurulan.exe del b64_kurulan.exe
type "%S%"
echo.
echo Sonuc bu klasordeki windows_sonucu.txt dosyasina yazildi.
if not defined SINA_BEKLEME pause
endlocal
exit /b 0

rem ---------------------------------------------------------------------
rem  :dene ARAC "giren" "beklenen" -- bir satiri aractan gecirir
:dene
>giren.tmp echo %~2
"%~1" <giren.tmp >cikan.tmp
if errorlevel 1 goto :dene_kaldi
set "CIKAN="
set /p CIKAN=<cikan.tmp
if not "%CIKAN%"=="%~3" goto :dene_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  [%~2] girdi, [%CIKAN%] cikti
exit /b 0
:dene_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  [%~2] girdi, [%CIKAN%] cikti, beklenen [%~3]
exit /b 0

rem  :ozet_al DOSYA -- SHA-256 ozetini OZET degiskenine koyar
:ozet_al
set "OZET="
certutil -hashfile "%~1" SHA256 >ozet.tmp 2>nul
for /f "skip=1 delims=" %%H in (ozet.tmp) do if not defined OZET set "OZET=%%H"
if defined OZET set "OZET=%OZET: =%"
exit /b 0

rem  :kurulan DOSYA "nereden" -- metinden kurulan dosyayi dener
:kurulan
if not exist "%~1" goto :kurulan_kaldi
call :ozet_al "%~1"
if /i not "%OZET%"=="%BEKLENEN_OZET%" goto :kurulan_kaldi
>giren.tmp echo -1
"%~1" <giren.tmp >cikan.tmp
set "CIKAN="
set /p CIKAN=<cikan.tmp
if not "%CIKAN%"=="34" goto :kurulan_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~2 kurulan dosya ayni ve calisiyor
exit /b 0
:kurulan_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~2 kurma: ozet [%OZET%]
exit /b 0
