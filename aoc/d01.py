# Day 01 Puzzle 1
# https://adventofcode.com/2022/day/1
# Puzzle Statements:
# 1) How many total Calories is that Elf carrying?
# 2) How many total Calories are the top 3 Elves carrying

from dataclasses import dataclass
from aocd.models import Puzzle


@dataclass
class Elf:
    calories: list[int]

    @property
    def total_calories(self):
        return sum(self.calories)


def parse_elf(elf: str):
    return Elf(calories=[int(x) for x in elf.splitlines()])


def parse_input(puzzle):
    # input data contains one integer per line for items the elf is carrying.
    # elves are separated by an empty line
    return [parse_elf(elf) for elf in puzzle.input_data.split('\n\n')]


def puzzle_one(puzzle):
    elves = parse_input(puzzle)
    top_elf = max(elves, key=lambda elf: elf.total_calories)
    print(top_elf.total_calories)


def puzzle_two(puzzle):
    elves = parse_input(puzzle)
    elves.sort(key=lambda elf: elf.total_calories, reverse=True)
    top_three_elves = elves[:3]
    print(sum(elf.total_calories for elf in top_three_elves))


if __name__ == '__main__':
    day_one_puzzle = Puzzle(year=2022, day=1)
    puzzle_one(day_one_puzzle)
    puzzle_two(day_one_puzzle)
