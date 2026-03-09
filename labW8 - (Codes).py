'''for index in range(1,6):
        print(index)'''
        
result = []
for k in range(2, 200):
    if (k % 7 == 0):
        result.append(str(k))
print(' , '.join(result))
        
