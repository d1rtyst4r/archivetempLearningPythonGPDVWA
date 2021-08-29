# even or odd
number = input("Enter number and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print("\nYour number " + str(number) + " is even.")
else:
    print("\nYour number " + str(number) + " is odd.")