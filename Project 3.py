print("Welcome to the vending machine change maker program")
print("Change maker initialized.")
print("Stock contains: ")
print("     25 nickels")
print("     25 dimes")
print("     25 quarters")
print("     0 ones")
print("     0 fives\n")

price = float(input("Enter the purchase price(xx.xx) or 'q' to quit: "))

if (round(price * 100, 2)) <= 0 or (round(price * 100, 2)) % 5 != 0:
        print("Illegal price: Must be a non-negative multiple of 5 cents.")
        price = (input("Enter the purchase price(xx.xx) or 'q' to quit: "))
   
print("\n")
print('Menu for deposits:')
print("  'n' - deposit a nickel")
print("  'd' - deposit a dime")
print("  'q' - deposit a quarter")
print("  'o' - deposit a one dollar bill")
print("  'f' - deposit a five dollar bill")
print("  'c' - cancel the purchase")

print('\n')

n = (0.05 * 100)
d = (0.1 * 100)
q = (0.25 * 100)
o = (1 * 100)
f = (5 * 100)

calculation = (price * 100)

print(f'Payment due: {int(calculation // 100)} dollars and {int(calculation % 100)} cents')

exchange = input("Indicate your deposit: ")

nickel = calculation - n
dime = calculation - d
quarter = calculation - q
one = calculation - o
five = calculation - f
    
while exchange != 'n' and exchange != 'd' and exchange != 'q' and exchange != 'o' and exchange != 'f' and exchange != 'c':
        print("Illegal selection:", exchange)
        exchange = input("Indicate your deposit: ")
        break

if round(calculation / 100, 2) > 1:
      if exchange == 'f':
          print(f"Payment due: {int(five // 100)} dollars and {int(five % 100)} cents")
      elif exchange == 'o':
         print(f"Payment due: {int(one // 100)} dollars and {int(one % 100)} cents")
      elif exchange == 'q':
         print(f"Payment due: {int(quarter // 100)} dollars and {int(quarter % 100)} cents")
      elif exchange == 'd':
         print(f"Payment due: {int(dime // 100)} dollars and {int(dime % 100)} cents")
      elif exchange == 'n':
         print(f"Payment due: {int(nickel // 100)} dollars and {int(nickel % 100)} cents")
elif round(calculation // 100) <= 1:
      if exchange == 'f':
          print(f"Payment due: {int(five % 100)} cents") 
      elif exchange == 'o':
         print(f"Payment due: {int(one % 100)} cents")
      elif exchange == 'q':
         print(f"Payment due: {int(quarter % 100)} cents")
      elif exchange == 'd':
         print(f"Payment due: {int(dime % 100)} cents")
      elif exchange == 'n':
         print(f"Payment due: {int(nickel % 100)} cents")
else:
   print(quit)
