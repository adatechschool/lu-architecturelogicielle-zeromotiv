from penduModel import Pendu
from unidecode import unidecode
from random import choice

def chooseWord():
    f = open('mots.txt', 'r')
    contenu = f.readlines()
    return list(unidecode(choice(contenu)).upper().replace('\n',''))

def initGame():
    pendu = Pendu(chooseWord(),"name")
    print(pendu.word)
    pendu.setUserName()
    pendu.getEmpty(pendu.word)
    print("Coucou "+pendu.userName)
    return pendu

pendu = initGame()

while (pendu.mistakes < 11 and '_' in pendu.empty):
    pendu.turn()
