#!/usr/bin/env bash

files=( "wallger/__init__.py" "wallger/__main__.py" "wallger/helpers.py" "wallger/run.py" "wallger/version.py" "wallger/providers/__init__.py" "wallger/providers/local.py" "wallger/providers/provider.py" "wallger/providers/unsplash.py" "wallger/providers/wallhaven.py")
for i in "${files[@]}"
do
  :
  pycodestyle --show-source --show-pep8 --format=default "$i"
done
