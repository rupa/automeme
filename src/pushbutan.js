if (top !== self)
    top.location.href = self.location.href;

function AutoMeme(tagButton, tagMeme)
{
    var memes = new Array();
    var blocked = false;

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
        req.open("GET", "moar.html?lines=20&ts=" + new Date().getTime(), true);
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
}

window.onload = function()
{
    var halp = false;
    var toggle = function(e) {
        e.preventDefault();
        (halp)
            ? $('#halp').slideUp('normal')
            : $('#halp').slideDown('normal');
        halp = !halp;
    };
    $('#wut').click(toggle);
    $('#dismiss').click(toggle);
    $('#halp').hide().css({'z-index':'9001','visibility':'visible'});

    var automeme = new AutoMeme(document.getElementById('butan'),
                                document.getElementById('meme'));
};
