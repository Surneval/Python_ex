# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# рандомно генерим список от -n до n>>
def random_list(number):
    rand_list = []
    import random
    for i in range(number):
        i = random.randint(-number, number)
        rand_list.append(i)
    print(f"Random list with items value from -n to n is: {rand_list}")
    return rand_list

# считываем файл txt и получаем в виде списка строк его содержание построчно


def read_file(file_link):
    try:
        file = open(file_link, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found")
    positions_str = file.read().splitlines()
    file.close()
    return positions_str

# переводит список из строк в список из целых чисел


def str_int(positions_str):
    positions_int = []
    for item in positions_str:
        i = int(item)
        positions_int.append(i)
    print(f"Positions from text file are: {positions_int}")
    return positions_int

# находит произведения элементов из рандомного списка, стоящих на позициях списка из листа


def product(positions_int, values_list):
    product = 1
    for item in positions_int:
        if item < len(values_list):
            product *= values_list[item]
        else:
            print(f"position {item} is more than {values_list} array length")
    return product


# собственно, считаем по функциям
number = int(input("Enter a number: >> "))
random_list = random_list(number)
file_address = "C:/Users/nadez/Desktop/Python/home_work/hw02/pos.txt"
positions_str = read_file(file_address)
positions_int = str_int(positions_str)
values_product = product(positions_int=positions_int, values_list=random_list)
print(
    f"Product of random array members on the positions from txt equals {values_product}")


##
# a = file.readlines()
# list_numb = list(map(str.strip.a))
## strip - убрать переходы между строками int(a[i].strip()) map - сразу разметить элементы
# print(int("\n12"))