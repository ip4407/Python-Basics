"""
Урок 5.
Задание 6.

Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

lessons_dict = {}
key_list, val_1, val_2, val_3 = '', '', '', ''
replace_list = ['(л)', '(пр)', '(лаб)', '-', ':']
sum_study = 0

with open("text_les5-ex6.txt", encoding='UTF-8') as f:
    while True:
        read_line = f.readline()
        if not read_line:
            break
        else:
            for i in replace_list:
                read_line = read_line.replace(i, '')
            read_list = list(read_line.split())
            sum_study = 0
            lesson_key = read_list[0]
            for i in range(1, len(read_list)):
                sum_study += int(read_list[i])
            lessons_dict.update({lesson_key: sum_study})

print(lessons_dict)
