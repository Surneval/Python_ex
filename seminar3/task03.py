# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

import random
import string


def generator(size=5, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for i in range(size))


def num_generator(lower=10, upper=1000):
    random_num = random.randint(lower, upper)
    return random_num


def list_values(size=8):
    list_values = []
    for i in range(int(size)):
        list_bin = [generator(), num_generator()]
        i = str(random.choice(list_bin))
        list_values.append(i)
    print(list_values)
    return list_values


def search_sec(random_list, value_find):
    k = 0  # start point for second value search
    neg_flag = 0  # flag for negative result
    for i in range(len(random_list)):
        if random_list[i] == value_find:
            k = i + 1
            for n in range(k, len(random_list)):
                if random_list[n] == value_find:
                    return n

        else:
            neg_flag += 1
    if neg_flag > 0:
        return -1000

list_str = list_values()
#list_str[0] = "rty"
list_str[7] = list_str[3]
print(list_str)
#to_find = "rty"
to_find = input("enter a value to find: ")
second_in = search_sec(random_list = list_str, value_find = to_find)

if second_in >= 0:
    print(f"Second occurrence of {to_find} is index {second_in}")
else:
    print(f"There is no second occurence for {to_find}")
      
