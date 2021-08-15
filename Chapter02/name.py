name = "ada lovelace"
print(name.title())  # changing first letter to upper

name = "Ada Lovelace"
print(name.upper())  # changing all letters to upper
print(name.lower())  # changing all letters to lower

first_name = "ada"
second_name = "lovelace"
full_name = first_name + " " + second_name  # String concatenation
print(full_name.title())
print("Hello" + ", " + full_name.title() + "!")

message = "Hello, " + first_name.title() + " " + second_name.title() + "!"  # Concatenation using variable
print(message)
