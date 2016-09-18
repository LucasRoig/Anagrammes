'''
Contient des fonctions utilisee dans les autres fichiers
'''
from time import time
#stocke les frequences d'apparition des caracteres en francais
freq = [3,19,12,11,1,18,20,21,4,22,32,9,14,6,10,13,17,7,2,5,8,16,29,24,25,28]

def inferieur(a,b):
    '''
    definie une relation d'ordre sur les caracteres en fonction de leur
    frequence d'apparition en francais.
    Retourne True si a < b
    '''
    return freq[ord(a) - 65] > freq[ord(b) - 65]

def frequence(c):
    '''
    c : un caractere
    Retourne la frequence d'apparition de c en francais
    '''
    return freq[ord(c)-65]

def countBit1(n):
    n = n - ((n>>1)& 0x55555555)
    n = (n & 0x33333333) + ((n>>2) & 0x33333333)
    n = (n + (n>>4)) & 0x0F0F0F0F
    n = n + (n>>8)
    n = n + (n>>16)
    return n & 0x0000003F

def countBit1p(n):
    return (bin(n).count("1"))

t = time()
for i in range(1000000):
    countBit1(i)
print(time() - t)
