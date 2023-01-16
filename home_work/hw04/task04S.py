#from the seminar
import random
k = int(input("Enter a power value > "))
result = ""
for i in range(k, -1, -1):
    coeff = random.randint(0, 100)
    if coeff == 0:
        continue
    if i == 1:
        result += f"{coeff}*x**{i}+"
    result += f"{coeff}*x**{i}+"
print(result)