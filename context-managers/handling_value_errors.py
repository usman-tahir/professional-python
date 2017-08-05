
class HandleValueError(object):
    def __enter__(self):
        return self
    
    def __exit__(self, exception_type, exception_instance, traceback):
        # Return true if there is no exception
        if not exception_type:
            return true
        
        # If this is a ValueError, handle it and return True
        if issubclass(exception_type, ValueError):
            print('Handling ValueError: %s' % exception_instance)
            return True
        
        # Propagate any other errors
        return False

with HandleValueError():
    raise ValueError('Wrong value.')

with HandleValueError():
    raise TypeError('Wrong type.')