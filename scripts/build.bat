@echo off

setlocal

set /p VERSION=<VERSION

if /I "%~1"=="" (
    echo "Usage: build.bat [--briefcase|--pyinstaller]"
    exit /b 1
)

set START_DIR=%CD%

if /I "%~1"=="--briefcase" (

    rmdir /s /q castoranalytics\build
    cd castoranalytics
    call briefcase create
    call briefcase build

) else if /I "%~1"=="--pyinstaller" (

    rmdir /s /q castoranalytics\dist
    cd castoranalytics
    pyinstaller ^
        --windowed ^
        --name "CastorAnalytics" ^
        --add-data "src/castoranalytics/resources:castoranalytics/resources" ^
        src\app.py

) else (
    echo "Usage: build.bat [--briefcase|--pyinstaller]"
)

cd %START_DIR%

endlocal