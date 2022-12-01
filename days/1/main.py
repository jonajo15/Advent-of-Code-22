from dataclasses import dataclass
from typing import List

import functions

filename = 'input.txt'

@dataclass
class Elf():
    calories: int

    def __init__(self, values:List[str]):
        self.calories = sum([int(value) for value in values])


def get_elves(_input: List[str]) -> List[Elf]:
    elves: List[Elf] = []

    curr_values = []
    for value in _input:
        if value == "":
            elves.append(Elf(curr_values))
            curr_values = []
        else:
            curr_values.append(value)

    return elves


def task1():
    _input = functions.read_file_to_list(filename, str)

    elves = get_elves(_input)
    fat_elf = max(elves, key=lambda x: x.calories)

    print("\tAnswer: ", fat_elf.calories)


def task2():
    _input = functions.read_file_to_list(filename, str)

    elves = get_elves(_input)
    top_three = sorted(elves, key=lambda x: x.calories, reverse=True)[0:3]

    calories = sum([fat.calories for fat in top_three])

    print("\tAnswer: ", calories)


if __name__ == '__main__':
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")