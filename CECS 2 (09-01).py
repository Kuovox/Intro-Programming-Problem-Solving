'''import math
#quadratic equation
a = float(input("Enter a "))
b = float(input("Enter b "))
c = float(input("Enter c "))

#determinant
d = b**2 - 4 * a * c
print("Delta=", d)

x1 = (-b + d**0.5)/(2*a)
x2 = (-b - math.sqrt(d))/(2*a)

print("The solution of equation", a, "x^2 +", b, "x +", c, " = ", x1)
print(f"The solution of equation {a} x^2 + {b} + {c} = {x2} ")'''

#Determine the fewest number of quarters, dimes, nickels, and pennies neccessary to make a certain amount of money
#Some time I have to use titeral values (constants)
QUARTER = 25
DIME = 10
NICKEL = 5
DOLLAR = 100
amount = float(input("How many dollars would you like to make into change? "))
numberOfCents = int(amount * DOLLAR)

print(f"${amount} is {numberOfCents} cents")

numberOfQuarters = numberOfCents // QUARTER
leftOver = numberOfCents%QUARTER

print(f"${amount} is {numberOfCents} cents {numberOfQuarters} and {leftOver}")

