import time
import sys
def cle(string):
    cle = 0
    if 'A' in string:
        cle = cle | 1
    if 'B' in string:
        cle = cle | 1<<1
    if 'C' in string:
        cle = cle | 1<<2
    if 'D' in string:
        cle = cle | 1<<3
    if 'E' in string:
        cle = cle | 1<<4
    if 'F' in string:
        cle = cle | 1<<5
    if 'G' in string:
        cle = cle | 1<<6
    if 'H' in string:
        cle = cle | 1<<7
    if 'I' in string:
        cle = cle | 1<<8
    if 'J' in string:
        cle = cle | 1<<9
    if 'K' in string:
        cle = cle | 1<<10
    if 'L' in string:
        cle = cle | 1<<11
    if 'M' in string:
        cle = cle | 1<<12
    if 'N' in string:
        cle = cle | 1<<13
    if 'O' in string:
        cle = cle | 1<<14
    if 'P' in string:
        cle = cle | 1<<15
    if 'Q' in string:
        cle = cle | 1<<16
    if 'R' in string:
        cle = cle | 1<<17
    if 'S' in string:
        cle = cle | 1<<18
    if 'T' in string:
        cle = cle | 1<<19
    if 'U' in string:
        cle = cle | 1<<20
    if 'V' in string:
        cle = cle | 1<<21
    if 'W' in string:
        cle = cle | 1<<22
    if 'X' in string:
        cle = cle | 1<<23
    if 'Y' in string:
        cle = cle | 1<<24
    if 'Z' in string:
        cle = cle | 1<<25
    cle = cle | len(string) << 26

    return cle


def bin(s):
    return str(s) if s<=1 else bin(s>>1) + str(s&1)

def addToHashTable(mot, hashTable):
    clef = cle(mot)
    if clef in hashTable :
        hashTable[clef].append(mot)
    else :
        hashTable[clef] = [mot]

def sontAnagrames(mot1,mot2):
    return sorted(mot1) == sorted(mot2) and mot1 != mot2

def searchAnagrams(mot,hashTable):
    #0,0001 sec
    return [i for i in hashTable[cle(mot)] if sontAnagrames(i,mot)]

def searchMaxAnagram(hashTable,tab):
    """Trouve le mot ayant le plus d'anagrammes"""
    #4 sec
    max = 0
    m = ""
    for mot in tab :
        l = searchAnagrams(mot,hashTable)
        if len(l) > max:
            max = len(l)
            m = mot
    print(max,m)

def best(l,hashTable):
    #0,15sec
    """renvoie la liste des mots de longueur l qui ont le plus d'anagrammes"""
    keyList = []
    for key in hashTable.keys():
        if key >> 26 == l:
            keyList.append(key)
    motListe = [] # liste des mots de longueur l
    for key in keyList:
        motListe.extend(hashTable[key])

    maxMot = []
    maxlen = 0
    for mot in motListe:
        anagrammes  = searchAnagrams(mot,hashTable)
        if len(anagrammes) == maxlen:
            maxMot.append(mot)
        elif len(anagrammes) > maxlen:
            maxlen = len(anagrammes)
            maxMot = [mot]
    print(maxMot)
    print(maxlen)


file = open("dico.txt","r")
string = file.read()
tab = string.split()
hashTable = {}
t = time.time()
for mot in tab :
    addToHashTable(mot,hashTable)
print(time.time() - t)
print(sys.getsizeof(hashTable))
print(sys.getsizeof(tab))
print(sys.getsizeof(int))
