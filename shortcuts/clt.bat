@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\git\cltools) else (cd /D %home%\git\cltools)