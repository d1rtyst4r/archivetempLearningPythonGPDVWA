file_name = 'pi_digits.txt'

"""read file"""
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = '' # for pi in one line(string)
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))