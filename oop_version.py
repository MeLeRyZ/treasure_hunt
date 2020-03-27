from utils import get_digit


class CellNotFoundError(BaseException):
    pass


class Cell:
    """Represents cell on treasure map

    Attributes:
        x: X coordinate on board
        y: Y coordinate on board
        hint: Content of the cell with hint for next step
    """
    __slots__ = 'x', 'y', 'hint'

    def __init__(self, x, y, hint):
        self.x, self.y = x, y
        self.hint = hint

    @property
    def is_treasure_cell(self):
        return self.coordinates == self.hint_coordinates

    @property
    def coordinates(self):
        return self.x, self.y

    @property
    def hint_coordinates(self):
        if isinstance(self.hint, str) and len(self.hint) == 2:
            return int(self.hint[0]), int(self.hint[1])
        return get_digit(self.hint, 1), get_digit(self.hint, 0)

    def __repr__(self):
        return f'Cell:{self.coordinates} Hint:{self.hint_coordinates}'


class Board:
    """
    Represents board object that holds the list of all cells on map
    """
    __slots__ = 'cells'

    def __init__(self, board_data):
        self.cells = self._generate_board(board_data)

    def _generate_board(self, board_data):
        """Converts board data to list of `Cell` objects"""
        cells = []
        for row_index, row in enumerate(board_data, 1):
            cells.extend([
                Cell(x=row_index, y=column_index, hint=hint)
                for column_index, hint in enumerate(row, 1)
            ])
        return cells

    def get_cell(self, x, y):
        for cell in self.cells:
            if cell.x == x and cell.y == y:
                return cell
        else:
            raise CellNotFoundError(f'No such cell with coordinates ({x}, {y})')


class TreasureSolver:
    """Solver object 

    Attributes:
        board: instance of Board class
        moves: list of all moves required to reach the goal
        solved: flag that indicates if solver object solved current board
        traveled_cells: set of Cell objects used to detect if board is unsolvable
    """

    def __init__(self, board):
        self.board = board
        self.moves = []
        self.solved = False
        self.traveled_cells = set()

    def print_result(self):
        if self.solved:
            print(f'Output: {", ".join([str(x) for x in self.moves])}')
        else:
            print('Current board is not solved yet')

    def reset_solver(self):
        """Resets current instance attributes for reusability"""
        self.traveled_cells.clear()
        self.moves.clear()
        self.solved = False

    def solve(self, x=1, y=1):
        if self.solved:
            self.reset_solver()
        self.moves.append(int(f'{x}{y}'))
        active_cell = self.board.get_cell(x, y)
        while not self.solved:
            if active_cell in self.traveled_cells:
                print(f'This board can not be solved using this first step ({x}, {y})')
                break
            if active_cell.is_treasure_cell:
                self.solved = True
                self.print_result()
                break
            self.moves.append(active_cell.hint)
            self.traveled_cells.add(active_cell)
            active_cell = self.board.get_cell(*active_cell.hint_coordinates)
        return self.moves if self.solved else None
