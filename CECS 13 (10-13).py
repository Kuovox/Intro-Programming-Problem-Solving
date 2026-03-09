#Important: defining a function does not execute the code inside
#We must "call" the function, as we do with print, input, int, etc.
number = int(input("Enter a number: "))
abs_number = absolute_value(number)
print(f"The absolute value of {number} is {abs_number}")

def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num

'''def is_factor(dividend, divisor):
    if divided % divisor == 0:
        #print(f"{divisor} is a factor of {dividend}")
        return True
    else:
        #print(f"{divisor} is not a factor of {dividend}")
        return False
    
num = int(input("Enter the first value"))
denum = int(input("Enter the second value"))
factor = is_factor(num, denum)

if factor:
    print("{denum} is a factor of {num}")
else:
    print(print(f"{denum} is not a factor of {num}")'''

x = 185  #global               #Can't use global and local at the same time  #Global constants are okay, but global variable are not
print(f"{x} at the top")
def isValid(val):
    print(f"{x} in isValid function")
    print(f"{y} in isValid function")
    global x
    x = 34   #local
    val = 99
    if val < 0:
        val = 67
        return False
    else:
        return True

def getVal():
    #Description: this function should return a positive value
    #No parameter
    #return a positive integer
    val = int(input("Please enter a + value"))
    while not isValid(val):
        val = int(input("Please enter a + value"))
    return val
num= getVal()
print(num)

def funs(x):          #run time error for using a global variable as a parameter
    print(x)

#default oarameter, order
def nameLoc(name, location):
    print(f"Hello {name}, you are in {location}")

fName = input("What is your nam? ") 
loc = input("Where are you now? ")

#Inputs override the assigned parameter

nameLoc(fName, loc) or nameLoc(location = loc, name = fName)




#funs(2)






'''num = int(input("Enter a value: "))
while not isValid(num):
    num = int(input("Wrong entry! Please try again, enter a value: "))

#square
def square(num):
    '''Description: Calculate the square of a value one parameter num
return the square of my parameter'''
    return num * num

result = square(number)
print(f"The square of {number} is {result}")'''


