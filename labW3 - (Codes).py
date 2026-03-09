num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operator = input("enter operator: ")

if(operator == '+'):
    resultNum = num1 + num2
elif(operator == '-'):
    resultNum = num1 - num2
elif(operator == '*'):
    resultNum = num1 * num2
elif(operator == '/'):
    resultNum = num1/ num2
elif(operator == '// '):
    resultNum = num1 // num2
elif(operator == '%'):
    resultNum = num1 % num2
elif(operator == '^'):
    resultNum = num1 ^ num2

print(resultNum)
    
