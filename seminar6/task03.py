# 43)Имеется список id сотрудников из 10 элементов,
# каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)
# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.
# Выведете имена сотрудников, получившие нечетное id.
# Решить с помощью zip,filter,lambda

import random
id = random.sample(range(1, 100), 10)
print(id)
employees = ["Ana", 'Jack', "Jul", 'Can','Mike', "Rob", 'Bella', "Lohn", 'Carrie', 'Samanta']
result = list(zip(id, employees))
print(result)
result = sorted(result, key=lambda x: x[0], reverse=False)
print(result)
odd = list(filter(lambda x: x[0] % 2, result))
print(odd)