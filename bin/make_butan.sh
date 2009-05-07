#!/bin/bash

set -e

outputdir=../html
mkdir -p $outputdir

# make :awesome: button
convert ../images/awesome.png \
    -bordercolor transparent -border 20x20 \
    -resize 300 \
    /tmp/b1.png
convert ../images/awesome.png \
    -bordercolor transparent -border 4x4 \
    -swirl 25 \
    -resize 300 \
    /tmp/b2.png
convert /tmp/b{1,2}.png \
    -append -resize 150 \
    $outputdir/butan.png

# bonus buttons
convert ../images/awesome-katara.png \
    -bordercolor transparent -border 20x20 \
    -resize 300 \
    /tmp/katara.png
convert /tmp/{b1,katara}.png \
    -append -resize 150 \
    $outputdir/butan-katara.png

# icons (favicon, iphone, etc)
cp -p /tmp/b1.png $outputdir/icon.png
convert $outputdir/icon.png \
    -resize 32x32 \
    $outputdir/icon32.png
