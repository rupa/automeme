//if (top !== self)
//    top.location.href = self.location.href;

function AutoMeme(tagButton, tagMeme, tagHint)
{
    var memes = new Array();
    var blocked = false;
    var first = true;

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
        tagButton.style.cursor = 'wait';
    }
    function unblock()
    {
        blocked = false;
        tagButton.style.cursor = 'pointer';
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
        req.open("GET", "moar.html?ts=" + new Date().getTime(), true);
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

        if (first) {
            tagHint.style.display = 'none';
            first = false;
        }

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
    var automeme = new AutoMeme(document.getElementById('butan'),
                                document.getElementById('meme'),
                                document.getElementById('hint'));
};
