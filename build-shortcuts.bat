@echo off
del shortcuts\*.bat /s
python make-shortcut.py b home\bin
python make-shortcut.py d desktop
python make-shortcut.py dw downloads 
python make-shortcut.py g git 
python make-shortcut.py h home
python make-shortcut.py wh ;
python make-shortcut.py -f i c:\inetpub\wwwroot\
python make-shortcut.py docs documents
python make-shortcut.py vs documents\Visual Studio 2015\Projects
