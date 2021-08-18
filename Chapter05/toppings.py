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

