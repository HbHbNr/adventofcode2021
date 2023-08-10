#!/bin/bash

if [ $# -eq 0 ]; then
    FILES='.'
else
    FILES="$@"
fi

mypy $FILES
