#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input("Enter a number: >>"))

def random_list(number):
    rand_list = []
    import random
    for i in range(-number, number + 1):
        rand_list.append(i = random.randint(0, 9))
    return rand_list

random_list = random_list(number)

