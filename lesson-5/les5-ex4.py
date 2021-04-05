"""
Урок 5.
Задание 4.

Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

ru_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
word1 = ''
word2 = ''

f2 = open("text_RU_les5-ex4.txt", 'w', encoding='UTF-8')
with open("text_EN_les5-ex4.txt", encoding='UTF-8') as f1:
    while True:
        read_line = f1.readline()
        if not read_line:
            break
        else:
            word1, word2 = list(read_line.split(sep=' - '))
            for k, v in ru_dict.items():
                if k == word1:
                    f2.write(v + ' - ' + word2)
f2.close()
