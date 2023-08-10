#!/bin/bash

if [ $# -eq 0 ]; then
    pytest --cov=days --cov=util "$@" && coverage html
else
    pytest "$@"
fi
