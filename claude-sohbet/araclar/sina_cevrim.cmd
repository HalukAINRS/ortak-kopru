@echo off
rem ======================================================================
rem  sina_cevrim.cmd -- cevrim.exe'yi ve iki betigi Windows'ta sinar.
rem  Bu dosyanin yaninda cevrim.exe durmalidir (geri_donus.cmd ile
rem  yeni_gidis.cmd de oradaysa onlar da sinanir). Cift tiklayin ya da
rem  komut isteminde calistirin. Sonuc ayni klasordeki cevrim_sonucu.txt
rem  dosyasina yazilir. Yalniz komut isteminin kendi komutlarini ve dosya
rem  karsilastirmak icin fc'yi kullanir; certutil varsa ozete de bakar.
rem  Deneme metinleri burada uretilir; sizin dosyalariniza dokunmaz.
rem ======================================================================
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
set "S=cevrim_sonucu.txt"
set /a GECEN=0
set /a KALAN=0
>"%S%" echo cevrim.exe Windows sinamasi
>>"%S%" echo zaman: %DATE% %TIME%
ver >>"%S%"
if not exist "cevrim.exe" goto :yok

rem --- fc gercekten ayirt ediyor mu (etmiyorsa karsilastirmalar sayilmaz)
>fa.tmp echo a
>fb.tmp echo b
set "FC_VAR=1"
fc /b fa.tmp fa.tmp >nul 2>nul
if errorlevel 1 set "FC_VAR=0"
fc /b fa.tmp fb.tmp >nul 2>nul
if not errorlevel 1 set "FC_VAR=0"
if "%FC_VAR%"=="0" >>"%S%" echo NOT    fc iki dosyayi ayirt etmiyor: dosya karsilastirmalari yapilmadi

rem --- tohum (t), baslik (h) ve beklenen nokta (nb)
>t.tmp echo bas
>>t.tmp echo ### H
>>t.tmp echo x
>>t.tmp echo.
>>t.tmp echo ### G
>>t.tmp echo y
>h.tmp echo .
>>h.tmp echo ### H
>>h.tmp echo .c:
>>h.tmp echo metin
>>h.tmp echo .
>>h.tmp echo .
>nb.tmp echo bas
>>nb.tmp echo ### H
>>nb.tmp echo x
>>nb.tmp echo.
>>nb.tmp echo .c:
>>nb.tmp echo metin
>>nb.tmp echo .
>>nb.tmp echo.
>>nb.tmp echo ### G
>>nb.tmp echo y

rem --- yeni gidis: baslik + tohum - nokta
copy /y /b h.tmp+t.tmp g.tmp >nul
cevrim.exe <g.tmp >n.tmp 2>k.tmp
call :kod 0 "yeni gidis"
call :ayni n.tmp nb.tmp "yeni gidis: nokta beklenenle ayni"
call :bos k.tmp "yeni gidis: yerlesmeyen bolum yok"

rem --- geri donus: nokta - tohum + baslik
cevrim.exe <n.tmp >t2.tmp 2>h2.tmp
call :kod 0 "geri donus"
call :ayni t2.tmp t.tmp "geri donus: tohum bayt bayt geri geldi"
call :ayni h2.tmp h.tmp "geri donus: bolumler basligiyla geri geldi"

rem --- yeniden gidis: donen tohum + donen baslik - ayni nokta
copy /y /b h2.tmp+t2.tmp g2.tmp >nul
cevrim.exe <g2.tmp >n2.tmp 2>k2.tmp
call :kod 0 "ikinci gidis"
call :ayni n2.tmp n.tmp "ikinci gidis: ikinci nokta ilkiyle ayni"

rem --- bolumu olmayan metin aynen gecer
cevrim.exe <t.tmp >t3.tmp 2>k3.tmp
call :kod 0 "bolumsuz metin"
call :ayni t3.tmp t.tmp "bolumsuz metin aynen gecti"
call :bos k3.tmp "bolumsuz metinde ikinci cikis bos"

