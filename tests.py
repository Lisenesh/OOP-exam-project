import Classes
import main

x = 0
def CalcCheck(x, y): #Classes.Dress.basePrice, main.UserTypedName):
    for dress in main.dresses:
        if main.UserTypedName == dress.name:
            break
        x += 1
        Classes.Dress.CalculatePrice(main.dresses[x].basePrice, main.dresses[x].length, main.dresses[x].material)
    return Classes.Dress.basePrise


def secondTest():
    pass


def thirdTest():
    pass