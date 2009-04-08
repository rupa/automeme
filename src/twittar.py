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

    crap = None
    while not crap:
        crap = randel(tuple(filter(lambda s: len(s.encode('utf-8')) <= 140,
            (meme.generate('twitter') for x in xrange(10)) )))

    status = t.PostUpdate(crap)
    print status.text
    try:
        print 'http://twitter.com/%s/status/%d' % (status.user.screen_name, status.id)
    except (AttributeError, TypeError):
        pass


def main():
    if '--cron' in sys.argv and randint(1,24) != 7:
        return
    post()


if __name__ == '__main__':
    main()
