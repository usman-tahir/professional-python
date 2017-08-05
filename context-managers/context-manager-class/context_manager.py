
class ContextManager(object):
    def __init__(self):
        self.entered = False
    
    def __enter__(self):
        self.entered = True
        return self
    
    def __exit__(self, exception_type, exception_instance, traceback):
        self.entered = False
        # Exception handling, etc.

# Not entering a context
content_manager = ContextManager()
print(content_manager.entered) # False

# Entering a context
with content_manager:
    print(content_manager.entered)
print(content_manager.entered)