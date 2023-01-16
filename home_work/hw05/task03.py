# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

numb = '111112222334445'
txt = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'

def encode(msg):
    encoded = ""
    count = 1
    for i in range(len(msg)):
        if i+1 < len(msg):
            if msg[i] == msg[i+1]:
                count += 1
            else:
                encoded += str(count) + msg[i]
                count = 1
        else:
            encoded += str(count) + msg[i]
    return encoded


def decode(msg):
    decoded = ""
    i = 0
    if msg.isnumeric():
        while i + 1 < len (msg):
            decoded += str(msg[i + 1] * int(msg[i]))
            i += 2
    else:
        while i < len(msg):
            if msg[i].isdigit() and msg[i+1].isdigit():
                decoded += str(msg[i + 2] * int(msg[i:i+2]))
                i += 3
            elif msg[i].isdigit():
                decoded += str(msg[i + 1] * int(msg[i]))
                i += 2
    return decoded

encoded_num = encode(msg=numb)
encoded_txt = encode(txt)
print(encoded_num)
print(encoded_txt)

decoded_num = decode(encoded_num)
print(decoded_num)
decoded_txt = decode(encoded_txt)
print(decoded_txt)
