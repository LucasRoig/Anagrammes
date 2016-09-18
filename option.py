import p11
from functools import partial
from time import time

def est_presque_anagramme(mot1,mot2,n):
    '''
    Renvoie True si mot1 et mot2 sont presque-anagrammes pour la valeur n
    '''
    if (len(mot2) > len(mot1)):
        mot1, mot2 = mot2, mot1
    #On a len(mot1) >= len(mot2)

    return len(mot1) == len(mot2) + n and all([mot1.count(c) >= mot2.count(c) for c in mot2])

def presque_anagrammes(mot,n):
    '''
    Renvoie la liste des "n-presque-anagrammes" de mot
    '''
    clef = p11.prehash(mot)
    listeClef = p11.hashTable.getKeysWithLen(len(mot) + n)
    listeClef = filter(partial(peut_etre_presque_anagrammes,clef2 = clef,n=n), listeClef)
    resultat = []
    for key in listeClef:
        resultat.extend(filter(partial(est_presque_anagramme,mot2=mot,n=n), p11.hashTable.get(key)))
    return resultat


def peut_etre_presque_anagrammes(clef1,clef2,n):
    '''
    Renvoie true si les mots dont les clefs de hash sont clef1 et clef2 peuvent
    etre des n-presque-anagrammes. Le test etant seulement effectue grace aux
    clefs de hash, il ne suffit pas a assurer que les mots sont des presque
    anagrammes'''
    if (clef1 >> 26 < clef2 >> 26):
        clef1, clef2 = clef2, clef1
    #clef1 est la clef du mot le plus long
    #On supprime la partie de la clef represantant la longueur
    #67108863 est un masque comportant des 1 sur les 26 premiers bits
    clef1 = clef1 & 67108863
    clef2 = clef2 & 67108863
    #Verifie que tous les caracteres de clef2 sont presents dans clef1
    if clef1 & clef2 != clef2 :
        return False
    return True

def quick(mot):
    '''
    Fonction renvoyant les 1-presque-anagrammes de mot. Utilisee pour repondre
    a la question du sujet.
    '''
    clef = p11.prehash(mot) & 67108863
    res = []
    cpt = 1
    for i in range(0,26):
        temp = clef | 1 << i
        if temp != clef:
            temp |= (len(mot) + 1) << 26
            L = p11.hashTable.get(temp)
            for mot2 in L :
                if (est_presque_anagramme(mot2,mot,1)):
                    res.append(mot2)
    clef |= (len(mot) + 1) << 26
    for mot2 in p11.hashTable.get(clef):
        if (est_presque_anagramme(mot2,mot,1)):
            res.append(mot2)
    return res

print(len(presque_anagrammes("AITRES",1)))
