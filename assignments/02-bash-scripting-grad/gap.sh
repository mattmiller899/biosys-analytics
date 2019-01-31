#!/bin/bash

DIR="$PWD/../../data/gapminder/"
FILE_LIST="$PWD/file_list"
ls $DIR | sort > $FILE_LIST

COUNT=1
if [[ $# -eq 0 ]]; then
    while read -r LINE; do
        echo "$COUNT $(basename $LINE .cc.txt)"
        COUNT=$((COUNT + 1))
    done < $FILE_LIST
else
    while read -r LINE; do
        basename $LINE .cc.txt
    done < $FILE_LIST
fi
