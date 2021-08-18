from itertools import cycle
import time


class TrafficLight:
    __color = 'red'
    __count = 0
    __stop = 10

    def running(self):
        for el in cycle([('red', 7), ('yellow', 2), ('green', 4)]):
            self.__color = el[0]
            print(f'{self.__color}')
            time.sleep(el[1])
            self.__count += 1
            if self.__count == self.__stop:
                break


a = TrafficLight()
a.running()
