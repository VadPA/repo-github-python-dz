# ----- task 1 --------

name_file = input('Введите имя файла: ')
print('Введите текст, которвый вы хотите записать в этот файл:')
lst = []
while True:
    s = input()
    lst.append(s)
    if not s:
        break

f = open(name_file, 'w', encoding='utf-8')
for el in lst:
    f.write('{0}\n'.format(el))
f.close()
