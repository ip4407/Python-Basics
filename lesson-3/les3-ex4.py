"""
Урок 3. Функции
Задание 4.

Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_exponentiation_1(number, degree):
    """
    Возведение числа number в степень degree.
    :param number: число
    :param degree: Степень
    :return: Возвращает результат возведения числа number в степень degree
    """
    return number ** degree


def my_exponentiation_2(number, degree):
    """
    Возведение числа number в степень degree.
    :param number: число
    :param degree: Степень
    :return: Возвращает результат возведения числа number в степень degree
    """
    i = 0
    multiplication = 1
    if degree < 0:
        while i < abs(degree):
            multiplication *= number
            i += 1
        return 1 / multiplication
    else:
        while i < degree:
            multiplication *= number
            i += 1
        return multiplication


x = 2.1
y = -3
print('Рзультат функции 1.')
print(f'Число {x} в степени {y} = {my_exponentiation_1(x, y)}\n')
print('Рзультат функции 2.')
print(f'Число {x} в степени {y} = {my_exponentiation_2(x, y)}\n')
