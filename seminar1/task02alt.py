# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат

def input_numbers(q):
    xyz = ['x', 'y', 'z']
    values = []
    for i in range(q):
        values.append(input(f"Enter {xyz[i]}: "))
    return values


def check_predicate(values):
    left = not (values[0] or values[1] or values[2])
    right = not values[0] and not values[1] and not values[2]
    result = left == right
    return result


user_statem = input_numbers(q=3)
if check_predicate(user_statem) == True:
    print("The statement is True")
else:
    print("The statement is false")

#вводим 0 или 1 в разных комбинациях - позволяет проверить каждую комбинацию