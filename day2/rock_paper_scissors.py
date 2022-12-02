from enum import Enum
import os


class Shape(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


SHAPE_MAP = {
    "A": Shape.ROCK,
    "B": Shape.PAPER,
    "C": Shape.SCISSORS,
    "X": Shape.ROCK,
    "Y": Shape.PAPER,
    "Z": Shape.SCISSORS,
}

SHAPE_SCORES = {
    Shape.ROCK: 1,
    Shape.PAPER: 2,
    Shape.SCISSORS: 3,
}

OUTCOME_SCORES = {
    "L": 0,
    "D": 3,
    "W": 6,
}


def calculate_outcome(opponent_shape, my_shape) -> str:
    if opponent_shape == my_shape:
        return "D"
    elif opponent_shape == Shape.ROCK:
        if my_shape == Shape.SCISSORS:
            return "L"
        else:
            return "W"
    elif opponent_shape == Shape.PAPER:
        if my_shape == Shape.ROCK:
            return "L"
        else:
            return "W"
    elif opponent_shape == Shape.SCISSORS:
        if my_shape == Shape.PAPER:
            return "L"
        else:
            return "W"


TARGET_OUTCOME_MAP = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}


def chose_shape(opponent_shape, target_outcome):
    if target_outcome == "D":
        return opponent_shape
    elif target_outcome == "W":
        if opponent_shape == Shape.ROCK:
            return Shape.PAPER
        elif opponent_shape == Shape.PAPER:
            return Shape.SCISSORS
        else:
            return Shape.ROCK
    elif target_outcome == "L":
        if opponent_shape == Shape.ROCK:
            return Shape.SCISSORS
        elif opponent_shape == Shape.PAPER:
            return Shape.ROCK
        else:
            return Shape.PAPER


def part_one(first, second):
    opponent_shape, my_shape = SHAPE_MAP[first], SHAPE_MAP[second]
    outcome = calculate_outcome(opponent_shape, my_shape)
    score = SHAPE_SCORES[my_shape] + OUTCOME_SCORES[outcome]
    return score


def part_two(first, second):
    opponent_shape, target_outcome = SHAPE_MAP[first], TARGET_OUTCOME_MAP[second]
    my_shape = chose_shape(opponent_shape, target_outcome)
    score = SHAPE_SCORES[my_shape] + OUTCOME_SCORES[target_outcome]
    return score


def calculate_total_score():
    part_one_score = 0
    part_two_score = 0

    input_path = os.path.join(os.path.dirname(__file__), "./input")
    with open(input_path) as f:
        for round_line in f:
            first, second = tuple(round_line.strip().split(" "))
            part_one_score += part_one(first, second)
            part_two_score += part_two(first, second)

    print(part_one_score)
    print(part_two_score)


if __name__ == '__main__':
    calculate_total_score()
