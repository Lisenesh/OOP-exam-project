from tests import CalcCheck
import Instanses


# The main filter is the type of the dress
# The filters after that will be affected by the type of dress chosen
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
        t = dress.CalculatePrice(dress.basePrice, userTypedL, userTypedM)
        if CalcCheck() == t:
            print("The price is calculated correctly")
        else:
            print("Something went wrong")
        continue
    x += 1
    if x == len(Instanses.dresses):
        print("Sorry, we have found no such dresses")
