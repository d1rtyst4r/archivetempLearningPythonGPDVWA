eric = {
    'first_name': 'eric',
    'last_name': 'dow',
    'age': 35,
    'city': 'riga'
}

tom = {
    'first_name': 'tom',
    'last_name': 'grib',
    'age': 30,
    'city': 'liepaja'
}

rob = {
    'first_name': 'rob',
    'last_name': 'bite',
    'age': 17,
    'city': 'tallinn'
}

people = [eric, tom, rob]
for user in people:
    for key, value in user.items():
        print(key.title() + ": " + str(value).title())
    print()
    