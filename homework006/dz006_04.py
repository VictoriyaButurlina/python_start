# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

#было
mylist =  [1,2,2,2,3,3,4,4,5,5,6,7,7,8,8,9]
res_list = [] 
for item in mylist: 
    if item not in res_list: 
        res_list.append(item) 
print(res_list)

#стало
from functools import reduce
mylist = [1,2,2,2,3,3,4,4,5,5,6,7,7,8,8,9]
print(reduce(lambda l, x: l.append(x) or l if x not in l else l, mylist, []))
