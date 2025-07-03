#!/bin/bash
#----------------- Session 1 -----------------#
cd session1 || exit 1
for file in *.py; do
    pylint "$file"
    if [ $? -ne 0 ]; then
        echo "[🟥] Error running pylint for $file"
        exit 1
    fi
    python "$file"
    if [ $? -ne 0 ]; then
        echo "[🟥] Error running $file"
        exit 1
    fi
    echo "[🟩] $file ran successfully"
done
----------------- Session 2 -----------------#
cd ../session2 || exit 1
for file in *.py; do
    pylint "$file"
    if [ $? -ne 0 ]; then
        echo "[🟥] Error running pylint for $file"
        exit 1
    fi
    python "$file"
    if [ $? -ne 0 ]; then
        echo "[🟥] Error running $file"
        exit 1
    fi
    echo "[🟩] $file ran successfully"
done
