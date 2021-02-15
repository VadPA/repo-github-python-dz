class Vector:

    def __init__(self, arr_):
        self.arr = arr_

    def __str__(self):
        return f'Наш вектор: {self.arr}'

    def __add__(self, other):
        new_arr = []
        for i in range(len(self.arr)):
            new_arr.append(self.arr[i] + other.arr[i])
        return Vector(new_arr)


class Matrix:

    def __init__(self, matrix_):
        self.matrix = matrix_

    def __str__(self):
        result_str = ''
        s_temp = ''
        lst_max = []
        for i in range(len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if i == 0:
                    lst_max.append(len(str(self.matrix[i][j])))
                elif lst_max[j] < len(str(self.matrix[i][j])):
                    lst_max[j] = len(str(self.matrix[i][j]))

        for el in range(len(self.matrix)):
            for i, e in enumerate(self.matrix[el]):
                s_temp += str(e).rjust(lst_max[i]) + '  '
            s_temp = s_temp.rstrip()
            result_str += '|' + s_temp + '|' + '\n'
            s_temp = ''
        return result_str

    def __add__(self, other):
        new_matrix = []
        for el in range(len(self.matrix)):
            new_arr = Vector(self.matrix[el]) + Vector(other.matrix[el])
            new_matrix.append(new_arr.arr)
        return Matrix(new_matrix)


m_1 = Matrix([[111, 4, 13, 6, 12588], [2, 8, 47, 5, 9], [8, 4, 1, 3, 5]])
m_2 = Matrix([[2, 8, -187, 455, 9], [8, 4, 1, 3, 5], [12, 4, 3, 6, 8]])
m_3 = m_1 + m_2
print(m_1)
print(m_2)
print('--- Сумма двух матриц ----')
print(m_3)
