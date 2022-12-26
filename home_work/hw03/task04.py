# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

numb = int(input("Enter any number: "))

def binary(number):
    bin_str = ""
    while number // 2 > 0:
        digit = number % 2
        bin_str = str(digit) + bin_str
        number = number // 2
    bin_str = str(number % 2) + bin_str
    return bin_str


bin_numb = binary(number=numb)
print(f"Binary view of {numb} is {bin_numb}")

#bin(number) - transforming
#result[::-1] с зада наперед
#срезы print(a[3:7: 1 - шаг / -1, если идти с конца]) - с 3 по 7 индекса
#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
    #
    # *Пример:*
    #
    # - 45 -> 101101
    # - 3 -> 11
    # - 2 -> 10
# def dec_to_bin(num, result = ""):
#     if num == 0:
#         return result[::-1]
#     result += str(num%2)
#     return dec_to_bin(num//2,result)
#
#
# n = int(input())
#
# if n!=0:
#     print(dec_to_bin(n))
# else:
#     print(0)
