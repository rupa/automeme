Auto-Meme
=========

Here is the source code for [Auto-Meme](http://meme.boxofjunk.ws/).

Auto-Meme is one very cheeky random nonsense generator. It's inspired by the
utter insanity of 4chan, and internet memes in general. Sometimes it's cute;
sometimes it's downright offensive. You have been warned.

The bulk of the code was written in Summer 2008. It has been edited on and off
since then.


Caveats
-------

This was purely a pet project, and was not created with distribution in mind.
Thus, there are some caveats:

* It's not a standard Python module (i.e. you can't just `import automeme`).

* It probably won't work out of the box.

* There won't be much in the way of documentation or support.

* Expect to see hard-coded variables and hastily written hacks.


Diving in
---------

A quick overview of the folder structure:

* `src` -- All the essential stuff.
* `bin` -- Some scripts for updating `meme.boxofjunk.ws`. You'll need to
           edit some variables if you want to use these.
* `images` -- Image files used by scripts in the `bin` folder.

To see the meme generator in action:

    $ cd src
    $ ./raw.cgi

If nothing goes wrong, you should see something like this:

    Content-type: text/html; charset=UTF-8

    POOL'S CLOSED DUE TO PENGUINS
    THANK YOU, ACID BURN. BUT OUR BUTTON IS IN ANOTHER CANADIAN
    DISREGARD THAT, I HACK PIZZA
    SPENGBAB IS NOT A MEME!
    NOOOO THEY BE BOOTING UP MY GIBSON
    I SEE WHAT YOU PHOTOSHOPPED THERE
    TRVE KVLTCAT IS TRVE KVLT
    HITLER? IN <em>MY</em> HACKER?
    I HAVE REPORTED YOU TO YOUTUBE FOR STEALING NOSES AS IT IS A CRIME.
    IMMA FIRIN MAH WART
