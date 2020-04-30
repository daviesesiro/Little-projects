alphaDict = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}

def word_score(word) :
    sum = 0
    for i in word:
        sum += alphaDict[i.lower()]

    return sum


d1 = 'aeilnorstu'
d2 = 'dg'
d3 = 'bcmp'
d4 = 'fhvwy'
d5 = 'k'
d8= 'jx'
d10 = 'qz'

def word_score2(word):
    sum = 0
    word = word.lower()
    for i in word:
        if i in d1:
            sum +=1
        elif i in d2:
            sum += 2
        elif i in d3:
            sum += 3
        elif i in d4:
            sum += 4
        elif i in d5:
            sum += 5
        elif i in d8:
            sum += 8
        elif i in d10:
            sum += 10
        
    return sum


print(word_score("Maximize"))
print(word_score2("Maximize"))