#Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
def prompt(msg):
    print(msg)
    quant = int(input())
    return quant


def random_gen(size):
    import random
    random_list = [random.randint(1, 5) for x in range(0, size)]
    print(random_list)
    return random_list

size = prompt("Enter size")
random_list = random_gen(size)
random_set = set(random_list)
max = 0
for i in random_set:
    if random_list.count(random_list[i]) > max:
        max = random_list.count(random_list[i])
print(max)


# import random
#
# list_num = []
# max = 0
# for i in range(10):
#     a= random.randint(2,5)
#     list_num.append(a)
# print(list_num)
# print(set(list_num))
# for i in set(list_num):
#     if list_num.count(i)>max:
#         max = list_num.count(i)
# print(max)

# print(set(array))
# d = {}

# for i in array:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

# max = 0
# for i in range(a, (b + 1)):
#     if (d[i] > max):
#         max = d[i]

# print(f"Максимальное повторение элемента {max} раз.")





##########
# import random

# a = 1
# b = 6

# array = [random.randint(a, b) for i in range(20)]
# print(array)

# print(set(array))
# d = {}

# for i in array:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)

# max = 0
# for i in range(a, (b + 1)):
#     if (d[i] > max):
#         max = d[i]

# print(f"Максимальное повторение элемента {max} раз.")

##################

# import random

# number = int(input())
# maxRandom = int(input('input max random number'))
# maxAmount = 0

# list = []
# count = [0] * (maxRandom+1)

# for i in range(0, number):
#     list.append(random.randint(0, maxRandom))

# for i in list:
#     count[int(i)] += 1

# for i in count:
#     if i > maxAmount:
#         i = maxAmount

# print(list)
# print(max(count))
# print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')
