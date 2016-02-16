import time
def openAsTable(path):
    #0.2sec
    """path : le chemin du dico a ouvrir"""
    dico = open("dico.txt","r")
    str = dico.read()
    tab = str.split()
    return tab

def searchAnagramInTab(str,tab):
     #0.25sec
    motTrie = sorted(str)
    res = []
    for mot in tab :
        if sorted(mot) == motTrie:
            res.append(mot)
    return res

def searchMaxAnagramInTab(tab):
    #340000*0.25sec = 19 heures
    max = 0
    i = 0
    for mot in tab:
        l = searchAnagramInTab(mot,tab)
        if(len(l) > max):
            max = len(l)
    print(max)
t = time.time()
tab = openAsTable("dico.txt")
print(time.time() - t)

t = time.time()
searchAnagramInTab("SAPIN",tab)
print(time.time() - t)
