#!/bin/bash

DIR="$PWD/../../data/gapminder/"
FILE_LIST="$PWD/file_list"
if [[ $# -eq 0 ]]; then
    ls $DIR | sort > $FILE_LIST
elif [[ $# -eq 1 ]]; then
    ls $DIR | grep -ie "^$1" | sort > $FILE_LIST
fi

COUNT=1
LC=$(wc -l $FILE_LIST | awk '{print $1}')
if [[ $LC -eq 0 ]]; then
    echo "There are no countries starting with \"$1\""
else
    while read -r LINE; do
        echo "$COUNT $(basename $LINE .cc.txt)"
        COUNT=$((COUNT + 1))
    done < $FILE_LIST
fi
