from pathlib import Path
from typing import Tuple
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def walk(
    xy: Tuple[int, int],
    dxdy: Tuple[int, int],
) -> Tuple[int, int]:
    return (xy[0] + dxdy[0], xy[1] + dxdy[1])


def task1():
    _input = functions.read_file_to_list(filename, str)

    grid = {}
    for x, line in enumerate(_input):
        for y, height in enumerate(list(line)):
            grid[x, y] = int(height)

    trees = []

    for tree in grid:
        height = grid[tree]
        visible = False

        for dxdy in DIRECTIONS:
            pos = tree

            while not visible and pos in grid:
                tree_pos = walk(pos, dxdy)

                if tree_pos not in grid:
                    # never blocked => visible
                    visible = True
                    break

                if grid[tree_pos] >= height:
                    # bigger tree => not visible
                    break

                pos = tree_pos

            if visible:
                break

        if visible:
            trees.append(tree)

    answer = len(trees)
    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    grid = {}
    for x, line in enumerate(_input):
        for y, height in enumerate(list(line)):
            grid[x, y] = int(height)

    scenic_scores = []

    for tree in grid:
        score = 1
        height = grid[tree]

        for dxdy in DIRECTIONS:
            curr_pos = walk(tree, dxdy)

            dir_score = 0
            while curr_pos in grid:
                dir_score += 1

                if grid[curr_pos] >= height:
                    # bigger tree
                    break

                curr_pos = walk(curr_pos, dxdy)

            score *= dir_score

        scenic_scores.append(score)

    answer = max(scenic_scores)
    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
