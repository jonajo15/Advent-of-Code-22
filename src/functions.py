from typing import List


def read_file_to_list(filename, _type):
    with open(filename) as file:
        return [_type(line.rstrip()) for line in file.readlines()]


def read_file_to_string(filename):
    with open(filename) as file:
        return file.read().rstrip()


def read_line_to_list(filename, _type):
    with open(filename) as file:
        return [_type(number) for number in file.readline().split(",")]


def find(lst, key, value, _default=None):
    return next((item for item in lst if item[key] == value), _default)


def every(arr: List[int], compare: List[int]) -> bool:
    return next((False for item in arr if item not in compare), True)


def any(arr: List[int], compare: List[int]) -> bool:
    return next((True for item in arr if item in compare), False)
