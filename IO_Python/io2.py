import sys

if (len (sys.argv)<3):
    print("not enough arguments, input two variables: ")
elif (len (sys.argv)>3):
    print ("too many arguments, input two variables")
else:
    s = int (sys.argv[1])
    t = int (sys.argv[2])
    answer= s+t
    print("The sum is: ", answer)