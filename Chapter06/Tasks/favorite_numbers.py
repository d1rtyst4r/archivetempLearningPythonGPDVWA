favorite_numbers = {
    'eric': [15, 13, 77],
    'tom': [73, 41, 13],
    'vadim': [33, 88, 54],
    'andris': [13, 22, 51]
}

for user, numbers in favorite_numbers.items():
    print('\n' + user.title() + 's favorite numbers are:')
    for number in numbers:
        print("\t" + str(number))
