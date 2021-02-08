# ----- task 6-2 --------

from itertools import cycle


# lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O']

n = len(lst)

for el in cycle(lst):
    if n == 0:
        break
    print(el)
    n -= 1

