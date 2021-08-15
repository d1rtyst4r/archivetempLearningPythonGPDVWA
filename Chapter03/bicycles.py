bicycles = ['trek', 'cannondale', 'redline', 'specialized']  # list
print(bicycles)

print(bicycles[0].title())  # print first element from the list
print(bicycles[1].title())  # print second element from the list
print(bicycles[3].title())  # print forth element from the list
print(bicycles[-1].title())  # print last element from the list

# concatenation string with element from the list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
