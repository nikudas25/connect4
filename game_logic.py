ROWS = 6
COLS = 7
EMPTY = 0
PLAYER_1 = 1
PLAYER_2 = 2

def create_board():
    return[[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# def drop_piece(board, col, player):
#     if col < 0 or col >= COLS:
#         return False
    
#     for row in range(ROWS - 1, -1, -1):
#         if board[row][col] == EMPTY:
#             board[row][col] = player
#             return True
#     return False
def get_next_open_row(board, col):
    if col < 0 or col >= COLS:
        return None
    
    for row in range(ROWS -1, -1, -1):
        if board[row][col] == EMPTY:
            return row
        
    return None

def place_piece(board, row, col, player):
    board[row][col] = player

def check_horizontal(board, player):
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True
    return False

def check_vertical(board, player):
    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True
    return False

def check_diagonal_down(board, player):
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
    return False
        
def check_diagonal_up(board, player):
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True
    return False
        


def check_winner(board, player):
    return(
        check_horizontal(board, player) or
        check_vertical(board, player) or
        check_diagonal_down(board, player) or
        check_diagonal_up(board, player)
    )

def is_board_full(board):
    return all(board[0][col] != EMPTY for col in range(COLS))
