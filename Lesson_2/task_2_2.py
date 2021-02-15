lst = [2, 56, 'qwerty', [56, 'yew'], 3.14, {1, 2, 3, 4, 5}, 'non']
print(f'Есть список: {lst}.')
err: bool = False
str1 = ''
while not err:
    try:
        str1 = input(f'Есть желание дополнить (Y/N)?:')
        if str1 == 'Y' or str1 == 'N' or str1 == 'y' or str1 == 'n':
            err = True
        else:
            print('вы ввели не те значения, повторите пожалуйста')
    except Exception as e:
        if e is not None:
            print('вы ввели не те значения, повторите пожалуйста')

str_ = ''
if str1 == 'Y' or str1 == 'y':
    while str_ != 'n' or str_ != 'N':
        lst.append(input(f'Введите элемент для дополнения:'))
        lst.insert(len(lst), lst[len(lst) - 1][::-1])
        str_ = input(f'продолжим (Y/N)?:')
        if str_ == 'n' or str_ == 'N':
            break

print(f'старый список: {lst}')
print(f'')
count = 0
end = len(lst) if len(lst) % 2 == 0 else len(lst) - 1
while count < end:
    lst[count], lst[count + 1] = lst[count + 1], lst[count]
    count += 2
print(f'новый список: {lst}')
