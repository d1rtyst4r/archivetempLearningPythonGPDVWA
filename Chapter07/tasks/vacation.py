# Task 7-10

vacation = {}

poll_active = True
while poll_active:
    name = input("Please enter your name: ")
    vacation[name] = input("Please enter your next place for vacation :")
    repeat = input("Do you have any person for the poll? (yes/no) ")
    if repeat == 'no':
        poll_active = False

print("\n--- Poll results ---")
for name, answer in vacation.items():
    print(name.title() + " would like to go to " + answer + ".")
