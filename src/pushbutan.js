//if (top !== self)
//    top.location.href = self.location.href;

function Zalgo()
{
    // ----- modified from http://github.com/Marak/zalgo.js -----
    var up = [
    '̍','̎','̄','̅',
    '̿','̑','̆','̐',
    '͒','͗','͑','̇',
    '̈','̊','͂','̓',
    '̈','͊','͋','͌',
    '̃','̂','̌','͐',
    '̀','́','̋','̏',
    '̒','̓','̔','̽',
    '̉','ͣ','ͤ','ͥ',
    'ͦ','ͧ','ͨ','ͩ',
    'ͪ','ͫ','ͬ','ͭ',
    'ͮ','ͯ','̾','͛',
    '͆','̚'
    ];

    var down = [
          '̖','̗','̘','̙',
          '̜','̝','̞','̟',
          '̠','̤','̥','̦',
          '̩','̪','̫','̬',
          '̭','̮','̯','̰',
          '̱','̲','̳','̹',
          '̺','̻','̼','ͅ',
          '͇','͈','͉','͍',
          '͎','͓','͔','͕',
          '͖','͙','͚','̣'];

    var mid = [
          '̕','̛','̀','́',
          '͘','̡','̢','̧',
          '̨','̴','̵','̶',
          '͜','͝','͞',
          '͟','͠','͢','̸',
          '̷','͡',' ҉'];

    var all = [].concat(up,down,mid);

    var zalgo = {};

    function randomNumber(range) {
      r = Math.floor(Math.random()*range);
      return r;
    };

    function is_char(character) {
      var bool = false;
      all.filter(function(i){
       bool = (i == character);
      })
      return bool;
    }

    zalgo.heComes = function(text, u, m, d, size){
        result = '';

        var options = {"up" : u || true, "down" :  d || true, "mid" : m || true, "size" : size || "mini"};

        text = text.split('');
         for(var l in text){
           if(is_char(l)) {
             continue;
           }
           result = result + text[l];

           var counts = {"up" : 0, "down" : 0, "mid" : 0};

          switch(options.size) {
            case 'mini':
              counts.up = randomNumber(8);
              counts.min= randomNumber(2);
              counts.down = randomNumber(8);
            break;
            case 'maxi':
              counts.up = randomNumber(16) + 3;
              counts.min = randomNumber(4) + 1;
              counts.down = randomNumber(64) + 3;
            break;
            default:
              counts.up = randomNumber(8) + 1;
              counts.mid = randomNumber(6) / 2;
              counts.down= randomNumber(8) + 1;
            break;
          }
          var arr = ["up", "mid", "down"];
          for(var d in arr){
            var index = arr[d]
            for (var i = 0 ; i <= counts[index]; i++)
            {
              if(options[index]) {
                  p = eval(index)
                  result = result + p[randomNumber(p.length)]
                }
              }
            }
          }
        return result;
    };
    // ----- end of zalgo.js ----- */

    return zalgo.heComes;
}

function AutoMeme(tagButton, tagMeme)
{
    var memes = new Array(),
        blocked = false,
        max = 10,
        zalgo = null;

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
            if (zalgo) m = zalgo(m);
            tagMeme.innerHTML = m;
        }
    }

    function fetch(callback)
    {
        var req = makeHttpObject();
        if (!req) { return; }

        var recd = false;
        $('#loading span').fadeIn('fast');
        req.open("GET", "/moar.html?lines="+max+"&ts="+new Date().getTime(), true);
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

    tagButton.onclick = function() { meme(); };
    $('body').upUpDownDown({
        watchFor: [38,38,40,40,37,39,37,39,66,65],
        callback: function() {
            if (!zalgo) {
                zalgo = Zalgo();
                $('body').css({
                    fontFamily: "Helvetica, Arial, 'DejaVu Sans', sans-serif",
                    overflowX: 'hidden'
                });
                tagMeme.innerHTML = zalgo(tagMeme.innerHTML);
                $('#footer-links a, #halp h1, #halp a').each(function() {
                    $(this).html(zalgo($(this).html()));
                });
            }
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
    $('<span><a href="#" id="wut">wut?</a> &middot;&nbsp;</span>').prependTo($('#footer-links'));
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
