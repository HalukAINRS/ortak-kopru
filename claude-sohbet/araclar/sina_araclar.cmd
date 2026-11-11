@echo off
rem ======================================================================
rem  sina_araclar.cmd -- oran.exe, 128.exe ve yuva.exe'yi Windows'ta sinar.
rem  Bu dosyanin yaninda o uc dosya durmalidir. Yanlarinda 33.exe,
rem  kesisim.txt, say.txt ve *.b64.txt dosyalari varsa onlar da denenir.
rem  Cift tiklayin ya da komut isteminde calistirin.
rem  Sonuc ayni klasordeki araclar_sonucu.txt dosyasina yazilir.
rem  Yalniz komut isteminin kendi komutlarini kullanir. certutil varsa
rem  dosya ozetine de bakar. Baska hicbir seye dokunmaz, aga cikmaz.
rem ======================================================================
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
set "S=araclar_sonucu.txt"
set /a GECEN=0
set /a KALAN=0
>"%S%" echo oran.exe, 128.exe, yuva.exe Windows sinamasi
>>"%S%" echo zaman: %DATE% %TIME%
ver >>"%S%"

rem --- oran.exe: ilk iki sayi sargidir (a b); sonrakiler x * b / a olur
if not exist "oran.exe" goto :oran_yok
call :dene oran.exe "8 1 128 bit" "16 bit" 0
call :dene oran.exe "1 8 16 bayt" "128 bayt" 0
call :dene oran.exe "1 1073741824 16" "17179869184" 0
call :dene oran.exe "1 8 17179869184" "137438953472" 0
call :dene oran.exe "64 1 128" "2" 0
call :dene oran.exe "1 2 64" "128" 0
call :dene oran.exe "8 1 12" "12" 1
call :dene oran.exe "3 2 9 10 -6" "6 10 -4" 1
call :dene oran.exe "-1 1 5 -7 0" "-5 7 0" 0
call :dene oran.exe "1 33 2 token" "66 token" 0
call :dene oran.exe "0 5 7" "7" 1
rem --- gidis ve donus: sargilar yer degistirince sayi geri gelir
>giren.tmp echo 8 1 128
oran.exe <giren.tmp >cikan.tmp
set "CIKAN="
set /p CIKAN=<cikan.tmp
>giren.tmp echo 1 8 %CIKAN%
oran.exe <giren.tmp >cikan.tmp
set "CIKAN="
set /p CIKAN=<cikan.tmp
if "%CIKAN%"=="128" goto :donus_gecti
set /a KALAN+=1
>>"%S%" echo KALDI  oran gidis-donus: [%CIKAN%]
goto :zincir
:donus_gecti
set /a GECEN+=1
>>"%S%" echo GECTI  oran gidis-donus: 128 - 16 - [%CIKAN%]
:zincir
rem --- iki arac art arda: oran, sonra 33 (birimler arasi, sonra birim ici)
if not exist "33.exe" goto :m128
>giren.tmp echo 8 1 128
oran.exe <giren.tmp | 33.exe >cikan.tmp
set "CIKAN="
set /p CIKAN=<cikan.tmp
if "%CIKAN%"=="17" goto :zincir_gecti
set /a KALAN+=1
>>"%S%" echo KALDI  oran ve 33 art arda: [%CIKAN%]
goto :m128
:zincir_gecti
set /a GECEN+=1
>>"%S%" echo GECTI  oran ve 33 art arda: 128 - 16 - [%CIKAN%]
goto :m128
:oran_yok
set /a KALAN+=1
>>"%S%" echo KALDI  oran.exe bu klasorde yok

