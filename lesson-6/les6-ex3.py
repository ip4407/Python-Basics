"""
Урок 6.
Задание 3.

Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        worker_full_name = self.name + ' ' + self.surname
        return worker_full_name

    def get_total_income(self):
        worker_income = self._income['wage'] + self._income['bonus']
        return worker_income


position1 = Position('Иван', 'Иванов', 'Специалист', 3000, 500)
print(f'Имя: {position1.name:>11}')
print(f'Фамилия: {position1.surname:>9}')
print(f'Должность: {position1.position:>11}\n')
print(f'Полное имя: {position1.get_full_name():>13}')
print(f'Полный доход: {position1.get_total_income()}\n')

position2 = Position('Петр', 'Петров', 'Эксперт', 4000, 750)
print(f'Имя: {position2.name:>11}')
print(f'Фамилия: {position2.surname:>9}')
print(f'Должность: {position2.position:>8}\n')
print(f'Полное имя: {position2.get_full_name():>13}')
print(f'Полный доход: {position2.get_total_income()}')
