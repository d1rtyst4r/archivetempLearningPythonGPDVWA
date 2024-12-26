from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Simple ice cream stand model"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flovers = ['cream', 'chocolate','vanila']

    def get_flovers(self):
        """print ice cream flowers to consol"""
        print("We have this flowers:")
        for flover in self.flovers:
            print("\t" + flover.title())

if __name__ == '__main__':
    my_ice_cream_stand = IceCreamStand("Milk bar", 'ice cream stand')
    my_ice_cream_stand.get_flovers()