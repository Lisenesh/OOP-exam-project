import Instanses


def CalcCheck(UserTypedName):
    x = 0
    lengthPrice = 1
    materialPrice = 0
    for dress in Instanses.dresses:
        if UserTypedName == dress.name:
            break
        x += 1
    match Instanses.dresses[x].length:
        case "short":
            lengthPrice = 1
        case "medium":
            lengthPrice = 1.5
        case "long":
            lengthPrice = 2
    match Instanses.dresses[x].material:
        case "wool":
            materialPrice = 5
        case "cotton":
            materialPrice = 10
        case "chiffon":
            materialPrice = 15
        case "silk":
            materialPrice = 20
        case "velvet":
            materialPrice = 25
    Sum = (Instanses.dresses[x].basePrice + materialPrice) * lengthPrice
    return Sum
