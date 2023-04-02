def make_sandwich(*toppings):
    """Print sandwich toppings"""
    print("You ordered sandwich with folowing toppings:")
    for topping in toppings:
        print("- " + topping)


make_sandwich('cheese')
make_sandwich('cheese', 'mustard')
make_sandwich('ham', 'cheese', 'butter')

