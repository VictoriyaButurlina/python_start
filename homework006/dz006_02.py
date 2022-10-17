# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# было
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

# стало
import random
num=int(input('Введите число '))
num_lst=[]
for i in range(num):
    num_lst.append(random.randint(1,num))
print(num_lst, '->', [(num_lst[i]*num_lst[-1-i]) for i in range((len(num_lst)+1)//2)] )
