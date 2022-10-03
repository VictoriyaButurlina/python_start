# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
my_list= ('123', '1231234', '3675','3333345', '123')
number = '123'
nul = 0  
for i in my_list:
    if number in i:
        print(i, my_list.index(i, nul))
        nul = my_list.index(i, nul)+1 # элемент nul нужен, чтобы при поиске если первый nul найден и = number , повторно этот nul не использовать, а искать дальше по списку
        
my_list = ["123","234", "12333", "567", "123"]
number = "123"

for i, elem in enumerate(my_list):
    if number in elem:
        print(elem)
        print(i)