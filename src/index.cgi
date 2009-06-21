#!/usr/bin/env python

"""HTML output wrapper module for meme.py"""

import cgi
import sys
import time

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

if __name__ == '__main__':
    output = ''

    try:
        import meme

        t = time.time()
        args = cgi.FieldStorage()
        egg = args.has_key('imhotep') and args['imhotep'].value == 'invisible'
        if not egg and args.has_key('butan'):
            egg = args['butan'].value

        output = meme.html(egg)
        output += '<!-- %.5f s -->' % (time.time()-t)
    except Exception, err:
        output = "HTTP/1.0 500 Internal Server Error\n"
        sys.stderr.write('Error: %s\n' % str(err))

    print output
