from date import Date


d = int(input("Day: "))
m = int (input ("Month: "))
y = int(input ("year: "))

d1 = Date(d,m,y)
print("Entered: ", d1)