@echo off

setlocal

set /p VERSION=<VERSION

set START_DIR=%CD%

if /I "%~1"=="--test" (
    cd castoranalytics
    call briefcase dev --test
) else if /I "%~1"=="--exe" (
    cd castoranalytics
    call briefcase run
) else if /I "%~1"=="--nuitka" (
    cd castoranalytics\build-nuitka\app.dist
    call CastorAnalytics.exe
) else (
    call briefcase dev
)

cd %START_DIR%


endlocal