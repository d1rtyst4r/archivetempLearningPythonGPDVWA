# task 7-5

age = int(input("PLease enter your age: "))
if age < 3:
    price = 0
elif age < 12:
    price = 10
else:
    price = 15

if price == 0:
    print("You entrance ticket is free!")
else:
    print("Your entrance ticket price is " + str(price) + "$.")
