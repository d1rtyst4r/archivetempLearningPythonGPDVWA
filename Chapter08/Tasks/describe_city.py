def describe_city(city='Riga', country='Latvia'):
    """"return modified string with city and country"""
    print(city.title() + " is in " + country.title() + ".")


describe_city()
describe_city(city="Klaipeda", country='Lithuania')
describe_city(city='Jurmala')
describe_city('Tallinn', 'Igaunia')