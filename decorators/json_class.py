import functools
import json

class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message
    
    def __str__(self):
        return self._message
    
    def json_output(decorated):
        '''Run the decorated function, serialize the result of that function
        to JSON, and return the JSON string'''
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as e:
                result = {'status': 'error', 'message': str(e)}
            retrun json.dumps(result)
        return inner
    
    @json_output
    def error():
        raise JSONOutputError('Error handling JSON input.')