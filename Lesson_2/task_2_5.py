my_list = [8, 7, 5, 5, 3, 3, 3, 2]
print(f'Имеем рейтинг: {my_list}')
ad = False
n = int(input('Введите новой рейтинг:'))
for i, el in enumerate(my_list):
    if n >= my_list[i]:
        my_list.insert(i, n)
        ad = True
        break
if not ad:
    my_list.insert(len(my_list), n)
print(f'Имеем новый рейтинг: {my_list}')
