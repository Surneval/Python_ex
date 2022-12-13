# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

def prompt(msg):
    print(msg)
    num = int(input())
    return num

def list_num(num):
    list = []
    for i in range(num):
        val = int(input(f"Enter a number {i} "))
        list.append(val)
    return list

def max(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

num = prompt("Enter quantity of numbers")
list_num = list_num(num)
max = max(list_num)
print(f" maximum from list {list_num} is {max}")

# list = []
# for i in range(5):
#     num = int(input())
#     list.append(num)

# max = -99999999999999
# for i in range(len(list)):
#     if list[i] > max:
#         max = list[i]

# print("max = ", max)
