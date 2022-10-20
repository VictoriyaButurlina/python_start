def input_numbers():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    number_phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    list_n = [name, surname, number_phone, comment]
    return list_n

def input_name_file():
    f_file = input("Введите название и формат файла (например: file.txt или file.csv): ")
    return f_file

def output_name_file():
    out_file = input("Введите название и расширение файла для прочтения: ")
    return out_file

def what_to_do():
    to_do = int(input("Введите номер действия: 1 - Импортировать данные в файл, 2 - Экспортировать данные из файла: "))
    return to_do

def new_input():
    new_in = input("Повторить ввод данных? (Yes -1 /No - 2): ")
    return new_in
