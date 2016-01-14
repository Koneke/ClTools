@echo off
REM show hidden files, skip first 7
dir %* /o:GN /a | more +7
