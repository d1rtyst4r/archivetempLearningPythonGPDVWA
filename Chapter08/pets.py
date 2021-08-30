def describe_pet(pet_name, animal_type='dog'):  # default values for arguments
    """Print information about pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('loki', 'cat')
describe_pet('harry', 'hamster')
