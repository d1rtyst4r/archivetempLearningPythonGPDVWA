# List copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # list copy

print('My favorite foods are:')
print(my_foods)

print('\nMy friend favorite foods are:')
print(friend_foods)

my_foods.append('ice cream')
friend_foods.append('cannoli')
print('My favorite foods are:')
print(my_foods)
print('\nMy friend favorite foods are:')
print(friend_foods)

# !!!Incorrect copy!!!!
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # link to same "memory"

print('My favorite foods are:')
print(my_foods)

print('\nMy friend favorite foods are:')
print(friend_foods)

my_foods.append('ice cream')
friend_foods.append('cannoli')
print('My favorite foods are:')
print(my_foods)
print('\nMy friend favorite foods are:')
print(friend_foods)
