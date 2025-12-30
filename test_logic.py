from game_logic import *

board = create_board()

drop_piece(board, 0, PLAYER_1)
drop_piece(board, 0, PLAYER_1)
drop_piece(board, 0, PLAYER_1)
drop_piece(board, 0, PLAYER_1)

print("winner:", check_winner(board, PLAYER_1))
