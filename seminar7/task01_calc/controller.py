
import view as v

operation = v.get_operation()

if operation == '+':
    import sum as op
elif operation == '-':
    import substract as op
elif operation == '//':
    import int_divide as op
elif operation == "%":
    import reminder as op
elif operation == "*":
    import product as op
elif operation == "**":
    import power as op
elif operation == "/":
    import divide as op
else:
    print("Wrong operation. Try again")


    
def button_click():
    tup = v.type_numbers()
    type_a = tup[0]
    type_b = tup[1]
    if operation == "//" or operation == '%':
        if type_a == 1 or type_b == 1:
            print("Mistake you can't apple '//' to complex numbers")
        else:
            value_a = v.get_value()
            value_b = v.get_value()
            if type_a == 1:
                value_a = complex(value_a)
            else:
                value_a = int(value_a)
            
            if type_b == 1:
                value_b = complex(value_b)
            else:
                value_b = int(value_b)
            op.init(value_a, value_b)
            result = op.do_it()
            v.view_data(value_a, value_b, result, operation)
    else:
        value_a = v.get_value()
        value_b = v.get_value()
        if type_a == 1:
            value_a = complex(value_a)
        else:
            value_a = int(value_a)
            
        if type_b == 1:
            value_b = complex(value_b)
        else:
            value_b = int(value_b)
        op.init(value_a, value_b)
        result = op.do_it()
        v.view_data(value_a, value_b, result, operation)
    
    

