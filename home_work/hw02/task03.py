# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

length = int(input("Enter a number: "))
seq = {}
sum = 0
for i in range(1, length + 1):
    seq[i] = round((1 + 1/i)**i, 2)
    sum += seq[i]
print(f"Sequence of numbers: {seq}")
print(f"Sum of sequence members is: {sum}")
