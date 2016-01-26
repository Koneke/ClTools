@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\documents) else (cd /D %home%\documents)