# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

try:
    first_el = int(input("Enter the first member > "))
    step = int(input("Enter the step > "))
    length = int(input("Enter the length > "))
except(ValueError, TypeError):
    print("Error, try again")
f = lambda i: (i-1) * step + first_el
seq = [f(i) for i in range(1, length+1)]
print(seq)