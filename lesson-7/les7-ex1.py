"""
Урок 7.
Задание 1.

Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

"""

matrix_32 = [[31, 22], [37, 43], [51, 86]]
matrix_33 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
matrix_24 = [[3, 5, 8, 3], [8, 3, 7, 1]]


class Matrix:
    __max_len_arg = 0

    def __init__(self, list_arg):
        self.list_arg = list_arg

        for i in range(len(self.list_arg)):
            for j in range(len(self.list_arg[i])):
                len_arg = len(str(self.list_arg[i][j]))
                if len_arg > Matrix.__max_len_arg:
                    Matrix.__max_len_arg = len_arg

    def __str__(self):

        str_matrix = ''
        for i in range(len(self.list_arg)):
            for j in range(len(self.list_arg[i])):
                str_matrix += f'{str(self.list_arg[i][j]):>{Matrix.__max_len_arg + 2}}'
            str_matrix += '\n'
        return str_matrix

    def __add__(self, other):
        new_matrix = ''
        for i in range(len(self.list_arg)):
            for j in range(len(self.list_arg[i])):
                new_matrix += f'{str(int(self.list_arg[i][j]) + int(other.list_arg[i][j])):>{Matrix.__max_len_arg + 2}}'
            new_matrix += '\n'
        return new_matrix


m1 = Matrix(matrix_33)
print(f'Матрица-1:\n{m1}')

m2 = Matrix(matrix_33)
print(f'Матрица-2:\n{m2}')

m3 = m1 + m2

print(f'Результат сложения Матрицы-1 с Марицей-2 :\n{m3}')
