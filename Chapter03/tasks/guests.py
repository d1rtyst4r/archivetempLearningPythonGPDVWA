guests = ['elizabeth', 'albert', 'peteris', 'jonny']
print("Hi " + guests[0].title() + ", I would like to invite you to my party!")
print("Hi " + guests[1].title() + ", I would like to invite you to my party!")
print("Hi " + guests[2].title() + ", I would like to invite you to my party!")
print("Hi " + guests[3].title() + ", I would like to invite you to my party!")
print("Here is number of guests: " + str(len(guests)) + ".")

# Update the list
guest_who_could_not_come = guests.pop(0)
guests.insert(0, 'theodore')
print("\n" + guest_who_could_not_come.title() + "'ll mise the party.")
print("\nHi " + guests[0].title() + ", I would like to invite you to my party!")
print("Hi " + guests[1].title() + ", I would like to invite you to my party!")
print("Hi " + guests[2].title() + ", I would like to invite you to my party!")
print("Hi " + guests[3].title() + ", I would like to invite you to my party!")
print("Here is number of guests: " + str(len(guests)) + ".")

# Add new guests
guests.insert(0, "richard")
guests.insert(3, "cesar")
guests.append("cleo")
print("\nHi " + guests[0].title() + ", I would like to invite you to my party!")
print("Hi " + guests[1].title() + ", I would like to invite you to my party!")
print("Hi " + guests[2].title() + ", I would like to invite you to my party!")
print("Hi " + guests[3].title() + ", I would like to invite you to my party!")
print("Hi " + guests[4].title() + ", I would like to invite you to my party!")
print("Hi " + guests[5].title() + ", I would like to invite you to my party!")
print("Hi " + guests[6].title() + ", I would like to invite you to my party!")
print("Here is number of guests: " + str(len(guests)) + ".")
# Remove guests
print("\nHi, sorry but I have only two places, so some guests will mise my party.")
guest_who_could_not_come = guests.pop()
print("Hi " + guest_who_could_not_come.title() + ", sorry but party canceled!")
guest_who_could_not_come = guests.pop()
print("Hi " + guest_who_could_not_come.title() + ", sorry but party canceled!")
guest_who_could_not_come = guests.pop()
print("Hi " + guest_who_could_not_come.title() + ", sorry but party canceled!")
guest_who_could_not_come = guests.pop()
print("Hi " + guest_who_could_not_come.title() + ", sorry but party canceled!")
guest_who_could_not_come = guests.pop()
print("Hi " + guest_who_could_not_come.title() + ", sorry but party canceled!")
print("\nHi " + guests[0].title() + ", I would like to invite you to my party!")
print("Hi " + guests[1].title() + ", I would like to invite you to my party!")
print("Here is number of guests: " + str(len(guests)) + ".")

# Remove by del
del guests[1]
del guests[0]
print(guests)
print("Here is number of guests: " + str(len(guests)) + ".")
