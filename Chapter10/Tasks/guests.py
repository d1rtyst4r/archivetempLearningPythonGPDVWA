file_name = 'guests.txt'

name = input('Please enter your name: ')

with open(file_name, 'w') as file_object:
    file_object.write(name)