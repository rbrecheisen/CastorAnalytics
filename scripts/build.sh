#!/bin/bash

if [ "${1}" == "" ]; then

    echo "Usage: build.sh [--briefcase|--pyinstaller]"
    exit 1

elif [ "${1}" == "--briefcase" ]; then

    cd castoranalytics
    rm -rf build
    briefcase create
    briefcase build

elif [ "${1}" == "--pyinstaller" ]; then

    cd castoranalytics
    rm -rf dist
    pyinstaller \
        --windowed \
        --name "CastorAnalytics" \
        --add-data "src/castoranalytics/resources:castoranalytics/resources" \
        src/app.py

fi
