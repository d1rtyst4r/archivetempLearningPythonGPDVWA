class Restaurant():
    def __init__(self, restaurant_name :str, cuisine_type : str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title() + " and it is " + self.cuisine_type + " restarurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open!")
    
    def updadate_served(self, served_clients :int):
        self.number_served += served_clients
    
    def set_served(self):
        return self.number_served
    
    def increment_server(self, served : int):
        self.number_served +=served

fish_and_chips = Restaurant("Drunk Duck", "fish and chips")
print(fish_and_chips.restaurant_name)
print(fish_and_chips.cuisine_type)
fish_and_chips.describe_restaurant()
fish_and_chips.open_restaurant()

mcdonalds = Restaurant("Mcdonalds", 'fast food')
janitis = Restaurant('Janitis', 'pizza')
mcdonalds.describe_restaurant()
janitis.describe_restaurant()
print(str(janitis.set_served()))
janitis.updadate_served(14)
janitis.increment_server(15)
print(str(janitis.set_served()))