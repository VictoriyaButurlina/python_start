# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
from time import time
my_time = time()
print(my_time)
print(int((my_time%10)*100))
