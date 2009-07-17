#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Retrieve some memes and post one to Twitter.

Please don't spam Twitter with this.

Requires the wonderful python-twitter:

    http://code.google.com/p/python-twitter/

"""
import ConfigParser
import re
import sys
import urllib2

from os import path
from random import randint

import twitter


__author__ = 'Liam Cooke <http://github.com/inky>'

cfg_files = [
    path.join(path.expanduser('~'), '.automeme'),
    '../.automeme',
]

def cred():
    cfg = ConfigParser.ConfigParser()
    cfg.read(cfg_files)
    u, p = None, None
    try:
        u = cfg.get('Twitter', 'username', None)
        p = cfg.get('Twitter', 'password', None)
    except ConfigParser.NoSectionError:
        sys.stderr.write("""\
.automeme must contain a Twitter section, with the format:\n
[Twitter]
username: janedoe
password: hunter2
""")
    return u, p

def api():
    u, p = cred()
    if not u or not p:
        sys.stderr.write('Could not read username and password from config file\n')
        return None
    return twitter.Api(username=u, password=p)

def format_tweet(text):
    text = re.sub(r'(^|\W) -- (\W|$)', ur'\1\u2014\2', text)
    return text.replace('...', u'\u2026')

def len_tweet(text):
    return len(text.encode('utf-8'))

def meme():
    req = urllib2.Request('http://meme.boxofjunk.ws/moar.txt')
    try:
        response = urllib2.urlopen(req)
    except urllib2.URLError:
        print 'Could not access meme.boxofjunk.ws'
        return ''
    memes = response.read().rstrip().split('\n')
    memes = filter(lambda m: len_tweet(m) <= 140,
                   (format_tweet(m) for m in memes))
    return max(memes)

def post():
    print 'Posting to Twitter...'
    t = api()
    if not t:
        return
    tweet = meme()
    if not tweet:
        return
    status = t.PostUpdate(tweet)
    print status.text
    try:
        print 'http://twitter.com/%s/status/%d' % (status.user.screen_name, status.id)
    except (AttributeError, TypeError):
        pass

def main():
    if '--cron' in sys.argv:
        if not randint(0, 15):
            post()
        else:
            print 'Reroll!'
    elif '--poast' in sys.argv:
        post()
    else:
        text = meme()
        if text:
            print text

if __name__ == '__main__':
    main()
