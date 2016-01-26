@echo off
if "%home%"=="" (cd /D %homedrive%%homepath%) else (cd /D %home%)