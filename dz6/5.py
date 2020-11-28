
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing...")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start PEN {self.title} drawing!")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start PENCIL {self.title} drawing!")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start HANDLE {self.title} drawing!")

myPen = Pen("pen")
myPen.draw()
print("")

myPencil = Pencil("pencil")
myPencil.draw()
print("")

myHandle = Handle("handle")
myHandle.draw()
print("")

