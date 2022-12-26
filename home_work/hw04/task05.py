# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def read_file(file_link):
    try:
        file = open(file_link, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found")
    positions_str = file.readline().strip()
    file.close()
    return positions_str

link1 = "C:/Users/nadez/Desktop/Python/home_work/hw04/task05_f1.txt"
link2 = "C:/Users/nadez/Desktop/Python/home_work/hw04/task05_f2.txt"

string1 = read_file(link1)
string2 = read_file(link2)

print(string1)
print(string2)

list_1 = string1.split(" = ")
list_2 = string2.split(" = ")

list_m1 = list_1[0].split(" + ")
list_m2 = list_2[0].split(" + ")


def list_style(some_list):
    for i in range(len(some_list)):
        some_list[i] = some_list[i].split(" * ")
        for j in range(1):
            if some_list[i][j].isdigit():
                some_list[i][j]=int(some_list[i][j])
    return some_list

list_int1 = list_style(list_m1)
list_int2 = list_style(list_m2)

sum_list = []
if len(list_int1) > len(list_int2):
    max_list = list_int1
    min_list = list_int2
else:
    max_list = list_int2
    min_list = list_int1

add = len(max_list) - len(min_list)
for f in range (add):
    f = [0, ""]
    min_list.append(f)

for i in range(len(max_list)):
    for j in range(1):
        if max_list[i][1] == min_list[i][1]:
            sum_list.append([max_list[i][0] + min_list[i][0], max_list[i][1]])
        else:
            sum_list.append([max_list[i][0], max_list[i][1]])

print_list = []
for i in range(len(sum_list)):
    for j in range(1):
        sum_list[i][j] = str(sum_list[i][j])
        
    i = " * ".join(sum_list[i])
    print_list.append(i)
to_print = " + ".join(print_list) + " = 0"

print(to_print)

data = open("C:/Users/nadez/Desktop/Python/home_work/hw04/task05_result.txt", "w+", encoding="utf-8")    
data.write(to_print)
data.close()

