catalog = []
print('Внесите полученный товар в складскую тетрадь:')
ex = False
count = 1
while not ex:
    print('Введите:')
    name = input('наименование товара:')
    cost = float(input('стоимость товара:'))
    q = int(input('количество товара:'))
    n = input('единицу измерения товара:')
    el = {'наименование': name,
          'стоимость': cost,
          'количество': q,
          'ед. изм.': n}
    el_lst = (count, el)
    catalog.append(el_lst)
    count += 1
    str1 = input('Продолжать (Y,N):')
    if str1 == 'Y' or str1 == 'y':
        ex = False
    elif str1 == 'N' or str1 == 'n':
        ex = True

for i, e in catalog:
    print(i, e)
