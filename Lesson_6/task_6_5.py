class Stationery:
    title = ''

    def __init__(self, title_):
        self.title = title_

    def draw(self):
        print(f'Запуск отрисовки объектом: {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


a = Pen('ручка')
a.draw()
b = Pencil('карандаш')
b.draw()
c = Handle('маркер')
c.draw()
