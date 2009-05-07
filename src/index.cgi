#!/usr/bin/env python

"""HTML output wrapper module for meme.py"""

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

if __name__ == '__main__':
    output = ''

    try:
        import cgi
        import meme, time
        t = time.time()

        args = cgi.FieldStorage()
        eegg = args.has_key('imhotep') and args['imhotep'].value == 'invisible'

        output = meme.html(eegg)
        output += '<!-- %.5f s -->' % (time.time()-t)
    except:
        output = "HTTP/1.0 500 Internal Server Error\n"

    print output
