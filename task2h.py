# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значения предикатов, где 1 - True или 0 - False')
x = bool(int(input('Введите значение для X: ')))
y = bool(int(input('Введите значение для Y: ')))
z = bool(int(input('Введите значение для Z: ')))
if x == False and y == False and z == False:
    p1 = False
else:
    p1 = True
if x == True and y == True and z == True:
    p2 = True
else:
    p2 = False
if p1 == p2:
    print('Выражение истинно')
else:
    print('Выражение ложно')