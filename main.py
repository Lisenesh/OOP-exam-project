from tests import CalcCheck
import Instanses


userTypedT = input("Input Dress type(WeddingDress/SummerDress/EveningDress/BallGown):")
match userTypedT:
    case "WeddingDress":
        userTypedC = "white"
        userTypedL = input("Input Dress length(long/short):")
        userTypedM = input("Input Dress material(silk/cotton):")
    case "SummerDress":
        userTypedC = input("Input Dress color(yellow/aqua/ruby):")
        userTypedL = input("Input Dress length(medium/short):")
        userTypedM = "cotton"
    case "EveningDress":
        userTypedC = "dark"
        userTypedL = "medium"
        userTypedM = input("Input Dress material(chiffon/silk/velvet):")
    case "BallGown":
        userTypedC = input("Input Dress color(lightblue/pink/lila):")
        userTypedL = "long"
        userTypedM = input("Input Dress material(wool/cotton/velvet):")
x = 0
for dress in Instanses.dresses:
    if dress.findDressName(userTypedT, userTypedL, userTypedM, userTypedC):
        print("The price of this dress is " + str(int(dress.CalculatePrice(dress.basePrice, userTypedL, userTypedM))))
        UserTypedName = input("What's the name of the dress you would like to find?")
        if CalcCheck(UserTypedName) == dress.CalculatePrice(dress.basePrice, userTypedL, userTypedM):
            print("The price is calculated correctly")
        else:
            print("Something went wrong")
        continue
    x += 1
    if x == len(Instanses.dresses):
        print("Sorry, we have found no such dresses")


UserTypedName = "Flondon"
x = 0
if CalcCheck(UserTypedName) == Instanses.dresses[x].CalculatePrice(Instanses.dresses[x].basePrice, Instanses.dresses[x].length, Instanses.dresses[x].material):
    print("The check was successful")
else:
    print("Something went wrong")


UserTypedName = "Trinda"
x = 4
if CalcCheck(UserTypedName) == Instanses.dresses[x].CalculatePrice(Instanses.dresses[x].basePrice, Instanses.dresses[x].length, Instanses.dresses[x].material):
    print("The check was successful")
else:
    print("Something went wrong")


UserTypedName = "Verosiks"
x = 8
if CalcCheck(UserTypedName) == Instanses.dresses[x].CalculatePrice(Instanses.dresses[x].basePrice, Instanses.dresses[x].length, Instanses.dresses[x].material):
    print("The check was successful")
else:
    print("Something went wrong")


UserTypedName = "Baret"
x = 10
if CalcCheck(UserTypedName) == Instanses.dresses[x].CalculatePrice(Instanses.dresses[x].basePrice, Instanses.dresses[x].length, Instanses.dresses[x].material):
    print("The check was successful")
else:
    print("Something went wrong")
