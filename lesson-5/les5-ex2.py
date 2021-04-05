"""
Урок 5.
Задание 2.

Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

row_count = 0
word_count = 0
all_word_count = 0

with open("text_les5-ex2.txt") as f:
    while True:
        read_line = f.readline()
        if not read_line:
            break
        else:
            row_count += 1
            word_count = len(list(read_line.split()))
            all_word_count += word_count
            print(f'В строке {row_count} количество слов = {word_count}.')

print(f'Всего строк в файле: {row_count}.')
print(f'Количество слов в файле: {all_word_count}')
