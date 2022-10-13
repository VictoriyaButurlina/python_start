# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных
def encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding
s = 'fffffffdddddwwwwwwwwrrrrrrrraaaaaaaaaavvvvvvvvvvvvv'
print(encode(s))


