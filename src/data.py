# vim: set fileencoding=utf-8 :

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

footer = []
footer.append('<p>Read the <a href="http://automeme.tumblr.com/">Blog</a> '
              'for updates and crap')
footer.append('<p>Comments? Suggestions? Email: <em>meme</em> at '
              '<em>boxofjunk.ws</em></p>')

css = """
html { font-size: 100.01%; text-transform: uppercase; }
body { background: #fff; font: 1em/1 'DejaVu Sans', Helvetica, sans-serif; }
div,p,body { margin:0; padding:0; }
a { color: #666; }
a:hover { color: #C00 !important; }
a,img { border: none !important; }
#body { padding-top: 50px; }
#meme-w1 { width: 100%; float: right; color: #C00; margin-left: -250px; }
#meme-w2 { margin-left: 250px; font-weight: bold; }
#meme { background: #eed; font-size: 3em; letter-spacing: -0.05em;
        word-spacing: 0.1em; margin: 0 40px 0 0; padding: 0.3em 0.4em 0.4em;
        -moz-border-radius: 0.25em; -webkit-border-radius: 0.25em; }

#push { width: 250px; height: 350px; float: left; }
#butan { width: 150px; height: 0; padding-top: 150px; margin: 80px 0 0 50px;
         overflow: hidden; background: url(butan.png) 0 0 no-repeat; }
#butan:hover { background-position: 0 -150px; }
#footer { color: #888; clear: both; overflow: visible; text-align: center;
          font-size: 0.7em; width: 728px; margin: 0 auto; padding-top: 12px; }
#footer p { text-align: center; margin: 0.75em; }
#donate { padding: 0.5em 0; }
#donate img { display: none; }
.hide { display: none; }
""".replace('\n\n','\n').strip()

html_template = u"""
Content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://www.w3.org/2005/10/profile">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>%s</title>
<meta name="description" content="FOR GREAT JUSTICE"/>
<link rel="icon" type="image/png" href="/icon32.png"/>
<link rel="apple-touch-icon" href="/icon.png"/>
<meta name="viewport" content="width=800"/>
<style type="text/css">%s</style>
<script type="text/javascript" src="pushbutan.js"></script>
<meta name="microid" content="mailto+http:sha1:76913cf666bba15787e5936fb332bb8779bffe5e"/>
<link rel="alternate" type="application/rss+xml" title="RSS" href="http://mongs.tumblr.com/rss"/>
</head><body><div id="body">
<div id="meme-w1"><div id="meme-w2"><p id="meme">
%s
</p></div></div>
<div id="push"><div id="butan">&nbsp;</div></div>
<div id="footer">%s</div>
</div></body></html>
""".strip()
