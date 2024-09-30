@echo off
setlocal enabledelayedexpansion

rem Define o nome do arquivo de entrada e de saída
set "arquivo_entrada=C:\XML\23240107332190001246550010006479171921242313.xml"
set "arquivo_saida=C:\XML\teste1.xml"

for /f "tokens=2 delims=<>" %%a in ('findstr "<element1>" "%arquivo_entrada%"') do set "string1=%%a"
for /f "tokens=2 delims=<>" %%b in ('findstr "<element2>" "%arquivo_entrada%"') do set "string2=%%b"

echo %string1% %string2% > %arquivo_saida%

rem Abre o arquivo de saída
start "" %arquivo_saida%