"""
Урок 4.
Задание 6.

Реализовать два небольших скрипта:
●	итератор, генерирующий целые числа, начиная с указанного;
●	итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

"""

from itertools import count, cycle


def integer_generator(start_value, end_value):
    for i in count(int(start_value)):
        if i <= end_value:
            yield i
        else:
            break


print(list(integer_generator(3, 10)))

my_list = ['ab', 'cd', 'ef']


def cycle_generator(list_value, repetition_rate):
    repetition_counter = 0
    for i in cycle(list_value):
        if repetition_counter < repetition_rate:
            repetition_counter += 1
            yield i
        else:
            break


print(list(cycle_generator(my_list, 8)))