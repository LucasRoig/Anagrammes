# Lucas Roig

from HashTable import HashTable

hashTable = HashTable()
dico = []

def getDico():
    global dico
    return dico

def prehash(mot):
    """mot : un mot de longueur > 0
    sortie : le hash du mot"""
    cle = 0
    for i in mot :
        cle |= 1<<(ord(i)-65)
    cle = cle | len(mot) << 26
    return cle


def openDico(path):
    """Ouvre le fichier passer en argument et ajoute l'ensemble des mots qu'il
    contient a la table de hachage"""
    global dico
    global hashTable
    file = open(path,"r")
    dico = file.read()
    dico = dico.split()
    for mot in dico:
        hashTable.add(mot, prehash(mot))

def est_anagramme(mot1,mot2):
    """Renvoie True si mot1 est un anagramme de mot2"""
    return sorted(mot1) == sorted(mot2)

def anagrammes(mot, hashTable):
    """Renvoie la liste des anagrammes de mot"""
    li = hashTable.get(prehash(mot))
    result = []
    for m in li:
        if est_anagramme(m, mot):
            result.append(m)
    return result

def best(l):
    """ l : entier l > 0
    Renvoie la liste des mots de longueur l ayant un nombre maximum
    d'anagrammes"""
    global hashTable
    motListe = [] # liste des mots de longueur l
    for key in hashTable.keys():
        if key >> 26 == l:
            #Pour chaque mot de longueur L, si motListe ne contient pas deja
            #un anagramme de ce mot, on l'ajoute dans motListe
            dejaAjoute = []
            for mot in hashTable.get(key):
                #Assure que l'on ajoute pas deux mots etant des anagrammes
                #puisque deux anagrammes ont la meme clef
                if(sorted(mot) not in dejaAjoute):
                    dejaAjoute.append(sorted(mot))
                    motListe.append(mot)

    #Dans la liste des mots de longueur l, on cherche les mots ayant le plus
    #d'anagrammes
    maxMot = []
    maxlen = 0
    for mot in motListe:
        ana  = anagrammes(mot,hashTable)
        if len(ana) == maxlen:
            maxMot.append(mot)
        elif len(ana) > maxlen:
            maxlen = len(ana)
            maxMot = [mot]
    return maxMot

openDico("lexique.txt")
