
import functools

def requires_user(func):
    @functools.wraps(func)
    def inner(user, *args, **kwargs):
        '''Verify that the user is truthy; if so, run the decorated method,
        and if not, raise ValueError'''
        if user and isinstance(user, User):
            return func(user, *args, **kwargs)
        else:
            raise ValueError('A valid user is required to run this program.')
    return inner

class User(object):
    '''A representation of a user'''

    def __init__(self, username, email):
        self.username = username
        self.email = email

class AnonymousUser(User):
    '''An anonymous user (a stand in for an actual user that is not actually)
    a user'''

    def __init__(self):
        self.username = None
        self.email = None

    def __nonzero__(self):
        return False
