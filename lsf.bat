@echo off
dir %* /a:-d /O:GN | more +5 | take -2
