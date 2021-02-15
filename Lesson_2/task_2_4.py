s = input(f'Введите строку:').split(' ')
# s = 'Маша мыла раму, потому что была воспитанной девочкой.'
for i, el in enumerate(s):
    print(i, el[0:10])

# или так

print('')
lst = list(s)
i = 0
for el in lst:
    print(i, el[0:10])
    i += 1
