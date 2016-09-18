from ChercheAnagramme import ChercheAnagramme
import p11
from time import time

def A2(mot, n):
    '''
    Retourne la liste des anagrammes composes de n mots ou moins de mot
    mot : chaine de caracteres
    '''
    if n == 1:
        return p11.anagrammes(mot, p11.hashTable)
    else:
        chercheur = ChercheAnagramme(list(mot),n,p11.dico,p11.hashTable)
        return chercheur.search()

def A1(mot):
    '''
    Retourne la liste des anagrammes composes de mot
    mot : chaine de caracteres
    '''
    chercheur = ChercheAnagramme(list(mot),-1,p11.dico,p11.hashTable)
    return chercheur.search()

print(A2("POLYNOME",2))
