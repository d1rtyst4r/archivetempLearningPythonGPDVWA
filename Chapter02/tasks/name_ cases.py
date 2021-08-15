first_name = "eric"
print("Hello " + first_name.title() + ", " + "would you like to learn some Python today?")

print(first_name.title())
print(first_name.lower())
print(first_name.upper())

first_name = "albert"
second_name = "einstein"
message = first_name.title() + " " + second_name.title() + " once said, "\
                                                           + '"A person who never made a mistake ' \
                                                             'never tried anything new."'

print(message)

name = "\t name "
print(name)
print(name.lstrip())  # also remove \t
print(name.rstrip())
print(name.strip())  # also remove \t
