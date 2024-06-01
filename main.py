class Dress:
    def __init__(self, name, color, length, material, price):
        self.type = self.__class__.__name__
        self.name = name
        self.color = color
        self.length = length
        self.material = material
        self.price = price

    def findDressName(self, userTypedType, userTypedLength, userTypedMaterial, userTypedColor):
        if (userTypedMaterial == self.material and userTypedLength == self.length and userTypedType == self.type and userTypedColor == self.color):
            print("The "+ userTypedType + " you are looking for is " + self.name)

class WeddingDress(Dress):
    def __init__(self, name, color, length, material, price):
        super().__init__(name,color,length,material,price)
        self.type = self.__class__.__name__
        self.name = name
        self.color = color
        self.length = length
        self.material = material
        self.price = price


class SummerDress(Dress):
    def __init__(self, name, color, length, material, price):
        super().__init__(name,color,length,material,price)
        self.type = self.__class__.__name__
        self.name = name
        self.color = color
        self.length = length
        self.material = material
        self.price = price


dresses = [
    WeddingDress("Flondon", "white", "long", "silk", 100),
    WeddingDress("Gondor", "white", "short", "cotton", 66),
    WeddingDress("Liskom", "lila", "long", "cotton", 139),
    SummerDress("Lalaba", "yellow", "medium", "silk", 55),
    SummerDress("Trinda", "aqua", "short", "cotton", 150),
    SummerDress("Skilora", "ruby", "medium", "cotton", 79)
]

#The point of the function is to take the average price of all the dresses according to filters
#The main filter is the type of the dress
#The filters after that will be affected by the type of dress chosen
userTypedT = input("Input Dress type:")
userTypedL = input("Input Dress length:")
userTypedM = input("Input Dress material:")
userTypedC = input("Input Dress color:")

for dress in dresses:
    dress.findDressName(userTypedT, userTypedL, userTypedM,userTypedC)
