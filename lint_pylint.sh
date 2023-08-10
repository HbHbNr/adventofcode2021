#!/bin/bash

if [ $# -eq 0 ]; then
    FILES='**/*.py'
else
    FILES="$@"
fi

echo "Check for errors with pylint..."
pylint --errors-only $FILES
if [ $? -ne 0 ]; then
    exit 1
fi

echo "Check syntax with pylint..."
pylint --disable=C,R $FILES
if [ $? -ne 0 ]; then
    exit 1
fi

echo "Check conventions with pylint..."
pylint $FILES
