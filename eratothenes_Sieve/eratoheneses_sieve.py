num = int (input ("Enter the number: "))
numbers = []
for i in range(2,num+1):
    numbers.append(i)

for val in numbers:
    if (val**2 <= num):
        for loopVal in numbers: 
            if (loopVal>val and loopVal%val==0):
                j = numbers.index(loopVal)
                del numbers[j]
print(numbers)
