# Реализуйте алгоритм перемешивания списка

# создали список
import random


def random_list(msg):
    n = int(input(msg))
    random_list = []
    import random
    for i in range(n):
        i = random.randint(0, 9)
        random_list.append(i)
    return random_list


# перемешиваем лист алгоритмически
def shuffle(list_num):
    for i in range(0, int(len(list_num)/2)):
        temp = list_num[i]
        list_num[i] = list_num[(len(list_num) - i-1)]
        list_num[len(list_num) - i-1] = temp
    return list_num


random_list1 = random_list("Enter list length >> ")
print(f"Basic randomly generated list: {random_list1}")
random_list2 = shuffle(random_list1)
print(f"Shuffled list: {random_list2}")


# очень легкий способ перемешать список из random
random.shuffle(random_list1)
print(f"Shuffled list with random.shuffle() {random_list1}")
