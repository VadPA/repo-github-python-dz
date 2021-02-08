# ----- task 5 --------

import math
import random

file_name_num = 'test_5_num.txt'

n = int(input('Введите пороговое число (целое):'))
lst_num = []
for el in (range(20)):
    lst_num.append(random.randint(-n, n))
print(f'Имеем список чисел: {lst_num}')
print(f'Сумма чисел списка: = {math.fsum(lst_num)}')

f = open(file_name_num, 'w', encoding='utf-8')
line_num = [str(el) + ' ' for el in lst_num]
s = ''.join(line_num)
f.write(s)
# ---------- or -----------
# print(s, file=f)
# ------------------------
f.close()
