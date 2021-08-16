motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'  # changing first element in list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')  # add element in the end of the list
print(motorcycles)

# add by one element to the list
motorcycles = []
motorcycles.append("honda")
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

# Add element by index
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Remove element using del
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)

# Remove element using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motocycle = motorcycles.pop()  # remove last element
print(motorcycles)
print(poped_motocycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# Remove element from list using index and pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# Remove element from the list by value (remove())
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is to expensive for me.")
