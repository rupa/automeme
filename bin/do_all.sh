#!/bin/bash

# exit on error
set -e

outputdir=../html
server=boxofjunk
uploadto=domains/meme.boxofjunk.ws/html

[ "$1" = "--clean" ] && rm -rfv $outputdir && mkdir $outputdir

# update the output directory
./update.sh

# upload it
chmod 711 $outputdir
rsync -Pcav --del --rsh=ssh $outputdir/ $server:$uploadto/
