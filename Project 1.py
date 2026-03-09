print("Richter \t \tJoules \t \t \t TNT")
print("1 \t 1995262.3149688789 \t \t   0.00047687913837688307")
print("5 \t 1995262314968.8828\t\t476.87913837688404")
print("9.1 \t 2.818382931264449e+18 \t 673609687.2046962")
print("9.2 \t 3.981071705534953e+18 \t 951498973.5982201")
print("9.5 \t 1.1220184543019653e+19\t2681688466.3048882\n")

import math   #Importing the math module to calculate the Richter scale measurement
rScale= float(input("Please enter a Richter scale value: "))   
print("Richter scale value:", rScale)

sum = (1.5*rScale) + 4.8
energy = math.pow(10, sum)     #Calculating Richter scale measurement in joules
tonsOfTnT= energy / (4.184*(10**9))   #Calculating Richter scale measurement in tons of TnT

print("Equivalence in joules:", energy)
print("Equivalence in tons of TNT:", tonsOfTnT)
















