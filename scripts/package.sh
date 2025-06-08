#!/bin/bash

VERSION=$(cat castoranalytics/src/castoranalytics/resources/VERSION)

python scripts/python/updatetomlversion.py ${VERSION}

cd castoranalytics
briefcase package --adhoc-sign