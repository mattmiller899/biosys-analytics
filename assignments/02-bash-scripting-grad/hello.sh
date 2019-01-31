#!/bin/bash

if [[ $# -gt 2 ]] || [[ $# -eq 0 ]]; then
    echo "Usage: hello.sh GREETING [NAME]"
    exit 1
elif [[ $# -eq 1 ]]; then
    NAME="Human"
    GREETING=$1
else
    NAME=$2
    GREETING=$1
fi

echo "${GREETING}, ${NAME}!"
