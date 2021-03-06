import re
from random import choice, randint

re_sub = lambda p, r, s: re.compile(p, re.U | re.VERBOSE).sub(r, s)
re_isub = lambda p, r, s: re.compile(p, re.U | re.I | re.VERBOSE).sub(r, s)

ing_in = lambda s: re_sub(r'(IN)G(\W|$)', r'\1\2', s)
no_the = lambda s: re_sub(
    r'(^|\s) THE (\W|S)', r'\2', s
).strip().replace('[THE]', 'THE')
no_article = lambda s: re_isub(r'^(AN?|THE|YOUR|DAT)\s', '', s)
thants = lambda s: re_isub(r'<(TH|BL) [^AEIOU4]*([^>]*)>', r'\1\2', s)

patterns = [
    ('im in ur {1}, {2} ur {3}', ('noun', 'noun1'), 'verb4', 'noun1'),
    ('how do i {1} {2}?', 'verb2', ('noun', '~web', 'name')),
    ('{1} {2} {3}', 'name', ('~kills', 'verb1'), ('name', '~Dumbledore')),
    ('All your {1} are belong to {2}', 'noun1', ('~us', 'noun', 'name')),
    (
        '{1a} is {2} too',
        ('noun', 'noun', ['name', no_article]), ('~fine', 'adj')
    ),
    ('Disregard that, I {1} {2}', 'verb', 'noun1'),
    ("{1}'s closed due to {2}", ('~Pool', 'noun'), ('noun1', 'name')),
    [
        (
            'Push {1}, receive {2}',
            ('~button', '~butan'),
            ('noun', 'noun1', 'name')
        ),
        no_the
    ],
    [
        (
            'so i herd u {1} {2}',
            ('~liek', '~liek', 'verb'),
            ('noun1', 'noun1', 'name')
        ),
        no_the
    ],
    (
        'You have {1} most of a small {2}. '
        'Please pick your {3} with greater care.',
        'verb3',
        'noun',
        'noun1'
    ),
    ('{1} is not a meme!', ('name', 'noun')),
    [('i has {1a}. you can has my {1}.', ('noun', 'noun', 'noun1')), no_the],
    (
        'This is {1}. I can tell by the {2}, and from having seen '
        'a lot of {3} in my day.',
        ('~photoshopped', 'adj'),
        'noun1',
        'noun1'
    ),
    ('Maximum {1} yields maximum {2}', ('~volume', 'noun1'), 'noun1'),
    (
        "i think {1} is a pretty cool guy. "
        "eh {2} {3} and doesn't afraid of anything",
        ('name', 'noun', 'noun1'),
        'verb1',
        'noun1'
    ),
    lambda: choice((('{1}cat is {1}', 'adj0'), ('{1}cat is {1a}', 'noun0'))),
    ('{1}? In _my_ {2}?', ('name', 'noun1'), 'noun'),
    ('This is {1} {2}, I must {3} it', 'adj0', ('~cake', 'noun'), 'verb'),
    (
        'I have reported you to {1} for {2} {3} as it is a crime.',
        'name',
        ('~stealing', 'verb4'),
        'noun1'
    ),
    ('Imma {1} mah {2}', ('~chargin', '~firin'), ('noun', 'noun1')),
    ('is it can be {1} tiem nao plees?', ('noun', 'noun', 'noun1', 'adj')),
    ("It's over. {1} is finished.", ('name', 'noun')),
    ('The {1} is a lie', 'noun'),
    ('BECAUSE YOU ARE _{1} {2}_', ('~headcrab', 'adj', 'noun'), 'noun'),
    ('No, {1}. You are the {2}.', (['name', no_article], 'noun'), 'noun1'),
    # http://lurkmore.com/wiki/DOOM:_Repercussions_of_Evil
    [('No! You will be {1} by {2}', 'verb', ('noun1', 'name')), no_the],
    lambda: choice((
        (
            'PROTIP: To {1} the {2}, {3} at it until it {4}.',
            ('~defeat', 'verb'),
            'noun',
            ('~shoot', 'iverb'),
            ('~dies', 'iverb1')
        ),
        (
            'PROTIP: To {1} the {2}, {3} it until it {4}.',
            ('~defeat', 'verb'),
            'noun',
            ('~shoot at', 'verb'),
            ('~dies', 'iverb1')
        ),
    )),
    ('MUST PUT {1} IN {2}-CHAN', 'noun', (['name', no_article], 'noun')),
    (
        'There is {1a} in my {2}, your argument is invalid',
        'noun',
        ('~beard', 'bodypart', 'noun')
    ),
    (
        'I like my {1} like I like my {2}: covered in {3}',
        ('~women', 'noun1'),
        'noun1',
        'noun1'
    ),
    (
        'in {1} {2} {3}',
        ('~b4', '~before'),
        'adj',
        (['name', no_article], 'noun', 'noun1')
    ),
    (
        'This {1} is now about {2} {3}',
        ('~thread', 'noun'),
        'adj',
        (['name', no_article], 'noun1')
    ),
    ('Become an {1}', (['name', no_article], 'noun', 'noun1')),
    ('I see what {1} {2} there', ('~you', 'name'), 'verb2'),
    ('{1} is serious {2}', ('noun', 'name'), 'noun'),
    ('{1} {2} are _SUPERIOR_', 'adj', 'noun1'),
    ('Attack its weak point for {1} {2}', 'adj', ('noun', 'noun1')),
    ('My {1} is full of {2}.', 'noun', 'noun1'),
    (
       'I will not {1} this {2} -- it is {3}.',
       ('~buy', 'verb'),
       'noun',
       ('adj', 'adj', 'name')
    ),
    (
        'Thank you, {1}. But our {2} is in another {3}',
        ['name', no_article],
        'noun',
        ('~castle', 'noun')
    ),
    (
        'Noooo they be {1} my {2}',
        'verb4',
        ('noun', 'noun1', ['name', no_article])
    ),
    (
        '{1} hai, i {2} {3} {4}',
        ('~o', '~oh'),
        ('~upgraded', 'verb2'),
        ('~ur', '~your'),
        ('noun', 'noun1', ['name', no_article])
    ),
    ('{1} is pig disgusting', ('name', 'noun', 'noun1')),
    [('They see me {1}, they {2}', 'verb4', ('~hatin', 'verb4')), ing_in],
    (
        'i made you {1a} but i {2} it',
        ('noun', 'noun', ['name', no_article]),
        'verb2'
    ),
    (
        'This is {1a} {2}. It is made of {3} and {4}.',
        'adj',
        ('~sandwich', 'noun'),
        ('adj', 'noun1', 'name'),
        ('adj', 'noun1', 'name')
    ),
    lambda: choice((
        ('my {1}, let me show you it', (['name', no_article], 'noun')),
        ('my {1}, let me show you them', 'noun1')
    )),
    ('I {1} _all_ the {2}', ('~ate', 'verb2'), 'noun1'),
    ('{1} the {2}!', 'verb', ('~harpoons', 'noun1')),
    (
        "JESUS CHRIST IT'S {1a} GET IN THE {2}",
        ('noun', 'noun', ['name', no_article]),
        ('~car', 'noun')
    ),
    ('I am _BEST {1}_, the best {1} ever!', ('noun', ['name', no_article])),
    ('You have no chance to {1}, make your time', ('iverb')),
    ('i accidentally {1a}, is this {2}?', 'noun', ('~bad', '~dangerous')),
    [
        (
            'how is {1} formed? how {2} get {3}?',
            ('noun', 'noun', 'name'),
            ('noun', 'noun', 'name'),
            ('adj', '~pragnent')
        ),
        no_the
    ],
    [
        (
            'Hello. My name is {1}. You killed my {2}. Prepare to {3}.',
            ('name', 'name', 'spengbab'),
            ('noun', 'noun1'),
            'iverb'
        ),
        no_the
    ],
    ("{1} {2}: {3} DOESN'T LIKE IT", ('~SCREAMING', 'adj'), 'noun', 'name'),
    [('Thanks, {1}. <TH {1}>.', ('noun1', 'name')), no_the, thants],
    [('Bless you, {1}. <BL {1}>.', ('noun1', 'name')), no_the, thants],
    ("These are not the {1} you're looking for", 'noun1'),
    ("Whatever {1} your {2}", 'verb1', ('noun', 'noun1')),
    ("That's not {1a}; _this_ is {1a}", 'noun'),
    ("I am {1}, hear me {2}", 'name', ('iverb', 'iverb', '~roar')),
    ("Dammit Jim, I'm {1a}, not {2a}", 'noun', 'noun'),
    ("In Soviet Russia, {1} {2} _YOU!_", ('noun', 'noun', 'name'), 'verb1'),
    ("I, for one, welcome our new {1} overlords", 'noun'),
    ("You wouldn't {1} {2a}", ('~download', 'verb'), 'noun'),
    (
        "To be {1a}, you must have {2}... {2} and {3a}.",
        ('~man', 'noun'),
        ('noun', 'noun1'),
        ('noun', '~penis')
    ),
    ("I {1}, therefore I {2}.", ('iverb', 'iverb', '~think'), 'iverb'),
    # religion is the opiate of the mudkips
    ("{1} is the {2} of the {3}", ('name', 'noun', 'noun'), 'noun', 'noun1'),
    (
        'Dr. {1}, or how I learned to stop {2} and {3} the {4}',
        ['name', no_article],
        ('~worrying', 'iverb4', 'iverb4'),
        ('~love', 'verb'), ('noun', 'noun1')
    ),
    (
        "We've secretly replaced {1}'s {2} with {3a}. "
        "Let's see if he notices...",
        'name',
        ('noun', 'noun1'),
        'noun'
    ),
    ("What _are_ {1}? We just don't know.", 'noun1'),
    (
        "{1} the {2}... with your {3}",
        ('~crush', 'verb'),
        'noun1',
        ('~mind', 'noun', 'noun1')
    ),
    (
        "oh god how did {1} get here I am not good with {2}",
        ('~this', '~this', 'name', 'noun1'),
        ('noun', 'noun1', 'name')
    ),
    ("This is your brain on {1}", 'noun1'),
    (
        "My {1} just {2} me; shit was SO {3}",
        'noun', 'verb2',
        ('noun', 'adj', '~cash')
    ),
    (
        "Yo {1}, I'm really happy for you, Imma let you finish, "
        "but {2} had one of the best {3} of all time",
        ['name', no_article],
        'name',
        'noun1'
    ),
    (
        "Yo dawg, I heard you like {1}, so we put some {1} in your {1} "
        "so you can {2} while you {2}.",
        'noun1',
        'iverb'
    ),
    ("{1} don't know about my {2}", ('~bitches', 'noun1'), ('noun', 'noun1')),
    [('{1} or gtfo', ('noun1', 'noun1', 'name')), no_the],
    (
        '{1} is the {2} that is killing {3}',
        ('name', 'noun1'),
        ('~cancer', 'noun'),
        ('name', 'noun', 'noun1')
    ),
    [
        (
            '{1} {2} {3}',
            ('~LOLI', 'name'),
            ('~HAET', '~LOEV', '~HAET'),
            ('noun', 'noun1', 'name')
        ),
        no_the
    ],
    lambda: (
        "I'M {1a}! I'M {1a}! SUCK MY D%sCK! I'M {1a}!" % ('I' * randint(5, 8)),
        'noun'
    ),
    ('{1} YOUR FUCKING {2}. {1} THEM.', ('~eat', 'verb'), 'noun1'),
    ('WHAT THE FUCK? YOU ARE {1}! AND {2}', ('adj', 'name', 'noun'), 'adj'),
    ("Ceiling {1} is watching you {2}", 'noun', ('~fap', 'iverb', 'iverb')),
    ('Fucking {1}, how do they work?', 'noun1'),
    ('{1} _all_ the {2}', 'verb', 'noun1'),
    ('better {1} my own {2}', 'verb', 'noun'), # bear grylls
    (
        "I don't always {1}, but when I do, I {2} {3}",
        'iverb',
        'verb',
        ('noun', 'noun1', 'name')
    ),
    ('Not sure if {1}, or just {2}', 'iverb4', 'adj'),
    ('hello? yes, this is {1}', 'noun'),
    # horse_ebooks
    ('"This is not acceptable!" I screamed as {1} {2}', 'name', 'iverb2' ),
    (
        'very important for {1} to {2} him {3}',
        'name',
        ('~do', 'verb'),
        ('~job', 'noun')
    ),
]
