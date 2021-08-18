# Slices
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # return 3 firsts elements from list. 3 is border!
print(players[1:4])
print(players[:4])  # if first index not set, it will starts from beginning
print(players[2:])  # if last index not set, it will ends with last element
print(players[-3:])  # return tree last elements

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

