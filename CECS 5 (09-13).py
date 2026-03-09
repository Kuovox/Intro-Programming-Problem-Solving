num = int(input("Enter an integer value...."))

if num == 0:
    print("Skip division operation")
if num != 0:
    x = 24/num
#application to detemine if the number is odd or even
    
'''if num % 2 == 1:
    print("Fizz")
else:
    print("Buzz")
print('The end....')'''

'''if num % 3 == 0:
    print("Fizz")
else:
    if num % 5 == 0:
        print("Buzz")
    else:
        if num % 15 ==0:
            print("FizzBuzz")
        else:
            print(num)'''

if num % 15 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print(num)

name1 = "Adam"
name2 = "am"
flag = name1<name2
flag = -10
print(flag)
if flag:
    print("True")
else:
    print("False")
