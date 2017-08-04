
class Registry(object):
    def __init__(self):
        self._functions = []

    def register(self, decorated):
        self._functions.append(decorated)
        return decorated

    def run_all(self, *args, **kwargs):
        return_values = []
        for function in self._functions:
            return_values.append(function(*args, **kwargs))
        return return_values

# Usage of the Registry class
a = Registry()
b = Registry()

@a.register
def foo(x = 3):
    return x

@b.register
def bar(x = 5):
    return x

@a.register
@b.register
def baz(x = 7):
    return x

# Run the registry methods
print("run all for @a: " + str(a.run_all()))
print("run all for @b: " + str(b.run_all()))
