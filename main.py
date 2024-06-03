class Dress:
    def __init__(self, name, color, length, material, basePrice):
        self.type = self.__class__.__name__
        self.name = name
        self.color = color
        self.length = length
        self.material = material
        self.basePrice = basePrice

    def findDressName(self, userTypedType, userTypedLength, userTypedMaterial, userTypedColor):
        if userTypedMaterial == self.material and userTypedLength == self.length and userTypedType == self.type and userTypedColor == self.color:
            print("The " + userTypedType + " you are looking for is " + self.name)
            return True
        return False

    def CalculatePrice(self, basePrice, userTypedLength, userTypedMaterial):
        match userTypedMaterial:
            case "wool":
                basePrice += 5
            case "cotton":
                basePrice += 10
            case "chiffon":
                basePrice += 15
            case "silk":
                basePrice += 20
            case "velvet":
                basePrice += 25
            case _:
                "Please try another material"
        match userTypedLength:
            case "short":
                basePrice *= 1
            case "medium":
                basePrice *= 1.5
            case "long":
                basePrice *= 2
            case _:
                "Please try another length"
        print("The price of this dress is " + str(basePrice))


class WeddingDress(Dress):
    def __init__(self, name, length, material):
        super().__init__(name, "white", length, material, 100)
        self.type = self.__class__.__name__


class SummerDress(Dress):
    def __init__(self, name, color, length):
        super().__init__(name, color, length, "cotton", 60)
        self.type = self.__class__.__name__

    def CalculatePrice(self, basePrice, userTypedLength, userTypedMaterial):
        basePrice += 10
        match userTypedLength:
            case "short":
                basePrice *= 1
            case "medium":
                basePrice *= 1.5
            case "long":
                basePrice *= 2
            case _:
                "Please try another length"
        print("The price of this dress is " + basePrice)
        return basePrice


class EveningDress(Dress):
    def __init__(self, name, material,):
        super().__init__(name, "dark", "medium", material, 70)
        self.type = self.__class__.__name__

    def CalculatePrice(self, basePrice, userTypedLength, userTypedMaterial):
        match userTypedMaterial:
            case "wool":
                basePrice += 5
            case "cotton":
                basePrice += 10
            case "chiffon":
                basePrice += 15
            case "silk":
                basePrice += 20
            case "velvet":
                basePrice += 25
            case _:
                "Please try another material"
        basePrice *= 1.5
        return basePrice


class BallGown(Dress):
    def __init__(self, name, color, material):
        super().__init__(name, color, "long", material, 85)
        self.type = self.__class__.__name__

    def CalculatePrice(self, basePrice, userTypedLength, userTypedMaterial):
        match userTypedMaterial:
            case "wool":
                basePrice += 5
            case "cotton":
                basePrice += 10
            case "chiffon":
                basePrice += 15
            case "silk":
                basePrice += 20
            case "velvet":
                basePrice += 25
            case _:
                "Please try another material"
        basePrice *= 2
        return basePrice


dresses = [
    WeddingDress("Flondon", "long", "silk"),
    WeddingDress("Gondor", "short", "cotton"),
    WeddingDress("Liskom",  "long", "cotton"),
    SummerDress("Lalimba", "yellow", "medium"),
    SummerDress("Trinda", "aqua", "short"),
    SummerDress("Skilora", "ruby", "medium"),
    EveningDress("Pirezi", "chiffon"),
    EveningDress("Lamida", "silk"),
    EveningDress("Verosiks", "velvet"),
    BallGown("Vrisket", "lightblue", "wool"),
    BallGown("Baret", "pink", "cotton"),
    BallGown("Erida", "lila", "velvet")
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