def make_pizza(*toppings):
    """Print ordered topppings"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('pepperoni', 'green peppers', 'extra cheese')
