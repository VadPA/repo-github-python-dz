class Car:
    speed = int(0)
    color = ''
    name = ''
    type = ''
    is_police = bool
    max_speed = 0
    direction = {'лево': ' повернула налево',
                 'право': ' повернула направо'
                 }

    def __init__(self, name_, color_, type_, is_police_):
        self.color = color_
        self.name = name_
        self.type = type_
        self.is_police = is_police_
        self.mov = False

    def go(self):
        if not self.mov:
            print(f'Машина "{self.name} - {self.type}" поехала')
            self.speed += 10
            self.show_speed(self.speed)
            self.mov = True
        else:
            self.speed += 10
            print('ускоряемся!')
            self.show_speed(self.speed)

    def speed_down(self):
        if not self.mov or self.speed == 0:
            print('замедляться некуда. Стоим итак.!')
            self.show_speed(self.speed)
        else:
            print(f'Машина "{self.name} - {self.type}" замедляется')
            self.speed -= 10
            self.show_speed(self.speed)
            if self.speed != 0:
                self.mov = True
            else:
                self.mov = False

    def stop(self):
        print(f'Машина "{self.name} - {self.type}" остановилась')
        self.mov = False

    def turn(self, direction_):
        if not self.mov:
            print('Чтобы повернуть сначала нужно поехать!')
        else:
            print(f'Машина "{self.name} - {self.type}" {self.direction[direction_]}')

    def show_speed(self, speed_):
        if self.speed > self.max_speed:
            self.is_police = True
            self.penalty_car()

        elif self.max_speed >= self.speed > 0:
            print(f'Скорость автомобиля: {self.speed}')
        elif self.speed == 0:
            self.mov = False
            self.stop()

    def penalty_car(self):
        if self.type != 'PoliceCar':
            self.is_police = True
        print(f'Автомобиль {self.name} - {self.type}! Вы превышаете разрешенную скорость, срочно сбавьте скорость!')
        print(f'Скорость автомобиля: {self.speed}. Допустимая: {self.max_speed}')
        if self.type != 'PoliceCar' and self.type != 'SportCar':
            print(f'Автомобиль {self.name} - {self.type}! За превышение скорости вам выписан штраф!')


class TownCar(Car):
    max_speed = 60


class SportCar(Car):
    max_speed = 200

    def show_speed(self, speed_):
        if self.speed > self.max_speed:
            print(f'Вы точно на гонках?')
            print(f'Скорость автомобиля: {self.speed}')
        else:
            print(f'Скорость автомобиля: {self.speed}')


class WorkCar(Car):
    max_speed = 40


class PoliceCar(Car):
    max_speed = 200

    def show_speed(self, speed_):
        if self.speed > self.max_speed:
            print(f'Осторожно! Вы превышаете безопасную скорость, поимка преступника не стоит вашей жизни!')
            print(f'Скорость автомобиля: {self.speed}')
        else:
            print(f'Скорость автомобиля: {self.speed}')


print('------------ Правила -----------')
print(' машина может поехать (набрать скорость), клавиша - "g" и "+",\n может повернуть налево, клавиша - "l",\n '
      'направо, клавиша - "r",\n остановится - клавиша "s" (также выход из программы)\n')

print('-----------------------')
print('Опишем машину:')
name = input('марка:')
color = input('цвет:')
print('-----------------------')

car = None
cl = ''
ex = False
while not ex:
    cl = input('Выберем машину (TownCar = "t", SportCar = "sc", WorkCar = "w", PoliceCar = "p"):')
    if cl == 't':
        car = TownCar(name, color, 'TownCar', False)
        ex = True
    elif cl == 'sc':
        car = SportCar(name, color, 'SportCar', False)
        ex = True
    elif cl == 'w':
        car = WorkCar(name, color, 'WorkCar', False)
        ex = True
    elif cl == 'p':
        car = PoliceCar(name, color, 'PoliceCar', False)
        ex = True
    else:
        print('Пробуем ещё!')

print('-------  Начинаем -------------')

a = car
ex = False
while not ex:
    cl = input()
    if cl == 'g' or cl == '+':
        a.go()
    elif cl == 'l':
        a.turn('лево')
    elif cl == 'r':
        a.turn('право')
    elif cl == '-':
        a.speed_down()
    elif cl == 's':
        a.stop()
        ex = True
