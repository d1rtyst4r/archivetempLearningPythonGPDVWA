class Dog():
    """Simple dog model"""
    def __init__(self, name :str, age : int):
        self.name = name
        self.age = age

    def site(self):
        """Dog site after commnad"""
        print(self.name.tittle() + " is now sitting.")
    def roll_over(self):
        """Dog roll over after command"""
        print(self.name.tittle() + " is rolled over!")


my_dog = Dog("willie", 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")