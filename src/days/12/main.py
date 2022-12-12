""" Breadth-first search, https://en.wikipedia.org/wiki/Breadth-first_search"""
from pathlib import Path
from collections import defaultdict
from typing import Dict, Tuple, List
from queue import Queue
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"

DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def get_adjancency_list(grid: Dict[Tuple[int, int], int]):
    adjancency: Dict[Tuple[int, int], List[Tuple[int, int]]] = defaultdict(list)

    for pos, height in grid.items():
        for dir in DIRECTIONS:
            neighbor = (pos[0] + dir[0], pos[1] + dir[1])

            if neighbor in grid and grid[neighbor] <= height + 1:
                adjancency[pos].append(neighbor)

    return adjancency


def bfs(
    starts: List[Tuple[int, int]],
    peak: Tuple[int, int],
    grid: Dict[Tuple[int, int], int],
):
    adjancency = get_adjancency_list(grid)

    visited = set()
    queue: Queue = Queue()

    for start in starts:
        queue.put(((start), 0))
        visited.add(start)

    while queue:
        curr_pos, distance = queue.get()

        for neighbor in adjancency[curr_pos]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, distance + 1))

                if neighbor == peak:
                    return distance + 1


def task1():
    _input = functions.read_file_to_list(filename, str)

    grid = {}
    start_pos = None
    peak = None
    for y, row in enumerate(_input):
        for x, letter in enumerate(list(row)):

            if letter == "S":
                start_pos = (x, y)
                grid[(x, y)] = ord("a")
            elif letter == "E":
                peak = (x, y)
                grid[(x, y)] = ord("z")
            else:
                grid[(x, y)] = ord(letter)

    answer = bfs([start_pos], peak, grid)

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    grid = {}
    starts = []
    peak = None
    for y, row in enumerate(_input):
        for x, letter in enumerate(list(row)):

            if letter == "S" or letter == "a":
                starts.append((x, y))
                grid[(x, y)] = ord("a")
            elif letter == "E":
                peak = (x, y)
                grid[(x, y)] = ord("z")
            else:
                grid[(x, y)] = ord(letter)

    answer = bfs(starts, peak, grid)

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
