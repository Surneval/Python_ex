#2. Запросить у пользователя координаты x и y двух точек на плоскости. Посчитать расстояние между заданными точками и вывести результат на консоль с точностью до трёх знаков после запятой (плавающей точки).
#Примечание: у каждой точки есть две координаты: x и y. Расстояние рассчитывается по формуле, которую вы с лёгкостью найдёте в Интернете (да, гуглить всё, что вы не знаете - очень полезно!).

a_coord = (int(input("Enter x coordinate >> ")), int(input("Enter y coordinate >> ")))
print(a_coord)
b_coord = (int(input("Enter x coordinate >> ")), int(input("Enter y coordinate >> ")))
import math
direc = math.sqrt((b_coord[0] - a_coord[0])**2 + (b_coord[1] - a_coord[1])**2)
print(f"Derection between two point A and B equals {direc:1.3f}")