@echo off
echo.
for /D %%s in (*) do pushd . && echo =============== %%s =============== && cd %%s && git status && popd && echo.
