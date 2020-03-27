from utils import get_digit


def board_solver(board):
    moves = []
    solved = False

    def move_to_next_cell(x=1, y=1):
        nonlocal solved
        if solved:
            solved = False
            moves.clear()
        current_cell = int(f'{x}{y}')
        moves.append(current_cell)
        next_cell = board[x - 1][y - 1]
        if next_cell == current_cell:
            solved = True
            return moves
        next_x, next_y = get_digit(next_cell, 1), get_digit(next_cell, 0)
        return move_to_next_cell(next_x, next_y)

    return move_to_next_cell
