def greet_users(users):
    """Return simple greeting for users"""
    for name in users:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
