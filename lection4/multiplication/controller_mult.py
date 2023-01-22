import model_mult
import view_mult

def button_click():
    value_a = view_mult.get_value()
    value_b = view_mult.get_value()
    model_mult.init(a=value_a, b=value_b)
    multiplication = model_mult.mult()
    view_mult.view_result(multiplication)
    