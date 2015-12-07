@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\git) else (cd /D %home%\git)