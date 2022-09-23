# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#    Примеры:
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90

a = 5
data = []
for count in range(a):
    data.append(int(input('Введите число:   ')))

maxl = data[0]
for i in data:
    if i > maxl:
        maxl = i

print(maxl)
