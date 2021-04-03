"""
Урок 4.
Задание 1.

Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

"""

from sys import argv

program_name, output_in_hours, rate_per_hour, bonus = argv


def payroll_accounting(output_in_hours, rate_per_hour, bonus):
    return (float(output_in_hours) * float(rate_per_hour)) + float(bonus)


print(f"Имя программы: {program_name}")
print(f"Выработка в часах: {output_in_hours} час.")
print(f"Ставка в час: {rate_per_hour} руб.")
print(f"Премия: {bonus} руб.")
print(f'Зарплата сотрудника: {payroll_accounting(output_in_hours, rate_per_hour, bonus):.2f} руб.')
