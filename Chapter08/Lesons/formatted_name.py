def get_formatted_name(first_name, last_name, middle_name=''):
    """return formatted full name"""
    if middle_name:
        full_name = first_name.title() + " " + middle_name.title() + " " + last_name.title()
    else:
        full_name = first_name.title() + " " + last_name.title()
    return full_name


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

while True:
    print("\nPlease tell me your name!")
    print("(enter 'q' at any time to quit)")
    f_name = input("Your first name: ")
    if f_name == 'q':
        break
    l_name = input("Your last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello " + formatted_name + "!")
