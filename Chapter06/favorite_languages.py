favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Only keys
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title())


for name in sorted(favorite_languages.keys()):
    print((name.title()) + ', thank you for taking the poll.')

# set

for language in set(favorite_languages.values()):  # set saves information without duplicates
    print(language.title())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c++'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())

