#!/bin/bash

rm -r _build
jb build ./
ghp-import -n -p -f ./_build/html
git add .
git commit -m “$1”
git push -u origin master