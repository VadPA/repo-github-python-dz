class Road:
    _length = 0  # длина дороги
    _width = 0  # ширина дороги
    _density_asphalt = 1500  # плотность асфальта
    weight = 0  # масса слоя асфальта
    thickness = 0  # толщина слоя асфальта

    def __init__(self, length_, width_, thickness_):
        self._length = length_
        self._width = width_
        self.thickness = thickness_
        self.weight = length_ * width_ * thickness_ * self._density_asphalt

    def road_info(self):
        print('Параметры дороги:')
        print(f'Ширина дороги: {self._width} м.')
        print(f'Длина дороги: {self._length} м.')
        print(f'При толщине слоя асфальта {self.thickness:.2f} м масса асфальта: {self.weight:.2f} кг.')


width_ = float(input('Введите длину дороги (м):'))
length_ = float(input('Введите ширину дороги (м):'))
thickness_ = float(input('Введите толщина слоя асфальта (м):'))
print('-----------------------')
r1 = Road(length_, width_, thickness_)
r1.road_info()
print('-----------------------')
width_ = float(input('Введите длину дороги (м):'))
length_ = float(input('Введите ширину дороги (м):'))
thickness_ = float(input('Введите толщина слоя асфальта (м):'))
print('-----------------------')
r2 = Road(length_, width_, thickness_)
r2.road_info()
