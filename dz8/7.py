
class Complex:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f"({self.a} + {self.b}*i)"


c1 = Complex(5, 4)
c2 = Complex(6, 0)
c3 = Complex(2, 3)

print(f"{c1} + {c2} = {c1 + c2}")
print(f"{c1} * {c2} = {c1 * c2}")
print(f"{c1} * {c3} = {c1 * c3}")
print(f"{c1} + {c2} + {c3} = {c1 + c2 + c3}")