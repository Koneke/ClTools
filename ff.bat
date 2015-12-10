@echo off
set shh=
set filt=

IF [%1]==[-s] (
	for /f "tokens=2,* delims= " %%a in ("%*") do set rest=%%b
	set "shh= 1>NUL"
	set filt=%2
) ELSE (
	for /f "tokens=1,* delims= " %%a in ("%*") do set rest=%%b
	set filt=%1
)

for /F "tokens=*" %%a in ('sl %filt%') do %rest:"=%%shh% 2>NUL
