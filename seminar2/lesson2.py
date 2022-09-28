# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

import random

n =  int(input("Введите произвольное целое число: "))
for i in range(n):
    print(random.randint(-100,100))



# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    
#     *Пример:*
    
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# number = input("Введите число N: ")
# result = []
# for i in range(1, int(number)+1):
#   result.append([i, 3*i + 1])
# print(dict(result))

# number = input("Введите число N: ")
# result = []
# for i in range(1, int(number)+1):    
#     elem = [i, 3*i + 1]
#     result.append(elem)
# print(result)
# print(dict(result))

number = input("Введите число N: ")
result = dict() #словарь
for i in range(1, int(number)+1):    
    result[i] = 3*i + 1
print(result)


# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
str1 = input('Введите первую строку для проверки:')
str2 = input('Введите вторую строку для поиска в первой строке:')

print(f'Вторая строка входит в первую {str1.count(str2)} раз(а).')
