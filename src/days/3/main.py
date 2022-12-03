from dataclasses import dataclass
from typing import List
from pathlib import Path

import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def get_priority(char: str):
    if char.islower():
        return ord(char) - 96

    return ord(char) - 38


@dataclass
class Rugsack:
    items: str
    compartment_one: str
    compartment_two: str

    def __init__(self, items: str):
        self.items = items

        split_index = len(items) // 2

        self.compartment_one = items[:split_index]
        self.compartment_two = items[split_index:]

    def get_rugsack_priority(self):
        return next(
            get_priority(one)
            for one in self.compartment_one
            if one in self.compartment_two
        )


@dataclass
class Group:
    rugsacks: List[Rugsack]

    def __init__(self, _input: List[str]):
        self.rugsacks = [Rugsack(sack) for sack in _input]

    def get_badge(self):
        first, second, third = self.rugsacks

        return next(
            get_priority(character)
            for character in first.items
            if character in second.items and character in third.items
        )


def task1():
    rugsacks = functions.read_file_to_list(filename, str)

    answer = sum([Rugsack(sack).get_rugsack_priority() for sack in rugsacks])

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    answer = sum(
        [
            Group([_input[i], _input[i + 1], _input[i + 2]]).get_badge()
            for i in range(0, len(_input), 3)
        ]
    )

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
