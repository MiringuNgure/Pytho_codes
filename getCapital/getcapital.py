#Author: Peter Ngure
#Date: 1/3/2021


# function to get the countries capital
def getCapital(country):
    capital = input ("Enter capital of {}: ".format(country))
    return capital

# function to check which is longer between to strings
def longer(str1, str2):

    length1 = int (len(str1))
    length2 = int (len (str2))

    if (length1 > length2):
        result = str1
    else:
        result = str2
    return print (result)

# get the countries
country1 = input("Enter first country: ")
country2 = input ("Enter second country: ")

#output the longer of the two
longer(getCapital(country1),getCapital(country2))


