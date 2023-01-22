import controller as c
def type_numbers():
    flag_a = 0
    flag_b = 0
    
    numbers_a = input("Type 'c' if the first number is a complex number, type 'r' if real number>>")
    if numbers_a == 'c':
        flag_a = 1
        
    elif numbers_a == 'r':
        flag = 0
    else:
        print('Mistake. Type "r" for real numbers mode and "c" for complex numbers mode')

    numbers_b = input("Type 'c' if the second number is a complex number, type 'r' if real number>>")
    if numbers_b == 'c':
        flag_b= 1
        
    elif numbers_b == 'r':
        flag_b = 0
        
    else:
        print('Mistake. Type "r" for real numbers mode and "c" for complex numbers mode')
    
    return (flag_a, flag_b)


def view_data(x, y, data, operation):
    print(f'Result of operation:{x} {operation} {y} = {data}')

def get_value():
    return input('Enter a number >> ')
    

    

  

def get_operation():
    return input("Operation is (enter one of: +, -, *, **, /, //, %) >> ")

