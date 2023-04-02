def make_car(brand, model, **aditional_information):
    """Create dictionary with car information"""
    information ={}
    information['brand'] = brand
    information['model'] = model
    for key, value in aditional_information.items():
        information[key] = value
    return information


car = make_car('subaru', 'outback', color='red',tow_packing=True, price=36000)
print(car)
