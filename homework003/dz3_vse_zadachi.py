#1 Задайте список, состоящий из произвольных чисел, количество задает пользователь. Напишите, программу, которая найдет сумму элементов списка, стоящих на нечетных позициях (не индексах)
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




#2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
num=int(input('Введите число '))
num_lst=[]
for i in range(num):
   num_lst.append(random.randint(1,10)) #Создание списка
print(num_lst)
new_lst=list()
for item in range(0, int(len(num_lst)/2)):
    new_lst.append(num_lst[item]*num_lst[-(item+1)]) #Создание нового списка из произведения первого и последних элементов списка num_lst
print(new_lst)



#3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
my_list = [2.84, 9.42, 1.87] 
new_lst =[]
for i in range(0, len(my_list)):
    if i % 1== 0:         
        new_lst.append(math.modf(my_list[i])) #Возвращает дробную и целую части x
print(new_lst)
a, b = max(new_lst, key=lambda x: x[0]), min(new_lst, key=lambda x: x[0]) #ищем мин и макс
print(a,b)
res = tuple(map(lambda i, j: i - j, a, b)) #считаем разницу
print('разница между максимальным и минимальным значением дробной части элементов', round(res[0], 3)) #выводим ответ используя первый индекс



# 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
numb = int(input('Введите целое число: ')) 
x = ''
while numb != 0:
    x += str(numb % 2)
    numb = numb // 2
print(f'Двоичное представление числа: {x}')



# 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('Введите число: '))
x = [1,1]
for i in range(2, k):
    x.append(x[-1] + x[-2])
# print(', '.join(str(y) for y in x))
y = [1, -1]
for i, elem in enumerate(x, 2):
    if i % 2 != 0:
        y.append(elem * -1)
    else:
        y.append(elem)
y.reverse()
y.append(0)
print(y+x)