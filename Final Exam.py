'''list_of_strings = ['antelope', 'manta', 'wallaby', 'vulture']

for a_string in list_of_strings:
    print('element by element:', end='')
    print(a_string)'''

'''def calculate_box_volume(length, width, height):
    volume = float(length) * float(width) * float(height)
    return volume
'''
'''
first = 6
second = 13
second = first
first=second
print(second)
'''

'''
s = "There are no secrets to success. It is the result of preparation, hard work, and learning from failure"
words = s.split()
wordlist = []


for word in words:
    if len(word) == 5:
        wordlist.append(word)
        print(wordlist)
    
'''

def all_smaller(x, values):
    for k in values:
        if k < x:
            return True
        else:
            return False

'''
x = [4,3,2,1,0]
x.insert(4,5)
x.remove(0)
x.append(6)
x.pop(2)
print(x[2])
'''
'''
x=[
    [0,4,0],
    [2,7,0],
    [9,0,2]
]
print(x[2][0])
'''
'''
class Widget:
    def __init__(self, v =30):
        if v >= 30:
            self.value = v
        else:
            self.value = 0
    def get(self):
        return self.value
    def bump(self):
        if self.value < 50:
            self.value += 1
def main():
    w1 = Widget()
    w2 = Widget(5)

    w1.bump()
    w2.bump()

    for i in range(30):
        w1.bump()
        w2.bump()

    print(w1.get())
    print(w2.get())

if __name__== '__main__':
    main()
'''
'''
def letterA(sentence):
    aCounter = 0
    charCounter = 0
    phase = sentence.lower()
    for k in sentence:
        if not k.isalpha():
            continue
        charCounter += 1
        if k == 'a':
            aCounter += 1
    print(f"Your text contains {charCounter} alphabetic characters, of which {eCounter} ({((eCounter / charCounter) * 100):0.1f}%) are 'e'.\n")
'''
