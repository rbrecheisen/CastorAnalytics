@echo off

setlocal

set /p VERSION=<VERSION

set START_DIR=%CD%
cd castoranalytics
if /I "%~1"=="--test" (
    call briefcase dev --test
) else (
    call briefcase dev
)
cd %START_DIR%

endlocal