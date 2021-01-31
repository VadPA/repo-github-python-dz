err = False
correct = False
while not err:
    try:
        while not correct:
            sec = int(input('Введите кол-во секунд:'))
            if sec > 0:
                correct = True
            else:
                print('Вы ввели отрицательное число или ноль, повторите попытку:')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите число')
hour = sec // 3600
minut = (sec - hour * 3600) // 60
secc = sec - hour * 3600 - minut * 60
print(f'Результат перевода {sec} секунд в формат чч:мм:сс ->')
print(f'{hour:02}:{minut:02}:{secc:02}')
