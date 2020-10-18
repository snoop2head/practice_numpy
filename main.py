import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER_ONE_PIECE = 1
PLATER_TWO_PIECE = 2


def create_board():
    mat_board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return mat_board


def drop_piece(mat_moard, int_row, int_col, piece):
    mat_board[int_row][int_col] = piece
    return mat_board


def is_valid_location(mat_board, int_column):
    return mat_board[5][int_column] == 0


def get_next_open_row(mat_board, int_column):
    for r in range(ROW_COUNT):
        if mat_board[r][int_column] == 0:
            return r


def flip_board(mat_board):
    mat_flipped_board = np.flip(mat_board, 0)  # column axis flipping
    return mat_flipped_board


mat_board = create_board()
print(mat_board)
fliped_board = [[]]
turn = 0

bool_game_over = False

while not bool_game_over:
    # ask for player 1 input
    if turn == 0:
        str_column = input("Player 1 make your column (0-6):")
        int_column = int(str_column)
        # print(int_column, type(int_column))
        if is_valid_location(mat_board, int_column):
            int_row = get_next_open_row(mat_board, int_column)
            mat_board = drop_piece(mat_board, int_row, int_column, PLAYER_ONE_PIECE)

    # ask for player 2 input
    else:
        str_column = input("Player 2 make your column (0-6):")
        int_column = int(str_column)
        if is_valid_location(mat_board, int_column):
            int_row = get_next_open_row(mat_board, int_column)
            mat_board = drop_piece(mat_board, int_row, int_column, PLATER_TWO_PIECE)

    fliped_board = flip_board(mat_board)
    print(fliped_board)
    turn += 1
    turn = turn % 2  # alternating between 0 and 1
