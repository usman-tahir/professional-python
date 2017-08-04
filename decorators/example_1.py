
def decorated_by(func):
    func.__doc__ += '\nDecorated by the decorated_by function'
    return func

def also_decorated_by(func):
    func.__doc__ += '\nDecorated by the also_decorated_by function'
    return func

# Preferred way of decoration
@also_decorated_by
@decorated_by
def add(x, y):
    '''Return the sum of x and y'''
    return x + y

# add = decorated_by(add)
help(add)
