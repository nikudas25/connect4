import copy
import random
from game_logic import *

AI_PLAYER = PLAYER_2
HUMAN_PLAYER = PLAYER_1

def get_valid_columns(board):
    return [c for c in range(COLS) if get_next_open_row(board, c) is not None]

def score_window(window, player):
    score = 0
    opp = HUMAN_PLAYER if player == AI_PLAYER else AI_PLAYER

    if window.count(player) == 4:
        score += 100

    elif window.count(player) == 3 and window.count(EMPTY) == 1:
        score += 5

    elif window.count(player) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, player):
    score = 0

    center_col = [board[r][COLS // 2] for r in range(ROWS)]
    score += center_col.count(player) * 3

    #Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            window = board[r][c:c+4]
            score += score_window(window, player)

    #Vertical
    for c in range(COLS):
        col = [board[r][c] for r in range(ROWS)]
        for r in range(ROWS - 3):
            score += score_window(col[r:r + 4], player)

    #Diagonals
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            score += score_window(
                [board[r+i][c+i] for i in range(4)], player
            )

            score += score_window(
                [board[r+3-i][c+i] for i in range(4)], player
            )
    return score

def minimax(board, depth, alpha, beta, maximizing):
    valid_cols = get_valid_columns(board)
    terminal = (
        check_winner(board, HUMAN_PLAYER) or
        check_winner(board, AI_PLAYER) or
        len(valid_cols) == 0
    )

    if depth == 0 or terminal:
        if check_winner(board, AI_PLAYER):
            return None, 1_000_000
        elif check_winner(board, HUMAN_PLAYER):
            return None, -1_000_000
        else:
            return None, score_position(board, AI_PLAYER)
        

    if maximizing:
        value = -float("inf")
        best_col = random.choice(valid_cols)
        for col in valid_cols:
            row = get_next_open_row(board, col)
            temp = copy.deepcopy(board)
            place_piece(temp, row, col, AI_PLAYER)
            _, new_score = minimax(temp, depth-1, alpha, beta, False)

            if new_score > value:
                value = new_score
                best_col = col

            alpha = max(alpha, value)
            if alpha >= beta:
                break

        return best_col, value
    
    else:
        value = float("inf")
        best_col = random.choice(valid_cols)
        for col in valid_cols:
            row = get_next_open_row(board, col)
            temp = copy.deepcopy(board)
            place_piece(temp, row, col, HUMAN_PLAYER)
            _, new_score = minimax(temp, depth-1, alpha, beta, True)
            if new_score < value:
                value = new_score
                best_col = col

            beta = min(beta, value)
            if alpha >= beta:
                break

        return best_col, value
    
def ai_move(board, depth = 4):
    col,  _ = minimax(board, depth, -float("inf"), float("inf"), True)
    return col