# ----- task 7 --------

# --- var 1 -------
from functools import reduce


def my_iter(end):
    i_ = 1
    while i_ <= end:
        yield i_
        i_ += 1


n = int(input('Введите число:'))


def my_fact(el_prev, el):
    return el_prev * el


for i in my_iter(n):
    print(f'{i}!= {reduce(my_fact, [el for el in my_iter(i)])}')

print('----------------')


# --- var 2 -------

def fact(n_):
    res = 1
    for a in my_iter(n_):
        res *= a
        yield res


for i, elem in enumerate(fact(n)):
    print(f'{i + 1}!={elem}')

