# List in the dictionary

pizza = {'crust': 'think',
         'toppings': ['mushrooms', 'extra cheese']}

# Order
print("Your ordered a " + pizza['crust'] + "- crust pizza " +
      'whit the following toppings:')
for topping in pizza['toppings']:
    print("\t" + topping)