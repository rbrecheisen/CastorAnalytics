@echo off

setlocal

rmdir /s /q castoranalytics\build-nuitka

cd castoranalytics\src

nuitka ^
    --standalone ^
    --enable-plugin=pyside6 ^
    --include-qt-plugins=all ^
    --include-data-dir=castoranalytics/resources=castoranalytics/resources ^
    --windows-console-mode=disable ^
    --output-dir=..\build-nuitka ^
    --output-filename=CastorAnalytics ^
    app.py

endlocal