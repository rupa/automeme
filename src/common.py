__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

from random import randint
import re, sys

USER_AGENT = 'Auto-Meme/9000 +http://meme.boxofjunk.ws/'

# random element from list/tuple/string
randel = lambda x: x[randint(0, len(x)-1)]

# if v is a function, call and replace it with its return value
expand = lambda v: (callable(v) and [v()] or [v])[0]

# regular expression (s)earch & (r)eplace
re_sub = lambda p, r, s: re.compile(p, re.U|re.VERBOSE).sub(r, s)
re_isub = lambda p, r, s: re.compile(p, re.U|re.I|re.VERBOSE).sub(r, s)
