# lst = [1, 2, 5, -8, 12, 54, 12, 89, 65, 7]
lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# print([el for i, el in enumerate(lst) if lst[i] > lst[i-1] and (i != 0)])
# new_lst = [el for i, el in enumerate(lst) if lst[i] > lst[i-1] and (i != 0)]
new_lst = [el for i, el in enumerate(lst) if lst[i] > lst[i - 1] and (i != 0)]
print(new_lst)
