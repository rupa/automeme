#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Post an Auto-Meme string to Twitter.

Please don't spam Twitter with this.

Requires the wonderful python-twitter:

    http://code.google.com/p/python-twitter/
"""

__author__ = 'Liam Cooke <http://github.com/inky>'


import ConfigParser
import sys
from os import path
from random import randint

import twitter

import meme
from common import *


CFG_FILE = path.join(path.expanduser('~'), '.automeme')


def cred():
    cfg = ConfigParser.ConfigParser()
    cfg.read(CFG_FILE)
    u, p = None, None
    try:
        u = cfg.get('Twitter', 'username', None)
        p = cfg.get('Twitter', 'password', None)
    except ConfigParser.NoSectionError:
        sys.stderr.write("""\
%s must contain a Twitter section, with the format:

[Twitter]
username: abcd
password: wxyz
""" % CFG_FILE)

    return u, p


def get():
    meme.vocab['name'].extend((
        'Twitter',
        ))
    meme.vocab['noun'].extend((
        'tweet; ~s',
        'Twitter; ~s',
        ))
    meme.vocab['verb'].extend((
        'follow; ~s; followed; ~; following',
        'tweet about; tweets about; tweeted about; ~; tweeting about',
        ))
    meme.vocab['iverb'].extend((
        'tweet; tweets; tweeted; ~; tweeting',
        ))
    meme.vocab['adj'].extend((
        'SEO',
        'Twitter',
        ))
    crap = None
    while not crap:
        try:
            crap = reduce(lambda x, y: len(y) > len(x) and y or x,
                        filter(lambda s: len(s.encode('utf-8')) <= 140,
                                (meme.generate('twitter') for x in xrange(5)) ))
        except TypeError:
            continue
    return crap


def api():
    u, p = cred()
    if not u or not p:
        sys.stderr.write('Could not read username and password from config file\n')
        return None
    return twitter.Api(username=u, password=p)


def post():
    t = api()
    if not t:
        return

    status = t.PostUpdate(get())
    print status.text
    try:
        print 'http://twitter.com/%s/status/%d' % (status.user.screen_name, status.id)
    except (AttributeError, TypeError):
        pass


def main():
    if '--dryrun' in sys.argv or '-n' in sys.argv:
        print get()
    elif '--cron' in sys.argv and randint(1,24) != 7:
        return
    else:
        post()


if __name__ == '__main__':
    main()
