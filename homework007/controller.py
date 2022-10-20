import csv
import os.path

def add_phone_number(f_file, name, surname, number_phone, comment):
    if os.path.exists(f_file):
        with open(f_file, mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\n")
            file_writer.writerow([name, surname, number_phone, comment])
    else:
        with open(f_file, mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\n")
            file_writer.writerow(["Имя", "Фамилия", "Телефон", "Комментарий"])
            file_writer.writerow([name, surname, number_phone, comment])

def import_phone_number(a_file):
    with open(a_file, 'r', encoding='utf-8') as r_file:
        file_read = r_file.read()
    return file_read