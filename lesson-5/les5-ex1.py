"""
Урок 5.
Задание 1.

Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open("text_les5-ex1.txt", 'a') as f:
    line = None
    stop_line = ''
    while line != stop_line:
        line = input('Введите текст.\nДля завершения ввода введите пустую строку:\n')
        f.write(line + '\n')
        # Вариант вывода текстовых строк в файл:
        # print(line, file=f)
