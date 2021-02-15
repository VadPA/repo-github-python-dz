class Stationery:
    def __init__(self, title_=None):
        self.title = title_

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: ручка')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: карандаш')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: маркер')


a = Pen()
a.draw()
b = Pencil()
b.draw()
c = Handle()
c.draw()
