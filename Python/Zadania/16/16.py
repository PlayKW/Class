#imports
from math import sqrt


#max:
def max(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

#min
def min(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

#isOdd
def isOdd(num):
    return num%2==0

#absolute
def absolute(num):
    return sqrt(num**2)

#sum
def sum(*ings):
    result = 0
    for x in ings:
        result += x
    return result
