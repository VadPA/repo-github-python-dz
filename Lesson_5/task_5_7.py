# ----- task 7 --------
#
import json

file_name = 'test_7.txt'

with open(file_name, 'r', encoding='utf-8') as f:
    lst_str_f = f.readlines()
lst_temp_f = []
for el in lst_str_f:
    lst_temp_f.append(el.replace("\n", '').split())

name = ''
profit = 0
d_firm = dict()
i = 0
summ = 0
for el in lst_temp_f:
    name = el[0]
    profit = float(el[2])-float(el[3])
    if profit > 0:
        summ += profit
        i += 1
    d_firm[name] = profit

d_average_profit = {'average_profit': summ / i}
lst_res = [d_firm, d_average_profit]
s_json = json.dumps(lst_res)

with open('data_7.json', 'w', encoding='utf-8') as f:
    s_json = json.dumps(lst_res, ensure_ascii=False)
    f.write(s_json)

print(s_json)
