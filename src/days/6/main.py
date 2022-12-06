from pathlib import Path
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def task1():
    datastream = functions.read_file_to_string(filename)

    subset_length = 4
    answer = 0

    for index in range(0, len(datastream) - subset_length + 1):
        subset = set(datastream[index : index + subset_length])

        if len(subset) == subset_length:
            answer = index + subset_length
            break

    print("\tAnswer: ", answer)


def task2():
    datastream = functions.read_file_to_string(filename)

    subset_length = 14
    answer = 0

    for index in range(0, len(datastream) - subset_length + 1):
        subset = set(datastream[index : index + subset_length])

        if len(subset) == subset_length:
            answer = index + subset_length
            break

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
