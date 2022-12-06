from pathlib import Path
from typing import List
import functions
import re

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def get_crate_stacks(stacks_input: str) -> List[List[str]]:
    columns: List[List[str]] = []

    *rows, cols = stacks_input.split("\n")

    number_of_stacks = int(cols.split("   ")[-1])

    for x in range(number_of_stacks):
        stack: List[str] = []
        index = x * 4 + 1  # character positions

        for y in range(len(rows)):
            character = rows[y][index]

            if character == " ":
                continue

            stack.append(character)

        columns.append(stack)

    return columns


def task1():
    _input = functions.read_file_to_string(filename)

    stacks_input, procedures = _input.split("\n\n")
    procedures = procedures.split("\n")
    stacks = get_crate_stacks(stacks_input)

    for proc in procedures:
        amount, _from, _to = [int(number) for number in re.findall("[0-9]+", proc)]

        for _ in range(amount):
            moving_crate = stacks[_from - 1].pop(0)
            stacks[_to - 1].insert(0, moving_crate)

    answer = "".join(stack[0] for stack in stacks)

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_string(filename)

    stacks_input, procedures = _input.split("\n\n")
    procedures = procedures.split("\n")
    stacks = get_crate_stacks(stacks_input)

    for proc in procedures:
        amount, _from, _to = [int(number) for number in re.findall("[0-9]+", proc)]

        for i in range(amount):
            moving_crate = stacks[_from - 1].pop(0)
            stacks[_to - 1].insert(i, moving_crate)

    answer = "".join(stack[0] for stack in stacks)

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
