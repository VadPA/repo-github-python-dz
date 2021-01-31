err: bool = False
correct = False
while not err:
    try:
        while not correct:
            a = float(input('Введите сколько спортсмен пробежал в первый день:'))
            if a >= 0:
                correct = True
            else:
                print('Вы ввели отрицательное число, дистанция не может быть отрицательной:')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите положительное число')

err: bool = False
correct = False

while not err:
    try:
        while not correct:
            b = float(input('Введите сколько спортсмен должен пробегать:'))
            if b > a:
                correct = True
            elif b < 0:
                print(f'Вы ввели отрицательное число, дистанция не может быть отрицательной:')
            elif b <= a:
                print(f'Вы ввели число меньше или равно {a}, цель не может быть отрицательной, он же спортсмен.')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите положительное число')

i = 1
x = a
while x < b:
    print(f'{i}-й день пробежал: {x:0.2f} км')
    x = x * 1.1
    i += 1
print(f'{i}-й день пробежал: {x:0.2f} км')
print(f'Результат будет достигнут на {i}-й день.')
