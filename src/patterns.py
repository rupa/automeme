__author__ = 'Liam Cooke <http://boxofjunk.ws/>'

from common import *

ing_in = lambda s: re_sub(r'(IN)G(\W|$)', r'\1\2', s)
no_the = lambda s: re_sub(r'(^|\s) THE (\W|S)', r'\2',
                          s).strip().replace('[THE]','THE')
no_article = lambda s: re_isub(r'^(AN?|THE|YOUR)\s', '', s)

patterns = [
    ( 'im in ur {1}, {2} ur {3}', ('noun','noun1'), 'verb4', 'noun1' ),
    ( 'how do i {1} {2}?', 'verb2', ('noun', '~web', 'name') ),
    ( '{1} {2} {3}', 'name', ('~kills', 'verb1'), ('name', '~Dumbledore') ),
    ( 'All your {1} are belong to {2}', 'noun1', ('~us', 'noun', 'name') ),
    ( '{1a} is {2} too', ('noun', 'noun', ['name', no_article]), ('~fine', 'adj') ),
    ( "{1} don't know about my {2}", ('~bitches', 'noun1'), ('noun', 'noun1') ),
    ( 'Disregard that, I {1} {2}', 'verb', 'noun1' ),
    ( "{1}'s closed due to {2}", ('~Pool','noun'), ('noun1','name') ),
    [( 'Push {1}, receive {2}', ('~button', '~butan'),
            ('noun', 'noun1', 'name') ), no_the],
    [( 'so i herd u {1} {2}', ('~liek','~liek', 'verb'),
            ('noun1', 'noun1', 'name') ), no_the],
    [( '{1} or gtfo', ('noun1', 'noun1', 'name') ), no_the],
    ( 'You have {1} most of a small {2}. Please pick your {3} with greater care.',
            'verb3', 'noun', 'noun1' ),
    ( '{1} is not a meme!', ('name', 'noun') ),
    [( 'i has {1a}. you can has my {1}.', ('noun','noun','noun1') ), no_the],
    ( 'This is {1}. I can tell by the {2}, and from having seen '\
      'a lot of {3} in my day.', ('~photoshopped', 'adj'), 'noun1', 'noun1' ),
    ( 'Maximum {1} yields maximum {2}', ('~volume', 'noun1'), 'noun1' ),
    ( "i think {1} is a pretty cool guy. eh {2} {3} and doesn't afraid of anything.",
            ('name', 'noun', 'noun1'), 'verb1', 'noun1' ),
    lambda: randel(( ( '{1}cat is {1}', 'adj0' ),  ( '{1}cat is {1a}', 'noun0' ) )),
    ( '{1} is the {2} that is killing {3}', ('name', 'noun1'),
            ('~cancer','noun'), ('name','noun','noun1') ),
    ( '{1}? In _my_ {2}?', ('name', 'noun1'), 'noun' ),
    ( 'This is {1} {2}, I must {3} it', 'adj0', ('~cake', 'noun'), 'verb' ),
    ( 'I have reported you to {1} for {2} {3} as it is a crime.',
        'name', ('~stealing', 'verb4'), 'noun1' ),
    ( 'Imma {1} mah {2}', ('~chargin','~firin'), ('noun','noun1') ),
    ( "I really do hope you're {1} and not actually that fucking {2}.",
            'iverb4', 'adj' ),
    ( 'Your {1} is not {2}', 'noun', ('~cool','adj') ),  #tumblrs represent
    ( 'is it can be {1} tiem nao plees?', ('noun','noun','noun1','adj') ),
    ( "It's over. {1} is finished.", ('name','noun') ),
    ( 'The {1} is a lie.', 'noun' ),
    ( 'BECAUSE YOU ARE _{1} {2}_', ('~headcrab','adj','noun'), 'noun' ),
    ( 'No, {1}. You are the {2}.', (['name', no_article], 'noun'), 'noun1' ),
    # http://lurkmore.com/wiki/DOOM:_Repercussions_of_Evil
    [( 'No! You will be {1} by {2}', 'verb', ('noun1', 'name')), no_the],
    lambda: randel((
        ( 'PROTIP: To {1} the {2}, {3} at it until it {4}.', ('~defeat', 'verb'),
            'noun', ('~shoot', 'iverb'), ('~dies', 'iverb1') ),
        ( 'PROTIP: To {1} the {2}, {3} it until it {4}.', ('~defeat', 'verb'),
            'noun', ('~shoot at', 'verb'), ('~dies', 'iverb1') ),
        )),
    [( '{1} {2} {3}', ('~LOLI', 'name'), ('~HAET', '~LOEV', '~HAET'),
            ('noun','noun1','name') ), no_the],
    ( 'MUST PUT {1} IN {2}-CHAN', 'noun', (['name', no_article], 'noun') ),
    lambda: ( "I'M {1a}! I'M {1a}! SUCK MY D%sCK! I'M {1a}!" % ('I' * randint(5,8)),
              'noun' ),
    ( 'There is {1a} in my {2}, your argument is invalid', 'noun',
            ('~beard','bodypart','noun') ),
    ( '{1} YOUR FUCKING {2}. {1} THEM.', ('~eat','verb'), 'noun1' ),
    ( 'I like my {1} like I like my {2}: covered in {3}',
            ('~women', 'noun1'), 'noun1', 'noun1' ),
    ( 'in {1} {2} {3}', ('~b4', '~before'), 'adj',
            (['name', no_article], 'noun', 'noun1') ),
    ( 'This {1} is now about {2} {3}', ('~thread', 'noun'), 'adj',
            (['name', no_article], 'noun1') ),
    ( 'Become an {1}', (['name', no_article], 'noun', 'noun1') ),
    ( 'I see what {1} {2} there', ('~you', 'name'), 'verb2' ),
    ( '{1} is serious {2}', ('noun','name'), 'noun' ),
    ( 'WHAT THE FUCK? YOU ARE {1}! AND {2}', ('adj','name','noun'), 'adj' ),
    ( '{1} {2} are _SUPERIOR_', 'adj', 'noun1' ),
    ( 'Attack its weak point for {1} {2}', 'adj', ('noun','noun1') ),
    ( 'My {1} is full of {2}.', 'noun', 'noun1' ),
    ( 'I will not {1} this {2} -- it is {3}.', ('~buy','verb'), 'noun',
            ('adj','adj','name') ),
    ( 'Thank you, {1}. But our {2} is in another {3}', ['name', no_article],
            'noun', ('~castle', 'noun') ),
    ( 'Noooo they be {1} my {2}', 'verb4', ('noun','noun1',['name',no_article]) ),
    ( '{1} hai, i {2} {3} {4}', ('~o','~oh'), ('~upgraded','verb2'),
            ('~ur','~your'), ('noun','noun1',['name', no_article]) ),
    ( '{1} is pig disgusting', ('name','noun','noun1') ),
    [( 'They see me {1}, they {2}', 'verb4', ('~hatin', 'verb4') ), ing_in],
    ( 'i made you {1a} but i {2} it', ('noun', 'noun', 'noun1', 'name'), 'verb2' ),
    ( 'This is {1a} {2}. It is made of {3} and {4}.', 'adj', ('~sandwich', 'noun'),
            ('adj', 'noun1', 'name'), ('adj', 'noun1', 'name') ),
    lambda: randel(( ('my {1}, let me show you it', (['name', no_article], 'noun')),
                     ('my {1}, let me show you them', 'noun1') )),
    ( 'I {1} _all_ the {2}', ('~ate', 'verb2'), 'noun1' ),
    ( '{1} the {2}!', 'verb', ('~harpoons', 'noun1') ),
    ( "JESUS CHRIST IT'S {1a} GET IN THE {2}",
            ('noun', 'noun', ['name', no_article]), ('~car', 'noun') ),
    ( 'I am _BEST {1}_, the best {1} ever!', ('noun', ['name', no_article]) ),
    ( 'You have no chance to {1}, make your time', ('iverb') ),
    ( 'i just accidentally a {1}, is this {2}?', 'noun', ('~bad', '~dangerous') ),
    ( 'how is {1} formed? how {2} get {3}?', ('noun', 'noun', 'name'),
            ('noun', 'noun', 'name'), ('adj', '~pragnent') ),
    [( 'My name is {1}. You killed my {2}. Prepare to {3}.',
            ('name', 'name', 'spengbab'), ('noun', 'noun1'), 'iverb' ), no_the],
]
