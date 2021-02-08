# ----- task 4 --------

file_name = 'test_4.txt'
file_new = 'tes_4_rus.txt'

f = open(file_name, 'r', encoding='utf-8')
lst_str_old = f.readlines()
f.close()

lst_str_new = []
for el in lst_str_old:
    lst_str_new.append(el.replace('One', 'Один').replace('Two', 'Два').replace('Three', 'Три').replace('Four', 'Четыре'))

f_new = open(file_new, 'w', encoding='utf-8')
f_new.writelines([el for el in lst_str_new])

f_new.close()

