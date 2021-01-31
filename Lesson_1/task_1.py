err: bool = False
while not err:
    try:
        n = int(input('Введите целое число:'))
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не целое значение, введите целое число')

err: bool = False
while not err:
    try:
        f = float(input('Введите действительное число:'))
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числое значение, введите число')

err: bool = False
while not err:
    try:
        s = input('Введите строку:')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не пойми чего, введите строку')

print(f'Вы вели целое число: {n}, действительное число: {f}, и строку: {s}')