# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input("Введите число: ")
res_number = number.replace('.', '').replace('-', '').replace('0', '').replace(',', '')
res_number = [int(i) for i in str(res_number)]
print(res_number)
sum = 0
for digit in res_number:
    sum+= digit
print(number, '->', sum)