rem --- basligi olmayan bolum yerlesmez, sayilir, geri gelir
>hz.tmp echo .
>>hz.tmp echo ### Z
>>hz.tmp echo .c:
>>hz.tmp echo metin
>>hz.tmp echo .
>>hz.tmp echo .
copy /y /b hz.tmp+t.tmp gz.tmp >nul
cevrim.exe <gz.tmp >nz.tmp 2>kz.tmp
call :kod 1 "basligi olmayan bolum"
call :ayni nz.tmp t.tmp "basligi olmayan bolum: tohum degismedi"
call :ayni kz.tmp hz.tmp "basligi olmayan bolum: ikinci cikistan geri geldi"

rem --- bozuk baslik: hicbir sey verilmez, kod -1
>hb.tmp echo .
>>hb.tmp echo yabanci
copy /y /b hb.tmp+t.tmp gb.tmp >nul
cevrim.exe <gb.tmp >nbz.tmp 2>kb.tmp
call :kod -1 "bozuk baslik"
call :bos nbz.tmp "bozuk baslik: birinci cikis bos"

rem --- iki betik (yanimizdaysa): adi bosluklu ve parantezli dosyayla
if not exist "yeni_gidis.cmd" goto :betik_yok
if not exist "geri_donus.cmd" goto :betik_yok
set "ESKI_BEKLEME=%SINA_BEKLEME%"
set "SINA_BEKLEME=1"
copy /y /b t.tmp "sina deneme (1).txt" >nul
call yeni_gidis.cmd "%~dp0sina deneme (1).txt" "%~dp0h.tmp" >b1.tmp 2>nul
call :kod 0 "yeni_gidis.cmd"
call :ayni "sina deneme (1).nokta.txt" nb.tmp "yeni_gidis.cmd: nokta beklenenle ayni"
call :yok_olmali "sina deneme (1).yerlesmeyen.txt" "yeni_gidis.cmd: yerlesmeyen dosyasi birakilmadi"
call :yok_olmali "sina deneme (1).t0.tmp" "yeni_gidis.cmd: gecici dosya birakilmadi"
call geri_donus.cmd "%~dp0sina deneme (1).nokta.txt" >b2.tmp 2>nul
call :kod 0 "geri_donus.cmd"
call :ayni "sina deneme (1).nokta.tohum.txt" t.tmp "geri_donus.cmd: tohum bayt bayt geri geldi"
call :ayni "sina deneme (1).nokta.bolumler.txt" h.tmp "geri_donus.cmd: bolumler basligiyla geri geldi"
rem     icinde zaten bolum olan dosya: once ayrilir, sonra yeniden yerlesir
call yeni_gidis.cmd "%~dp0sina deneme (1).nokta.txt" "%~dp0h.tmp" >b3.tmp 2>nul
call :kod 0 "yeni_gidis.cmd (dosyada zaten bolum var)"
call :ayni "sina deneme (1).nokta.nokta.txt" nb.tmp "yeni_gidis.cmd: bolum iki kez girmedi"
call :ayni "sina deneme (1).nokta.onceki_bolumler.txt" h.tmp "yeni_gidis.cmd: onceki bolumler ayri dosyada"
rem     basligi olmayan bolum: kod 1, yerlesmeyen dosyasi kalir
call yeni_gidis.cmd "%~dp0sina deneme (1).txt" "%~dp0hz.tmp" >b4.tmp 2>nul
call :kod 1 "yeni_gidis.cmd (basligi olmayan bolum)"
call :ayni "sina deneme (1).yerlesmeyen.txt" hz.tmp "yeni_gidis.cmd: yerlesmeyen bolum dosyada duruyor"
rem     bolumu olmayan dosya: geri donus bir sey yazmaz, kod 1
call geri_donus.cmd "%~dp0sina deneme (1).txt" >b5.tmp 2>nul
call :kod 1 "geri_donus.cmd (bolum yok)"
call :yok_olmali "sina deneme (1).tohum.txt" "geri_donus.cmd: bolum yokken dosya yazilmadi"
set "SINA_BEKLEME=%ESKI_BEKLEME%"
del "sina deneme (1)*.txt" 2>nul
goto :ozet
:betik_yok
>>"%S%" echo NOT    yeni_gidis.cmd ya da geri_donus.cmd yaninda yok: betikler sinanmadi

