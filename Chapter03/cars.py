cars = ['mazda', 'honda', 'bmw', 'audi']
text = 'I would like to buy '

print(text + cars[0].title() + ".")
print(text + cars[1].title() + '.')
print(text + cars[2].title() + '.')
print(text + cars[3].title() + '.')

# Sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Reverse sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print()
print(cars)

# Temporarily sorted
print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list:")
print(cars)

# Reverse list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the reversed list:")
cars.reverse()
print(cars)

# List length
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # method len return list length (integer)

