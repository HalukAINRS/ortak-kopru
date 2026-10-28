@echo off
setlocal
set "DEUS_PY=Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime\Python\python.exe"
if not exist "%DEUS_PY%" (
  echo Python bulunamadi: %DEUS_PY%
  exit /b 1
)
echo deus_ex_machina: http://localhost:8765
echo Bu pencereyi kapatmak sunucuyu durdurur; Y: uzerindeki kayitlar kalir.
"%DEUS_PY%" -X utf8 "%~dp0bridge.py" --state-dir "Y:\HalukAI\Ortak_Kopru\DEUS_CLI" serve --port 8765
