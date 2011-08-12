def vocab(v):
    v['name'] = [
        'Brooklyn',
        'Echo Park',
        'Etsy',
        'Helvetica',
        "McSweeney's",
        'Pitchfork',
        'Shoreditch',
        'Silverlake',
        'Tumblr',
        'Wes Anderson',
        'Williamsburg',
        '3 Wolf Moon',
    ]
    v['noun'] = [
        'art party; art parties',
        'bicycle; ~s',
        'cardigan; ~s',
        'chambray; ~s',
        'Cosby sweater; ~s',
        'dreamcatcher; ~s',
        'fedora; ~s',
        'fixie; ~s',
        'hoodie; ~s',
        'iPhone; ~s',
        'jeggings',
        'jorts',
        'keffiyah; ~s',
        'keytar; ~s',
        'leggings',
        'messenger bag; ~s',
        'mixtape; ~s',
        'moustache; ~s',
        'PBR',
        'quinoa',
        'vinyl record; vinyl',
        'skateboard; ~s',
    ]
    v['adj'] = [
        'American Apparel',
        'Apple',
        'denim',
        'Etsy',
        'freegan',
        'gluten-free',
        'indie',
        'ironic',
        'letterpress',
        'lo-fi',
        'lomo',
        'organic',
        'readymade',
        'retro',
        'scenester',
        'skinny',
        'sustainable',
        'tattooed',
        'tofu',
        'twee',
        'vegan',
        'VHS',
        'vintage',
        'vinyl',
    ]
    v['iverb'].extend([
        'sell out; sells out; sold out; ~; selling out',
        'put a bird on it; puts a bird on it; put a bird on it; ~; putting a bird on it',
    ])

    bodyparts = [
        'neckbeard',
    ]
    v['bodypart'].extend(bodyparts)
    v['noun'].extend(bodyparts)
    return v
