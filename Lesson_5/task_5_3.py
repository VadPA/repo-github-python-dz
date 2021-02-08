# ----- task 3 --------
file_name = 'zp.txt'

f = open(file_name, 'r', encoding='utf-8')
lst_str = f.readlines()
f.close()
lst_person = []
for el in lst_str:
    lst_person.append(el.replace('\n', '').split())

dict_personal = dict(lst_person)
l = float(input('Введите пороговую сумму:'))
print(f'Меньше {l} рублей получают следующие сотрудники:')
summ = 0
for key, value in dict_personal.items():
    summ += float(value)
    if float(value) < l:
        print(f'{key} - {float(value)} руб.')
ma = summ/len(lst_person)
print(f'Средняя з\\плата сотрудников состовляет: {ma:.2f} рублей.')

print(f'Меньше средней з\\плата получают следующие сотрудники:')

for key, value in dict_personal.items():
    if float(value) < ma:
        print(f'{key} - {float(value)} руб.')

