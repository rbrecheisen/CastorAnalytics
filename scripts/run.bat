@echo off

setlocal

@REM if /I "%~1"=="" (
@REM     echo "Usage: run.bat [--dev|--test|--exe|--pyinstaller]"
@REM     exit /b 1
@REM )

set START_DIR=%CD%

if /I "%~1"=="" (
    cd castoranalytics
    call briefcase dev
) else if /I "%~1"=="--test" (
    cd castoranalytics
    call briefcase dev --test
) else if /I "%~1"=="--exe" (
    cd castoranalytics
    call briefcase run
)

@REM ) else if /I "%~1"=="--pyinstaller" (
@REM     cd castoranalytics\dist\CastorAnalytics
@REM     call CastorAnalytics.exe
@REM ) else (
@REM     echo "Usage: run.bat [--dev|--test|--exe|--pyinstaller]"
@REM )

cd %START_DIR%


endlocal