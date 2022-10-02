# Реализуйте алгоритм перемешивания списка.
import random
lst = list(range(1, 10))
print(type(lst))
print(lst)
while lst:  
    new_list=lst.pop(random.randint(0, len(lst)-1))
    print(new_list)

