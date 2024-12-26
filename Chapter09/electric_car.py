from car import Car
from battery import Battery

class ElectricCar(Car):
    """Elictric car specifications"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

if __name__ == "__main__":
    my_tesla = ElectricCar('tesla', 'model s', 2016)
    print(my_tesla.get_disreptive())
    my_tesla.battery_size.describe_battery()
    my_tesla.battery_size.get_range()
    my_tesla.battery_size.update_battery()
    my_tesla.battery_size.describe_battery()
    my_tesla.battery_size.get_range()