from pathlib import Path
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def task1():
    signals = functions.read_file_to_list(filename, str)

    cycle = 0
    x = 1
    answer = 0
    next_cycle = 20

    for action in signals:
        if action == "noop":
            cycle += 1
        else:
            cycle += 2

        if cycle >= next_cycle:
            answer += x * (cycle - cycle % 10)
            next_cycle += 40

        if action.startswith("addx"):
            _, value = action.split(" ")

            x += int(value)

    print("\tAnswer: ", answer)


def task2():
    signals = functions.read_file_to_list(filename, str)

    x_over_cycles = []
    x = 1

    for action in signals:
        if action == "noop":
            x_over_cycles.append(x)
        else:
            x_over_cycles.append(x)
            x_over_cycles.append(x)

            _, value = action.split(" ")

            x += int(value)

    for y in range(6):
        row = ""
        for col in range(40):
            cycle = y * 40 + col
            curr_x = x_over_cycles[cycle]

            if col in [curr_x - 1, curr_x, curr_x + 1]:
                row += "#"
            else:
                row += "."

        print(row)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
