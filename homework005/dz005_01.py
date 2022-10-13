# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
text_my = 'абвавбввы абв Python — мультипарадигмальный абв  язык абв программирования.абв'
text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
my = " ".join(text_my)
print(my)
