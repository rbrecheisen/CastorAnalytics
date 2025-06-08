@echo off

setlocal

set /p VERSION=<castoranalytics\src\castoranalytics\resources\VERSION

python scripts\python\updatetomlversion.py %VERSION%

set START_DIR=%CD%

cd castoranalytics
call briefcase package --adhoc-sign

@REM if /I "%~1"=="--briefcase" (
@REM     rmdir /s /q castoranalytics\build
@REM     cd castoranalytics
@REM     call briefcase create
@REM     call briefcase build
@REM ) else if /I "%~1"=="--pyinstaller" (
@REM     rmdir /s /q castoranalytics\dist
@REM     cd castoranalytics
@REM     pyinstaller ^
@REM         --windowed ^
@REM         --name "CastorAnalytics" ^
@REM         --add-data "src/castoranalytics/resources:castoranalytics/resources" ^
@REM         src\app.py
@REM ) else (
@REM     echo "Usage: build.bat [--briefcase|--pyinstaller]"
@REM )

cd %START_DIR%

endlocal