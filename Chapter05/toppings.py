# Not equal
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')

# Check is a element in the list
requested_toppings = ['mushrooms', 'bacon', 'pepperoni']
print('mushrooms' in requested_toppings)
print('onion' in requested_toppings)

# Many if checks
requested_toppings= ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinishing making your pizza.')

# if in the for cycle
requested_toppings = ['mushrooms', 'green pepper', 'pepperoni']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print("Sorry, we are out of green peppers right now.")
    else:
        print('Adding ' + requested_topping + '.')

print()

# checking is any element in the list
requested_toppings = []  # in this case return False
if requested_toppings:  # return true if any element is in the list
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print("\nFinished making your pizza.")
else:
    print('Are you sure you want plain pizza?')

# Check element from 1 list in another
available_toppings = ['mushrooms', 'olives', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'fresh fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print('\nFinished making your pizza.')
