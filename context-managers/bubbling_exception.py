
class BubbleExceptions(object):
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_instance, traceback):
        if exception_instance:
            print('Bubbling up exception: %s' % exception_instance)
        return False

with BubbleExceptions():
    print(5 + 5)

with BubbleExceptions():
    print(5 / 0)
