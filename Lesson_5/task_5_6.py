# ----- task 6 --------

file_name = 'test_6.txt'

f = open(file_name, 'r', encoding='utf-8')
lst_str_pr = f.readlines()
f.close()

lst_temp = []
for el in lst_str_pr:
    lst_temp.append(el.replace('\n', '').replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').split(':'))
summ = 0
for el in lst_temp:
    num = el[1].split()
    for i in num:
        summ += int(i)
    el[1] = summ
    summ = 0

dict_pr = dict(lst_temp)
print(dict_pr)

