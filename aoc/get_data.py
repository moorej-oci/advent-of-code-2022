import argparse
import pathlib

from aocd.models import Puzzle


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', type=int, required=True)
    parser.add_argument('-y', '--year', type=int, required=False, default=2022)
    return parser.parse_args()


def get_data_dir():
    return pathlib.Path(__file__).parent.absolute() / 'data'


def main(day, year):
    puzzle = Puzzle(year, day)
    output_file = get_data_dir() / f'{year}-{day}.txt'
    output_file.write_text(puzzle.input_data)


if __name__ == '__main__':
    args = get_args()
    main(args.day, args.year)
