class Battery():
    """Simple battery model"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """print information about battery"""
        print("This car has " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go opproximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85

if __name__ == '__main__':
    battery = Battery()
    battery.describe_battery()
    battery.get_range()
    battery.update_battery()
    battery.describe_battery()