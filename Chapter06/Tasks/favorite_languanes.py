users = ['eric', 'jen', 'ruslan']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'python'
}
for user in users:
    if user not in favorite_languages.keys():
        print(user.title() + " please take a roll!")
