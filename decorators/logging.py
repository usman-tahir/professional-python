
import functools
import logging
import time

def logged(method):
    '''Cause the decorated method to be run and its results logged, along
    with other diagnostic information'''
    @functools.wraps(method)
    def inner(*args, **kwargs):
        start = time.time()

        return_value = method(*args, **kwargs)

        end = time.time()

        delta_time = end - start
    
        # Log the method call and the result
        logger = logging.getLogger('decorater.logged')
        logger.warn('Called method %s at %.02f; execution time %.02f seconds; result %r'
            % (method.__name__, start, delta_time, return_value))
    
        # Return the method's original value
        return return_value
    return inner

@logged
def sleep_and_return(return_value):
    time.sleep(2)
    return return_value

sleep_and_return(100)