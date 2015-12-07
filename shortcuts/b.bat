@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\bin) else (cd /D %home%\bin)