lst = [2, 56, 'qwerty', [56, 'ytrewq'], 3.14, {1, 2, 3, 4, 5}]
count = 0
while count < len(lst):
    print(f'{count}-й элемент списка "{lst[count]}" является типом: {type(lst[count])}')
    count += 1
