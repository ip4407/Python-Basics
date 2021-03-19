"""
Урок 1.
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


time_in_seconds = int(input('Введите время в секундах: '))

hour = time_in_seconds // 3600
minutes = (time_in_seconds - hour * 3600) // 60
seconds = (time_in_seconds - hour * 3600 - minutes * 60)
# вариант: seconds = time_in_seconds % 60

print(f'Введено: {time_in_seconds} секунд')
print(f'{hour:02d}:{minutes:02d}:{seconds:02d}')
