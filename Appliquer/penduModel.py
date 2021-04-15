

from unidecode import unidecode
from random import choice

class Pendu:
    def __init__(self,word, userName):
        self.word = word
        self.userName = userName
        self.mistakes = 0 #ne peut aller que jusqu'a 11
        self.triedLetters = []
        self.empty = []


    def getEmpty(self, word):
        for i in range(len(word)):
            self.empty.append("_")
        return self.empty

    def setUserName():
        pass
