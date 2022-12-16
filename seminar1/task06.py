# Напишите функцию, которая возвращает список с уникальными (неповторяющихся) элементам.
# # Напишите функцию unique...
# mylist = [1, 1, 2, 1, 3, 2, 3]
# print(unique(mylist))

# # Вывод:
# >> [1, 2, 3]
def prompt(msg):
    print(msg)
    quant = int(input())
    return quant


def random_gen(size):
    import random
    random_list = [random.randint(1, 5) for x in range(0, size)]
    return random_list


def unique(random_list):
    for i in reversed(random_list):
        if random_list.count(i) > 1:
            random_list.remove(i)
    return random_list


size = prompt("Enter size > ")
r_list1 = random_gen(size)
print(r_list1)
r_list2 = unique(r_list1)
print(r_list2)

