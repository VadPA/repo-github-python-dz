err: bool = False

while not err:
    try:
        val = float(input('Введите выручку фирмы за месяц (в рублях):'))
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите число (в рублях)')

err = False
correct = False

while not err:
    try:
        while not correct:
            cost = float(input('Введите затраты фирмы за месяц (в рублях):'))
            if cost >= 0:
                correct = True
            else:
                print('Вы ввели отрицательное число, затраты не могут быть отрицательными:')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите число (в рублях)')

    err = False
    correct = False
    while not err:
        try:
            while not correct:
                person = int(input('Введите кол-во сотрудников в фирме:'))
                if person > 0:
                    correct = True
                else:
                    print('Вы ввели отрицательное число или равное 0, кол-во человек не может быть отрицательными:')
            err = True
        except Exception as e:
            if e is not None:
                print('вы ввели не числовое значение, введите положительное число:')

if val > cost:
    print(f"Прибыль фирмы за месяц: {val - cost}")
    print(f'Рентабельность: {(val - cost) / val:.2f}')
    print(f'Прибыль фирмы в расчете на одного сотрудника: {(val - cost) / person:.2f}')
elif val == cost == 0 and person > 0:
    print(f'Результат работы фирмы: Вы чем там занимаетесь?!')
elif val == cost:
    print(f'Результат работы фирмы: можно лучше!')
else:
    print(f'Результат работы фирмы: Не очень. Надо лучше работать. Убыток составил: {val - cost} руб.')
    print(f'Убыток фирмы в расчете на одного сотрудника: {(val - cost) / person:.2f}')
