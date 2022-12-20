# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# import datetime
# n = int(input("Enter maximum number for ramdom num gemeretion"))
# rand = datetime.datetime.now().microsecond % (n+1)
# print(rand)

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# list_val = ["dr", "qwe", 12, "rtt"]
# #число цифрой
# for i in list_val:
#     if type(i) == int:
#         print(list_val.index(i))
# list_val = ["dr", "qwe", "12", "rtt"]
# for i in list_val:
#     if i.isdigit():
#         print(list_val.index(i))

# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list_str = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
sub_str = "asd"
count = 0
for i in range(len(list_str)):
    if list_str[i] == sub_str:
        count += 1
        if count == 2:
            print(f"the second occurence is {i}")
            break #exit loop
if count < 2:
    print(f"No second occurence")
