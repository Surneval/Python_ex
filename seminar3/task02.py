# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

import random
import string
list_a = ["fds", "vyjcfjtg", "guni", 56, 87, 97]
# or


def generator(size=5, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for i in range(size))


#print(generator())


def num_generator(lower=10, upper=100):
    random_num = random.randint(lower, upper)
    return random_num

#print(num_generator())


def list_values(size = 6):
    list_values = []
    for i in range(int(size)):
        list_bin = [generator(), num_generator()]
        i = random.choice(list_bin)
        list_values.append(i)
    print(list_values)
    return list_values


list_random = list_values()

def certain_numb():
    count_no = 0
    count_yes = 0
    number_find = int(input("Enter a number to find: "))
    for i in range(len(list_random)-1):
        if list_random[i] == number_find:
            count_yes += 1
            print(f"there is a number {number_find}")
        else:
            count_no += 1
    if (count_no > 0 and count_yes == 0):
        print(f"There is no number {number_find}")
    return ""
    

def is_digit():
    count_no = 0
    count_yes = 0
    list_random = list_values()
    for i in range(len(list_random)):
        if str(list_random[i]).isdigit():
            count_yes += 1
            print(f"there is a digit {list_random[i]}")
        else:
            count_no += 1
    if (count_no > 0 and count_yes == 0):
        print(f"There is no digit")
    return ""


certain_numb()
is_digit()