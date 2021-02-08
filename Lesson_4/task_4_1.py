from sys import argv


def sum_zp(x_: int, y_: float, p_: float):
    return x_ * y_ + p_


_, x, y, p = argv
print(f'Заработная плата = {sum_zp(int(x), float(y), float(p))} $/weekly')
