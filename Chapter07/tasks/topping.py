# task 7-4

topping = "PLease enter topping for your pizza!"
topping += "\nPrint 'quit' foe ending the order!"

while True:
    order = input(topping)
    if order == 'quit':
        print("End of your order!")
        break
    else:
        print("Adding " + order + " to your pizza")