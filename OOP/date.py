class Date:
    stdYear = 1970
    daysPerMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    def __init__(self, d=1, m=1, y=stdYear):
        self.day = d
        self.month = m
        self.year = y
        self.checkDate()
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return self.day == other.day and self.month ==other.month and self.year==other.year
    
    @staticmethod
    def isLeapYear(year):
        return (year%4==0 and year % 100 ==0 or year%400==0)
    
    def checkDate(self):
        if (self.year < 1 or self.month <1 or self.month>12 or self.day<1
        or (self.day > Date.daysPerMonth[self.month-1]
        and not (self.day == 29 and self.month == 2))):

            self.day = 1
            self.month = 1
            self.year = Date.stdYear

    def incDay(self):
        self.day += 1
        if (self.day > date.daysPerMonth[self.month - 1]
            and not (self.day == 29 and self.month ==2 and self.isLeapYear(year))):
                self.day = 1
                self.month += 1

                if self.month > 12:
                    self.month = 1
                    self.year += 1
        return self

d1 = Date(12,-1,2020)
d2 = Date (12,12,2010)
print(d1)
print (d1==d2)
print(Date.isLeapYear(1970))
