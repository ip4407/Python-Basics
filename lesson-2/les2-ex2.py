"""
Урок 2.
Задание 2.

Для списка реализовать обмен значений соседних элементов, т.е.
значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

l1 = ' '
list_el = []

while l1 != '':
    l1 = input('Введите любое целое число. Для завершения ввода введите пустую строку: ')
    if l1 != '':
        list_el.append(int(l1))

print(list_el)

for i in range(0, len(list_el), 2):
    if i + 1 < len(list_el):
        el1, el2 = list_el[i], list_el[i + 1]
        list_el[i], list_el[i + 1] = el2, el1

print(list_el)

