#Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

x_a = int(input("Enter x_a: "))
x_b = int(input("Enter x_b: "))
y_a = int(input("Enter y_a: "))
y_b = int(input("Enter y_b: "))

dist = round(sqrt((x_b - x_a)**2 + (y_b - y_a)**2), 2)
print(f"Distance between A: {(x_a, y_a)} and B {(x_b, y_b)} is {dist}")