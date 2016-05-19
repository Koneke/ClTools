@echo off

REM strip quotes
echo %2 | enscript createnote /i %1
