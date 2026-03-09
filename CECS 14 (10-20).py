import math
print(f"Pi is {math.pi}")
print(f"{5} Factorial is {math.factorial(5)}")
#Calculate Pi

def piCal(n):
    i = 0
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += 4 / (2*i + 1)
        else:
            sum -= 4 / (2*i + 1)
    return sum #will have the value of Pi
print(piCal(100))

#or

def piCal(n):
    i = 0
    sum = 0
    for i in range(n)
        sum += (-1)**i *4 / (2*i + 1)
    return sum #will have the value of Pi
print(piCal(100))

print("Calculating factorial")
def facts(n):
    for i in range(1, n+1):
        fac *= i
    return fac

print(facts(5))


print("Calculating factorial")
def facts(n):
    if n == 0:
        return 1
    else:
        return (n * facts(n-1))

print(facts(5))
