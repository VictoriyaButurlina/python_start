# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# было
from random import sample
n = int(input('Введите число: '))
lst = list(sample(range(0, 99), n))
print(lst)
nechet_lst = []
for i in range(len(lst)):
    if i%2==0:
        nechet_lst.append(lst[i])
print("Список элементов на нечетных позициях", nechet_lst)
print("Сумма нечетных элементов", sum(nechet_lst))

# стало
from random import sample
from functools import reduce
n = int(input('Введите число: '))
lst = list(sample(range(0, 99), n))
print(lst)
print(reduce(lambda x, y: x + y, map(lambda x: x[0], filter(lambda x: x[1] % 2 != 0, zip(lst, range(1, len(lst)+1))))))