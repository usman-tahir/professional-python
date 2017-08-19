
import random

class Dice(object):
    """A class representing a dice with an arbitrary number
    of sides"""
    def __init__(self, sides = 6):
        self._sides = 6
    
    def roll(self):
        return random.randint(1, self._sides)
    
    def roll_times(self, number = 1):
        rolls = []
        for i in range(number):
            rolls.append(self.roll())
        return rolls

# Basic dice
d = Dice()

# Roll once
print(d.roll())

# Roll X times
print(d.roll_times(12))