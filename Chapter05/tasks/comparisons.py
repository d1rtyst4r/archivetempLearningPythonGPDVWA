cars = ['mazda', 'ford', 'kia', 'audi']
print('mazda' in cars)

my_car = 'bmw'
if my_car in cars:
    print('We can repair it!')
else:
    print("Sorry You have to find another service!")

if my_car not in cars:
    print("Wow! new one!")
else:
    print("We have this car in the list!")

age = 25
if age >= 21:
    print("You can buy alcohol.")
else:
    print("Sorry, we can't sell you")

color = 'red'
print('red' == color)
print('blue' == color)

min_height = 150
min_age = 13
your_height = 161
brother_height = 145
your_age = 15
brother_age = 13

if your_age >= min_age and your_height >= min_age:
    print("Your welcome!")
else:
    print('You are too young or too low.')

print(brother_age >= min_age or brother_height >= min_height)
print(your_age >= min_age or your_height >= min_height)
print(brother_age >= min_age and brother_height >= min_height)