#!/usr/bin/env python
"""
This code is an absolute mess.
"""

import cgi
import re
import sys

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

def main():
    header = 'Content-type: %s; charset=utf-8\n'
    lines = 10
    format, ctype = 'html', 'text/html'

    try:
        import meme

        ref = cgi.os.environ.get('HTTP_REFERER', '')
        if not re.match('^http://meme.boxofjunk.ws/pc', ref):
            meme.use_nsfw()

        args = cgi.FieldStorage()
        if args.has_key('format'):
            if args['format'].value in meme.CONTENT_TYPES.keys():
                format = args['format'].value
                ctype = meme.CONTENT_TYPES[format]
        if args.has_key('json') and args['json'].value:
            try:
                import json  # python-json
                ctype = 'application/json'
            except ImportError:
                pass
    except Exception, err:
        print header % ctype
        print 'SOMEONE DIVIDED BY ZERO. OH SH-'
        sys.stderr.write('Error: %s\n' % str(err))
        return

    print header % ctype

    try:
        if args.has_key('lines'):
            if args['lines'].value.isdigit():
                lines = min(80, int(args['lines'].value)) or lines

        memes = (meme.generate(format) for x in xrange(lines))
        if ctype.endswith('json'):
            print json.write(tuple(memes))
        else:
            print '\n'.join(memes)
    except:
        print 'DIVIDE BY ZERO ERROR'
        return

if __name__ == '__main__':
    main()
