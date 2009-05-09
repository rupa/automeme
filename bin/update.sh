#!/bin/bash

set -e

outputdir=../html

# generate button image if it doesn't exist
([ -e $outputdir/butan.png ] && [ -e $outputdir/icon.png ]) || ./make_butan.sh

# copy source files to the output directory
cp -p \
    ../src/.htaccess \
    ../src/*.{py,cgi,html,js,txt,css} \
    ../images/{tumblr_background.jpg,click.png,{awesome,loading}.gif} \
    $outputdir/
