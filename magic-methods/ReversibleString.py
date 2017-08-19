
class ReversibleString(object):
    def __init__(self, s):
        self.s = s
    
    def __invert__(self):
        return type(self) (self.s[::-1])
    
    def __repr__(self):
        return 'ReversibleString: %s' % self.s
    
    def __str__(self):
        return self.s

rs = ReversibleString('the quick brown fox jumped over the lazy dogs')
print(str(rs))
print(~rs)
print(~~rs)