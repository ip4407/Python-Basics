"""
Урок 3. Функции
Задание 6.

Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(user_input):
    return user_input.capitalize()


def cap_text(text):
    text_list = text.split()
    cap_text_list = ' '.join([int_func(j) for j in text_list])
    return cap_text_list


print(f'Резульат работы функции int_func:\n{int_func("text")}\n')
print(f'Резульат работы функции cap_text:\n{cap_text("a line with some text")}')
