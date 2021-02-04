def sum_num(l_num):
    summa = 0
    for element in l_num:
        summa += int(element)
    return summa


print(f'В цикле подсчитываем сумму введеных чисел нарастающим итогом, введенных через пробел')
print(' до тех пор пока среди чисел не появится символ "n"')

lst_num = []
l_int = []
ex = False
while not ex:
    err: bool = False
    while not err:
        try:
            l_str = input('Введите целые числа через пробел:').split(' ')
            for i, el in enumerate(l_str):
                if el != 'n' and el != 'N':
                    l_int.append(int(el))
                else:
                    ex = True
            print(f'Сумма чисел = {sum_num(lst_num + l_int)}')
            if len(lst_num) >= 1:
                print(f'Прежняя сумма чисел = {sum_num(lst_num)}')
            if len(l_int) >= 1:
                lst_num.extend(l_int)
            l_int.clear()
            l_str.clear()
            err = True
        except Exception as e:
            if e is not None:
                l_int.clear()
                l_str.clear()
                print('вы ввели не те значения, повторите пожалуйста')
