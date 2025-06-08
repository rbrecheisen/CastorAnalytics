@echo off

setlocal

set /p VERSION=<VERSION

if /I "%~1"=="" (
    @REM echo "Usage: run.bat [--dev|--test|--exe|--nuitka|--pyinstaller]"
    echo "Usage: run.bat [--dev|--test|--exe|--pyinstaller]"
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

@REM ) else if /I "%~1"=="--nuitka" (
@REM     cd castoranalytics\build-nuitka\app.dist
@REM     call CastorAnalytics.exe

) else if /I "%~1"=="--pyinstaller" (

    cd castoranalytics\dist\CastorAnalytics
    call CastorAnalytics.exe
    
) else (
    echo "Usage: run.bat [--dev|--test|--exe|--nuitka]"
)

cd %START_DIR%


endlocal