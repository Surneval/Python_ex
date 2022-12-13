# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if (not(x or y or z)) == ((not x) and (not y) and (not z)):
                print(f"for x: {x}, y: {y}, z: {z}>> {True}")
            else:
                print(f"for x: {x}, y: {y}, z: {z}>> {False}")
           
#так как для каждой комбинации значений мы получили True - тождество верно