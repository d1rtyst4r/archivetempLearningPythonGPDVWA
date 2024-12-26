class Car():
    """Simple car model"""
    def __init__(self,make : str, model : str, year : int):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_disreptive(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " milies on it.")

    def update_odometer(self, milage : int):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else: print("You can't roll back on odometer")

    def increment_odometer(self, miles : int):
        self.odometer_reading += miles  

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