@echo off

setlocal

set /p VERSION=<castoranalytics\src\castoranalytics\resources\VERSION

set START_DIR=%CD%

if /I "%~1"=="" (

    cd castoranalytics
    call briefcase dev

) else if /I "%~1"=="--test" (

    cd castoranalytics
    call briefcase dev --test

) else if /I "%~1"=="--exe" (

    rmdir /s /q castoranalytics\build
    cd castoranalytics
    call briefcase create
    call briefcase build
    call briefcase run

) else if /I "%~1"=="--package" (

    call python scripts\python\updatetomlversion.py %VERSION%
    cd castoranalytics
    call briefcase package --adhoc-sign
    
)

cd %START_DIR%


endlocal