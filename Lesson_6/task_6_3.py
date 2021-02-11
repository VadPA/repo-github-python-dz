class Worker:
    name = ''
    surname = ''
    position = ''
    wage = 0
    bonus = 0
    _income = {}

    def __init__(self, name_, surname_, position_, wage_, bonus_):
        self.name = name_
        self.surname = surname_
        self.position = position_
        self._income = {"wage": wage_, "bonus": bonus_}


class Position(Worker):

    def get_full_name(self):
        print(f'имя сотрудника: {self.name}')
        print(f'фамилия сотрудника: {self.surname}')
        print(f'должность сотрудника: {self.position}')

    def get_total_income(self):
        print(f'доход сотрудника {self.surname}: {self._income["wage"] + self._income["bonus"]}:')


lst_personal = []

for i in range(2):
    print('-----------------------')
    print('Введите данные сотрудника:')
    name = input('Имя сотрудника:')
    surname = input('Фамилия сотрудника:')
    position = input('Должность сотрудника:')
    wage = float(input('должостной оклад сотрудника:'))
    bonus = float(input('должностная примия:'))
    print('-----------------------')
    pers = Position(name, surname, position, wage, bonus)
    pers.get_full_name()
    pers.get_total_income()
    lst_personal.append(pers)

print('------------ Personal -----------')

for el in lst_personal:
    el.get_full_name()
    print('-----------------------')
    el.get_total_income()
    print('-----------------------')
