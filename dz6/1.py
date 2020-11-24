import time

class TrafficLight:
    __intervals = [
        {"color": "red", "interval": 7},
        {"color": "yellow", "interval": 2},
        {"color": "green", "interval": 10},
    ]
    def __init__(self):
        self.__color = "red"
        self.__i = 0

    def running(self):
        while True:
            self.__color = self.__intervals[self.__i]['color']
            print(self.__color)
            time.sleep(self.__intervals[self.__i]['interval'])
            self.__i += 1
            if self.__i >= len(self.__intervals):
                self.__i = 0


myTL = TrafficLight()
myTL.running()