
class SuppressExceptions(object):
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_instance, traceback):
        if exception_instance:
            print('Suppressing exception: %s' % exception_instance)
        return True

with SuppressExceptions():
    print(5 + 5)

with SuppressExceptions():
    print(5 / 0)

with SuppressExceptions():
    try:
        print(5 / 0)
    except ZeroDivisionError:
        print('Exception caught within context block.')