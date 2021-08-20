current_users = ['alex', 'alec', 'rita', 'admin', 'erica']
new_users = ['alex', 'rita', 'robert', 'same', 'john']

if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print('Sorry, this user exists, try something else.')
        else:
            print('Welcome ' + user + '. Thank you for registration!')
