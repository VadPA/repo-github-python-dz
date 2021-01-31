err = False
correct = False
while not err:
    try:
        while not correct:
            num = int(input('Введите положительное число:'))
            if num > 0:
                correct = True
            else:
                print('Вы ввели отрицательное число или ноль, повторите попытку:')
        err = True
    except Exception as e:
        if e is not None:
            print('вы ввели не числовое значение, введите число')

#print(num)
#print(num * 10 + num)
#print(num * 100 + num * 10 + num)
print(f'Результат перевода числа {num} в формат n + nn + nnn ->')
print(f'result :{num + num * 10 + num + num * 100 + num * 10 + num}')
