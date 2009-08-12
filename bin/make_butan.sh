#!/bin/bash

set -e

outputdir=../html
mkdir -p $outputdir


# make :awesome: button

convert ../images/awesome.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/b1.png
convert ../images/awesome.png \
    -swirl 25 \
    -resize 150 \
    /tmp/b2.png
convert /tmp/b{1,2}.png \
    -append $outputdir/butan-original.png


# bonus buttons

convert ../images/awesome.gif \
    -filter box -resize 150 \
    /tmp/emot.png
convert ../images/awesome-datass.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/datass.png
convert ../images/awesome-eyebrow.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/eyebrow.png
convert ../images/awesome-hurrrr.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/hurrrr.png
convert ../images/awesome-katara.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/katara.png
convert ../images/awesome-weegee.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/weegee.png

convert /tmp/{b1,emot}.png \
    -append $outputdir/butan-awesome.png
convert /tmp/{b1,datass}.png \
    -append $outputdir/butan-datass.png
convert /tmp/{b1,eyebrow}.png \
    -append $outputdir/butan-eyebrow.png
convert /tmp/{b1,hurrrr}.png \
    -append $outputdir/butan-hurrrr.png
convert /tmp/{b1,katara}.png \
    -append $outputdir/butan-katara.png
convert /tmp/{b1,weegee}.png \
    -append $outputdir/butan-weegee.png

convert ../images/milkips.png \
    -bordercolor transparent -border 10x10 \
    -resize 150 \
    /tmp/milkips1.png
convert ../images/milkips.png \
    -swirl -50 \
    -resize 150 \
    /tmp/milkips2.png
convert /tmp/milkips{1,2}.png \
    -append $outputdir/butan-milkips.png


# icons (favicon, iphone, etc)

cp -p /tmp/b1.png $outputdir/icon.png
convert $outputdir/icon.png \
    -resize 32x32 \
    $outputdir/icon32.png
