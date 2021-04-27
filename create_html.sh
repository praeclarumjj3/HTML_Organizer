#!/bin/sh

python test.py \
    --title "Baseline Results on PCNet-C" \
    --img_dir "demos"

rm -rf `find -type d -name __pycache__`  