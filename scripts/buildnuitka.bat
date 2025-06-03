@echo off

setlocal

cd castoranalytics\src

del /q "..\build-nuitka"

nuitka ^
    --standalone ^
    --enable-plugin=pyside6 ^
    --include-qt-plugins=all ^
    --include-data-dir=castoranalytics/resources=castoranalytics/resources ^
    --windows-console-mode=disable ^
    --output-dir=..\build-nuitka ^
    --output-filename=CastorAnalytics ^
    castoranalytics\__main__.py

endlocal