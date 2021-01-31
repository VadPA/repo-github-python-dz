c = {
    'name': 'Alex',
    'age': 45,
}
print(c['name'])
print(type(c['name']))
print(type(c['age']))
# print('Вас зовут %s, вам %d лет' % (c['name'], c['age']))
# print('Вас зовут {}, вам {} лет'.format(c['name'], c['age']))
print(f'Вас зовут {c["name"]}, вам {c["age"]} лет')
# c['name'] = input('Введите ваше имя:')
# c['age'] = int(input('Введите сколько вам лет:'))
n = [1, 3, 6, 7, 'wer']
n[len(n) - 1] = 'qwerty'
n.append(45)
print(n[len(n) - 1])
print(type(len(n) - 1))
print(n)
n.pop(4)
print(n)
b = (1, 3, 6, 7, 'wer')
print(b)
print(type(len(b) - 1))
print(type(b))
