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