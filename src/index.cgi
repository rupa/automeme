#!/usr/bin/env python

"""HTML output wrapper module for meme.py"""

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

if __name__ == '__main__':
    output = ''

    try:
        import meme, time
        t = time.time()
        output = meme.html()
        output += '<!-- %s s -->' % (time.time()-t)
    except:
        output = "HTTP/1.0 500 Internal Server Error\n"

    print output
