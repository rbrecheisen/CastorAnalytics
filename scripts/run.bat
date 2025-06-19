@echo off

setlocal

set /p VERSION=<castoranalytics\src\castoranalytics\resources\VERSION

set START_DIR=%CD%

if /I "%~1"=="" (

    cd castoranalytics
    call briefcase dev

) else if /I "%~1"=="--help" (

    echo "Usage: run.bat [--help|--test|--build|--package]"
    echo ""
    echo "--help    Shows help information"
    echo "--test    Runs tests"
    echo "--build   Builds .exe or .app"
    echo "--package Creates .msi or .dmg installer"
    exit /b 1

) else if /I "%~1"=="--test" (

    cd castoranalytics
    call briefcase dev --test

) else if /I "%~1"=="--exe" (

    cd castoranalytics
    call briefcase run

) else if /I "%~1"=="--build" (

    rmdir /s /q castoranalytics\build
    call python scripts\python\updatetomlversion.py %VERSION%
    call python scripts\python\updatetomlrequirements.py
    cd castoranalytics
    call briefcase create
    call briefcase build

) else if /I "%~1"=="--package" (

    cd castoranalytics
    call briefcase package --adhoc-sign
    
)

cd %START_DIR%


endlocal