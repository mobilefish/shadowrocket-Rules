#!/bin/bash

git pull


python ./scripts/build-ad.py
python ./scripts/build-netease.py
python ./scripts/build-node.py
python ./scripts/build-sgmodule.py

git add .
git commit -m "manual update" -a
git push
