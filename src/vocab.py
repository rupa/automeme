# vim: set fileencoding=utf-8 :

__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

from common import *

spengbab = lambda: choice(\
        ['Spange','Speng','Sporg','Splorg','Spang',
        'Spernd','Splort','Spunk','Scram','Spange','Speeng',
        'Splen','Spengj','Spinge','Spong']\
        ) + choice(\
        ['bob','bob','bob','bab','bab','beb','blat','berp','bharb',
        'blar','borg'])
sqarpents = lambda: choice(\
        ['Sqar','Skur','Sven','Squat','Spleen','Snare','Sklabh',
        'Squere','Dildo']\
        ) + choice(\
        ['pents','ponce','porks','peeps','pops','pans','pints',
        'ponts'])

vocab = {
    'spengbab': [
        lambda: '%s %s' % (spengbab(), sqarpents()),
    ],

    'name': [
        '4chan',
        'Abbath',
        'Abe Vigoda',
        'Acid Burn',
        'an hero',
        'Anonymous',
        'AOL',
        'Apple',
        'Battletoads',
        'Bill Gates',
        'Boxxy',
        'Brian Peppers',
        'Burzum',
        'Catwoman',
        'Crash Override',
        'Creepy Chan',
        'Dagron',
        'Dethklok',
        'Digg',
        'Domokun',
        'Dragonforce',
    'The Dude',
        'Duke Nukem',
        'Dumbledore',
        'ebaumsworld',
        'Elvis',
    'The FBI',
    'The Flying Spaghetti Monster',
        'FOX News',
    'The Fresh Prince of Bel-Air',
        'George Bush',
        'G.I. Joe',
        'GIRUGAMESH',
        'Glenn Beck',
        'God',
        'Google',
        'Harry Potter',
        'Hitler',
        'Homer',
        'Imhotep',
        'INTERNET HATE MACHINE',
        'Jawsus',
        'Jean-Luc Picard',
        'Jesus',
        'John Freeman',
        'John Romero',
        'Kanye West',
        'Kevin Rose',
        'Keyboard Cat',
        'KOMPRESSOR',
        'Kotaku',
        'Lars Ulrich',
        'Lil Jon',
        'Loituma Girl',
        'Longcat',
        'Luigi',
        'Magibon',
        'MAI WAIFU',
        'Mario',
        'Metallica',
        'Mexico',
        'Michael Jackson',
        'Microsoft',
        'Milhouse',
        'moot',
   'your mom',
    'The movie industry',
    'The music industry',
        'Nine Inch Nails',
        'Nod Flenders',
        'Obama',
        'Pedobear',
    'The Pirate Bay',
        'Raptorjesus',
        'Reddit',
    'The RIAA',
        'Richard Stallman',
        'Scientology',
   'your sister',
        'Spengbab',
        'Spiderman',
        'Star Wars',
        'Star Wars Kid',
        'Steve Ballmer',
        'Steve Irwin',
        'Steve Jobs',
        'Superboy',
        'Superman',
        'Superwoman',
        'Thrillho',
        'Trent Reznor',
        'Trogdor',
        'Tron Guy',
        'Weegee',
        'Woll Smoth',
        'W.T. Snacks',
        'Xenu',
        'Xzibit',
        'YouTube',
        'Za Warudo',
        'Zero Cool',
        'Zoidberg',
        lambda: '%s %s' % (spengbab(), sqarpents()),
        lambda: 'Spengbab %s' % sqarpents(),
    ],

    'noun': [
        'alien; ~s',
        'American; ~s',
        'animated gif; ~s',
        'anime',
        'anime video; ~s',
        'ant; ~s',
        'apple; ~s',
        'asteroid; ~s',
        'atheist; ~s',
        'babby; ~s',
        'bacon',
        'bank; ~s',
        'banker; ~s',
        'bear; ~s',
        'bed; ~s',
        'bee; ~s',
        'beer; ~s',
        'bird; ~s',
        'blogger; ~s',
        'boat; ~s',
        'bone; ~s',
        'book; ~s',
        'bucket; ~s',
        'button; ~s',
        'cake; ~s',
        'Canadian; ~s',
        'car; ~s',
        'castle; ~s',
        'cat; ~s',
        'centipede; ~s',
        'cheat code; ~s',
        'Christian; ~s',
        'Coca-Cola bottle; ~s',
        'coffee; ~s',
        'coin; ~s',
        'college degree; ~s',
        'comic; ~s',
        'computer; ~s',
        'conservative; ~s',
        'copypasta',
        'cow; ~s',
        'demon; ~s',
        'dictionary; dictionaries',
        'dinosaur; ~s',
        'doctor; ~s',
        'dog; ~s',
        'donut; ~s',
        'door; ~s',
        'dragon; ~s',
        'drink; ~s',
        'drug; ~s',
        'duck; ~s',
        'dude; ~s',
        'eel; ~s',
        'emo; ~s',
        'eskimo; ~s',
        'extra life; extra lives',
        'Facebook profile; ~s',
        'fish',
        'fist; ~s',
        'forest; ~s',
        'furry; furries',
        'gamer; ~s',
        'garbage file; ~s',
        'German; ~s',
        'gibson; ~s',
        'girl; ~s',
        'girlfriend; ~s',
        'girl gamer; ~s',
        'goat; ~s',
        'goth; ~s',
        'government; ~s',
        'grammar; ~s',
        'grandspasguitar; ~s',
        'guitar; ~s',
        'guy; ~s',
        'hacker; ~s',
        'hacker on steroids; hackers on steroids',
        'h4x0r; ~z',
        'hero; ~es',
        'horse; ~s',
        'house; ~s',
        'hovercraft; ~s',
        'human; ~s',
        'ice cream',
        'insect; ~s',
        'interior crocodile alligator; ~s',
        'internet; ~s',
        'IPHONE; ~s',
        'iPod; ~s',
        'Irishman; Irishmen',
        'jedi; ~s',
        'jedi knight; ~s',
        'junk',
        'keyboard; ~s',
        'kitten; ~s',
        'large hadron collider; ~s',
        'lawyer; ~s',
        'leprechaun; ~s',
        'Linux user; ~s',
        'lion; ~s',
        'LiveJournal; ~s',
        'lupus',
        'lulz',
        'MacBook; ~s',
        'MacBook Air; ~s',
        'mallgoth; ~s',
        'man; men',
        'manga',
        lambda: 'megah%srtz' % choice('ue'),
        'mom; ~s',
        'moron; ~s',
        'mp3 file; ~s',
        'mudkip; ~z',
        'music; ~ videos',
        'MySpace; ~ angles',
        'MySpace profile; ~s',
        'MySpace password; seven different passwords',
        'nerd; ~s',
        'ninja; ~s',
        'panda; ~s',
        'password; ~s',
        'penguin; ~s',
        'photographer; ~s',
        'pig; ~s',
        'pirate; ~s',
        'pizza; ~s',
        'planet; ~s',
        'plank; ~s',
        lambda: 'Pokem%sn; Pokemans' % choice('oa'),
        'potato; ~es',
        'purple drank; ~s',
        'record label; ~s',
        'robot; ~s',
        'rocket; ~s',
        'sandwich; ~es',
        'sausage; ~s',
        'scientologist; ~s',
        'script-kiddie; ~z',
        'skittle; ~s',
        'snake; ~s',
        'snowman; snowmen',
        'song; ~s',
        'spoon; ~s',
        'stalker; ~s',
        'superhero; ~es',
        'swine flu',
        'Tamagotchi; ~s',
        'Techcrunch rumour; ~s',
        'techno weenie; ~s',
        'tentacle; ~s',
        'torrent; ~s',
        'trap; ~s',
        'troll; ~s',
        'TV; ~s',
        'videogame; ~s',
        'vidja gaem; ~s',
        'wart; ~s',
        'webcam; ~s',
        'weeaboo; ~s',
        'whale; ~s',
        'windmill; ~s',
        'window; ~s',
        'Windows user; ~s',
        'woman; women',
        'xbox; ~es',
        'YouTube comment; ~s',
        'YouTube video; ~s',
        'zombie; ~s',
    ],

    'bodypart': [
        'afro; ~s',
        'arm; ~s',
        'armpit; ~s',
        'back; ~s',
        'beard; ~s',
        'ear; ~s',
        'eye; ~s',
        'finger; ~s',
        'foot; feet',
        'hand; ~s',
        'head; ~s',
        'leg; ~s',
        'moustache; ~s',
        'mouth; ~s',
        'mullet; ~s',
        'nose; ~s',
        'nostril; ~s',
        'toe; ~s',
        'tongue; ~s',
        'unix beard; ~s',
    ],

    # transitive verbs (object)
    'verb': [
        # I write; He writes; I wrote; I have/had written; I am/was writing
        'accidentally; ~; ~; ~; ~',
        'blog about; blogs about; blogged about; ~; blogging about',
        'bobba; ~; ~; ~; ~',
        'burn; ~s; burned; ~; burning',
        'boot up; boots up; booted up; ~; booting up',
        'defenestrate; ~s; defenestrated; ~; defenestrating',
        'destroy; ~s; destroyed; ~; destroying',
        'discombobulate; ~s; discombobulated; ~; discombobulating',
        'drink; ~s; drank; drunk; drinking',
        'download; ~s; downloaded; ~; downloading',
        'eat; ~s; ate; eaten; eating',
        'fisticuff; ~s; fisticuffed; ~; fisticuffing',
        'google; ~s; googled; ~; googling',
        'hack; ~s; hacked; ~; hacking',
        'h4x0r; ~z; h4x0r3d; ~; hacking',
        'kick; ~s; kicked; ~; kicking',
        'kill; ~s; killed; ~; killing',
        'masticate; ~s; masticated; ~; masticating',
        'photoshop; ~s; photoshopped; ~; photoshopping',
        'punch; ~es; punched; ~; punching',
        'shoop; ~s; shooped; ~; shooping',
        'shoot; ~s; shot; ~; shooting',
        'steal; ~s; stole; stolen; stealing',
        'throw; ~s; threw; thrown; throwing',
        'torrent; ~s; torrented; ~; torrenting',
        'troll; ~s; trolled; ~; trolling',
        'watch; ~es; watched; ~; watching',
    ],

    # intransitive verb (no object)
    'iverb': [
        # I write; He writes; I wrote; I have/had written; I am/was writing
        'blog; ~s; blogged; ~; blogging',
        'chew bees; chews bees; chewed bees; ~; chewing bees',
        'count; ~s; counted; ~; counting',
        'dance; ~s; danced; ~; dancing',
        'do a barrel roll; does a barrel roll; did a barrel roll; '\
                'done a barrel roll; doing a barrel roll',
        'download mp3s; downloads mp3s; downloaded mp3s; ~; downloading mp3s',
        'drink; ~s; drank; drunk; drinking',
        'drive; ~s; drove; driven; driving',
        'duck; ducks; ducked; ~; ducking',
        'eat; eats; ate; eaten; eating',
        'frigth back; frigths back; frigth back; ~; frigthing back',
        'hack; hacks; hacked; ~; hacking',
        "lol; ~s; lol'd; ~; lollin",
        'moonwalk; ~s; moonwalked; ~; moonwalking',
        'roar; ~s; roared; ~; roaring',
        'run; runs; ran; run; running',
        'scream; ~s; screamed; ~; screaming',
        'shoop; shoops; shooped; ~; shoopin',
        'sing; ~s; sang; sung; singing',
        'skeet; skeets; skeeted; ~; skeetin',
        'troll; trolls; trolled; ~; trolling',
        'whine; ~s; whined; ~; whining',
    ],

    'adj': [
        'angry',
        'bald',
        'broken',
        'crunk',
        'delicious',
        'dizzy',
        'drunk',
        'emo',
        'epic',
        'flying',
        'hairy',
        'grim',
        'grim and frostbitten',
        'homeless',
        'HUEG',
        'illegal',
        'inverted',
        'invisible',
        'juicy',
        'kvlt',
        'l33t',
        'large',
        'lazy',
        'long',
        'mighty',
        'necro',
        'old',
        lambda: 'o' * randint(3,8) + 'ld',
        'photoshopped',
        'pig disgusting',
        'pirated',
        'pointing',
        'pragnent',
        'raging',
        'right-wing',
        'screaming',
        'sentient',
        'serious',
        'short',
        'spicy',
        'successful',
        'sweaty',
        'tall',
        'trve kvlt',
        'ugly',
    ],
}

