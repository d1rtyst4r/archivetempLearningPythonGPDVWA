# input()

name = input("Please enter your name: ")
print("Hello, " + name.title() + '!')

prompt = "If you tell me your name, we can personalize the message you see."
prompt += "\nWhat is your first name: "
name = input(prompt)
print("\nHello, " + name.title() + "!")