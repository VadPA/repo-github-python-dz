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
        return self.name, self.surname, self.position


    def get_total_income(self):
        return self.surname, self._income["wage"] + self._income["bonus"]


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
    print(f'имя сотрудника: {el.get_full_name()[0]}')
    print(f'фамилия сотрудника: {el.get_full_name()[1]}')
    print(f'должность сотрудника: {el.get_full_name()[2]}')
    print('-----------------------')
    print(f'доход сотрудника {el.get_total_income()[0]}: {el.get_total_income()[1]}')
    print('-----------------------')
