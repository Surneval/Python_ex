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

#from the seminar
#enter a number to find simple multiples
n = int(input("Enter a number to finds it's simple multiples > "))
list_num = []
cur_mult = 2
while n!= 1:
    if n % cur_mult == 0:
        list_num.append(cur_num)
        m //= cur_mult
    cur_mult += 1

print(list_num)  

