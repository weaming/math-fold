from functools import reduce

arithmatic_mapping = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "**": lambda a, b: a ** b,
    "max": lambda a, b: a if a > b else b,
    "min": lambda a, b: a if a < b else b,
    "mean": lambda a, b: ((a[0] * a[1] + b) / (a[1] + 1), a[1] + 1)
    if isinstance(a, tuple)
    else ((a + b) / 2, 2),
}


def get_lambda(notation):
    if notation in arithmatic_mapping:
        return arithmatic_mapping[notation]
    if notation.startswith("lambda"):
        return eval(notation)
    raise Exception("unknown notation {}".format(notation))


def cal_list(lst, notation):
    return reduce(get_lambda(notation), lst)
