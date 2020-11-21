
class Road:
    def __init__(self,length,width):
        self._length=length
        self._width=width

    def asphaltWeight(self,weight1m,depth):
        return self._length*self._width*weight1m*depth

myR = Road(20,5000)
print(f"{myR.asphaltWeight(25,5)} kg")

