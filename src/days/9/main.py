from pathlib import Path
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


def step_head(curr, dir):
    x, y = curr
    if dir == "R":
        return (x + 1, y)
    if dir == "L":
        return (x - 1, y)
    if dir == "U":
        return (x, y + 1)

    # down
    return (x, y - 1)


def step_tail(head, tail):
    xdelta = head[0] - tail[0]
    ydelta = head[1] - tail[1]

    if abs(xdelta) < 2 and abs(ydelta) < 2:
        # dont move
        return tail

    if xdelta == 0:
        # move y
        return (tail[0], tail[1] + ydelta / abs(ydelta))

    if ydelta == 0:
        # move x
        return (tail[0] + xdelta / abs(xdelta), tail[1])

    # move diagonally
    return (tail[0] + xdelta / abs(xdelta), tail[1] + ydelta / abs(ydelta))


def task1():
    movements = functions.read_file_to_list(filename, str)

    visited = set()

    head = tail = (0, 0)
    for movement in movements:
        dir, moves = movement.split(" ")

        for _ in range(int(moves)):
            head = step_head(head, dir)
            tail = step_tail(head, tail)

            visited.add(tail)

    answer = len(visited)

    print("\tAnswer: ", answer)


def task2():
    movements = functions.read_file_to_list(filename, str)

    visited = set()

    knots = {nr: (0, 0) for nr in range(0, 10)}

    for movement in movements:
        dir, moves = movement.split(" ")

        for _ in range(int(moves)):
            for knot in knots:
                if knot == 0:
                    knots[knot] = step_head(knots[knot], dir)
                else:
                    knots[knot] = step_tail(knots[knot - 1], knots[knot])

                if knot == 9:
                    visited.add(knots[knot])

    answer = len(visited)

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
