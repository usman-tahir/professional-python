
class MyClass(object):
    def __init__(self):
        print('The __init__ method is working')
    
    def __eq__(self, other):
        return type(self) == type(other)

# Testing out initialization
m = MyClass()

# Testing out the equals operator
print(MyClass() == MyClass()) # True
print(MyClass() == 42) # False