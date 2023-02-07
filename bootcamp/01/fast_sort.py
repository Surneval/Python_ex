# 1/ arr = {1,0,-5,6,3, 1, -4} get array
#           0 1  2 3 4  5   6
# 2/ choose pivot 
# pivot element = arr[6]
# 3/ all elements less than pivot should stay to the left, all elements more than pivot should stay right
# 4/ take left sub-array and right sub-array and repeat steps 1-3

arr = [1,0,-5,6,3, 1, -4, -7]
result = []


def quick_sort(array):
    
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [array[i] for i in range(1, len(array)) if array[i] <= pivot]
        greater = [array[i] for i in range(1, len(array)) if array[i] > pivot]
        result = quick_sort(less) + [pivot] + quick_sort(greater)
        return result

result = quick_sort(arr)
print(result)

# #pivot = arr[len(arr)-1]

# def quick_sort (input_array, min_index, max_index):
#     pivot_ind = 0 #index of pivot
#     quick_sort(input_array, min_index, pivot-1)
#     quick_sort(input_array, pivot+1, max_index)
#     return input_array

# def get_pivot_index(input_array, min_index, max_index):
#     #assuming pivot is the last element
#     pivot_ind = min_index - 1
#     for i in range(min_index, max_index):
#         if input_array[i] <= input_array[max_index]:
#             pivot_ind += 1
