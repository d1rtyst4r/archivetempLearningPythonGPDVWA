# Task 4.13
buffet = ('pizza', 'soda', 'sandwiches', 'meat', 'carrot')
print("Today's menu:")
n = 1
for food in buffet:
    print('\t' + str(n) + '). ' + food.title())
    n += 1

# Tuple modification
buffet = ('pizza', 'soda', 'sandwiches', 'apples', 'tomatoes')
print("\nToday's new menu:")
n = 1
for food in buffet:
    print('\t' + str(n) + '). ' + food.title())
    n += 1
