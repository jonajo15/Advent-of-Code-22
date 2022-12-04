from pathlib import Path
from typing import List
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def get_assignments(interval: str) -> List[int]:
    low, high = interval.split("-")

    return list(range(int(low), int(high) + 1))


def task1():
    _input = functions.read_file_to_list(filename, str)

    redundant_pairs = 0
    for pair in _input:
        e1, e2 = pair.split(",")

        e1 = get_assignments(e1)
        e2 = get_assignments(e2)

        if functions.every(e1, e2) or functions.every(e2, e1):
            redundant_pairs += 1

    print("\tAnswer: ", redundant_pairs)


def task2():
    _input = functions.read_file_to_list(filename, str)

    redundant_pairs = 0
    for pair in _input:
        e1, e2 = pair.split(",")

        e1 = get_assignments(e1)
        e2 = get_assignments(e2)

        if functions.any(e1, e2) or functions.any(e2, e1):
            redundant_pairs += 1

    print("\tAnswer: ", redundant_pairs)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
