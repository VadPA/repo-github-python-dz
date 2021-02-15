def my_func(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Деление на ноль запрещено!!')
        return


ex = False

while not ex:
    err: bool = False
    print('Реализация функции, возвращающей результат деления числа "a" на число "b":')
    while not err:
        try:
            a = float(input('Введите число a:'))
            err = True
        except Exception as e:
            if e is not None:
                print('вы ввели не числовое значение, введите число!')

    err: bool = False
    while not err:
        try:
            b = float(input('Введите отличное от нуля число b:'))
            print(f'Результат деления {a} / {b} = {my_func(a, b):0.2f}')
            err = True
        except Exception as e:
            if e is not None:
                print('вы ввели не числовое значение или ноль, введите число отличное от нуля!')

    #print(f'Результат деления {a} / {b} = {my_func(a, b):0.2f}')

    s = ''
    while s != 'n' or s != 'N' or s != 'Y' or s != 'y':
        s = input('Продолжим? (Y/N :)')
        if s == 'Y' or s == 'y':
            ex = False
            break
        elif s == 'N' or s == 'n':
            ex = True
            break
        else:
            print('вы ввели не те значения, повторите пожалуйста!')
