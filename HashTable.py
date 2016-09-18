'''
Created on 18 feb. 2016

@author: Lucas Roig
'''
class HashTable():
    dictionnaire = {}

    def __init__(self):
        self.dictionnaire = {}

    def add(self,mot,clef):
        longueur = clef >> 26 #partie de la clef represantant la longueur du mot
        if longueur in self.dictionnaire :
            if clef in self.dictionnaire[longueur] :
                self.dictionnaire[longueur][clef].append(mot)
            else :
                self.dictionnaire[longueur][clef] = [mot]
        else :
            dico = {}
            dico[clef] = [mot]
            self.dictionnaire[longueur] = dico

    def get(self,clef):
        longueur = clef >> 26
        if longueur in self.dictionnaire:
            if clef in self.dictionnaire[longueur] :
                return self.dictionnaire[longueur][clef]
        return []

    def keys(self):
        clef = []
        for dico in self.dictionnaire.values() :
            clef.extend(dico.keys())
        return clef

    def getKeysWithLen(self,longueur):
        '''
        Renvoie les clefs de tous les mots de longueur demandee
        longueur : Entier > 0
        '''
        if longueur in self.dictionnaire :
            return self.dictionnaire[longueur].keys()
        else :
            return []

    #def getAllWords(self):
        #return self.dictionnaire.items()
