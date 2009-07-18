#!/bin/bash

set -e

outputdir=../html

# generate button image if it doesn't exist
([ -e $outputdir/butan-original.png ] && [ -e $outputdir/icon.png ]) || ./make_butan.sh

# minify javascript
cp ../src/jquery-1.3.2.min.js $outputdir/pushbutan.js
cat ../src/{plugins,pushbutan}.js | ./jsmin.py >> $outputdir/pushbutan.js

# copy source files to the output directory
cp -p \
    ../src/.htaccess \
    ../src/*.{py,cgi,html,txt,css} \
    ../images/*.{png,jpg,gif} \
    $outputdir/
