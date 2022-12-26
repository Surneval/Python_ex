#Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
num_a = int(input("Enter number a >>  "))
num_b = int(input("Enter number b >>  "))

common_mult = []
for i in range(1, num_b+1):
    mult = i * num_a
    if mult % num_b == 0:
        common_mult.append(mult)
print(common_mult)
least_cm = common_mult[0]
for item in common_mult:
    if item < least_cm:
        least_cm = item
print(f"Least common multiple of {num_a} and {num_b} is {least_cm}")

