import sys
import pygame

from game_logic import *
from ui import *

MENU = "menu"
GAME = "game"
GAME_OVER = "game_over"
state = MENU

board = create_board()
game_over = False
turn = PLAYER_1

mouse_pos = pygame.mouse.get_pos()
draw_menu(screen, mouse_pos)
draw_board(screen, board)

while True:
    # pygame.clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Menu code
        if state == MENU:
            mouse_pos = pygame.mouse.get_pos()
            draw_menu(screen, mouse_pos)

            if event.type == pygame.MOUSEBUTTONDOWN:
                action = menu_click(event.pos)

                if action == "play":
                    board = create_board()
                    turn = PLAYER_1
                    game_over = False

                    state = GAME
                    draw_board(screen, board)

                elif action == "quit":
                    pygame.quit()
                    sys.exit()

        #Game code
        elif state == GAME:

            if event.type == pygame.MOUSEMOTION and not game_over:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                x = event.pos[0]
                color = RED if turn == PLAYER_1 else YELLOW
                pygame.draw.circle(
                    screen,
                    color,
                    (x, SQUARE_SIZE // 2),
                    RADIUS
                )
                pygame.display.update()



            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
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
                    
                    if check_winner(board, turn):
                        winner = turn
                        state = GAME_OVER
                        
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        game_over = True

                    turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

        elif state == GAME_OVER:
            play_again_rect, menu_rect = draw_game_over(screen, winner)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    board = create_board()
                    turn = PLAYER_1
                    winner = None
                    game_over = False
                    state = GAME
                    draw_board(screen, board)

                elif menu_rect.collidepoint(event.pos):
                    state = MENU
    # if game_over:
    #     pygame.time.wait(2000)







#                 if check_winner(board, turn):
#                     label = FONT.render(
#                         f"Player {turn} wins!", 
#                         True,
#                         RED if turn == PLAYER_1 else YELLOW
#                     )

#                     screen.blit(label, (40, 10))
#                     pygame.display.update()
#                     game_over = True
                
#                 turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

    # if game_over:
    #     pygame.time.wait(3000)





"""
Old logic which led to directly to the game.
"""

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#         if event.type == pygame.MOUSEMOTION:
#             pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
#             x = event.pos[0]
#             color = RED if turn == PLAYER_1 else YELLOW
#             pygame.draw.circle(screen, color, (x, SQUARE_SIZE // 2), RADIUS)
#             pygame.display.update()

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))

#             col = event.pos[0] // SQUARE_SIZE

#             row = get_next_open_row(board, col)

#             if row is not None:
#                 animate_piece(screen, board, col, row, turn)
#                 place_piece(board, row, col, turn)
#                 draw_board(screen, board)

#                 if check_winner(board, turn):
#                     label = FONT.render(
#                         f"Player {turn} wins!", 
#                         True,
#                         RED if turn == PLAYER_1 else YELLOW
#                     )

#                     screen.blit(label, (40, 10))
#                     pygame.display.update()
#                     game_over = True
                
#                 turn = PLAYER_2 if turn == PLAYER_1 else PLAYER_1

    # if game_over:
    #     pygame.time.wait(3000)

