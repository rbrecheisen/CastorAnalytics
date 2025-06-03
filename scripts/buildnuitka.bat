@echo off

setlocal

cd castoranalytics\src

nuitka ^
    --standalone ^
    --enable-plugin=pyside6 ^
    --include-qt-plugins=all ^
    --include-data-dir=castoranalytics/resources=my_app/resources ^
    --windows-disable-console ^
    --output-dir=..\build\nuitka ^
    castoranalytics\__main__.py

endlocal