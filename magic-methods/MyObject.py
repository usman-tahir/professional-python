
class MyObject(object):
    def __str__(self):
        return 'MyObject\'s str() method'

print(str(MyObject()))
print('This is %s' % MyObject())