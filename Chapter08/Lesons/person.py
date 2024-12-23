def build_person(first_name, second_name, age=''):
    """return dictionary with persons information"""
    person = {"first": first_name, "second": second_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
