from restaurant import Restaurant

if __name__ == '__main__':
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