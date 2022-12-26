# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

#способ1  - используем set
def rand_list(length, min, max):
    rand = []
    for i in range(length):
        i = random.randint(min, max)
        rand.append(i)
    return rand

#способ2 - используем генератор списков
def delete(some_list):
    new_list = []
    [new_list.append(item) for item in some_list if item not in new_list]
    return new_list


random_list = rand_list(length=9, min=1, max=6)
print(random_list)
new_list = list(set(random_list))
print(new_list)
new_list1 = delete(random_list)
print(new_list1)
