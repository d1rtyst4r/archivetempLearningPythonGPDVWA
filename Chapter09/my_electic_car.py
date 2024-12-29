from electric_car import ElectricCar

if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_disreptive())
    my_tesla.battery_size.describe_battery()
    my_tesla.battery_size.get_range()
    my_tesla.battery_size.update_battery()
    my_tesla.battery_size.describe_battery()
    my_tesla.battery_size.get_range()