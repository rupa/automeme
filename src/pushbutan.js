// frame killer
//if (top !== self)
//    top.location.href = self.location.href;

var tumblr_quote_quote = 'CLICK FACE, RECEIVE MEME';
var tumblr_quote_source = '<a href="http://automeme.net/">Automeme</a>';

function AutoMeme(tagButton, tagMeme)
{
    var memes = new Array(),
        blocked = false,
        max = 10,
        tumblrButton = null,
        revealTimeout = null,
        easter_eggs = [ 'awesome',
                        'brains',
                        'cardcrusher',
                        'datass',
                        'eyebrow',
                        'hurrrr',
                        'katara',
                        'milkips',
                        'puddi',
                        'toast',
                        'weegee' ];

    unblock();

    function makeHttpObject()
    {
        try { return new XMLHttpRequest(); }
        catch (error) { }
        try { return new ActiveXObject("Msxml2.XMLHTTP"); }
        catch (error) { }
        try { return new ActiveXObject("Microsoft.XMLHTTP"); }
        catch (error) { }

        blocked = true;
        tagMeme.innerHTML = 'Your browser sucks.';
        tagButton.style.cursor = 'not-allowed';
        return null;
    }

    function block()
    {
        blocked = true;
    }
    function unblock()
    {
        blocked = false;
    }

    function queue(items)
    {
        for (var i = 0; i < items.length; i++) {
            m = items[i];
            if (m && m.charAt(0) != '\n' && m.charAt(0) != '\r')
                memes.push(m);
        }
    }

    function pop()
    {
        if (memes.length > 0) {
            var m = memes.shift();
            tagMeme.innerHTML = m;
            tumblr_quote_quote = m;
            tumblrButton.setAttribute("href", "http://www.tumblr.com/share/quote?quote=" + encodeURIComponent(tumblr_quote_quote) + "&source=" + encodeURIComponent(tumblr_quote_source));
        }
    }

    function fetch(callback)
    {
        var req = makeHttpObject();
        if (!req) { return; }

        var recd = false;
        $('#loading span').fadeIn('fast');
        req.open("GET", "http://api.automeme.net/html?lines="+max+"&ts="+new Date().getTime(), true);
        if (max < 40) max += max;
        req.send(null);
        req.onreadystatechange = function()
        {
            if (recd) return;
            if (req.status == 200) {
                lines = req.responseText.split('\n');
                if (lines.length < 5) return;
                recd = true;
                queue(lines);
                pop();
            } else {
                tagMeme.innerHTML = 'Try again :(';
            }
            $('#loading span').fadeOut('fast');
            unblock();
            if (typeof callback != 'undefined') callback();
        }
    }

    function meme(callback)
    {
        if (blocked) return;
        block();

        if (memes.length > 0) {
            pop();
            setTimeout(function() {
                unblock();
            }, 250);
            if (typeof callback != 'undefined') callback();
        } else {
            fetch(callback);
        }
    }

    function randomButton()
    {
        var egg = easter_eggs[Math.floor(Math.random() * easter_eggs.length)];
        $(tagButton).css('background-image', 'url(/butan-' + egg + '.png)');
    }

    tumblrButton = document.createElement("a");
    tumblrButton.setAttribute("href", "http://www.tumblr.com/share/quote?quote=" + encodeURIComponent(tumblr_quote_quote) + "&source=" + encodeURIComponent(tumblr_quote_source));
    tumblrButton.setAttribute("title", "Share on Tumblr");
    tumblrButton.setAttribute("style", "display:inline-block; text-indent:-9999px; overflow:hidden; width:81px; height:20px; background:url('http://platform.tumblr.com/v1/share_1T.png') top left no-repeat transparent;");
    tumblrButton.innerHTML = "Share on Tumblr";
    document.getElementById("tumblr_button_abc123").appendChild(tumblrButton);

    tagButton.onclick = meme;
    $('body').upUpDownDown({
        watchFor: [38,38,40,40,37,39,37,39,66,65],
        callback: function() {
            randomButton();
            $(tagButton).addClass('reveal');
            revealTimeout = setTimeout(function() {
                $(tagButton).removeClass('reveal');
            }, 500);
        }
    });

    var halp = false;
    var toggleHalp = function() {
        (halp)
            ? $('#halp').slideUp('normal')
            : $('#halp').slideDown('normal');
        halp = !halp;
    };
    var clickHalp = function(e) {
        e.preventDefault();
        toggleHalp();
    }
    $('<span><a href="#" id="wut">wut?</a> &middot;&nbsp;</span>').prependTo($('#footer-nav'));
    $('#wut').click(clickHalp);
    $('<p><a id="dismiss" href="#">okay</a></p>').appendTo($('#halp'));
    $('#dismiss').click(clickHalp);

    window.onkeypress = function(e) {
        if (e.which == 32) {
            meme();
            if (halp) {
                $('#halp').slideUp('normal');
                halp = false;
            }
        } else if (e.which == 27 && halp) {  // Esc
            $('#halp').slideUp('normal');
            halp = false;
        } else if (e.which == 63) {  // ?
            toggleHalp();
        }
    };

    if (/mobile.*safari/.test(navigator.userAgent.toLowerCase())) {
        document.title = 'Automeme';
    }
}

$(document).ready(function() {
    $('#halp').hide().css({'z-index':'9001','visibility':'visible'});
    $('#loading span').hide().css({'visibility':'visible'});

    var automeme = new AutoMeme(document.getElementById('butan'),
                                document.getElementById('meme'));

});
