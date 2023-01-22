#написать программу возведения числа x в чтупень y

x = 0
y = 0

#initialization of start value
def init(a, b):
    #global - распространение работы на всю программу
    global x
    global y
    x = a
    y = b

def do_it():
    return x ** y