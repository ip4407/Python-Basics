"""
Урок 3.
Задание 2.

Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(user_first_name, user_last_name, user_year_birth, \
              user_city, user_email, user_phone):
    """
    Ввод данных пользователя
    :param user_first_name: Имя
    :param user_last_name: Фамилия
    :param user_year_birth: Год рождения
    :param user_city: Город проживания
    :param user_email: E-mail
    :param user_phone: телефон
    :return: Возвращает введённые данные
    """
    print('Введённые данные пользователя:')
    print(f'Пользователь: {user_last_name} {user_first_name}, Год рождения: {user_year_birth}, Город проживания: \
{user_city}, E-mail: {user_email}, Телефон: {user_phone}')


user_data(user_email='name@gmail.com', user_phone='+7 (495) 456-78-90', user_year_birth=1971, \
          user_city='Москва', user_first_name='Иван', user_last_name='Иванов')
