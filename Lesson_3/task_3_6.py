def word_num_up(w, num_):
    word_ = []
    for i, el_ in enumerate(w):
        if i == num_:
            el_up = w[i].upper()
            word_.append(el_up)
        else:
            word_.append(el_)
    word_ = "".join(word_)
    return word_


lst_word = []
lst_result = []

s = input('Введите строку:')
num = int(input('Введите номер символа (от 1), который хотим перевести в верхний регистр:')) - 1
lst_word = s.split(' ')
for el in lst_word:
    w_ = word_num_up(el, num)
    lst_result.append(w_)

#print(lst_result)
print(f'Результирующая строка: {" ".join(lst_result)}')
