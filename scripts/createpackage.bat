@echo off

setlocal

set /p VERSION=<castoranalytics\src\castoranalytics\resources\VERSION

set /p CONFIRM="Creating package for version %VERSION%. Is this the correct version? (y/n) "
if /I NOT "%CONFIRM%"=="y" (
    echo Aborting package creation
    exit /b 1
)

echo Create output directory (delete if already exists)...
set OUTPUT_DIR=D:\CastorAnalytics\CastorAnalytics
set OUTPUT_ZIP=D:\CastorAnalytics\CastorAnalytics-%VERSION%.zip
rmdir /s /q %OUTPUT_DIR%
mkdir %OUTPUT_DIR% 2>nul

@REM Source code
robocopy castoranalytics %OUTPUT_DIR% /E /XD __pycache__ *.dist-info .pytest_cache build dist logs tests /XF .gitignore CHANGELOG

@REM Scripts
copy requirements.txt %OUTPUT_DIR%
copy scripts\packagefiles\clean-python-environment.bat %OUTPUT_DIR%
copy scripts\packagefiles\clean-python-environment.ps1 %OUTPUT_DIR%
copy scripts\packagefiles\run-castoranalytics.bat %OUTPUT_DIR%

powershell -Command "Compress-Archive -Path '%OUTPUT_DIR%' -DestinationPath '%OUTPUT_ZIP%' -Force"

echo Created ZIP archive: %OUTPUT_ZIP%
echo Finished

endlocal