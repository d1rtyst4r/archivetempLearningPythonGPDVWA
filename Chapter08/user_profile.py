def build_prifile(first, last, **user_info):
    """Create dictinary with user profile."""
    profile ={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile    

user_prifile = build_prifile('alber', 'einstein', location='princeton', field='physics')

print(user_prifile)