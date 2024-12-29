from random import randint

class Die():
    """Simple dies model"""
    def __init__(self, sides :int):
        self.sides = sides

    def roll_die(self):
        """Simple dies roll simulation"""
        roll = randint(1, self.sides)
        print(roll)

