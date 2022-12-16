# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#         *Пример:*
#         - Для N = 5: 1, -3, 9, -27, 81


length = int(input("Enter N >> "))
i = 1
list = [i]
for j in range(length-1):
    i*=-3
    list.append(i)
print(list)