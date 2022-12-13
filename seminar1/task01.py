# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# *Примеры:*
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

def prompt(msg):
    print(msg)
    num = int(input())
    return num


def sq(x, y):
    if x == y*y or y == x*x:
        return True
    else:
        return False


x = prompt("Enter x ")
y = prompt("Enter y ")
if sq(x, y):
    print("Yes")
else:
    print("No")
