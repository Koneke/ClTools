@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\home\bin) else (cd /D %home%\home\bin)