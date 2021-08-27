cities = {
    'london': {
        'country': 'great britain',
        'population': 1000000,
        'river': 'thames'
    },
    'riga': {
        'country': 'latvia',
        'population': 800000,
        'river': 'daugava'
    },
    'moscow': {
        'country': 'russia',
        'population': 12000000,
        'river': 'moscow'
    }
}
for city, information in cities.items():
    print('\n' + city.title() + ":")
    for key, value in information.items():
        print(key.title() + ": " + str(value).title())
