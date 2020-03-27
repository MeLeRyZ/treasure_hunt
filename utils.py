import json


class BoardValidationError(BaseException):
    pass


def get_digit(number, n):
    """Returns specific nth digit. Indexing from right to left starts at 0"""
    return number // 10**n % 10


def validate_board(board_source):
    """
    Checks if size of two-dimentional array is 5x5
    """
    rows_lengths = {len(x) for x in board_source}
    if len(board_source) == 5 and len(rows_lengths) == 1 and list(rows_lengths)[0] == 5:
        return True
    raise BoardValidationError('Board size must be 5 x 5')


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        board_data = json.load(f)
    if validate_board(board_data):
        return board_data
