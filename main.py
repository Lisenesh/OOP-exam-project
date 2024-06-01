class Dress:
    def __init__(self, color, length, material, price):
        self.color = color
        self.length = length
        self.material = material
        self.price = price

class WeddingDress(Dress):
    def __init__(self, color, length, material, price):
        super().__init__()
        self.color = color
        self.length = length
        self.material = material
        self.price = price

class SummerDress(Dress):
    def __init__(self, color, length, material, price):
        super().__init__()
        self.color = color
        self.length = length
        self.material = material
        self.price = price

