from abc import ABC, abstractmethod


class Store:
    equipments = {}

    def __init__(self):
        pass

    def push(self, e):
        if e.Identify() in self.equipments:
            print("WARNING!!! the item already in Store")
        else:
            print(f"Putting {e} in Store...")
            self.equipments[e.Identify()]=e
            e.setDepartment("Store")

    def pop(self, identifier, department):
        if identifier in self.equipments:
            print(f"Putting {self.equipments[identifier]} in department {department}...")
            self.equipments[identifier].setDepartment(department)
            del self.equipments[identifier]
        else:
            print("WARNING! Selected equipment not found in store")


class Equipment(ABC):
    color = "white"
    department = ""
    identifier = ""

    def __init__(self, identifier):
        self.identifier = identifier

    def setDepartment(self, department):
        self.department = department

    def Identify(self):
        return self.identifier

    @abstractmethod
    def describe(self):
        pass

    def __str__(self):
        return f"{self.describe()} {self.identifier} ({self.department})"

    def __repr__(self):
        return f"{self.describe()} {self.identifier} ({self.department})"


class Printer(Equipment):
    format = "A4"
    mode = "blackwhite"

    def __init__(self, identifier, format="A4", mode="blackwhite"):
        super().__init__(identifier)
        self.format = format
        self.mode = mode

    def describe(self):
        return f"Printer {self.format}/{self.mode}"

class Scaner(Equipment):
    speed = 1.2

    def __init__(self, identifier, speed=1.2):
        super().__init__(identifier)
        self.speed = speed

    def describe(self):
        return f"Scaner {self.speed}pps"


class Xerox(Equipment):
    network = False

    def __init__(self, identifier, network=False):
        super().__init__(identifier)
        self.network = network

    def describe(self):
        return f"Xerox {'net' if self.network else 'local'}"


store1 = Store()
contP1 = Printer("111111")
contP2 = Printer("222222")
store1.push(contP1)
store1.push(contP2)
print(contP1)
print(contP2)
print(store1.equipments)
print()

store1.pop(contP1.Identify(),"Contability")
print(contP1)
print(contP2)
print(store1.equipments)
print()

contX1 = Xerox("33333")
directorS1 = Scaner("44444")
store1.push(contX1)
store1.push(directorS1)
store1.push(directorS1)
store1.pop(directorS1.Identify(),"Director")
store1.pop(directorS1.Identify(),"Director")
print(contP1)
print(contP2)
print(contX1)
print(directorS1)
print(store1.equipments)
