#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

# note: python parses 'coding=' above

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

from random import randint

from common import *
from patterns import patterns
from vocab import vocab as primary_vocab

CONTENT_TYPES = {'html': 'text/html', 'txt': 'text/plain', 'plain': 'text/plain'}
title = 'AUTOMEME'

def get_word(words, index):
    """Return a word from a list of words. If the word contains
    the character ~, this is replaced with the word at index-1.
    """
    v = min(index, len(words)-1)
    if '~' in words[v]:
        return words[v].replace('~', v > 0 and get_word(words, v-1) or '')
    return words[v]

def randword(category, vocab):
    """Return a random word using a specified word category or
    list of word categories. A category is denoted by one of
    the following formats:
        X       category X, variant 0
        XY      category X, variant Y
        ~Z      literal string Z
    """
    category = expand(category)

    if type(category) == list:
        if not category:
            return ''
        if len(category) > 1:
            if callable(category[-1]):
                return category[-1](randword(category[:-1], vocab))
            else:
                return randword(category[:-1], vocab)
        else:
            category = expand(category[0])

    if type(category) == tuple:
        return randword(choice(category), vocab)

    if category[0] == '~':  # literal
        return category[1:]

    var = 0
    if category[-1].isdigit():
        var = int(category[-1])
        category = category[:-1]

    vars = expand(choice(vocab[category]))
    vars = '; ' in vars and vars.split('; ') or [vars]

    return get_word(vars, var)

def a_word(word):
    """Prepend 'a' or 'an' to a word."""
    w = word.split(' ', 1)[0].lower()
    if w in ('unix', ):
        return 'a ' + word
    if w[0] in 'aeiou' or w in ('hero', 'xbox') or w.startswith('mp3'):
        return 'an ' + word
    else:
        return 'a ' + word

def generate(format='html', pattern='', vocab=None):
    if vocab == 'hipster':
        import hipster
        vocab = hipster.vocab(primary_vocab)
    else:
        vocab = primary_vocab

    p = pattern and expand(pattern) or expand(choice(patterns))

    if type(p) == str:
        p = (p,)

    # pattern may be a list of the form: [pattern, function, ...]
    elif type(p) == list:
        if not p:
            return ''
        if len(p) > 1:
            if callable(p[-1]):
                return p[-1](generate(format, p[:-1]))
            else:
                return generate(format, p[:-1])
        else:
            p = expand(p[0])

    meme = expand( p[0] )
    subs = p[1:]

    for i, s in enumerate(subs):
        word = randword(s, vocab)
        meme = meme.replace('{%s}' % (i+1), word)
        if '{%sa}' % (i+1) in meme:
            meme = meme.replace('{%sa}' % (i+1), a_word(word))

    meme = meme.upper()
    if format in ('plain', 'twitter'):
        meme = re_sub(r'(^|\W) _([^_]*)_ (\W|$)', r'\1\2\3', meme)
    if format in ('html', ):
        meme = re_sub(r'(^|\W) -- (\W|$)', r'\1&mdash;\2', meme)
        meme = re_sub(r'(^|\W) _([^_]*)_ (\W|$)', r'\1<em>\2</em>\3', meme)
        meme = re_sub(r'SNOWM[AE]N', r'&#9731;', meme)
        meme = meme.replace('...', '&#8230;')
        meme = meme.replace("'", '&rsquo;')
    return meme
