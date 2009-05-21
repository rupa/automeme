#!/bin/bash

set -e

outputdir=../html

# generate button image if it doesn't exist
([ -e $outputdir/butan-original.png ] && [ -e $outputdir/icon.png ]) || ./make_butan.sh

# copy source files to the output directory
cat ../src/{jquery-1.3.2.min,plugins,pushbutan}.js > $outputdir/pushbutan.js
cp -p \
    ../src/.htaccess \
    ../src/*.{py,cgi,html,txt,css} \
    ../images/*.{png,jpg,gif} \
    $outputdir/
