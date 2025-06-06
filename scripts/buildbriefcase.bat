@echo off

setlocal

set /p VERSION=<VERSION

rmdir /s /q castoranalytics\build

set START_DIR=%CD%
cd castoranalytics
call briefcase create
call briefcase build
cd %START_DIR%

endlocal