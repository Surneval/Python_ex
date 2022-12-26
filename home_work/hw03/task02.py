# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def random_numbers(min_val=1, max_value=9, length=8):
    random_list = []
    import random
    for i in range(length):
        i = random.randint(min_val, max_value)
        random_list.append(i)
    return random_list

def sum_numb(list_random):
    new_list = []
    l = len(list_random)
    if l % 2 == 0:
        for i in range (l):
            if i < l // 2:
                k = list_random[i] * list_random[l - 1 - i]
                new_list.append(k)
    else:
        for i in range (l):
            if i < (l // 2):
                k = list_random[i] * list_random[l - 1 - i]
                new_list.append(k)
            elif i == l // 2 :
                new_list.append(list_random[i] ** 2)
    return new_list

random_list = random_numbers(min_val=1, max_value=9, length=8)
new_list = sum_numb(list_random = random_list)
print(f"Random list is: {random_list}")
print(f"New list made of random list is: {new_list}")

#middle  = length // 2 + length % 2
# for i in range (middle):
#     multi.append(list_num[i] * list_num[len(list_num) - i - 1])