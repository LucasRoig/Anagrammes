'''
Created on 18 feb. 2016

@author: Lucas Roig
'''
class HashTable():
    dictionnaire = {}
    
    def __init__(self):
        self.dictionnaire = {}
        
    def add(self,mot,clef):
        if clef in self.dictionnaire :
            self.dictionnaire[clef].append(mot)
        else :
            self.dictionnaire[clef] = [mot]
    
    def get(self,clef):
        return self.dictionnaire[clef]
    
    def keys(self):
        return self.dictionnaire.keys()