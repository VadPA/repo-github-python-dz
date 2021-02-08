def exp_el_var1(x_: float, y_: int):
    res = x_ ** y_
    return res


def exp_el_var2(a: float, b: int):
    res = 1
    n = abs(b)
    # ------- самый короткий вариант   :)
    for _ in range(abs(n)):
        res *= a
    # ---- вариант 2 ------
    # i = n
    # if n != 0:
    #     if n > 1:
    #         for i in range(n, 1, -1):
    #             r *= a
    #     else:
    #         res = a
    # else:
    #     res = 1
    # ------ вариант 1 ------
    # if n > 1:
    #     while i >= 2:
    #         r *= a
    #         i -= 1
    # elif n == 1:
    #     res = a
    # elif n == 0:
    #     res = 1
    # if b < 0:
    #     res = 1 / r
    return 1 / res


err: bool = False
while not err:
    try:
        x = float(input('Введите число больше нуля:'))
        if x >= 0:
            err = True
        else:
            print('вы ввели значения меньше нуля, повторите пожалуйста')
    except Exception as e:
        if e is not None:
            print('вы ввели не те значения, повторите пожалуйста')

err: bool = False
while not err:
    try:
        y = int(input('Введите целое число меньше нуля:'))
        if y <= 0:
            err = True
        else:
            print('вы ввели значения больше нуля, повторите пожалуйста!')
    except Exception as e:
        if e is not None:
            print('вы ввели не те значения, повторите пожалуйста')

print(f'Результат возведения числа "{x}" в степень "{y}" = {exp_el_var1(x, y):.16f}')
print(f'Результат возведения числа "{x}" в степень "{y}" = {exp_el_var2(x, y):.16f}')
