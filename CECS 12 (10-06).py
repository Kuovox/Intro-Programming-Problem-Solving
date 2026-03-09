'''for h in range (24):
    for m in rage (60):
        for s in range (60):
            print(f"{h}:{m}:{s}")'''

print ("Done")
print(1,2,3)
print(1,2,3, sep="*")
print("At a new line")

print(1,2,3, end="*")
print("At the same line")

for i in range (5):       # 0 to 4
    print(i, end=" ")
print('$$$$$$$')

for i in range (5):
    #print(i, end=" ")
    print(i) #, end=" ")

for i in range (9, 15): # 9 to 14
    print(i, end= " ")

for i in range(9, 25, 3): #9, 12, 15....24
    print(i, end= " ")
print()


for i in range(19, 15, -1): #9,..... 14)
    print(i, end= " ")
print()

for i in range(19, 15, -1): #9,..... 14)
    if i % 2 == 0:
        continue        #skip that iteration
    print(i, end= " ")
print()

for i in range(19, 15, -1): #9,..... 14)
    if i % 2 == 0:
        break        #stop the loop
    print(i, end= " ")
print()
