# Numbers to ordinal numbers

numbers = [value for value in range(1, 10)]

if numbers:
    for number in numbers:
        if number == 1:
            print(str(number) + 'st')
        elif number == 2:
            print(str(number) + 'nd')
        else:
            print(str(number) + 'th')
