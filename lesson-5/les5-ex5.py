"""
Урок 5.
Задание 5.

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint


numbers = randint(3, 40)
sum_numbers = 0

with open("text_les5-ex5.txt", 'w', encoding='UTF-8') as f:
    for i in range(numbers):
        f.write(str(randint(0, 100)) + ' ')

with open("text_les5-ex5.txt", 'r', encoding='UTF-8') as f:
    read_line = f.readline()
    list_numbers = list(read_line.split())
    for i in list_numbers:
        sum_numbers += int(i)

print(sum_numbers)
