import functions

from pathlib import Path

dir = Path(__file__).parent.resolve()

filename = dir / "input.txt"

SCORES = {"X": 1, "Y": 2, "Z": 3}

WINS = ["A Y", "B Z", "C X"]

DRAWS = [
    "A X",
    "B Y",
    "C Z",
]

LOSS = ["A Z", "B X", "C Y"]

CONVERTER = {
    "X": {"A": "Z", "B": "X", "C": "Y", "score": 0},
    "Y": {"A": "X", "B": "Y", "C": "Z", "score": 3},
    "Z": {"A": "Y", "B": "Z", "C": "X", "score": 6},
}


def task1():
    _input = functions.read_file_to_list(filename, str)

    answer = 0

    for comp in _input:
        [opp, me] = comp.split(" ")

        if comp in WINS:
            answer += 6 + SCORES[me]
        elif comp in DRAWS:
            answer += 3 + SCORES[me]
        elif comp in LOSS:
            answer += SCORES[me]

    print("\tAnswer: ", answer)


def task2():
    _input = functions.read_file_to_list(filename, str)

    answer = 0

    for comp in _input:
        [opp, me] = comp.split(" ")

        conv = CONVERTER[me]
        answer += conv["score"] + SCORES[conv[opp]]

    print("\tAnswer: ", answer)


if __name__ == "__main__":
    print("========== Task 1 ==========")
    task1()
    print("============================\n")

    print("========== Task 2 ==========")
    task2()
    print("============================")
