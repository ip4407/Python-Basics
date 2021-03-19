"""
Урок 1.
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_number = input('Введите целое положительное число: ')

# Вариани решения 1
i = 1
temp = user_number
max_digit = -1

while i <= len(user_number):
    digit = int(temp) % 10
    temp = int(temp) // 10
    i += 1
    if digit > max_digit:
        max_digit = digit

print('\nВариант решения 1.')
print(f'Максимальная цифра в введённом числе = {max_digit}')

# Вариани решения 2
temp = user_number
digits = []
while temp != 0:
    digit = int(temp) % 10
    temp = int(temp) // 10
    digits.append(digit)

print('\nВариант решения 2.')
print(f'Максимальная цифра в введённом числе = {max(digits)}')