# Task 8-6

def city_country(city, country):
    """return city and country"""
    formatted_city_country = city.title() + ", " + country.title() + "."
    return formatted_city_country


riga_latvia = city_country('riga', 'latvia')
print(riga_latvia)

vilnius_lithuania = city_country('vilnius', 'lithuania')
print(vilnius_lithuania)

tallinn_estonia = city_country('tallinn', 'estonia')
print(tallinn_estonia)
