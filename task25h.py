# 5. Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Введите количество элементов списка: ')) # Вариант с вводом целых последовательных чисел
list={}
print('Начальный список:')
for i in range(n):
    list[i]= i
    print(list[i], end='  ') 
random.shuffle(list)
print()
print('Перемешанный список:')
for i in range(n):
    print(list[i], end='  ') 
print() 
print()

list=['хелло','привет','салют','здравствуйте'] # Вариант с заданными тектовыми переменными
print('Начальный список:')
print(list)
random.shuffle(list)
print('Перемешанный список:')
print(list)