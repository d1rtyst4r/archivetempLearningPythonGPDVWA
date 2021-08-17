# Cycle for
magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # Check all elements in list
    print(magician)  # and print it

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", it was a great trick!")  # concatenation in cycle

# More actions in cycle
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", it was a great trick!")  # concatenation in cycle
    print("I can't wait to see your next trick, " + magician.title() + '!\n')
print("Thanks you everyone. That was a great magic show!")  # Action after cycle
