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
        return self._width, self._length, self.thickness, self.weight


lst_road = []

for i in range(1):
    width = float(input('Введите длину дороги (м):'))
    length = float(input('Введите ширину дороги (м):'))
    thickness = float(input('Введите толщина слоя асфальта (м):'))
    print('-----------------------')
    r = Road(length, width, thickness)
    lst_road.append(r)

for el in lst_road:
    print('-----------------------')
    print('Параметры дороги:')
    print(f'Ширина дороги: {el.road_info()[0]} м.')
    print(f'Длина дороги: {el.road_info()[1]} м.')
    print(f'При толщине слоя асфальта {el.road_info()[2]:.2f}м масса асфальта: {el.road_info()[3]:.2f} кг.')
    print('-----------------------')
