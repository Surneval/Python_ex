def view_result(data):
    print (f"Multiplication  = {data}")

def get_value():
    try:
        value = int(input("Value = "))
    except(ValueError, TypeError):
        print("Mistake. Try again ")
    return value