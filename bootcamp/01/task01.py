#array = 10 [1,5,7,8,3,4,2,8,4,6]
#m = 3 found maximum sum of 3 elements following each other
import math
array = [1,5,7,8,3,4,2,8,4,6]
i1 = None
ind1 = None
i2 = None
ind2 = None
i3 = None
Ind3 = None
sum_max = 0
for i in range(len(array)-2):
    sum_w = array[i] + array[i+1] + array[i+2]
    if sum_w > sum_max:
        sum_max = sum_w
        i1 = array[i]
        ind1 = i
        i2 = array[i+1]
        ind2 = i+1
        i3 = array[i+2]
        ind3 = i+2  

    else:
        continue
print(f'{sum_max} is {i1} with index {ind1} + {i2} with index {ind2} + {i3} with index {ind3}')