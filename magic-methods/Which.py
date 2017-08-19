
class Which(object):
    def __str__(self):
        return 'string'
    
    def __unicode__(self):
        return u'unicode'

print(u'The %s conversion was performed.' % Which())
print('The %s conversion was performed' % Which())
