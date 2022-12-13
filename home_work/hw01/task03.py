# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def prompt(msg):
    print(msg)
    #xy = ["x", "y"]
    user_input = int(input())
    return user_input

def check_zero(x):
    if x == 0:
        return False
    else:
        return True

def define_quarter(x, y):
    if check_zero(x) == True and check_zero(y) == True:
        if x > 0 and y > 0:
            return 1
        elif x < 0 and y > 0:
            return 2
        elif x < 0 and y < 0:
            return 3
        else:
            return 4


x = prompt("Enter x ")
y = prompt("Enter y ")
print(f"Coordinate is {define_quarter(x, y)}")