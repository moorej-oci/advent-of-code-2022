from enum import Enum
from dataclasses import dataclass
from aocd.models import Puzzle


class Choice(Enum):
    ROCK = 'A'
    PAPER = 'B'
    SCISSORS = 'C'


def get_choice_value(choice: Choice) -> int:
    if choice == Choice.ROCK:
        return 1
    elif choice == Choice.PAPER:
        return 2
    elif choice == Choice.SCISSORS:
        return 3
    else:
        raise ValueError(f'{choice=} is not supported!')


@dataclass
class Match:
    opponent_choice: Choice
    my_choice: Choice

    WIN: int = 6
    TIE: int = 3
    LOSS: int = 0

    @property
    def score(self):
        # score is equal to outcome of the match plus the value of your choice

        if self.my_choice == self.opponent_choice:
            outcome_score = self.TIE
        elif self.my_choice == Choice.ROCK and self.opponent_choice == Choice.PAPER:
            outcome_score = self.LOSS
        elif self.my_choice == Choice.ROCK and self.opponent_choice == Choice.SCISSORS:
            outcome_score = self.WIN
        elif self.my_choice == Choice.PAPER and self.opponent_choice == Choice.ROCK:
            outcome_score = self.WIN
        elif self.my_choice == Choice.PAPER and self.opponent_choice == Choice.SCISSORS:
            outcome_score = self.LOSS
        elif self.my_choice == Choice.SCISSORS and self.opponent_choice == Choice.ROCK:
            outcome_score = self.LOSS
        elif self.my_choice == Choice.SCISSORS and self.opponent_choice == Choice.PAPER:
            outcome_score = self.WIN
        else:
            raise ValueError(f'{self.my_choice=} and {self.opponent_choice=} not accounted for')

        return outcome_score + get_choice_value(self.my_choice)


def standardize_choice_puzzle_one(choice: str) -> Choice:
    if choice in {'A', 'B', 'C'}:
        return Choice(choice)
    elif choice == 'X':
        return Choice.ROCK
    elif choice == 'Y':
        return Choice.PAPER
    elif choice == 'Z':
        return Choice.SCISSORS
    else:
        raise ValueError(f'{choice=} is not supported!')


def standardize_choice_puzzle_two(opponent_choice: str, desired_outcome: str) -> (Choice, Choice):
    opponent_choice = Choice(opponent_choice)

    if desired_outcome == 'X':
        if opponent_choice == Choice.ROCK:
            return opponent_choice, Choice.SCISSORS
        elif opponent_choice == Choice.PAPER:
            return opponent_choice, Choice.ROCK
        elif opponent_choice == Choice.SCISSORS:
            return opponent_choice, Choice.PAPER
    elif desired_outcome == 'Y':
        return opponent_choice, opponent_choice
    elif desired_outcome == 'Z':
        if opponent_choice == Choice.ROCK:
            return opponent_choice, Choice.PAPER
        elif opponent_choice == Choice.PAPER:
            return opponent_choice, Choice.SCISSORS
        elif opponent_choice == Choice.SCISSORS:
            return opponent_choice, Choice.ROCK
    else:
        raise ValueError(f'{desired_outcome=} is not supported')


def parse_input(puzzle: Puzzle, puzzle_name: str):
    raw_matches = puzzle.input_data.splitlines()
    raw_split_matches = [match.split() for match in raw_matches]

    if puzzle_name == 'one':
        raw_standardized_matches = [
            (standardize_choice_puzzle_one(x), standardize_choice_puzzle_one(y)) for x, y in raw_split_matches]
    elif puzzle_name == 'two':
        raw_standardized_matches = [
            standardize_choice_puzzle_two(x, y) for x, y in raw_split_matches]
    else:
        raise ValueError(f'{puzzle_name=} is not supported')

    return [Match(*choices) for choices in raw_standardized_matches]


def puzzle_one(puzzle):
    matches = parse_input(puzzle, 'one')
    print(sum(m.score for m in matches))


def puzzle_two(puzzle):
    matches = parse_input(puzzle, 'two')
    print(sum(m.score for m in matches))


if __name__ == '__main__':
    day_two_puzzle = Puzzle(2022, 2)
    puzzle_one(day_two_puzzle)
    puzzle_two(day_two_puzzle)
