def fibonacci (fmax):
    a,b = 1,1
    while a < fmax:
        yield a
        a,b = b , a+b
for f in fibonacci(1000):
    print(f, end =  " ")