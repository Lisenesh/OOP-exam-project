class Dress:
    def __init__(self, name, color, length, material, price):
        self.type = self.__class__.__name__
        self.name = name
        self.color = color
        self.length = length
        self.material = material
        self.price = price

    def findDressName(self, userTypedType, userTypedLength, userTypedMaterial, userTypedColor):
        if userTypedMaterial == self.material and userTypedLength == self.length and userTypedType == self.type and userTypedColor == self.color:
            print("The " + userTypedType + " you are looking for is " + self.name + ". The price is " + str(self.price))
            return True
        return False


class WeddingDress(Dress):
    def __init__(self, name, length, material, price):
        super().__init__(name, "white", length, material, price)
        self.type = self.__class__.__name__


class SummerDress(Dress):
    def __init__(self, name, color, length, price):
        super().__init__(name, color, length, "cotton", price)
        self.type = self.__class__.__name__


class EveningDress(Dress):
    def __init__(self, name, material, price):
        super().__init__(name, "dark", "medium", material, price)
        self.type = self.__class__.__name__


class BallGown(Dress):
    def __init__(self, name, color, material, price):
        super().__init__(name, color, "long", material, price)
        self.type = self.__class__.__name__


dresses = [
    WeddingDress("Flondon", "long", "silk", 120),
    WeddingDress("Gondor", "short", "cotton", 176),
    WeddingDress("Liskom",  "long", "cotton", 139),
    SummerDress("Lalimba", "yellow", "medium", 55),
    SummerDress("Trinda", "aqua", "short", 63),
    SummerDress("Skilora", "ruby", "medium", 79),
    EveningDress("Pirezi", "chiffon", 155),
    EveningDress("Lamida", "silk", 159),
    EveningDress("Verosiks", "velvet", 167),
    BallGown("Vrisket", "lightblue", "wool", 55),
    BallGown("Baret", "pink", "cotton", 150),
    BallGown("Erida", "lila", "velvet", 79)
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
    if not dress.findDressName(userTypedT, userTypedL, userTypedM, userTypedC):
        x += 1
        if x == len(dresses):
            print("Sorry, we have found no such dresses")

print(userTypedT, userTypedL, userTypedM, userTypedC)