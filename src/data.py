# vim: set fileencoding=utf-8 :

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

footer = []
footer.append('<p>%s</p>' % '\n&nbsp;&middot;&nbsp; '.join((
    '<a href="#" id="wut">wut?</a>',
    '<a href="http://automeme.tumblr.com/">Blog</a>',
    '<a href="api.html">API</a>',
    '<a href="http://mongs.tumblr.com/">Tumblr</a>',
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


easter_eggs = ('awesome', 'datass', 'eyebrow', 'hurrrr', 'katara', 'milkips',
               'original')


html_template = u"""\
Content-type: text/html; charset=UTF-8
X-Meme: %s

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://www.w3.org/2005/10/profile">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>%s &bull; push button, receive lulz</title>
<meta name="description" content="One very cheeky random nonsense generator. Inspired by the utter insanity of 4chan, and internet memes in general."/>
<meta name="keywords" content="meme random nonsense generator 4chan lulz snowclone python"/>
<link rel="stylesheet" type="text/css" href="screen.css?20090509"/>
<link rel="icon" type="image/png" href="icon32.png"/>
<link rel="apple-touch-icon" href="icon.png"/>
<meta name="viewport" content="width=800"/>
<link rel="alternate" type="application/rss+xml" title="RSS" href="http://feeds2.feedburner.com/automeme"/>
%s</head>
<body>
<div id="halp">
 <h1>INTERNET MEME MACHINE</h1>
 <!-- google_ad_section_start -->
 <p>AUTO-MEME is a random nonsense generator, inspired by
    <a href="http://en.wikipedia.org/wiki/Mad_Libs">Mad Libs</a>,
    <a href="http://en.wikipedia.org/wiki/Snowclone">snowclones</a>,
    and the utterly insane world of
    <a href="http://en.wikipedia.org/wiki/Internet_meme">internet memes</a>.
    <span class="warning">Not safe for work.</span>
 </p>
 <p><img src="awesome.gif" alt=":razz:" title=":razz:"/> originates from <a
    href="http://forums.somethingawful.com/misc.php?action=showsmilies">Something
    Awful</a>.</p>
 <!-- google_ad_section_end -->
 <p><a id="dismiss" href="#">okay</a></p>
</div>
<div id="body">
 <div id="meme-w1"><div id="meme-w2">
   <!-- google_ad_section_start(weight=ignore) -->
   <div> <p id="meme">%s</p> <span class="arrow"></span> </div>
   <!-- google_ad_section_end -->
 </div></div>
 <div id="push">
  <div id="butan">&nbsp;</div>
  <div id="loading"><span>&nbsp;</span></div>
 </div>
 <div id="footer">%s</div>
</div>
<script type="text/javascript" src="jquery-1.3.2.min.js"></script>
<script type="text/javascript" src="pushbutan.js?20090509"></script>
</body></html>"""
