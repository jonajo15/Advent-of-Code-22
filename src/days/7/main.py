from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional, List
import functions

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"


@dataclass
class File:
    name: str
    size: int

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size


@dataclass
class Directory:
    name: str
    files: List[File] = field(default_factory=list)
    directories: List["Directory"] = field(default_factory=list)
    parent: Optional["Directory"] = None

    def __init__(self, name, parent: Optional["Directory"] = None):
        self.name = name
        self.parent = parent
        self.directories = []
        self.files = []

    def get_size(self) -> int:
        size = 0

        for file in self.files:
            size += file.get_size()

        for dir in self.directories:
            size += dir.get_size()

        return size

    def cd(self, dir: str):
        if dir == "..":
            return self.parent

        sub_dir_name = f"{self.name}/{dir}"
        sub_dir = Directory(sub_dir_name, self)
        self.directories.append(sub_dir)

        return sub_dir

    def add_file(self, name: str, size: int):
        self.files.append(File(name, int(size)))


def get_dir_sizes(dir: Directory) -> Dict[str, int]:
    sizes: Dict[str, int] = {}

    sizes[dir.name] = dir.get_size()

    for subdir in dir.directories:
        sizes.update(get_dir_sizes(subdir))

    return sizes


def get_tree() -> Directory:
    _input = functions.read_file_to_list(filename, str)
    home = Directory("/")
    current_dir = home

    for line in _input:
        if line.startswith("$ cd"):
            dir_name = line.split(" cd ")[1]

            if dir_name == "/":
                current_dir = home
            else:
                current_dir = current_dir.cd(dir_name)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            continue
        else:
            # files
            size, name = line.split(" ")
            current_dir.add_file(name, int(size))

    return home


def task1():
    home = get_tree()

    dir_sizes = get_dir_sizes(home)

    answer = sum([size for size in dir_sizes.values() if size <= 100_000])

    print("\tAnswer: ", answer)


def task2():
    home = get_tree()

    dir_sizes = get_dir_sizes(home)

    used = dir_sizes["/"]
    unused = 70_000_000 - used
    diff = 30_000_000 - unused

    answer = sorted([size for size in dir_sizes.values() if size >= diff]).pop(0)

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
