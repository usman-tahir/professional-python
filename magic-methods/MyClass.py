
class MyClass(object):
    def __new__(cls):
        instance = super(MyClass, cls).__new__(cls)
        print('The __new__ method is working')
        return instance

    def __init__(self):
        print('The __init__ method is working')
    
    def __eq__(self, other):
        return type(self) == type(other)
    
    def __del__(self):
        print('The __del__ method was called')

# Testing out initialization
m = MyClass()

# Testing out the equals operator
# print(MyClass() == MyClass()) # True
# print(MyClass() == 42) # False

# Testing out deletion/garbage collection
# When 'foo' is printed, the MyClass variable m
# is garbage collected
print("foo")