@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%\home) else (cd /D %home%\home)