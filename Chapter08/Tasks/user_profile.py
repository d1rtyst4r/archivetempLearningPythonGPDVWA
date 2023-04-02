def build_prifile(first, last, **user_info):
    """Create dictinary with user profile."""
    profile ={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = str(value)
    return profile    

user_prifile = build_prifile('ruslans', 'jasinovics', age=36, location='riga', field='IT')

print(user_prifile)