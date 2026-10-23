$ErrorActionPreference = "Stop"
. "Y:\HalukAI\HalukAI_Ortam.ps1"
$GitExe = "Y:\HalukAI\02_Govde\Canli\CLI_Katmanlari\Runtime\Git-Portable-2.56.0.2\cmd\git.exe"
Set-Location -LiteralPath "Y:\HalukAI\Ortak_Kopru\kopru"
Copy-Item -LiteralPath "Y:\HalukAI\Ortak_Kopru\kopru\kopru.html" -Destination "Y:\HalukAI\Ortak_Kopru\kopru.html" -Force
& $GitExe add kopru.html .nojekyll kopru_gonder.ps1
& $GitExe commit -m "Ortak Kopru guncellemesi"
& $GitExe push
