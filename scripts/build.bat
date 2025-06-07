@echo off

setlocal

set /p VERSION=<VERSION

if /I "%~1"=="" (
    echo "Usage: build.bat [--briefcase|--nuitka]"
    exit /b 1
)

set START_DIR=%CD%

if /I "%~1"=="--briefcase" (

    rmdir /s /q castoranalytics\build
    cd castoranalytics
    call briefcase create
    call briefcase build

) else if /I "%~1"=="--nuitka" (

    rmdir /s /q castoranalytics\build-nuitka
    cd castoranalytics\src
    call nuitka ^
        --standalone ^
        --enable-plugin=pyside6 ^
        --include-qt-plugins=all ^
        --include-data-dir=castoranalytics/resources=castoranalytics/resources ^
        --windows-console-mode=disable ^
        --output-dir=..\build-nuitka ^
        --output-filename=CastorAnalytics ^
        app.py
) else (
    echo "Usage: build.bat [--briefcase|--nuitka]"
)

cd %START_DIR%

endlocal