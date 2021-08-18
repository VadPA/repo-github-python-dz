# ----- task 6-1 --------

from sys import argv
from itertools import count
from itertools import cycle


_, c = argv

for el in count(int(c)):
    if el > 10:
        print('Сеанс окончен. Спасибо за внимание.')
        break
    elif el >= 3:
        print(el)
