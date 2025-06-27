#!/bin/bash
hdiutil create -volname "MyPySide6App Installer" \
    -srcfolder dist/MyPySide6App.app \
    -ov -format UDZO dist/MyPySide6App.dmg