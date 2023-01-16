# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# введем число k
k = int(input("Enter k >> "))

import random
length = k
coeff = []

for i in range(k):
    val = str(random.randint(0, 100))
    if val !=0:
        if i == 0:
            coeff.append(f"{val} * x**0")
        elif i == 1:
            coeff.append(f"{val} * x **1")
        else:
            coeff.append(f"{val} * x**{i}")

result = " + ".join(coeff) + " = 0"

print(result)

data = open("C:/Users/nadez/Desktop/Python/home_work/hw04/file1.txt", "w+", encoding="utf-8")    
data.write(result)
data.close()

