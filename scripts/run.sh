#!/bin/bash

if [ "${1}" == "" ]; then

    cd castoranalytics
    briefcase dev

elif [ "${1}" == "--test" ]; then

    cd castoranalytics
    briefcase dev --test

elif [ "${1}" == "--exe" ]; then

    cd castoranalytics
    briefcase run
fi