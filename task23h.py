# 3. Задайте список из n чисел последовательности (1 - 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число: '))
sum = 0
for i in range(n):
    sum += (1-1/(i+1))**(i+1) + i + 1
    print(i+1, '->', sum)
# суммы с примером не совпадают поскольку ноль в степени 1 будет ноль,
# n равное нулю брать нельзя, т.к. будет деление на ноль
