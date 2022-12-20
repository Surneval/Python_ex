# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

user_input = input("Enter any number >>")
sum_digit = 0
for symbol in user_input:
    if symbol.isdigit():
        sum_digit += int(symbol)
print(sum_digit)


# a = float(input())
# len_num = len(str(a))
# while a != int(a):
#     a = round(a * 10, len_num)
#     print(a)
# print(a)
# sum = 0
# while a > 0:
#     sum += a % 10
#     a /= 10
# print(sum)
