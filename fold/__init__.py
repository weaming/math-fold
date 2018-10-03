from functools import reduce

arithmatic_mapping = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "**": lambda a, b: a ** b,
}

bool_mapping = {
    ">": lambda a, b: a > b,
    "<": lambda a, b: a < b,
    ">=": lambda a, b: a >= b,
    "<=": lambda a, b: a <= b,
    "in": lambda a, b: a in b,
    "==": lambda a, b: a == b,
}


def get_lambda(notation):
    if notation in arithmatic_mapping:
        return arithmatic_mapping[notation]
    if notation in bool_mapping:
        return bool_mapping[notation]
    if notation.startswith('lambda'):
        return eval(notation)
    raise Exception("unknown notation {}".format(notation))


def cal_list(lst, notation):
    return reduce(get_lambda(notation), lst)
