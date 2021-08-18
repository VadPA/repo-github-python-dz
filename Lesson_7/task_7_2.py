from abc import ABC, abstractmethod


class Clothes:
    count = 0

    def __init__(self, clothes_, param):
        self.title = clothes_
        self.__param = param

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < 0:
            print('Недопустимый параметр!')
        else:
            self.__param = param

    @abstractmethod
    def consumption_cloth(self):
        return self.__param


class Topcoat(Clothes):

    def consumption_cloth(self):
        Clothes.count += self.param / 6.5 + 0.5
        return self.param / 6.5 + 0.5


class Costume(Clothes):

    def consumption_cloth(self):
        Clothes.count += self.param * 2 + 0.3
        return self.param * 2 + 0.3


p = Topcoat('Пальто', 45)
print(f'Расход материала на "{p.title}":{p.consumption_cloth():0.2f}')
c = Costume('Костюм', 12)
print(f'Расход материала на "{c.title}":{c.consumption_cloth():0.2f}')
cloth = Clothes("", 1)
print(f'Общий расход материала:{cloth.count:0.2f}')
