
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction="forward"

    def get_speed(self):
        return self.speed

    def get_color(self):
        return self.color

    def get_name(self):
        return self.name

    def get_is_police(self):
        return self.is_police

    def get_direction(self):
        return self.direction

    def go(self):
        print(f"{self.name} Run!")

    def stop(self):
        print(f"{self.name} stopped!")

    def turn(self,direction):
        self.direction = direction
        print(f"{self.name} turns {direction}!")

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}")

class TownCar(Car):
    def __init__(self,speed, color, name):
        super().__init__(speed,color,name,False)

    def show_speed(self):
        print(f"Town car {self.name}'s speed is {self.speed}")
        if self.speed > 60:
            print("WARNING! Too big speed!")

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f"Work car {self.name}'s speed is {self.speed}")
        if self.speed > 40:
            print("WARNING! Too big speed!")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


myCar = Car(121, "green", "MyCar", False)
print(f"{myCar.get_name()} has color {myCar.get_color()} and moves {myCar.get_direction()} with speed {myCar.get_speed()} and it {'is POLICE' if myCar.get_is_police() else 'ISNT police'}")
myCar.show_speed()
myCar.turn("left")
myCar.go()
myCar.stop()
print("")

myTcar = TownCar(45, "grey", "MyTcar")
print(f"{myTcar.get_name()} has color {myTcar.get_color()} and moves {myTcar.get_direction()} with speed {myTcar.get_speed()} and it {'is POLICE' if myTcar.get_is_police() else 'ISNT police'}")
myTcar.show_speed()
myTcar.turn("right")
myTcar.stop()
print("")

myScar = SportCar(250, "red", "myScar")
print(f"{myScar.get_name()} has color {myScar.get_color()} and moves {myScar.get_direction()} with speed {myScar.get_speed()} and it {'is POLICE' if myScar.get_is_police() else 'ISNT police'}")
myScar.show_speed()
myScar.stop()
print("")

myWcar = WorkCar(45, "yellow", "myWcar")
print(f"{myWcar.get_name()} has color {myWcar.get_color()} and moves {myWcar.get_direction()} with speed {myWcar.get_speed()} and it {'is POLICE' if myWcar.get_is_police() else 'ISNT police'}")
myWcar.show_speed()
myWcar.turn("right")
myWcar.go()
myWcar.stop()
print("")

myPcar = PoliceCar(80, "blue", "myPcar")
print(f"{myPcar.get_name()} has color {myPcar.get_color()} and moves {myPcar.get_direction()} with speed {myPcar.get_speed()} and it {'is POLICE' if myPcar.get_is_police() else 'ISNT police'}")
myPcar.show_speed()
myPcar.turn("backward")
myPcar.go()
myPcar.stop()

