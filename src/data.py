# vim: set fileencoding=utf-8 :

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

footer = []
footer.append('<p>%s</p>' % '\n&middot; '.join((
    '<a href="http://automeme.tumblr.com/">Blog</a>',
    '<a href="api.html">API</a>',
    '<a href="http://mongs.tumblr.com/">Tumblr</a>',
    '<a href="http://twitter.com/automeme">Twitter</a>',
    '<a href="http://github.com/inky/automeme/tree/master">Source</a>',
    )) )
footer.append("""
<div id="sellout">
<script type="text/javascript"><!--
google_ad_client = "pub-6989159164128459";
google_ad_slot = "8356229727";
google_ad_width = 728;
google_ad_height = 90;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
</div>
""".strip())

css = """
html { font-size: 100.01%; text-transform: uppercase; }
body { background: #fff; font: 1em/1 'Helvetica Neue', 'DejaVu Sans', 'Helvetica', sans-serif; }
div,p,body { margin:0; padding:0; }
a { color: #888; text-decoration:none; }
a:hover { color: #C00 !important; text-decoration:underline; }
a,img { border: none !important; }
#body { padding-top: 50px; }
#meme-w1 { width: 100%; float: right; color: #C00; margin-left: -250px; }
#meme-w2 { margin-left: 250px; font-weight: bold; }
#meme-w2 div { background: #eed; font-size: 3em; letter-spacing: -0.05em; position: relative;
               word-spacing: 0.1em; margin: 0 40px 0 0; padding: 0.3em 0.4em 0.4em;
               -moz-border-radius: 0.25em; -webkit-border-radius: 0.25em; float: left; }
#meme-w2 .arrow { width:0; height:0; line-height:0; position:absolute;
                  border-right:35px solid #eed; border-top:0.5em solid #fff;
                  border-bottom:0.1em solid #fff; bottom:0.5em; left:-34px; }

#push { width: 250px; float: left; }
#butan { width: 150px; height: 0; padding-top: 150px; margin: 80px 0 20px 50px;
         overflow: hidden; background: url(butan.png) 0 1px no-repeat; }
#butan:hover { background-position: 0 -150px; }
#hint { text-align: center; color: #888; font-size: 0.8em; line-height: 1.25; }
#hint p { margin-bottom: 0.25em; }
#footer { color: #888; clear: both; overflow: visible; text-align: center;
          font-size: 0.8em; width: 728px; margin: 2em auto 0; padding-top: 12px; }
#footer p { text-align: center; margin: 0.75em; }
#sellout { padding-top: 2em; }
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
<div id="meme-w1"><div id="meme-w2"><div><p id="meme">
%s
</p><span class="arrow"/></div></div></div>
<div id="push">
<div id="butan">&nbsp;</div>
<div id="hint"><p><img src="click.png" alt=""/></p><p>push butan<br/>receive meme</p></div>
</div>
<div id="footer">%s</div>
</div></body></html>
""".strip()
