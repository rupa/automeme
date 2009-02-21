#!/bin/bash

set -e

outputdir=../html
mkdir -p $outputdir

# Generate button
convert ../images/awesome.png \
    -bordercolor transparent -border 16x16 -resize 336 \
    /tmp/b1.png
convert ../images/awesome.png \
    -swirl 25 \
    /tmp/b2.png
convert /tmp/b{1,2}.png \
    -append -resize 150 \
    $outputdir/butan.png

# icons (favicon, iphone, etc)
cp -p /tmp/b1.png $outputdir/icon.png
convert $outputdir/icon.png \
    -resize 32x32 \
    $outputdir/icon32.png
