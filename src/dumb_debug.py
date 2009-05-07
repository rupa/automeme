#!/usr/bin/env python
__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

import sys
import time

import meme


def dumb_debug(grep):
    memes = []
    try:
        while True:
            if not memes:
                memes = filter(lambda s: grep in s,
                               (meme.generate('txt') for x in xrange(50)))
            if memes:
                print memes.pop()
                time.sleep(1)
    except KeyboardInterrupt:
        print

if __name__ == '__main__':
    dumb_debug(' '.join(sys.argv[1:]).upper())
