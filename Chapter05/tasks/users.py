# Special rule for 'admin' task 5.8
users= ['eric', 'alice', 'alex', 'admin']

for user in users:
    if user == 'admin':
        print('Hello ' + user + ', would you like to see a status report?')
    else:
        print('Hello ' + user.title() + ', thank you for logging again.')