nsfw = {
    'name': [
        'Cockmongler',
        'Dat Ass',
        'Dickbutt',
        'goatse',
        'Sexman',
        '2girls1cup',
    ],

    'noun': [
        '4chan; 4chonz',
        'arse eel; ~s',
        'box of rape; boxes of rape',
        '/b/tard; ~s',
        'camwhore; ~s',
        'freetard; ~s',
        'loli; ~s',
        'macfag; ~s',
        'mong; ~s',
        'nazi; ~s',
        'poop',
        'trendwhore; ~s',
        'webcock; ~s',
    ],

    'bodypart': [
        'arse; ~s',
        'boob; tits',
        'butt; ~s',
        'dong; ~s',
        'penis; ~es',
        'vagina; ~s',
        'wiener; ~s',
    ],

    'verb': [
        'blow; blows; blew; blown; blowing',
        'fap to; faps to; fapped to; ~; fapping to',
        'fist; ~s; fisted; ~; fisting',
        'sex up; sexes up; sexed up; ~; sexing up',
        'spank; ~s; spanked; ~; spanking',
        'teabag; ~s; teabagged; ~; teabagging',
    ],

    'iverb': [
        'fap; faps; fapped; ~; fapping',
        'gargle my balls; gargles my balls; gargled my balls; ~; gargling my balls',
        'get laid; gets laid; got laid; gotten laid; getting laid',
        'get low; gets low; got low; gotten low; getting low',
        'suck; sucks; sucked; ~; sucking',
    ],

    'adj': [
        'butthurt',
        'retarded',
        'underage',
    ],
}

vocab['noun'].extend(vocab['bodypart'])
nsfw['noun'].extend(nsfw['bodypart'])
