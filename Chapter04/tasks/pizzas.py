pizzas = ['pepperoni', 'margarita', 'chicago']
for pizza in pizzas:
    print('I like ' + pizza + 'pizza.')
print('\nI really like pizza!')

# Task 4.11
my_pizzas = ['pepperoni', 'margarita', 'chicago']
friend_pizzas = my_pizzas[:]  # list copy

my_pizzas.append('vasara')
friend_pizzas.append('bacon')
print('\nMy favorite pizzas are:')
for pizza in my_pizzas:
    print('\t' + pizza.title())

print('\nMy friend favorite pizzas are:')
for pizza in friend_pizzas:
    print('\t' + pizza.title())
