from penduModel import Pendu
from unidecode import unidecode
from random import choice


def getInput(self):
    pass

def chooseWord():
    f = open('mots.txt', 'r')
    contenu = f.readlines()
    return unidecode(choice(contenu)).upper().replace('\n','')

def initGame():
    pendu = Pendu(chooseWord(),"margaux")

    print(pendu.word)
    pendu.getEmpty(pendu.word)
    print(pendu.empty)

initGame()
