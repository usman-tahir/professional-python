
class Animal(object):
    """A class for representing an arbitrary animal"""
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        pass
    
    def go_to_vet(self):
        pass

class Cat(Animal):
    def meow(self):
        pass
    
    def purr(self):
        pass