# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
import math
try:
    a = float(input("Enter a >> "))
    b = float(input("Enter b >> "))
    c = float(input("Enter c >> "))
except (ValueError, TypeError):
    print("Enter a number")

def discr(a, b, c):
    disc = b*b - (4 * a * c)
    return disc


disc = discr(a, b, c)
print(f"Discriminamt = {disc}")

if disc == 0:
    x1 = round(-b / (2 * a), 2)
    print(f"one root = {x1}")
    
elif disc > 0:
    #x1 = round((-b + (disc ** 0.5)) / (2 * a), 2)
    x1 = round((-b + math.sqrt(disc)) / (2 * a), 2)
    #x2 = round((-b - (disc ** 0.5)) / (2 * a), 2)
    x2 = round((-b - math.sqrt(disc)) / (2 * a), 2)
    print(f"x1 = {x1}, x1 = {x2}")
else:
    print("no roots")
        
        


