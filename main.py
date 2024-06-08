import tests
import Classes

dresses = [
    Classes.WeddingDress("Flondon", "long", "silk"),
    Classes.WeddingDress("Gondor", "short", "cotton"),
    Classes.WeddingDress("Liskom",  "long", "cotton"),
    Classes.SummerDress("Lalimba", "yellow", "medium"),
    Classes.SummerDress("Trinda", "aqua", "short"),
    Classes.SummerDress("Skilora", "ruby", "medium"),
    Classes.EveningDress("Pirezi", "chiffon"),
    Classes.EveningDress("Lamida", "silk"),
    Classes.EveningDress("Verosiks", "velvet"),
    Classes.BallGown("Vrisket", "lightblue", "wool"),
    Classes.BallGown("Baret", "pink", "cotton"),
    Classes.BallGown("Erida", "lila", "velvet")
]

# The main filter is the type of the dress
# The filters after that will be affected by the type of dress chosen
userTypedT = input("Input Dress type(WeddingDress/SummerDress/EveningDress/BallGown):")
match userTypedT:
    case "WeddingDress":
        userTypedL = input("Input Dress length(long/short):")
        userTypedM = input("Input Dress material(silk/cotton):")
        userTypedC = "white"
    case "SummerDress":
        userTypedL = input("Input Dress length(medium/short):")
        userTypedM = "cotton"
        userTypedC = input("Input Dress color(yellow/aqua/ruby):")
    case "EveningDress":
        userTypedL = "medium"
        userTypedM = input("Input Dress material(chiffon/silk/velvet):")
        userTypedC = "dark"
    case "BallGown":
        userTypedL = "long"
        userTypedM = input("Input Dress material(wool/cotton/velvet):")
        userTypedC = input("Input Dress color(lightblue/pink/lila):")
x = 0
for dress in dresses:
    if dress.findDressName(userTypedT, userTypedL, userTypedM, userTypedC):
        dress.CalculatePrice(dress.basePrice, userTypedL, userTypedM)
        continue
    x += 1
    if x == len(dresses):
        print("Sorry, we have found no such dresses")

UserTypedName = input("What's the name of the dress that you would like to buy?")
tests.CalcCheck()