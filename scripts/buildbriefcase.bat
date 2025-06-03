@echo off

setlocal

set /p VERSION=<VERSION

set START_DIR=%CD%
cd castoranalytics
del /q "build"
call briefcase create
call briefcase build
cd %START_DIR%

endlocal