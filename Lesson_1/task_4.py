max_num = 0
err = False
correct = False

while not err:
    try:
        while not correct:
            num = int(input('Введите положительное число больше 10:'))
            if num > 0:
                correct = True
            else:
                print('Вы ввели отрицательное число или ноль, повторите попытку:')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите число')

ost = num
if num > 9:
    while ost >= 10:
        max_num = ost % 10 if max_num < ost % 10 else max_num
        ost = ost // 10
    max_num = ost if max_num < ost else max_num
    print(f'максимальная цифра в числе {num}: {max_num}')
else:
    print(f'максимальная цифра в числе {num}: {num}')
