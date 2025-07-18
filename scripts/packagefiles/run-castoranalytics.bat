@echo off
set /p VERSION=<src\castoranalytics\resources\VERSION
call python -m pip install -r requirements.txt
call python -m briefcase dev