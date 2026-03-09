''''a = 0
while a < 10:
    b=0
    while b <5:
        print('*', end=' ')
        b += 1
    print()
    a += 1'''

a = 0
while a < 100:
    b=0
    while b <40:
        if (a+b) % 2 == 0:
            print('*', end=' ')
        b += 1
    print()
    a += 1
