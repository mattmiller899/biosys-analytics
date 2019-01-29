#!/bin/bash

if [[ $# -eq 0 ]]; then
    echo "Usage: cat-n.sh FILE_PATH"
    exit 1
fi

FILE=$1

if [[ ! -f "$FILE" ]]; then
    echo "$FILE is not a file"
    exit 1
fi

COUNT=1
while read -r LINE; do
    echo "$COUNT $LINE"
    COUNT=$((COUNT + 1))
done < $FILE