:m128
rem --- 128.exe: (yer deger) ciftleri; cikis kodu 0 durdu, 1 hata, 2 sinir, 3 ret
if not exist "128.exe" goto :m128_yok
call :m128 "100 80000" 0 205 00000000000000000000000000000001
call :m128 "100 70000" 2 205 000000000000000000000000000186a0
call :m128 "100 90000" 1 204 00000000000000000000000000000000
call :m128 "100" 3 - -
call :m128 "200 1" 3 - -
call :m128 "0 1 100 10000 101 6107f 102 21001 103 80000" 0 001 80000000000000000000000000000000
call :m128 "0 1 100 10000 101 61080 102 21001 103 80000" 0 201 00000000000000000000000000000000
call :m128 "0 ffffffffffffffff 1 1 100 10000 101 11001 102 32001 103 22002 104 80000" 0 002 00000000000000010000000000000000
call :m128 "0 0xF0 1 0x3C 100 10000 101 11001 102 42001 103 53001 104 22002 105 23003 106 80000" 0 002 00000000000000000000000000000030
rem --- is yuku dosyalari varsa: cikti, beklenen dosyayla satir satir karsilastirilir
if exist "kesisim.txt" if exist "kesisim.beklenen.txt" call :m128beklenen kesisim.txt kesisim.beklenen.txt
if exist "say.txt" if exist "say.beklenen.txt" call :m128beklenen say.txt say.beklenen.txt
goto :yuva
:m128_yok
set /a KALAN+=1
>>"%S%" echo KALDI  128.exe bu klasorde yok

:yuva
rem --- yuva.exe: makinenin kendi kaydindan bellek yuvalari
if not exist "yuva.exe" goto :yuva_yok
yuva.exe >cikan.tmp
set "KOD=%errorlevel%"
if not "%KOD%"=="0" goto :yuva_okunamadi
set /a GECEN+=1
>>"%S%" echo GECTI  yuva.exe makinenin kaydini okudu. Satirlar (takili bayt, veri genisligi):
for /f "usebackq delims=" %%L in ("cikan.tmp") do >>"%S%" echo        yuva: %%L
goto :ozetler
:yuva_okunamadi
>>"%S%" echo NOT    yuva.exe kaydi okuyamadi (kod %KOD%); bu ortam kaydi vermiyor olabilir
goto :ozetler
:yuva_yok
set /a KALAN+=1
>>"%S%" echo KALDI  yuva.exe bu klasorde yok

:ozetler
rem --- dosya ozetleri ve metinden kurma (certutil varsa)
certutil -? >nul 2>nul
if errorlevel 1 goto :certutil_yok
call :ozet_al oran.exe
if not defined OZET goto :certutil_yok
call :ozet_denet oran f8422e88a688472bbfce532c3b1542fafe80d6d4692bdfa88bf5b8cf1b5a973c
call :ozet_denet 128 b686d70e266f0fa2fade7e578e441da89844fa57f67beeb099783e75d1e36739
call :ozet_denet yuva 13d7e92fd4d7c5c42e1c41d13af1ed6bfd2e58e5a62cfba76d761f0568cbbefb
goto :bitti
:certutil_yok
>>"%S%" echo NOT    certutil yok ya da calismiyor: ozet ve metinden kurma denenmedi

:bitti
>>"%S%" echo toplam: %GECEN% gecti, %KALAN% kaldi
if exist giren.tmp del giren.tmp
if exist cikan.tmp del cikan.tmp
if exist ozet.tmp del ozet.tmp
if exist b64_kurulan.exe del b64_kurulan.exe
type "%S%"
echo.
echo Sonuc bu klasordeki araclar_sonucu.txt dosyasina yazildi.
if not defined SINA_BEKLEME pause
endlocal
exit /b 0

rem ---------------------------------------------------------------------
rem  :dene ARAC "giren" "beklenen" KOD -- bir satiri aractan gecirir
:dene
>giren.tmp echo %~2
"%~1" <giren.tmp >cikan.tmp
set "KOD=%errorlevel%"
set "CIKAN="
set /p CIKAN=<cikan.tmp
if not "%CIKAN%"=="%~3" goto :dene_kaldi
if not "%KOD%"=="%~4" goto :dene_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  [%~2] girdi, [%CIKAN%] cikti, kod %KOD%
exit /b 0
:dene_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  [%~2] girdi, [%CIKAN%] cikti, kod %KOD%; beklenen [%~3], kod %~4
exit /b 0

