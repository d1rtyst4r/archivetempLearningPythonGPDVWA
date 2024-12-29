from car import Car

if __name__ == "__main__":    
    my_car = Car('audi', 'a4', 2016)
    print(my_car.get_disreptive())
    my_car.update_odometer(23)
    my_car.read_odometer()

    my_used_car = Car('subaru', 'outback', 2013)
    my_used_car.update_odometer(23500)
    my_used_car.increment_odometer(100)
    print(my_used_car.get_disreptive())
    my_used_car.read_odometer()