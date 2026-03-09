string = input('Please enter your name: ')

#Part 1:

#1
def allCharacters(sentence):
    count = 0
    for k in (sentence[::]):
        count += 1
    print(f'Your name is {count} characters long.\n')

#2
def lastCharacter (sentence):
    sentence = sentence[-1]
    print(f'The last character is: {sentence}\n')

#3
def letterE (sentence):
    position = 0
    character = 'e'
    while (position != len(sentence)) and (sentence[position] != character):
        position += 1
    if position == len(sentence):
        print(0)
    else:
        print(f"The first 'e' is at position {position + 1}.\n")
        
#4
def countWords(sentence):
    words = sentence.split()
    print(f'Your name has {len(words)} words.\n')

#5
def firstWord(sentence):
    word = sentence.split()[0]
    print(f'Your first name is {word}.\n')

#6
def numberVowels(sentence):
    numVowels = 0
    for k in sentence:
        if k in "aeiouAEIOU":
            numVowels += 1
    print(f'Your name contains {numVowels} vowels. \n')
    
#7
def capitalizeVowels(sentence):
    phase = ""
    for k in sentence:
        if k in "aeiouAEIOU":
            word = k.upper()
            phase += word
        else:
            phase += k.lower()
    print(f'Your name with uppercase vowels is: {phase}\n')

#8
def center(sentence):
    phase = sentence.center(50, '~')
    print(f'{phase.center(70, "+")}\n')

#9
def split(sentence):
    print(sentence[:len(sentence)//2]+'***************************************'+sentence[len(sentence)//2:])
    print('\n')

#Part 2:
#A
def reverse(sentence):
    phase = sentence[::-1]
    print(f'{phase}\n')

#B 
def remove(sentence, letter):
    result = ""
    for k in sentence:
        if not (k == letter):
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
        if k == 'e':
            eCounter += 1
    print(f"Your text contains {charCounter} alphabetic characters, of which {eCounter} ({((eCounter / charCounter) * 100):0.1f}%) are 'e'.\n")

#D
def duplicate(sentence, character):
    count = 0
    for k in sentence:
        if (k == character):
            count += 1
    print(f"Character 'e': {count}\n")

#E
def noWord(sentence):
    for k in sentence:
        if (k == 'e'):
            print('False', end=", ")
        else:
            print('True', end=", ")
    print('\n')

#F
def noCharacter(sentence, letter):
    for k in sentence:
        if (k == letter):
            print('False', end=", ")
        else:
            print('True', end=", ")
    print('\n')

#G
def noE(sentence):
    count = 0
    for word in sentence:
        word = word.strip()
        if not 'e' in word:
            count += 1
            print(word, end=" ")
    print(f' = {((count / 24) * 100):0.1f}%')
    print('\n')
    
#H
def avoids(sentence, forbidden):
    for k in sentence:
        if forbidden in sentence:
            print(f'{False}\n')
    print(f'{True}\n')

#I
def uses_only(word, sentence):
    for k in word:
        if k not in sentence:
            print(f'{False}\n')
        print(f'{True}\n')

#J
def uses_all(word, sentence):
    for k in sentence:
        if k not in word:
            print(f'{False}\n')
        print(f'{True}\n')

#K
def is_abecedarian(sentence):
    count = 0
    while count <len(sentence)-1:
        if sentence[count]>sentence[count + 1]:
            print(f'{False}\n')
        count += 1
    print(f'{True}\n')

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
            print(f'{index}\n')
        index += 1

#N
def is_sorted(sentence):
    for index, item in enumerate(sentence):
        try:
            if item > sentence[index + 1]:
                print('False', end=", ")
        except IndexError:
            print('True', end=" ")
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
    
allCharacters(string)
lastCharacter(string)
letterE(string)
countWords(string)
firstWord(string)
numberVowels(string)
capitalizeVowels(string)
center(string)
split(string)

reverse(string)
remove(string, 'h')
analyze(string)
duplicate(string, 'e')
noWord(string)
noCharacter(string, 'e')
noE(string)
avoids('blue','crystal')
uses_only('Kra', 'Kratos')
uses_all('aeiou', 'foxes')
is_abecedarian('abcdf')
find(string, 'a')
findIndex(string, 'a', 4)
is_sorted(string)
is_anagram('race', 'care')
has_duplicates(string)
remove_duplicates(string)
