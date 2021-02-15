# ----- task 5 --------

import decimal
from functools import reduce


def my_func_mult(prev_el, el):
    return prev_el * el


def my_gen(start, end):
    i = start
    while i <= end:
        if i % 2 == 0:
            yield i
            i += 1
        else:
            i += 1


# --- var 1 -------
print([el for el in range(100, 1001, 2)])
print(f'{decimal.Decimal((reduce(lambda x, y: x * y, [el for el in range(100, 1001, 2)]))):.4e}')

# --- var 2 -------
print([el for el in range(100, 1001, 2)])
print(f'{decimal.Decimal((reduce(my_func_mult, [el for el in range(100, 1001, 2)]))):.4e}')

# --- var 3 -------
print([el for el in my_gen(100, 1000)])
print(f'{decimal.Decimal((reduce(my_func_mult, [el for el in my_gen(100, 1000)]))):.4e}')
