

from unidecode import unidecode
from random import choice

class Pendu:
    def __init__(self,word, userName):
        self.word = word
        self.userName = userName
        self.mistakes = 0 #ne peut aller que jusqu'a 11
        self.triedLetters = []
        self.empty = []
        self.input = ""


    def getEmpty(self, word):
        for i in range(len(word)):
            self.empty.append("_")
        return self.empty

    def setUserName(self):
        self.userName = input("Votre nom :")
        return self.userName

    def getInput(self):
        self.input = input("Choisissez une lettre :")
        return self.input

    def turn(self):
        print("Voilà le mot"+str(self.empty))
        self.getInput()
        for i in range(len(self.word)):
            if self.word[i]== self.input.upper():
                self.empty[i] = self.input.upper()
                print ("bien joué !")
