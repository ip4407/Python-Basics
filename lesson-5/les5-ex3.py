"""
Урок 5.
Задание 3.

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

employee_count = 0
sum_salary = 0

with open("text_les5-ex3.txt", encoding='UTF-8') as f:
    while True:
        read_line = f.readline()
        if not read_line:
            break
        else:
            employee, salary = list(read_line.split())
            employee_count += 1
            sum_salary += float(salary)
            if float(salary) < 20000.00:
                print(f'Сотрудник: {employee}, оклад: {salary} < 20 000.00.')

print(f'\nВсего сотрудников: {employee_count}.')
print(f'Средняя величина дохода сотрудников: {sum_salary / employee_count:.2f}')
