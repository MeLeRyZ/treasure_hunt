import pytest

from oop_version import Board, Cell, CellNotFoundError, TreasureSolver
from functional_version import board_solver
from tests.fixtures import correct_board, incorrect_board


def test_solving_correct_board(correct_board):
    board = Board(correct_board)
    test = TreasureSolver(board).solve()
    assert test == [11, 34, 42, 15, 25, 31, 54, 13, 32,
        45, 35, 23, 43, 51, 21, 14, 41, 33, 52
    ]


def test_solving_incorrect_board(incorrect_board):
    """Solver should return None if board is unsolvable"""
    board = Board(incorrect_board)
    assert TreasureSolver(board).solve() == None


def test_cell_is_treasure():
    correct_cell = Cell(2, 3, 23)
    incorrect_cell = Cell(1, 1, 12)
    assert correct_cell.is_treasure_cell
    assert not incorrect_cell.is_treasure_cell


def test_cell_hint_parsing():
    """Tests if hint could be parsed as str or int"""
    str_cell = Cell(1, 1, '23')
    int_cell = Cell(1, 1, 23)
    assert str_cell.hint_coordinates == (2, 3)
    assert int_cell.hint_coordinates == (2, 3)


def test_board_generation(correct_board):
    board_obj = Board(correct_board)
    assert isinstance(board_obj.cells, list)
    assert len(board_obj.cells) == 25
    assert all([isinstance(x, Cell) for x in board_obj.cells])


def test_board_get_cell(correct_board):
    board_obj = Board(correct_board)
    assert board_obj.get_cell(1, 1).hint == 34
    with pytest.raises(CellNotFoundError) as exception:
        board_obj.get_cell(0, 0)


def test_solver_reusability(correct_board):
    """Tests if solver can be used again with different starting point"""
    board_obj = Board(correct_board)
    solver_obj = TreasureSolver(board_obj)
    assert solver_obj.solve(1, 1) == [11, 34, 42, 15, 25, 31, 54, 13, 32,
                                      45, 35, 23, 43, 51, 21, 14, 41, 33, 52]
    assert solver_obj.solve(2, 2) == [22, 42, 15, 25, 31, 54, 13, 32,
                                      45, 35, 23, 43, 51, 21, 14, 41, 33, 52]
    solver_obj.reset_solver()
    assert not all([solver_obj.moves, solver_obj.traveled_cells,
                    solver_obj.solve])


def test_equal_results(correct_board):
    """Results should be equal for both implementations"""
    result_1 = TreasureSolver(Board(correct_board)).solve()
    result_2 = board_solver(correct_board)()
    assert result_1 == result_2
