#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Enter number n >> "))
def prime_fact (num):
    prime = []
    factor = 2
    while num % factor == 0:
        prime.append(2)
        num //= 2
    factor += 1
    while factor * factor <=num:
        if num % factor == 0:
            prime.append(factor)
            num //= factor
        else:
            factor += 2

    if (num != 1 and num % 2 != 0):
        prime.append(num)
    return prime

prime_factors = prime_fact(n)
print(prime_factors)
        

