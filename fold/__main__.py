import sys
from . import cal_list, arithmatic_mapping


def to_number(x):
    return float(x)


def get_stdin():
    return sys.stdin.readlines()


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "notation",
        help="the math symbol. choices are {{}}".format(
            ", ".join(list(arithmatic_mapping))
        ),
    )
    args = parser.parse_args()

    try:
        numbers = [to_number(x) for x in get_stdin()]
        result = cal_list(numbers, args.notation)
        print(result)
    except Exception as e:
        print(str(e))
        sys.exit(1)
