file_name = 'programming.txt'

#with open(file_name, 'w') as file_object:
#    file_object.write('I love programming.\n')
#    file_object.write('I love creating new games.\n')

with open(file_name, 'a') as file_object:  # add information to the file
    file_object.write('I Also lovefinding meaning in large datasets.\n')
    file_object.write('I love creat apps that can run in a browser.\n')