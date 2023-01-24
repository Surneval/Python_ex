# Bubble sort
# [3, 1, 5, 0, 7, 9, 8]
# take first and second elements and check. it the second one is less than first - switch them.
# If you have switched smth - go to the start!!!
# take second and third element and if the third one is less than second one - swithch them
import random
array = random.sample(range(1, 100), 10)
print(array)

def bubble_sort(array):
    temp = None
    for j in range(len(array)):
        for i in range(len(array)-1):
            if array[i+1] < array[i]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
            else:
                continue
    return array

print(bubble_sort(array=array))
