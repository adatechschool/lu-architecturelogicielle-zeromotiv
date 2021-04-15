from penduController import PenduController
from penduModel import Pendu

def initGame(self):
    pendu = Pendu(chooseWord(),setUserName())

    print(pendu.word)
    pendu.getEmpty(pendu.word)
    print(pendu.empty)
    print(pendu.userName)
pendu = Pendu("blou", "name")
pendu.setUserName()

pendu.getInput()
print(pendu.userName)
