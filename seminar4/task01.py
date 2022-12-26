# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.



def create_list():
    num_list = []
    while True:
        user_input = input("Enter a number. To Stop type 'end' >> ").lower()
        if user_input.isdigit():
            num_list.append(int(user_input))
        elif user_input == "end":
            break
        else:
            print("Enter a number >>")
            continue
    return num_list

def list_numbers():
    numbers = list(map(int,input('Enter numbers separated by spaces >> ').split()))
    return numbers

num_list = create_list()
print(num_list)
numb_list = list_numbers()
print(numb_list)

def max_min(some_list):
    max_el = some_list[0]
    min_el = some_list[0]
    for i in range(1,len(some_list)):
        if some_list[i] > max_el:
            max_el = some_list[i]
        elif some_list[i] < min_el:
            min_el = some_list[i]
    min_max = (min_el, max_el)
    return min_max

min_max = max_min(num_list)
print(f"Minimum element in the list is {min_max[0]}. Maximim element is {min_max[1]}")