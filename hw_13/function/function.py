
def sum_of_num(a, b):
    result = a + b
    return result


def minus_num(a, b):
    result = a - b
    return result


def divide_num(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе!")
    return a / b


def mult_num(a, b):
    result = a * b
    return result
