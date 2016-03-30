@echo off
dir %* /a:d /O:GN | more +7 | take -2
