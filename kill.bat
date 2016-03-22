@echo off
set arg=%1
set arg=%arg:.exe=%
taskkill /im %arg%.exe /f
