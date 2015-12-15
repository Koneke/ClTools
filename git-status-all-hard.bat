@echo off
echo.
for /D %%s in (*) do pushd . && echo =============== %%s =============== && cd %%s && git remote update && git status && popd && echo.
