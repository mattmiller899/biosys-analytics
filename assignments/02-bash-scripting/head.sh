#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Usage: head.sh FILE [NUM]"
    exit 1
fi

FILE=$1

if [[ ! -f "$FILE" ]]; then
    echo "$FILE is not a file"
    exit 1
fi

if [[ $# -eq 2 ]]; then
    NUM=$2
else
    NUM=3
fi

COUNT=0
while read -r LINE; do
    if [[ $COUNT -eq $NUM ]]; then
        break
    fi
    echo "$LINE"
    COUNT=$((COUNT + 1))
done < $FILE
