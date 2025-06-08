#!/bin/bash

if [ "${1}" == "" ]; then

    echo "Usage: run.bat [--dev|--test|--exe|--pyinstaller]"
    exit 1

elif [ "${1}" == "--dev" ]; then

    cd castoranalytics
    briefcase dev

elif [ "${1}" == "--test" ]; then

    cd castoranalytics
    briefcase dev --test

elif [ "${1}" == "--exe" ]; then

    cd castoranalytics
    briefcase run

elif [ "${1}" == "--pyinstaller" ]; then

    cd castoranalytics/dist
    open -a CastorAnalytics.app

fi