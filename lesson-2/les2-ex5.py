"""
Урок 2.
Задание 5.

Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то
новый элемент с тем же значением должен разместиться после них.

Подсказка.
Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)

rate = int(input('Введите рейтинг: '))

for i in my_list:
    if rate > i:
        my_list.insert(my_list.index(i), rate)
        break
    elif my_list.index(i) == len(my_list) - 1:
        my_list.insert(my_list.index(i) + 1, rate)
        break

print(my_list)
