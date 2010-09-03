# vim: set fileencoding=utf-8 :

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

footer = ["""\
<p id="footer-links"><a href="/goodies.html">Goodies</a>
    &middot; <a href="http://moar.automeme.net/zing/">Zing</a>
    &middot; <a href="http://api.automeme.net/">API</a>
    &middot; <a href="http://blog.automeme.net/">Blog</a>
    &middot; <a href="http://twitter.com/automeme">Twitter</a>
    &nbsp; <a href="http://twitter.com/share" class="twitter-share-button" data-url="http://automeme.net/" data-count="horizontal" data-via="automeme" data-related="inky">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
</p>
<div id="sellout">
<script type="text/javascript"><!--
google_ad_client = "pub-6989159164128459";
google_ad_slot = "0822990148";
google_ad_width = 468;
google_ad_height = 60;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
</div>\
"""]


easter_eggs = ('awesome',
               'brains',
               'cardcrusher',
               'datass',
               'eyebrow',
               'hurrrr',
               'katara',
               'milkips',
               'toast',
               'weegee',
               'original')


html_template = u"""\
Content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head profile="http://www.w3.org/2005/10/profile">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<title>%s</title>
<meta name="description" content="The automatic meme generator: random nonsense on demand. Inspired by Mad Libs, snowclones, internet memes and the utter insanity of 4chan. Not safe for work."/>
<meta name="keywords" content="meme generator random nonsense 4chan lulz snowclone madlibs python"/>
<link rel="stylesheet" type="text/css" media="all" href="/main.css?201008121"/>
<link rel="stylesheet" type="text/css" media="only screen and (max-device-width: 480px)" href="iphone.css?20091227g"/>
<link rel="icon" type="image/png" href="/icon32.png"/>
<link rel="alternate" type="application/rss+xml" title="RSS" href="http://feeds2.feedburner.com/automeme"/>
<meta name="apple-mobile-web-app-capable" content="yes"/>
<meta name="viewport" content="width=800"/>
<meta name="google-site-verification" content="f7s5eHOpjbljxe0cEz_etlYwVNModKW78OFvAKyD4os"/>
<meta name="og:image" content="http://automeme.net/icon.png"/>
<meta name="google-site-verification" content="7ufvqs-G5eultBdcDfwdRVHs6gtoJvjciGIp5YFNUlQ"/>
%s</head>
<body>
<div id="halp">
 <!-- google_ad_section_start -->
 <h1>INTERNET LULZ MACHINE</h1>
 <p>Auto-Meme is an automated <i>meme generator</i>, churning out random nonsense on demand. Inspired by
    <a href="http://en.wikipedia.org/wiki/Mad_Libs">Mad Libs</a>,
    <a href="http://en.wikipedia.org/wiki/Snowclone">snowclones</a>,
    <a href="http://en.wikipedia.org/wiki/Internet_meme">internet memes</a>
    and the utter insanity of
    <a href="http://en.wikipedia.org/wiki/4chan">4chan</a>.
    Click the face or hit the spacebar for more.
    <span class="warning">Not safe for work.</span></p>
 <!-- google_ad_section_end -->
 <p>The <img src="/awesome.gif" alt=":razz:" title=":razz:"/> smiley originates from <a
    href="http://forums.somethingawful.com/misc.php?action=showsmilies">Something
    Awful</a>.</p>
</div>
<div id="body">
 <div id="meme-w1"><div id="meme-w2">
  <!-- google_ad_section_start(weight=ignore) -->
  <div>
    <p id="meme">Click face, receive meme</p>
    <span class="arrow"></span>
  </div>
  <!-- google_ad_section_end -->
 </div></div>
 <div id="push">
  <div id="butan">&nbsp;</div>
  <div id="loading"><span>&nbsp;</span></div>
 </div>
 <script type="text/javascript" src="/pushbutan.js?201008212"></script>
 <div id="footer-wrap"><div id="footer">%s</div></div>
</div>
</body></html>"""
