
class Matrix:
    def __init__(self,*rows):
        self.rows = rows

    def __str__(self):
        return "\r\n".join([" ".join([f"{c}" for c in r]) for r in self.rows])

    def __add__(self,other):
        return Matrix(*[[self.rows[ri][ci] + other.rows[ri][ci] for ci in range(0,len(self.rows[ri]))] for ri in range(0,len(self.rows))])


myM = Matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
newM = Matrix([5, 5 ,5], [6, 6, 6], [7, 7, 7])
M2 = Matrix([11, 12, 13], [122, 123, 321], [221, 101, 0])
print(f"{myM} \n + \n{newM} \n + \n{M2} \n = \n{myM + newM + M2}")
