import sys

from utils import read_json
from oop_version import Board, TreasureSolver
from functional_version import board_solver


board_map = read_json('treasures.json')


def main(board_map):
    version = input('Choose between OO(o) and Functional(f) versions and press [Enter] or [q] to quit: ').lower()

    if version == 'o':
        board = Board(board_map)
        TreasureSolver(board).solve()
    elif version == 'f':
        solver = board_solver(board_map)
        try:
            result = solver(1, 1)
            print(f'Output: {", ".join([str(x) for x in result])}')
        except RecursionError as exc:
            print(f'This board can not be solved using {exc.args[0]} as first step')
    elif version == 'q':
        sys.exit("Bye, bye!")
    else:
        main(board_map)


main(board_map)
