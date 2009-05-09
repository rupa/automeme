#!/usr/bin/env python
__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

import sys
import time

import meme


def dumb_debug(grep):
    memes = []
    lines = 20
    try:
        while True:
            if memes:
                print memes.pop()
                time.sleep(1)
            else:
                memes = filter(lambda s: grep in s,
                               (meme.generate('txt') for x in xrange(lines)))
                if lines < 1000:
                    lines += lines
    except KeyboardInterrupt:
        print

if __name__ == '__main__':
    dumb_debug(' '.join(sys.argv[1:]).upper())
