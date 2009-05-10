if (top !== self)
    top.location.href = self.location.href;

function AutoMeme(tagButton, tagMeme)
{
    var memes = new Array();
    var blocked = false;
    var max = 10;

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
        if (memes.length > 0)
            tagMeme.innerHTML = memes.shift();
    }

    function fetch()
    {
        var req = makeHttpObject();
        if (!req) { return; }

        var recd = false;
        $('#loading span').fadeIn('fast');
        req.open("GET", "moar.html?lines="+max+"&ts="+new Date().getTime(), true);
        if (max < 80) max += max;
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
        }
    }

    function meme()
    {
        if (blocked) return;
        block();

        if (memes.length > 0) {
            pop();
            setTimeout(function(){unblock();}, 250);
        } else {
            fetch();
        }
    }

    tagButton.onclick = function() { meme(); };
    $('body').keypress(function(e) {
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
    $('#wut').click(clickHalp);
    $('#dismiss').click(clickHalp);

    window.onkeypress = function(e) {
        if (e.which == 32) {
            meme();
        } else if (e.which == 27 && halp) {  // Esc
            $('#halp').slideUp('normal');
            halp = false;
        } else if (e.which == 63) {  // ?
            toggleHalp();
        }
    };
}

window.onload = function()
{
    $('#halp').hide().css({'z-index':'9001','visibility':'visible'});
    $('#loading span').hide().css({'visibility':'visible'});

    var automeme = new AutoMeme(document.getElementById('butan'),
                                document.getElementById('meme'));
};
