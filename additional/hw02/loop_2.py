# list comprehension
first_list = [1, 2, 3, 4, 5, 6]
second_list = [11, 12, 13, 14, 15]
#takind odds from the first one, taking even from the second one
odds = [x for x in first_list if x % 2]
even = [x for x in second_list if not x % 2]
joined_list = odds + even
print(joined_list)