# 1. Вывести лесенкой символ звёздочки по кол-ву строк, заданных пользователем:
# запросить ввод у пользователя кол-ва строк, вывести звёздочки лесенкой.
# - Например, пользователь ввёл число 2. Тогда выводим:
# *
# **
# - Например, пользователь ввёл число 4. Тогда выводим:
# *
# **
# ***
# ****
# и так далее, смысл должен быть ясен.
# Примечание: символ можно умножать на число, получая строку с дублированным символом
# (но решить можно и без этого)
while True:
    try:
        rows = int(input('Enter a number >> '))
        break
    except (TypeError, ValueError, NameError):
        rows = 0
        print("Enter a number")
    

for i in range(rows + 1):
    print(f'{"*" * i}')