rem  :m128 "girdi" KOD YER DEGER -- girdiyi 128.exe'ye verir, bir satira bakar
:m128
>giren.tmp echo %~1
128.exe <giren.tmp >cikan.tmp
set "KOD=%errorlevel%"
call :bak %2 %3 %4 "[%~1]"
exit /b 0

rem  :m128beklenen GIRDI BEKLENEN -- ciktinin her satiri beklenende, beklenenin her satiri ciktida olmali
:m128beklenen
128.exe <"%~1" >cikan.tmp
set "KOD=%errorlevel%"
set "UYMAYAN="
set /a SATIR=0
for /f "usebackq tokens=1,2" %%A in ("%~2") do call :satir_bak cikan.tmp %%A %%B
for /f "usebackq tokens=1,2" %%A in ("cikan.tmp") do call :satir_bak "%~2" %%A %%B
if not "%KOD%"=="0" goto :beklenen_kaldi
if defined UYMAYAN goto :beklenen_kaldi
if "%SATIR%"=="0" goto :beklenen_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  128: %~1 kod %KOD%; cikti %~2 ile ayni (%SATIR% satir karsilastirildi)
exit /b 0
:beklenen_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  128: %~1 kod %KOD%; uymayan yer [%UYMAYAN%]
exit /b 0

rem  :satir_bak DOSYA YER DEGER -- DOSYA icinde YER satirinin degeri DEGER mi
:satir_bak
set /a SATIR+=1
set "DEGER="
for /f "usebackq tokens=1,2" %%C in ("%~1") do if /i "%%C"=="%~2" set "DEGER=%%D"
if /i not "%DEGER%"=="%~3" set "UYMAYAN=%~2"
exit /b 0

rem  :bak KOD YER DEGER "ad" -- cikis kodunu ve YER satirindaki degeri denetler
:bak
set "DEGER="
for /f "usebackq tokens=1,2" %%A in ("cikan.tmp") do if /i "%%A"=="%~2" set "DEGER=%%B"
if not "%KOD%"=="%~1" goto :bak_kaldi
if "%~2"=="-" goto :bak_gecti
if /i not "%DEGER%"=="%~3" goto :bak_kaldi
:bak_gecti
set /a GECEN+=1
>>"%S%" echo GECTI  128: %~4 kod %KOD%, %~2 = %DEGER%
exit /b 0
:bak_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  128: %~4 kod %KOD%, beklenen %~1; %~2 = [%DEGER%], beklenen %~3
exit /b 0

rem  :ozet_al DOSYA -- SHA-256 ozetini OZET degiskenine koyar
:ozet_al
set "OZET="
certutil -hashfile "%~1" SHA256 >ozet.tmp 2>nul
for /f "skip=1 delims=" %%H in (ozet.tmp) do if not defined OZET set "OZET=%%H"
if defined OZET set "OZET=%OZET: =%"
exit /b 0

rem  :ozet_denet AD OZET -- AD.exe ozetini denetler; AD.b64.txt varsa ondan kurar
:ozet_denet
call :ozet_al "%~1.exe"
if /i not "%OZET%"=="%~2" goto :ozet_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~1.exe ozeti beklenenle ayni
goto :b64
:ozet_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~1.exe ozeti: [%OZET%]
:b64
if not exist "%~1.b64.txt" exit /b 0
if exist b64_kurulan.exe del b64_kurulan.exe
certutil -f -decode "%~1.b64.txt" b64_kurulan.exe >nul 2>nul
if not exist b64_kurulan.exe goto :b64_kaldi
call :ozet_al b64_kurulan.exe
if /i not "%OZET%"=="%~2" goto :b64_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~1.b64.txt dosyasindan kurulan dosya %~1.exe ile ayni
exit /b 0
:b64_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~1.b64.txt dosyasindan kurma: ozet [%OZET%]
exit /b 0
