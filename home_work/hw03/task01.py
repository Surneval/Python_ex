# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def random_numbers(min_val=0, max_value=9, length=7):
    random_list = []
    import random
    for i in range(length):
        i = random.randint(min_val, max_value)
        random_list.append(i)
    return random_list


def sum_odd_el(list_random):
    sum_odd = 0
    for i in range(1, len(list_random), 2):
        sum_odd += list_random[i]
    return sum_odd


random_list = random_numbers()
print(random_list)
sum_odd = sum_odd_el(list_random = random_list)
print(f"Sum of elements with odd positions  = {sum_odd}")
