whilecode = input("Enter the customer's code: ")
beginread = int(input("Enter the customer's beginning meter reading: "))
endread = int(input("The customer's ending meter reading:             "))
print("\n")
water = endread - beginread

min = 0
max = 999999999
if (min <= beginread <= max) and (min <= endread <= max):
   if code.capitalize() == "R":  #Residential customers
       money = float(5.00 + (0.0005 * water))
   elif code.capitalize() == "C":   #Commercial customers
       if water > 4000000:
           water -= 4000000
           money = float(1000.00 + (0.00025 * water))
       elif water <= 4000000:
           money = float(1000.00)
   elif code.capitalize() == "I":     #Industrial customers
       if water <= 4000000:
           money = 1000.00
       elif 4000000 < water <= 10000000:
           money = 2000.00
       elif water > 10000000:
           water -= 10000000
           money = 2000.00 + (0.00025 * water)
   else:
       water = 0
       money = 0
else:
   water = 0
   money = 0
print(f"Customer code: {code}")
print(f"Beginning meter reading: {beginread}")
print(f"Ending meter reading:     {endread}")
if water == 0 or money == 0:
   print("Invalid Entry")
print(f"Gallons of water used:   {water:.1f}")
print(f"Amount billed:   ${money:.2f}")
