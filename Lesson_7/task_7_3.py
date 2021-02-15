class OrganicCell:
    def __init__(self, number_, column_):
        self.__number = number_
        self.column = column_

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number_):
        if number_ < 0:
            print('Недопустимый параметр!')
        else:
            self.__number = number_

    def __add__(self, other):
        return OrganicCell(self.number + other.number, self.column)

    def __sub__(self, other):
        if self.number - other.number > 0:
            res = self.number - other.number
        else:
            res = -1
        return OrganicCell(res, self.column)

    def __mul__(self, other):
        return OrganicCell(self.number * other.number, self.column)

    def __truediv__(self, other):
        return OrganicCell(self.number // other.number, self.column)

    def make_order(self):
        def star(i_):
            s = ''
            for j in range(i_):
                s += '*'
            return s

        full = self.number // self.column
        remainder = self.number % self.column
        res_str = ''
        for i in range(full):
            res_str += star(self.column) + '\n'
        if remainder != 0:
            res_str += star(remainder) + '\n'
        return res_str


c = OrganicCell(12, 5)
c.number = -12
print(f'{c.make_order()}')
c1 = OrganicCell(18, 3)
print(f'{c1.make_order()}')
c4 = c + c1
print(f'{c4.make_order()}')
c2 = OrganicCell(20, 7)
print(f'{c2.make_order()}')
c3 = OrganicCell(48, 5)
print(f'{c3.make_order()}')
c5 = c3 - c2
print(f'{c5.make_order()}')
c6 = c3 / c2
print(f'{c6.make_order()}')
c7 = c2 * c
print(f'{c7.make_order()}')
