@echo off

setlocal

set /p VERSION=<VERSION

if /I "%~1"=="" (
    @REM echo "Usage: build.bat [--briefcase|--nuitka|--pyinstaller]"
    echo "Usage: build.bat [--briefcase|--pyinstaller]"
    exit /b 1
)

set START_DIR=%CD%

if /I "%~1"=="--briefcase" (

    rmdir /s /q castoranalytics\build
    cd castoranalytics
    call briefcase create
    call briefcase build

@REM ) else if /I "%~1"=="--nuitka" (
@REM     rmdir /s /q castoranalytics\build-nuitka
@REM     cd castoranalytics\src
@REM     nuitka ^
@REM         --standalone ^
@REM         --enable-plugin=pyside6 ^
@REM         --include-qt-plugins=all ^
@REM         --include-data-dir=castoranalytics/resources=castoranalytics/resources ^
@REM         --windows-console-mode=disable ^
@REM         --output-dir=..\build-nuitka ^
@REM         --output-filename=CastorAnalytics ^
@REM         app.py
        
) else if /I "%~1"=="--pyinstaller" (

    rmdir /s /q castoranalytics\dist
    cd castoranalytics
    pyinstaller ^
        --windowed ^
        --name "CastorAnalytics" ^
        --add-data "src/castoranalytics/resources:castoranalytics/resources" ^
        src\app.py

) else (
    echo "Usage: build.bat [--briefcase|--nuitka]"
)

cd %START_DIR%

endlocal