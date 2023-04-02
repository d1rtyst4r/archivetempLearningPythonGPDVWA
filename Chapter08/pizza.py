def make_pizza(size, *toppings):
    """Print ordered topppings"""
    print("\nMaking a + " + str(size) + "inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'green peppers', 'extra cheese')
