#3. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.

def prompt(msg):
    print(msg)
    num = int(input())
    return num

def check_div(number):
    if (number % 5 == 0 and number % 10 == 0) or (number % 15 == 0 and number % 30 != 0):
        return True
    else:
        return False

number  = prompt("Enter a number ")
if check_div(number) == True:
    print("Everything is all righ ")
else:
    print("No")