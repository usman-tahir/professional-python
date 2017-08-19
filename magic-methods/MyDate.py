
from datetime import datetime

class MyDate(datetime):
    def __format__(self, spec_str):
        if not spec_str:
            spec_str = '%Y-%m-%d %H:%M:%S'
        return self.strftime(spec_str)

md = MyDate(2012, 4, 21, 11)
print('{0}'.format(md)) # default formatting from the format method above
print('{0:%Y-%m-%d}'.format(md)) # specified formatting for spec_str