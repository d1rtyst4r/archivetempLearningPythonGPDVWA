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

# Tas 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # list copy
my_foods.append('ice cream')
friend_foods.append('cannoli')

print('\nMy favorite foods are:')
for food in my_foods:
    print('\t' + food.title())

print('\nMy friend favorite foods are:')
for food in friend_foods:
    print('\t' + food.title())