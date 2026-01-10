import sys
import pygame

from game_logic import *
from ui import *
from ai_player import ai_move

MENU = "menu"
GAME = "game"
GAME_OVER = "game_over"
MODE_SELECT = "mode_select"

state = MENU


AI_ENABLED = True
AI_DEPTH = 4

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
                    state = MODE_SELECT

                elif action == "quit":
                    pygame.quit()
                    sys.exit()

        elif state == MODE_SELECT:
            screen.fill(BLACK)
            mouse_pos = pygame.mouse.get_pos()

            back_base = pygame.Rect(30, 30, 160, 55)
            back_hover = back_base.collidepoint(mouse_pos)
            back_rect = back_base.inflate(6, 6) if back_hover else back_base

            pygame.draw.rect(screen, RED, back_rect, 2, border_radius=10)
            back_text = FONT.render("BACK", True, RED)
            screen.blit(back_text, back_text.get_rect(center=back_rect.center))

            title = FONT.render("CHOOSE MODE", True, RED)
            title_rect = title.get_rect(center=(WIDTH // 2, 180))
            screen.blit(title, title_rect)

            #Base rects
            pvp_base = pygame.Rect(WIDTH // 2 - 295, 300, 590, 70)
            ai_base = pygame.Rect(WIDTH // 2 - 250, 400, 500, 70)

            #Hover detection
            pvp_hover = pvp_base.collidepoint(mouse_pos)
            ai_hover = ai_base.collidepoint(mouse_pos)

            #Inflate hover
            pvp_rect = pvp_base.inflate(10, 10) if pvp_hover else pvp_base
            ai_rect = ai_base.inflate(10, 10) if ai_hover else ai_base

            pygame.draw.rect(screen, YELLOW, pvp_rect, 3, border_radius=12)
            pygame.draw.rect(screen, YELLOW, ai_rect, 3, border_radius=12)

            #Text
            pvp_text = FONT.render("PLAYER vs PLAYER", True, YELLOW)
            ai_text  = FONT.render("PLAYER vs BOT", True, YELLOW)

            screen.blit(pvp_text, pvp_text.get_rect(center=pvp_rect.center))
            screen.blit(ai_text, ai_text.get_rect(center=ai_rect.center))

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    state = MENU
                    continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_rect.collidepoint(event.pos):
                    AI_ENABLED = False

                elif ai_rect.collidepoint(event.pos):
                    AI_ENABLED = True

                else:
                    continue
                
                board = create_board()
                turn = PLAYER_1
                game_over = False
                state = GAME
                draw_board(screen, board)


        #Game code
        elif state == GAME:

            if AI_ENABLED and turn == PLAYER_2 and not game_over:
                pygame.time.wait(400)
                col = ai_move(board, AI_DEPTH)
                row = get_next_open_row(board, col)

                if row is not None:
                    animate_piece(screen, board, col, row, PLAYER_2)
                    place_piece(board, row, col, PLAYER_2)
                    draw_board(screen, board)

                if check_winner(board, PLAYER_2):
                    winner = PLAYER_2
                    state = GAME_OVER
                    game_over = True

                turn = PLAYER_1

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
                if AI_ENABLED and turn == PLAYER_2:
                    continue

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
                    board = create_board()
                    turn = PLAYER_1
                    winner = None
                    game_over = False
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

