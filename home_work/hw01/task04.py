# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

import math
p_inf = math.inf
n_inf = -math.inf


def prompt(msg):
    print(msg)
    quarter = int(input())
    return quarter


def is_ok(quarter):
    if quarter == 1 or quarter == 2 or quarter == 3 or quarter == 4:
        return True
    else:
        return False


def x_y_values(quarter):
    if is_ok(quarter):
        if quarter == 1:
            x = [0, p_inf]
            y = [0, p_inf]
            return (x, y)
        elif quarter == 2:
            x = [-n_inf, 0]
            y = [0, p_inf]
            return (x, y)
        elif quarter == 3:
            x = [n_inf, 0]
            y = [n_inf, 0]
            return (x, y)
        else:
            x = [0, p_inf]
            y = [n_inf, 0]
            return (x, y)
    else:
        print("Enter a number from 1 to 4")

quarter = prompt("Enter the number of quarter")
(x, y) = x_y_values(quarter)
print(f"x is {x}, y is {y}")
