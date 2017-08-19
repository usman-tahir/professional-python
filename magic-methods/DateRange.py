from datetime import date

class DateRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __contains__(self, needle):
        return self.start <= needle <= self.end

dr = DateRange(date(2015, 1, 1), date(2015, 12, 31))
print(date(2015, 4, 21) in dr)
print(date(2012, 4, 21) in dr)