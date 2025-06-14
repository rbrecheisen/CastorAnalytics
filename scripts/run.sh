#!/bin/bash

VERSION=$(cat castoranalytics/src/castoranalytics/resources/VERSION)

if [ "${1}" == "" ]; then

    cd castoranalytics
    briefcase dev

elif [ "${1}" == "--test" ]; then

    cd castoranalytics
    briefcase dev --test

elif [ "${1}" == "--exe" ]; then

    cd castoranalytics
    briefcase run

elif [ "${1}" == "--build" ]; then

    rm -rf castoranalytics/build
    python scripts/python/updatetomlversion.py ${VERSION}
    python scripts/python/updatetomlrequirements.py
    cd castoranalytics
    briefcase create
    briefcase build

elif [ "${1}" == "--package" ]; then

    cd castoranalytics
    briefcase package --adhoc-sign
fi