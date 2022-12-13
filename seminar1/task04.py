#2. Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.
    #     *Примеры:*
    # - 6,78 -> 7
    # - 5 -> нет
    # - 0,34 -> 3

def prompt(msg):
    print(msg)
    num = float(input())
    return num

def first_num(numb):
    first_num = int((num * 10)) % 10
    return first_num

num = prompt("Enter a number")
first_numb = first_num(numb = num)
print(f" first number = {first_numb}")