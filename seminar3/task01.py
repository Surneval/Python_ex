#19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
def random_num(max_num=10):
    import datetime
    random_num = datetime.datetime.now().microsecond/10**6
    print(random_num)
    return int(random_num * max_num)

random_number = random_num(10)
print(random_number)




# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного 
# генератора псевдослучайных чисел.

# import time

# ct = time.time()
# rn = 9999 * ct
# print(str(round(rn % 100)))


# current_time = time.time()
# print(current_time)
# rand_num = int(1000 * current_time)
# print(rand_num)
# print(rand_num % 100)
# print(str(rand_num)[-5:])

