import time
import sys
def cle(string):
    cle = 0
    for i in string :
        cle |= 1<<(ord(i)-65)
    cle = cle | len(string) << 26
    return cle

def cleSansLen(string):
    cle = 0
    for i in string :
        cle |= 1<<(ord(i)-65)
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
    return sorted(mot1) == sorted(mot2)

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