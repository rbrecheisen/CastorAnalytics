@echo off

setlocal

set /p VERSION=<VERSION

if /I "%~1"=="" (
    echo "Usage: run.bat [--dev|--test|--exe|--exe-nuitka]"
    exit /b 1
)

set START_DIR=%CD%

if /I "%~1"=="--dev" (
    cd castoranalytics
    call briefcase dev
) else if /I "%~1"=="--test" (
    cd castoranalytics
    call briefcase dev --test
) else if /I "%~1"=="--exe" (
    cd castoranalytics
    call briefcase run
) else if /I "%~1"=="--exe-nuitka" (
    cd castoranalytics\build-nuitka\app.dist
    call CastorAnalytics.exe
) else (
    echo "Unknown option"
)

cd %START_DIR%


endlocal