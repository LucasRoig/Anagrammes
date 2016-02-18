'''
Created on 18 feb. 2016

@author: Lucas Roig
'''
from HashTable import HashTable
from TreeNode import TreeNode
from time import time

hashTable = HashTable()
dico = []
def prehash(mot):
    """mot : string
    Renvoie le hash de mot"""
    
    cle = 0
    for i in mot :
        cle |= 1<<(ord(i)-65)
    cle = cle | len(mot) << 26
    return cle
def est_anagramme(mot1,mot2):
    """Renvoie True si mot1 est un anagramme de mot2"""
    
    return sorted(mot1) == sorted(mot2)

def anagrammes(mot):
    """Renvoie la liste des anagrammes de mot"""
    global hashTable
    li = hashTable.get(prehash(mot))
    for i in range(len(li)-1,-1,-1):
        if not(est_anagramme(mot, li[i])):
            li.pop(i)
    return li
def best(l):

    global hashTable
    keyList = []
    for key in hashTable.keys():
        if key >> 26 == l:
            keyList.append(key)
    motListe = [] # liste des mots de longueur l
    for key in keyList:
        motListe.extend(hashTable.get(key))

    maxMot = []
    maxlen = 0
    for mot in motListe:
        ana  = anagrammes(mot)
        if len(ana) == maxlen:
            maxMot.append(mot)
        elif len(ana) > maxlen:
            maxlen = len(ana)
            maxMot = [mot]
    print(maxMot)
    print(maxlen)
    
def openDico(path):    
    global dico
    global hashTable
    file = open(path,"r")
    dico = file.read()
    dico = dico.split()
    for mot in dico:
        hashTable.add(mot, prehash(mot))
        
def A1(mot):
    """Renvoie la liste des anagrammes stricts composes de plusieurs mots ou pas"""
    return A2(mot,-1)
    

def A2(mot,n):
    """Renvoie la liste des anagrammes stricts composes au maximum de n mots"""
    
    global dico
    tree = TreeNode()
    t = time()
    for word in dico:
        if all([c in mot for c in word]) and len(word)<=len(mot):
            tree.add(word)#On ajoute uniquement les mots qui nous interressent
    print("construction arbre :", time() - t)
    return tree.searchAnaCompose(list(mot), tree,maxMot = n)
    
    
t = time()
openDico("dico.txt")
print(time()-t)
t = time()
print(anagrammes("ARMES"))
print(time()-t)
t = time()
best(6)
print(time()-t)
t = time()
print(A2("CHAMPOLLION",4))
print(time()-t)