def user_list(name, surname, year_birth, city, email, tel):
    return f'Имя: {name}, Фамилия: {surname}, год рождения: {year_birth}, ' \
           f'город проживания: {city}, эл.почта: {email}, тел.: {tel}'


ex = False
b = False
i = 1
user_lst = []

while not ex:
    print('Введите данные пользователя:')
    name = input('Имя:')
    surname = input('Фамилия:')
    year_birth = input('год рождения:')
    city = input('город проживания:')
    email = input('эл.почта:')
    tel = input('тел.:')
    err: bool = False
    s = ''
    while not err:
        try:
            print(f'Проверьте правильность введённых данных:')
            print(user_list(name, surname, year_birth, city, email, tel))
            s = input('Правильно (Y/N):')
            if s == 'Y' or s == 'N' or s == 'y' or s == 'n':
                err = True
            else:
                print('вы ввели не те значения, повторите пожалуйста')
        except Exception as e:
            if e is not None:
                print('вы ввели не те значения, повторите пожалуйста')

    if s == 'Y' or s == 'y':
        us = {'Имя': name,
              'Фамилия': surname,
              'год рождения': year_birth,
              'город проживания': city,
              'эл.почта': email,
              'тел.': tel}
        user_el = (i, us)
        user_lst.append(user_el)
        i += 1
        err: bool = False
        s1 = ''
        while not err:
            try:
                s1 = input('Данные ввели правильно. Продолжим вносить? (Y/N):')
                if s1 == 'Y' or s1 == 'N' or s1 == 'y' or s1 == 'n':
                    err = True
                else:
                    print('вы ввели не те значения, повторите пожалуйста')
            except Exception as e:
                if e is not None:
                    print('вы ввели не те значения, повторите пожалуйста')
        if s1 == 'Y' or s1 == 'y':
            continue
        else:
            ex = True
    elif s == 'N' or s == 'N':
        ex = True
print(f'Вы не плохо потрудились. Вот результат:')
for i, e in user_lst:
    print(i, e)
