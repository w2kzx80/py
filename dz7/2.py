from abc import ABC, abstractmethod


class Clothes:
    def __init__(self,title):
        self.title = title

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, title, V):
        super().__init__(title)
        self.V = V

    @property
    def fabric(self):
        return self.V / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, title, H):
        super().__init__(title)
        self.H = H

    @property
    def fabric(self):
        return 2 * self.H + 0.3

def calc_fabrics(*clothes):
    return sum([c.fabric for c in clothes])

myCoat = Coat("My Coat", 10)
myCostume = Costume("My Costume", 15)
myCostume2 = Costume("New Costume", 16)

print(calc_fabrics(myCoat, myCostume, myCostume2))
