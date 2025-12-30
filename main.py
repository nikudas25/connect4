import sys
import pygame

from game_logic import *
from ui import *

board = create_board()
game_over = False
turn = PLAYER_1

draw_board(screen, board)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
            x = event.pos[0]
            color = RED if turn == PLAYER_1 else YELLOW
            pygame.draw.circle(screen, color, (x, SQUARE_SIZE // 2), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))

            col = event.pos[0] // SQUARE_SIZE

            row = get_next_open_row(board, col)

            if row is not None:
                animate_piece(screen, board, col, row, turn)
                place_piece(board, row, col, turn)
                draw_board(screen, board)

                if check_winner(board, turn):
                    label = FONT.render(
                        f"Player {turn} wins!", 
                        True,
                        RED if turn == PLAYER_1 else YELLOW
                    )

                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    game_over = True
                
                turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

    if game_over:
        pygame.time.wait(3000)

