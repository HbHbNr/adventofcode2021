#!/bin/bash
(ls days/day?[ab].py; ls days/day??[ab].py) | sed -E 's#(.+)/(.+).py#\1.\2#' | xargs -n1 python3 -m
