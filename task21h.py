# Напишите программу, которая принимает на вход вещественное число и
#  показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

x = input('Введите число: ')
summa = 0
for i in x:
    if i != '.':
        summa += int(i)
print(summa)