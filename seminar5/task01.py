#35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

#create file
with open(r'C:\Users\nadez\Desktop\Python\seminar5\sample_file.txt', mode='r') as file:
    data = file.readline().strip()
list_data = list(map(int, data.split()))
print(list_data)
for i in range(1, len(list_data)):
    if list_data[i] - 1 != list_data[i-1] :
        print(list_data[i] - 1)