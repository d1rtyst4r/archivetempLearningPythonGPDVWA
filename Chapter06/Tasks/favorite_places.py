user_favorite_places = {
    'ruslan': {
        'first': 'riga',
        'second': 'california',
        'third': 'london'
    },
    'rita': {
        'first': 'dzerumi',
        'second': 'crimea',
        'third': 'paris'
    },
    'luba': {
        'first': 'yosemite',
        'second': 'grand canyon',
        'third': 'paris'
    }
}

for user, favorite_places in user_favorite_places.items():
    print("\n" + user.title() + "'s favorite places are:")
    for favorite_place in favorite_places.values():
        print("\t" + favorite_place.title())
