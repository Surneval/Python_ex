# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
pi = math.pi
print(pi)

accur = float(input("enter given accuracy >> "))
count = 0
while accur < 1:
    accur *= 10
    count += 1
print(count)

pi_corr = round(pi, count)
print(f"With given accuracy {accur} pi number = {pi_corr}")

#enter accuracy
acc = input("Enter accuracy > ")
round_val = len(acc.split(".")[1])
print(round(math.pi, round_val))