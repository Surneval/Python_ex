# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

array1 = [1, 2, 3, 5, 7, 8, 9, 10]
array2 = [1, 2, 4, 8, 9]
inner = [i for i in array1 if i in array2]
inner2 = list(filter((lambda i: i in array2), array1))
print(inner)
print(inner2)