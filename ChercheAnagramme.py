from TreeNode import TreeNode
from HashTable import HashTable
import util
import p11
'''
Cette classe est utilisee pour retrouver les anagrammes composes d'un mot
'''

class ChercheAnagramme():
    maxMot = -1
    motRecherche = ""
    occLettres = [0]*26 #Contient le nombre d'occurences de chaque lettre.
    totalLettres = 0 #Contient le nombre de lettres restantes.
    tree = TreeNode()
    listeMot = [] #Pile utilisee pour stocker les mots de la solution actuelle
    solution = [] #Liste de toutes les solutions trouvees
    currentWord = [] #Stocke les lettres du mot que l'on est en train de trouver
    premierMots = [] #Stocke les mots pouvant etre les premiers mots d'une solution
    hashTable = HashTable()
    solutionDecodee = []

    def __init__(self, mot, maxMot,dico,hashTable):
        '''
        mot : le mot dont on souhaite trouver les anagrammes composes
        maxMot: nombre maximum de mots dont les solutions peuvent etre composees
        dico : la liste dans laquelle est stocke le dictionnaire
        '''
        self.motRecherche = mot
        self.occLettres = [0]*26
        self.totalLettres = 0
        self.tree = TreeNode()
        self.listeMot = []
        self.solution = []
        self.currentWord = []
        self.hashTable = hashTable
        self.solutionDecodee = []
        self.maxMot = maxMot
        self.premierMots = []


        #Compte tous les caracteres pressents dans le mot
        for char in mot :
            self.occLettres[ord(char) - 65] += 1
            self.totalLettres += 1

        char = self.__bestChar__()
        #Construit la liste de tous les mots pouvant apparaitre dans une solution
        li = filter(self.__accepteMot__, dico)

        #Construit l'arbre contenant tous les mots pouvant apparaitre dans une solution
        for motPossible in li :
            motPossible = list(motPossible)
            motPossible.sort(key = util.frequence, reverse = True)
            try:
                #si le mot contient le caractere recherche alors il peut etre
                #le premier mot d'une solution
                if(motPossible.count(char) > 0):
                    self.premierMots.append("".join(motPossible))
            except Exception as e:
                pass
            self.tree.add(motPossible)
        self.premierMots = set(self.premierMots)

    def __accepteMot__(self,mot):
        '''
        Retourne True si mot peut apparaitre dans un anagramme compose du mot
        recherche
        '''
        if (len(mot) > len(self.motRecherche)):
            return False
        for char in mot :
            if (mot.count(char) > self.motRecherche.count(char)):
                return False
        return True

    def search(self):
        '''
        Realise la recherche des anagrammes composes du mot recherche
        '''
        #Initialise les variables de la classe
        self.listeMot = []
        self.solution = []
        self.currentWord = []
        for mot in self.premierMots:
            for char in mot :
                self.occLettres[ord(char) - 65] -= 1
                self.totalLettres -= 1
            if (self.totalLettres == 0):
                #Si le mot est un anagramme du mot recherche
                self.solution.append([mot])
            else:
                self.listeMot.append(mot)
                self.__doSearch__(self.tree,self.__bestChar__())
                self.listeMot.pop()
            for char in mot :
                self.occLettres[ord(char) - 65] += 1
                self.totalLettres += 1
        self.__decodeSol__()
        return self.solutionDecodee

    def __doSearch__(self,tree,char):
        '''
        Backtracking, recherche recursive des solutions
        '''
        if(self.totalLettres == 0):
            #Si toutes les lettres ont ete utilisee, que l'on est a la fin d'un
            #mot et que l'on a deja rencontre le caractere recherche on ajoute
            #la solution actuelle a la liste des solutions
            if (tree.finDeMot and char == '\0'):
                mot = "".join(self.currentWord)
                self.listeMot.append(mot)
                self.solution.append(self.listeMot[:])
                self.listeMot.pop()
                return
            else :
                return
        elif(tree.finDeMot and char == '\0'):
            #Si l'on est a la fin d'un mot et que l'on a rencontre le caractere
            #recherche, on ajoute le mot a la solution actuelle. Et on cherche
            #a completer la solution.
            #En en profite pour verifier que l'on ne depasse pas le nombre max
            #de mots
            if(len(self.listeMot) + 1 < self.maxMot or self.maxMot == -1):
                saveWord = self.currentWord[:]
                self.listeMot.append(self.currentWord[:])
                self.currentWord = []
                self.__doSearch__(self.tree,self.__bestChar__())
                self.listeMot.pop()
                self.currentWord = saveWord

        for child in tree.childrens:
            #Si l'on trouve le caractere recherche alors on continu en indiquant
            #que l'on a deja rencontre le caractere grace a la valeur '\0'
            if (child.value == char and self.occLettres[ord(char)-65] > 0):
                self.occLettres[ord(child.value) - 65] -= 1
                self.totalLettres -= 1
                self.currentWord.append(child.value)
                self.__doSearch__(child,'\0')
                self.occLettres[ord(child.value) - 65] += 1
                self.totalLettres += 1
                self.currentWord.pop()
            #Si l'on a deja rencontre le caractere recherche ou que le caractere
            #present sur le noeud suivant est plus rare que le caractere recherche
            #on continu le parcours en recherchant toujours le meme caractere
            elif ((char == '\0' or util.inferieur(child.value,char)) and self.occLettres[ord(child.value) - 65] > 0):
                self.occLettres[ord(child.value) -65] -= 1
                self.totalLettres -= 1
                self.currentWord.append(child.value)
                self.__doSearch__(child,char)
                self.occLettres[ord(child.value) -65] += 1
                self.totalLettres += 1
                self.currentWord.pop()


    def __bestChar__(self):
        '''
        Trouve le caractere qu'il faut chercher en premier
        '''

        i = 0
        while (self.occLettres[i] == 0):
            i += 1
            if (i == 26):
                return '\0'
        minChar = chr(i+65)
        while(i < len(self.occLettres)):
            if (self.occLettres[i] > 0 and self.occLettres[i] <= self.occLettres[ord(minChar) - 65] and util.inferieur(chr(i+65),minChar)):
                minChar = chr(i+65)

            i += 1
        return minChar

    def __decodeSol__(self):
        '''
        A la fin de l'algorithme de recherche on dispose des anagrammes de
        chaque solutions puisqu'on a trie les mots avant de les ajouter
        dans l'arbre. Cette fonction recupere les veritables solutions.
        '''
        for sol in self.solution :
            anagrammes = []
            for mot in sol :
                 anagrammes.append(p11.anagrammes(mot,self.hashTable))
            self.__placerSol__(0, len(anagrammes), anagrammes, [])

    def __placerSol__(self,i,N,permut,solCourante):
        '''
        Retrouve recursivement les anagrammes de chaque solution.
        '''
        if (i == N):
            self.solutionDecodee.append(solCourante[:])
        else:
            for mot in permut[i]:
                solCourante.append(mot)
                self.__placerSol__(i+1, N, permut, solCourante)
                solCourante.pop()
