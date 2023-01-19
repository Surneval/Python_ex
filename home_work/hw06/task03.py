# Задача 32:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

try:
    a = int(input("Enter a > "))
    b = int(input("Enter b > "))
except(ValueError, TypeError):
    print("Error, try again")

def recursion(a, b):
    if b == 1:
        return a
    else:
        return a * recursion(a, b-1)

result = recursion(a=a, b=b)
print(result)

def neg_rec(a, b):
    if b == 1:
        return 1 / a
    else:
        return (1 / a) * neg_rec(a, b-1)

res = neg_rec(a=a, b=b)
print(res)