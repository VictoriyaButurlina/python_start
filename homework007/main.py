import controller as c
import view as v

if v.what_to_do() == 1:
    form_file = v.input_name_file()
    new_line = '1'
    while new_line == '1':
        c.add_phone_number(form_file, *v.input_numbers())
        new_line = v.new_input()
else:
    print(c.import_phone_number(v.output_name_file()))
