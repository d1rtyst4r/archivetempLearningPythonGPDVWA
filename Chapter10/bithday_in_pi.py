file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your bithday in format ddmmyy: ")
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your bithday does not appear in the first million digits of pi.')