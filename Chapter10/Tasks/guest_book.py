file_name = 'guest_book.txt'

print('Just press "Enter" for quit')
while True:
    name = input('Please enter your name: ')
    if name !='':
        with open(file_name, 'a') as file_object:
            file_object.write(name +'\n')
    else:
        break
