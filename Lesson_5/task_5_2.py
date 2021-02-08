# ----- task 2 --------

file_name = 'test_2.txt'
file_name_from = 'test_1.txt'

f_from = open(file_name_from, 'r', encoding='utf-8')
lst_str = f_from.readlines()
f_from.close()
f_to = open(file_name, 'w', encoding='utf-8')
for el in lst_str:
    f_to.write('{0}'.format(el))
f_to.close()
print(f'Количество строк в файле: {len(lst_str)}')
for i, el in enumerate(lst_str):
    s = el.replace('\n', ' ').replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    s = s.split()
    print(f'В {i + 1}-й строке слов: {len(s)}')
