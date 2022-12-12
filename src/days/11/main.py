from pathlib import Path
from typing import List, Callable, Dict
import functions
from math import lcm

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def get_operation(op: str) -> Callable[[int], int]:
    _, equation = op.split(" = ")
    _, op, value = equation.split(" ")

    if op == "*":
        return lambda x: x * (x if value == "old" else int(value))
    if op == "+":
        return lambda x: x + (x if value == "old" else int(value))
    if op == "-":
        return lambda x: x - (x if value == "old" else int(value))

    raise Exception("Unsupported operation")


class Monkey:
    index: int
    items: List[int]
    operation: Callable[[int], int]
    test_divisable: int
    test_success: int
    test_failed: int
    inspection_counter: int = 0

    def __init__(self, inp: str):
        (
            monkey_name,
            starting_items,
            operation,
            test_div,
            test_true,
            test_false,
        ) = inp.split("\n")

        self.index = int(monkey_name.split(" ")[1].split(":")[0])
        self.items = [
            int(item.strip()) for item in starting_items.split(":")[1].split(",")
        ]
        self.operation = get_operation(operation)
        self.test_divisable = int(test_div.split(" ")[-1])
        self.test_success = int(test_true.split(" ")[-1])
        self.test_failed = int(test_false.split(" ")[-1])

    def __str__(self) -> str:
        return f"index: {self.index}, items: {self.items}, inspections: {self.inspection_counter}"

    def business(self, monkey_mapper: Dict[int, "Monkey"], least_common, divider=3):
        # inspect
        for item in self.items:
            worry_level = (self.operation(item) // divider) % least_common
            self.inspection_counter += 1

            if worry_level % self.test_divisable == 0:
                monkey_mapper[self.test_success].items.append(worry_level)
            else:
                monkey_mapper[self.test_failed].items.append(worry_level)

        self.items = []


def task1():
    _input = functions.read_file_to_string(filename)

    monkeys = [Monkey(inp) for inp in _input.split("\n\n")]

    monkey_mapper = {monkey.index: monkey for monkey in monkeys}

    least_common_multi = lcm(
        *(monkey.test_divisable for monkey in monkey_mapper.values())
    )

    for _ in range(20):
        for monkey in monkey_mapper.values():
            monkey.business(monkey_mapper, least_common_multi)

    most_busy = sorted(
        monkey_mapper.values(),
        key=lambda x: x.inspection_counter,
        reverse=True,
    )

    answer = most_busy[0].inspection_counter * most_busy[1].inspection_counter

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_string(filename)

    monkeys = [Monkey(inp) for inp in _input.split("\n\n")]

    monkey_mapper = {monkey.index: monkey for monkey in monkeys}

    least_common_multi = lcm(
        *(monkey.test_divisable for monkey in monkey_mapper.values())
    )

    for _ in range(10000):
        for monkey in monkey_mapper.values():
            monkey.business(monkey_mapper, least_common_multi, 1)

    most_busy = sorted(
        monkey_mapper.values(),
        key=lambda x: x.inspection_counter,
        reverse=True,
    )

    answer = most_busy[0].inspection_counter * most_busy[1].inspection_counter

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
