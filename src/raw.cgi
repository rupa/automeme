#!/usr/bin/env python

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

def main():
    header = 'Content-type: %s; charset=UTF-8\n'
    lines = 10
    format, ctype = 'html', 'text/html'

    try:
        import meme, cgi
        args = cgi.FieldStorage()

        if args.has_key('format'):
            if args['format'].value in meme.CONTENT_TYPES.keys():
                format = args['format'].value
                ctype = meme.CONTENT_TYPES[format]
    except:
        print header % ctype
        print 'SOMEONE DIVIDED BY ZERO. OH SH-'
        return

    print header % ctype

    try:
        if args.has_key('lines'):
            if args['lines'].value.isdigit():
                lines = min(20, int(args['lines'].value)) or lines

        memes = (meme.generate(format) for x in xrange(lines))
        print '\n'.join(memes)
    except:
        print 'DIVIDE BY ZERO ERROR'
        return

if __name__ == '__main__':
    main()
