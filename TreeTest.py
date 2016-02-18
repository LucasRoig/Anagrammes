import time
class TreeNode:
    childrens = [] #Pointeurs vers les sous arbres
    value = "" #Le caractere represente par ce noeud
    finDeMot = False #Vrai si ce noeud est la fin d'un mot

    def __init__(self):
        self.childrens = []
        self.value = ""
        self.finDeMot = False

    def add(self, mot):
        """ajoute mot dans l'arbre"""
        if mot == "":
            self.finDeMot = True
        else :
            for child in  self.childrens:
                if child.value == mot[0]:
                    child.add(mot[1:])
                    return
            node = TreeNode()
            node.value = mot[0]
            self.childrens.append(node)
            node.add(mot[1:])
    
    def remove(self,mot):
        if(mot == ""):
            self.finDeMot = False
            return
        else:
            for child in self.childrens:
                if child.value == mot[0]:
                    child.remove(mot[1:])
                    return
                
    def printAllWords(self, currentWord):
        if self.finDeMot:
            print(currentWord + self.value)
        for child in self.childrens:
            child.printAllWords(currentWord + self.value)
    
    def searchAnaCompose(self,letters,root,wordList=[],currentWord=""):
        
        if currentWord == 'ANA':
            pass
        if letters == []:
            if not(self.finDeMot):
                return
            else :
                newWordList = wordList[:]
                newWordList.append(currentWord)
                print(newWordList)
        elif self.finDeMot:
            newWordList = wordList[:]
            newWordList.append(currentWord)
            root.searchAnaCompose(letters,root,newWordList,"")
        for child in self.childrens :
            if child.value in letters:
                newLetters = letters[:]
                newLetters.remove(child.value)
                child.searchAnaCompose(newLetters,root,wordList,currentWord+child.value)
        
def isInteresting(s,mot):
    #cle2 = cleSansLen(s)
    #return c == (c^cle2)|c
    return all([i in mot for i in s]) and len(s)<=len(mot)

def readDico(path):
    tree = TreeNode()
    fo = open(path,"r")
    #s = " "
    #while(s != ""):
    #    s = fo.readline()
    #    if (isInteresting(s)):
    #        tree.add(s)
    s = fo.read()
    tab = s.split()
    for string in tab:
        if isInteresting(string,"PROSE"):
            tree.add(string)
    return tree
    
t = time.time()
tree = readDico("dico.txt")
print(time.time() - t)
t = time.time()
tree.searchAnaCompose(list("PROSE"),tree)
print(time.time() - t)

print(sorted(["BLE","AS"]))