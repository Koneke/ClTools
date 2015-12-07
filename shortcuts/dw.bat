@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\downloads) else (cd /D %home%\downloads)