:ozet
rem --- dosya ozeti ve metinden kurma (certutil varsa)
certutil -? >nul 2>nul
if errorlevel 1 goto :certutil_yok
call :ozet_al cevrim.exe
if not defined OZET goto :certutil_yok
if /i not "%OZET%"=="420d752254741aaa0ff230e1ae4be9e9e3700cf085a5eabd354ed8e175349e5e" goto :ozet_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  cevrim.exe ozeti beklenenle ayni
goto :b64
:ozet_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  cevrim.exe ozeti: [%OZET%]
:b64
if not exist "cevrim.b64.txt" goto :bitti
if exist b64_kurulan.exe del b64_kurulan.exe
certutil -f -decode cevrim.b64.txt b64_kurulan.exe >nul 2>nul
call :ayni b64_kurulan.exe cevrim.exe "cevrim.b64.txt dosyasindan kurulan dosya cevrim.exe ile ayni"
goto :bitti
:certutil_yok
>>"%S%" echo NOT    certutil yok ya da calismiyor: ozet ve metinden kurma denenmedi
goto :bitti
:yok
set /a KALAN+=1
>>"%S%" echo KALDI  cevrim.exe bu klasorde yok

:bitti
>>"%S%" echo toplam: %GECEN% gecti, %KALAN% kaldi
del *.tmp 2>nul
if exist b64_kurulan.exe del b64_kurulan.exe
type "%S%"
echo.
echo Sonuc bu klasordeki cevrim_sonucu.txt dosyasina yazildi.
if not defined SINA_BEKLEME pause
endlocal
exit /b 0

rem ---------------------------------------------------------------------
rem  :kod BEKLENEN "ad" -- son calistirmanin cikis kodunu denetler
:kod
set "KOD=%errorlevel%"
if not "%KOD%"=="%~1" goto :kod_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~2: kod %KOD%
exit /b 0
:kod_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~2: kod %KOD%, beklenen %~1
exit /b 0

rem  :ayni A B "ad" -- iki dosya bayt bayt ayni mi
:ayni
if not exist "%~1" goto :ayni_kaldi
if "%FC_VAR%"=="0" exit /b 0
fc /b "%~1" "%~2" >nul 2>nul
if errorlevel 2 goto :ayni_kaldi
if errorlevel 1 goto :ayni_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~3
exit /b 0
:ayni_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~3
exit /b 0

rem  :bos DOSYA "ad" -- dosya 0 bayt mi
:bos
set "BOY=?"
for %%F in ("%~1") do set "BOY=%%~zF"
if not "%BOY%"=="0" goto :bos_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~2
exit /b 0
:bos_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~2: %BOY% bayt
exit /b 0

rem  :yok_olmali DOSYA "ad" -- dosya bulunmamali
:yok_olmali
if exist "%~1" goto :yok_kaldi
set /a GECEN+=1
>>"%S%" echo GECTI  %~2
exit /b 0
:yok_kaldi
set /a KALAN+=1
>>"%S%" echo KALDI  %~2
exit /b 0

rem  :ozet_al DOSYA -- SHA-256 ozetini OZET degiskenine koyar
:ozet_al
set "OZET="
certutil -hashfile "%~1" SHA256 >ozet.tmp 2>nul
for /f "skip=1 delims=" %%H in (ozet.tmp) do if not defined OZET set "OZET=%%H"
if defined OZET set "OZET=%OZET: =%"
exit /b 0
