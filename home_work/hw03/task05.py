# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

numb = int(input("Enter a number: "))


def fib(number):
    if number >= 0:
        if number == 0:
            return 0
        elif number in [1, 2]:
            return 1
        else:
            return fib(number - 1) + fib(number - 2)
    else:
        return int(((-1)**(number+1)) * fib(-number))


list_fib = []
for i in range(-numb, numb + 1):
    list_fib.append(fib(i))
print(list_fib)
