@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\desktop) else (cd /D %home%\desktop)