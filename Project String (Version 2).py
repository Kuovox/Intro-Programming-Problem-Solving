#Input
k1 = input('')
k2 = input('')
k3 = input('')
k4 = input('')
k5 = input('')
k6 = input('')
k7 = input('')
k8 = input('')

#A
def reverse(sentence):
    phase = sentence[::-1]
    print(f'{phase}\n')


#B 
def remove(sentence, letter):
    result = ""
    for k in sentence:
        if not (k.lower() == letter):
            result += k
    print(f'{result}\n')


#C
def analyze(sentence):
    eCounter = 0
    charCounter = 0
    phase = sentence.lower()
    for k in sentence:
        if not k.isalpha():
            continue
        charCounter += 1
        if k.lower() == 'e':
            eCounter += 1
    print(f"Your text contains {charCounter} alphabetic characters, of which {eCounter} ({((eCounter / charCounter) * 100):0.1f}%) are 'e'.\n")



#D
def duplicate(sentence, character):
    count = 0
    for k in sentence:
        if (k.lower() == character):
            count += 1
    print(f"Character 'e': {count}\n")


#E
def noWord(sentence):
    for k in sentence:
        if (k.lower() == 'e'):
            print('False', end=", ")
        else:
            print('True', end=", ")
    print('\n')


#F
def noCharacter(sentence, letter):
    for k in sentence:
        if (k.lower() == letter):
            print('False', end=", ")
        else:
            print('True', end=", ")
    print('\n')



#G
def noE(sentence):
    count = 0
    for word in sentence:
        word = word.lower().strip()
        if not 'e' in word:
            count += 1
            print(word, end=" ")
    print(f' = {((count / 745) * 100):0.1f}%')
    print('\n')

#H
def avoids(sentence, forbidden):
    for k in sentence:
        if forbidden in sentence:
            print('False', end=", ")
    print('True', end=", ")


#I
def uses_only(word, sentence):
    for k in word:
        if k not in sentence:
            print('False', end=", ")
        print('True', end=", ")


#J
def uses_all(word, sentence):
    for k in sentence:
        if k not in word:
            print('False', end=", ")
        print('True', end=", ")

#K
def is_abecedarian(sentence):
    count = 0
    while count <len(sentence)-1:
        if sentence[count]>sentence[count + 1]:
            print('False', end=", ")
        count += 1
    print('True', end=", ")

#L
def find(sentence, character):
    result = -1
    count = 0
    for k in range(len(sentence)):
        if (sentence[k] == character):
            count += 1
            result = count
    print(f'{result}\n')
    

#M
def findIndex(sentence, word, index):
    while index < len(sentence):
        if sentence[index] == word:
            print(index, end=", ")
        index += 1

#N
def is_sorted(sentence):
    for index, item in enumerate(sentence):
        try:
            if item > sentence[index + 1]:
                print('False', end=", ")
        except IndexError:
            print('True', end=", ")
    print('\n')


#O
def is_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        print('True', end=" ")
    else:
        print('False', end=" ")
    print('\n')

#P
def has_duplicates(sentence):
    phase = {k:sentence.count(k) for k in sentence}
    print(f'{phase}\n')


#Q
def remove_duplicates(sentence):
    new = sentence.split()
    k = []
    for v in new:
        if (sentence.count(v) >= 1 and (v not in k)):
            k.append(v)
    print(' '.join(k))


#Ouput
reverse(k1)
reverse(k2)
reverse(k3)
reverse(k4)
reverse(k5)
reverse(k6)
reverse(k7)
reverse(k8)



remove(k1, 'e')
remove(k2, 'e')
remove(k3, 'e')
remove(k4, 'e')
remove(k5, 'e')
remove(k6, 'e')
remove(k7, 'e')
remove(k8, 'e')


analyze(k1)
analyze(k2)
analyze(k3)
analyze(k4)
analyze(k5)
analyze(k6)
analyze(k7)
analyze(k8)


duplicate(k1, 'e')
duplicate(k2, 'e')
duplicate(k3, 'e')
duplicate(k4, 'e')
duplicate(k5, 'e')
duplicate(k6, 'e')
duplicate(k7, 'e')
duplicate(k8, 'e')

noWord(k1)
noWord(k2)
noWord(k3)
noWord(k4)
noWord(k5)
noWord(k6)
noWord(k7)
noWord(k8)


noCharacter(k1, 'e')
noCharacter(k2, 'e')
noCharacter(k3, 'e')
noCharacter(k4, 'e')
noCharacter(k5, 'e')
noCharacter(k6, 'e')
noCharacter(k7, 'e')
noCharacter(k8, 'e')


noE(k1)
noE(k2)
noE(k3)
noE(k4)
noE(k5)
noE(k6)
noE(k7)
noE(k8)


avoids(k1,'the')
avoids(k2,'the')
avoids(k3,'the')
avoids(k4,'the')
avoids(k5,'the')
avoids(k6,'the')
avoids(k7,'the')
avoids(k8,'the')


uses_only('name', k1)
uses_only('name', k2)
uses_only('name', k3)
uses_only('name', k4)
uses_only('name', k5)
uses_only('name', k6)
uses_only('name', k7)
uses_only('name', k8)



uses_all('aeiou', k1)
uses_all('aeiou', k2)
uses_all('aeiou', k3)
uses_all('aeiou', k4)
uses_all('aeiou', k5)
uses_all('aeiou', k6)
uses_all('aeiou', k7)
uses_all('aeiou', k8)


is_abecedarian(k1)
is_abecedarian(k2)
is_abecedarian(k3)
is_abecedarian(k4)
is_abecedarian(k5)
is_abecedarian(k6)
is_abecedarian(k7)
is_abecedarian(k8)


find(k1, 'a')
find(k2, 'a')
find(k3, 'a')
find(k4, 'a')
find(k5, 'a')
find(k6, 'a')
find(k7, 'a')
find(k8, 'a')


findIndex(k1, 'a', 4)
findIndex(k2, 'a', 4)
findIndex(k3, 'a', 4)
findIndex(k4, 'a', 4)
findIndex(k5, 'a', 4)
findIndex(k6, 'a', 4)
findIndex(k7, 'a', 4)
findIndex(k8, 'a', 4)


is_sorted(k1)
is_sorted(k2)
is_sorted(k3)
is_sorted(k4)
is_sorted(k5)
is_sorted(k6)
is_sorted(k7)
is_sorted(k8)

is_anagram(k1, 'care')
is_anagram(k2, 'care')
is_anagram(k3, 'care')
is_anagram(k4, 'care')
is_anagram(k5, 'care')
is_anagram(k6, 'care')
is_anagram(k7, 'care')
is_anagram(k8, 'care')


has_duplicates(k1)
has_duplicates(k2)
has_duplicates(k3)
has_duplicates(k4)
has_duplicates(k5)
has_duplicates(k6)
has_duplicates(k7)
has_duplicates(k8)

remove_duplicates(k1)
remove_duplicates(k2)
remove_duplicates(k3)
remove_duplicates(k4)
remove_duplicates(k5)
remove_duplicates(k6)
remove_duplicates(k7)
remove_duplicates(k8)

