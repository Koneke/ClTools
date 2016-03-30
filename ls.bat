@echo off
REM show hidden files, skip first 7 and last 2
dir %* /o:GN /a | more +7 | take -2
