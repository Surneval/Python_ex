#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    # *Примеры:* 
    # - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

def prompt(msg):
    print(msg)
    num = int(input())
    return num

def list_num(num):
    list = []
    for i in range(-num, num+1):
        list.append(i)
    return list

n = prompt("Enter n")
list_n = list_num(num = n)
print(f"{list_n} ")