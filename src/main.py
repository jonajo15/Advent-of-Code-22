from pathlib import Path
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "example.txt"


def task1():
    _input = functions.read_file_to_list(filename, str)

    answer = 0

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    answer = 0

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
