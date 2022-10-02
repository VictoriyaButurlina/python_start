# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
n = int(input('Введите число N: '))
list_n = list(range(1, n+1))
result = [round((1+1/i)**i, 2) for i in list_n]
print(f'Для n = {list_n}:{result}')
print(f'Сумма: {round(sum(list_n), 2)}')
