'''
Created on 18 feb. 2016

@author: Lucas Roig
'''

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
    
    def searchAnaCompose(self,letters,root,wordList=[],currentWord="",listeSolutions = [],maxMot = -1):
        if letters == []:
            if not(self.finDeMot):
                return
            else :
                newWordList = wordList[:]
                newWordList.append(currentWord)
                listeSolutions.append(newWordList)
        elif self.finDeMot and len(wordList)+1 != maxMot :
            newWordList = wordList[:]
            newWordList.append(currentWord)
            root.searchAnaCompose(letters,root,newWordList,"",listeSolutions,maxMot)
        for child in self.childrens :
            if child.value in letters:
                newLetters = letters[:]
                newLetters.remove(child.value)
                child.searchAnaCompose(newLetters,root,wordList,currentWord+child.value,listeSolutions,maxMot)
        return listeSolutions