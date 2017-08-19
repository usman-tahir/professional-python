
class MyClass(object):
    # def __new__(cls):
    #     instance = super(MyClass, cls).__new__(cls)
    #     print('The __new__ method is working')
    #     return instance

    # def __init__(self):
    #     print('The __init__ method is working')
    
    def __eq__(self, other):
        print('The following are being tested for equivalence:\n%r\n%r' % (self, other))
        return self is other
    
    # def __del__(self):
    #     print('The __del__ method was called')

class Unequal(object):
    def __eq__(self, other):
        return False

class MySubclass(MyClass):
    def __eq__(self, other):
        print('MySubclass\' __eq__ method is testing:\n%r\n%r' % (self, other))
        return False

# Testing out initialization
# m = MyClass()

# Testing out the equals operator
# print(MyClass() == MyClass()) # True
# print(MyClass() == 42) # False

# Testing out deletion/garbage collection
# When 'foo' is printed, the MyClass variable m
# is garbage collected
# print("foo")

c1 = MyClass()
c2 = MyClass()
print(c1 == c2)
print(c2 == c1)
print(c1 == c1)

print(MyClass() == Unequal())
print(Unequal() == MyClass())

print(MyClass() == MySubclass())
print(MySubclass() == MyClass())