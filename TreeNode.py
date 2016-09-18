class TreeNode():
    childrens = []
    finDeMot = False
    value = '\0'

    def __init__(self):
        self.childrens = []
        self.finDeMot = False
        self.value = '\0'
    def add(self,mot):
        '''Ajoute un mot a l'arbre'''
        if(len(mot) == 0):
            self.finDeMot = True
        else:
            for child in self.childrens:
                if (child.value == mot[0]):
                    child.add(mot[1:])
                    return
            node = TreeNode()
            node.value = mot[0]
            self.childrens.append(node)
            node.add(mot[1:])

    def printAllWords(self, currentWord):
        '''
        Affiche tous les mots de l'arbre
        currentWord est une liste
        '''
        if (self.finDeMot):
            print(currentWord)
        for child in self.childrens:
            currentWord.append(child.value)
            child.printAllWords(currentWord)
            currentWord.pop()

