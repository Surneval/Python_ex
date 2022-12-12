# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def prompt(user_request):
    print(user_request)
    day_num = int(input())
    return day_num


def is_ok(day_num):
    if day_num > 0 and day_num < 8:
        return True
    else:
        return False


def check_system(user_request):
    print(user_request)
    user_answer = input()
    str(user_answer).lower()
    if user_answer == "yes":
        return True
    else:
        return False


def check_day(user_request1, user_request2):
    day_number = prompt(user_request1)
    is_day_ok = is_ok(day_number)
    check_country = check_system(user_request2)
    if is_day_ok:
        if check_country:
            if day_number == 6 or day_number == 7:
                print("Day number", day_number, "is a weekend")
            else:
                print("Day number", day_number, "is not a weekend")
        else:
            if day_number == 7 or day_number == 1:
                print("Day number", day_number, "is a weekend")
            else:
                print("Day number", day_number, "is not a weekend")

is_weekend = check_day("Enter day number", "The country is Russia?")
#предполагается, что если страна не Россия, то это США, выходные 1 и 7 день
