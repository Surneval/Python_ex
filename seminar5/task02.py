# 36.Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность.
# Порядок элементов менять нельзя.
# Строить последовательность начиная с первого элемента, если последовательность построить невозможно,
#  начинать со следующего элемента и т.д.
# [1, 5, 2, 3, 4, 6, 1, 7] = [1,5,7]
# [7,5,2,3,4,6,7] = [5,6,7]
# [7,7,2,3,4,6,7] = [2,3,4,6,7]

input_list = [7, 7, 4, 2, 3, 4, 6, 1, 7]
new_list = []
max_item = max(input_list)
start = 0
start_i = 0
    
for i in range(0, len(input_list)):
    if input_list[i] < max_item:
        start = input_list[i]
        start_i = i
        new_list.append(start)
        break
for i in range(start_i+1, len(input_list)):
    if input_list[i] > start:
        start = input_list[i]
        new_list.append(start)

print(new_list)

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# print(res)
# res = where(lambda x: not x % 2, res)
# res  = select(lambda x: (x, x**2), res)
# print(res)