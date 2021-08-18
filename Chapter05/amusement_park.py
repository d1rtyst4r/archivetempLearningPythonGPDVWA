# if-elif-else check
age = 12
if age < 4:  # only if this section is False than check next section
    print("Your admission cost 0$.")
elif age < 18:  # if it will be 'if'(not elif) it will check bought sections
    print("your admission cost 5$.")
else:
    print("Your admission cost 10$.")

age = 3
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost " + str(price) + "$.")
