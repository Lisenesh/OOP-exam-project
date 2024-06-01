class Dress:
    def __init__(self, name, color, length, material, price):
        self.type = self.__class__.__name__
        self.name = name
        self.color = color
        self.length = length
        self.material = material
        self.price = price

    def checkfilters(self, type=None, color=None, length=None, material=None):
        x = 0
        if type is not None and not isinstance(self, type):
            x+=1

        if color is not None and self.color != color:
            x+=1

        if length is not None and self.length != length:
            x+=1

        if material is not None and self.material != material:
            x+=1

        if x==4:
            return True
        else:
            return False

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
x = input("Enter the type of dress")
print(WeddingDress.checkfilters(x,WeddingDress,"white","long","silk"))