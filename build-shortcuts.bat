@echo off
del shortcuts\*.bat /s
python make-shortcut.py b bin
python make-shortcut.py d desktop
python make-shortcut.py dw downloads 
python make-shortcut.py g git 
python make-shortcut.py h ;
python make-shortcut.py -f i c:\inetpub\wwwroot\
