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
