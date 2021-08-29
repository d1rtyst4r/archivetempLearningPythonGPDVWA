# cycle while

current_number = 1
while current_number <= 5:  # while TRUE!!!
    print(current_number)
    current_number += 1

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # skip next part of cycle and return to the begin of cycle
    print(current_number)

