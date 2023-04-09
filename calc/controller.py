import model_sub as model
import view


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.int(value_a, value_b)
    result = model.do_it()
    view.view_data(result,'do_it')
