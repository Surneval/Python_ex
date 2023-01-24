#Selection sort algorithm
# MIN -> MAX
# Take the first element. Take other elements and find the smallest. Switch the first and the smallest.
# O(n2)
import random
array = []
for i in range(11):
    i = random.randint(0, 15)
    array.append(i)
print(array)

def selection_sort(array):
    start = 0
    min_el = array[start]
    temp = None
    while start < len(array) - 1:
        for i in range(start + 1, len(array)):
            if array[i] < array[start]:
                temp = array[start]
                array[start] = array[i]
                array[i] = temp
        start += 1
    

selection_sort(array=array)
print(array)
