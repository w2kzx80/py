
class Cell:
    def __init__(self, ccnt:int):
        self.ccnt=ccnt

    def __str__(self):
        return f"{self.ccnt}"

    def __add__(self, other):
        if type(self) == Cell and type(other) == Cell:
            return Cell(self.ccnt + other.ccnt)
        raise TypeError

    def __sub__(self, other):
        if type(self) == Cell and type(other) == Cell:
            if self.ccnt > other.ccnt:
                return Cell(self.ccnt - other.ccnt)
            print("second cell too big")
            return self
        raise TypeError

    def __mul__(self, other):
        if type(self) == Cell and type(other) == Cell:
            return Cell(self.ccnt * other.ccnt)
        raise TypeError

    def __truediv__(self, other):
        if type(self) == Cell and type(other) == Cell:
            return Cell(self.ccnt // other.ccnt)
        raise TypeError

    def make_order(self, rlen):
        rows = []
        rsum = self.ccnt
        while rsum > rlen:
            rows.append("".join(["*" for ri in range(0,rlen)]))
            rsum -= rlen
        rows.append("".join(["*" for ri in range(0, rsum)]))
        return "\n".join(rows)


myCell1 = Cell(12)
myCell2 = Cell(5)
myCell3 = Cell(7)

print(myCell1 + myCell2 + myCell3)
print(myCell1 / myCell2)
print(myCell2 * myCell3)
print(myCell3 - myCell2)
print(myCell2 - myCell3)
print(f"ORDER c1:\n{myCell1.make_order(6)}\n\n")
print(f"ORDER c2:\n{myCell2.make_order(6)}\n\n")
print(f"ORDER c3:\n{myCell3.make_order(6)}\n\n")
print(myCell1 + 12)