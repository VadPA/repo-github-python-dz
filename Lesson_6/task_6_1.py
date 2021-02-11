import time


class TrafficLight:
    _color = {1: 'красный',
              2: 'желтый',
              3: 'зелёный'}

    def trafficLight_info(self, i):
        print(f'Горит {self._color[i]}!')

    def running(self, n_):
        while True:
            for el in range(n_, 4):
                if el == 1:
                    self.trafficLight_info(el)
                    time.sleep(7)
                elif el == 2:
                    self.trafficLight_info(el)
                    time.sleep(2)
                elif el == 3:
                    self.trafficLight_info(el)
                    time.sleep(5)
            n_ = 1


n = int(input('Введите значение от 1 до 3 - (1- красный, 2 - желтый, 3 - зеленый):'))
a = TrafficLight()
a.running(n)
