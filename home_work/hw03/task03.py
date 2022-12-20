# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def int_generator(lower=10, upper=100):
    random_num = random.randint(lower, upper)
    return random_num


def float_generator(lower=0.01, upper=99.99):
    random_num = round(random.uniform(lower, upper), 2)
    return random_num


def list_values(size=6):
    list_values = []
    for i in range(int(size)):
        list_bin = [int_generator(), float_generator()]
        i = random.choice(list_bin)
        list_values.append(i)
    return list_values


def sum_decimal(random_list):
    float_list = []
    for item in random_list:
        if type(item) != int:
            k = round(item - int(item), 3)
            float_list.append(k)
    return float_list


def max_val(some_list):
    max_element = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] > max_element:
            max_element = some_list[i]
    return max_element


def min_val(some_list):
    min_element = some_list[0]
    for i in range(len(some_list)):
        if some_list[i] < min_element:
            min_element = some_list[i]
    return min_element


random_list = list_values(size=7)
print(random_list)
float_list = sum_decimal(random_list=random_list)
print(float_list)
max_element = max_val(some_list = float_list)
min_element = min_val(some_list = float_list)
diff = max_element - min_element
print(f"Difference between maximum fractional part and minumum fractional part is {diff}")