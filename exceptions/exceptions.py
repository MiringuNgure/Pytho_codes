import random

def f():
    r = random.randint(1,5)
    if r ==1:
        print ("will not raise an exception")
    elif r ==2:
        print ("will raise a DivisionByZero error exception")
        wrong = 1/0
    elif r ==3:
        print ("will raise a NameError exception")
        wrong = a/b
    elif r==4:
        print ("will raise an OverflowError exception")
        wrong = 2.0 **100000
    else:
        print("will raise a ValueError")
        wrong = int ("abc")

try:
    f()
except ZeroDivisionError as e:
    print("caught ZeroDivisionError: ", e)
except (NameError, OverflowError) as e:
    print("caught NameError or OverflowError ", e)
except:
    print ("caught something maybe a ValueError or anything else")
else:
    print("caught nothing")
finally:
    print("this part is always executed")
