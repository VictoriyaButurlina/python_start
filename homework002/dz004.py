# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число
n = int(input('Введите число N: '))
lst = list(range(-n, n+1))
print(lst)
# data = open('./homework002/file.txt', 'a') 
# data.write('1\n')
# data.write('3') #запись
# data.close()
with open('./homework002/file.txt') as file:
        position1, position2 = [int(line) for line in file.readlines()]
        print('Первая позиция', position1,'\nВторая позиция', position2)
mult = lst[position1-1]*lst[position2-1]
print('Произведение элементов', mult)
