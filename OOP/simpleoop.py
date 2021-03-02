class Date:

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        infor = f"{self.day}.{self.month}.{self.year}"
        return infor
    
d2 = Date(12,23,2020)
print (d2)