"""
Урок 3. Функции
Задание 1.

Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_division1(arg1, arg2):
    """
    Деление двух чисел arg1 / arg2
    :param arg1: Числитель
    :param arg2: Знаменатель
    :return: Деление числителя на знаменатель
    """
    if arg2 == 0:
        return 'Ошибка деления на 0!\nВы ввели в качестве знаменателя 0.\nЗнаменатель не может быть равным нулю!'
    else:
        return arg1 / arg2


def my_division2(arg1, arg2):
    """
    Деление двух чисел arg1 / arg2
    :param arg1: Числитель
    :param arg2: Знаменатель
    :return: Деление числителя на знаменатель
    """

    try:
        division_result = arg1 / arg2
        return division_result
    except ZeroDivisionError:
        return 'Ошибка деления на 0!\nВы ввели в качестве знаменателя 0.\nЗнаменатель не может быть равным нулю!'


print('Деление двух чисел.\n')

print('Вариант функции 1.')
number1 = float(input('Введите числитель: '))
number2 = float(input('Введите знаменатель: '))
print(f'Результат деления: {my_division1(number1, number2)}\n')

# help(my_division1)

print('Вариант функции 2.')
number1 = float(input('Введите числитель: '))
number2 = float(input('Введите знаменатель: '))
print(f'Результат деления: {my_division2(number1, number2)}\n')
