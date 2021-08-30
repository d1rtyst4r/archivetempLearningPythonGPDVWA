# Task 7-8, 7-9

sandwich_orders = ['tuna', 'pastrami', 'chicken', 'vegan', 'pastrami', 'vegan', 'pastrami']
finished_sandwiches = []

print("Sorry, but we don't have pastrami ")
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    if finished_sandwich == "pastrami":
        continue
    else:
        print("I made your " + finished_sandwich + ".")
        finished_sandwiches.append(finished_sandwich)

print("\nI have made this sandwiches: ")
for sandwich in finished_sandwiches:
    print("\t" + sandwich + " sandwich;")