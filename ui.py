import pygame
from game_logic import *

pygame.init()

SQUARE_SIZE = 100
WIDTH = COLS * SQUARE_SIZE
HEIGHT = (ROWS + 1) * SQUARE_SIZE
RADIUS = SQUARE_SIZE // 2 - 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")

FONT = pygame.font.SysFont("monospace", 60)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

MENU_Y = 420
MENU_WIDTH = 460
MENU_HEIGHT = 80
MENU_X_OFFSET = -1.5


def draw_board(screen, board):
    screen.fill(BLACK)

    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(
                screen,
                BLUE,
                (col * SQUARE_SIZE, (row + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

            pygame.draw.circle(
                screen, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)
            
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == PLAYER_1:
                color = RED
            
            elif board[row][col] == PLAYER_2:
                color = YELLOW
            
            else:
                continue

            pygame.draw.circle(
                screen,
                color,
                (col * SQUARE_SIZE + SQUARE_SIZE // 2,
                (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2),
                RADIUS
            )

    pygame.display.update()

    
def animate_piece(screen, board, col, row, player):
    color = RED if player == PLAYER_1 else YELLOW

    clock = pygame.time.Clock()

    x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    y = SQUARE_SIZE // 2
    target_y = (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2

    velocity = 0
    gravity = 20

    while y < target_y:
        dt = clock.tick(60) / 100

        velocity += gravity * dt
        y += velocity * dt

        if y > target_y:
            y = target_y
            velocity *= -0.15

        draw_board(screen, board)
        pygame.draw.circle(
            screen,
            color,
            (x, int(y)),
            RADIUS
        )

        pygame.display.update()
        
def draw_menu(screen, mouse_pos):
    screen.fill(BLACK)

    title = FONT.render("CONNECT 4", True, RED)
    play_text = FONT.render("PLAY", True, YELLOW)
    quit_text = FONT.render("QUIT", True, YELLOW)

    play_rect = pygame.Rect(WIDTH // 2 - 150, 300, 300, 70)
    quit_rect = pygame.Rect(WIDTH // 2 - 150, 400, 300, 70)

    #Hover Detection
    play_hover = play_rect.collidepoint(mouse_pos)
    quit_hover = quit_rect.collidepoint(mouse_pos)

    #Colors
    play_color = BLACK if play_hover else YELLOW
    quit_color = BLACK if quit_hover else YELLOW
    play_bg = YELLOW if play_hover else BLACK
    quit_bg = YELLOW if quit_hover else BLACK

    #Draw title
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

    #Draw play button
    pygame.draw.rect(screen, play_bg, play_rect, border_radius=12)
    play_text = FONT.render("PLAY", True, play_color)
    screen.blit(
        play_text,
        (play_rect.centerx - play_text.get_width() // 2,
        play_rect.centery - play_text.get_height() // 2)
    )

    #Draw quit button
    pygame.draw.rect(screen, quit_bg, quit_rect, border_radius = 12)
    quit_text = FONT.render("QUIT", True, quit_color)
    screen.blit(
        quit_text,
        (quit_rect.centerx - quit_text.get_width() // 2,
        quit_rect.centery - quit_text.get_height() // 2)
    )

    # screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    # screen.blit(play_text, (WIDTH // 2 - play_text.get_width() // 2, 300))
    # screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, 400))

    pygame.display.update()

def menu_click(pos):
    # x = pos
    # y = pos

    play_rect = pygame.Rect(WIDTH // 2 - 100, 300, 200, 70)
    quit_rect = pygame.Rect(WIDTH // 2 - 100, 400, 200, 70)

    if play_rect.collidepoint(pos):
        return "play"
    
    if quit_rect.collidepoint(pos):
        return "quit"
    
    return None


def draw_game_over(screen, winner):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))

    if winner == PLAYER_1:
        winner_text = "PLAYER 1 WINS!"
        winner_color = RED
    
    elif winner == PLAYER_2:
        winner_text = "PLAYER 2 WINS!"
        winner_color = YELLOW
    else:
        winner_text = "DRAW"
        winner_color = (200, 200, 200)

    winner_surface = FONT.render(winner_text, True, winner_color)

    screen.blit(
        winner_surface,
        (
            WIDTH // 2 - winner_surface.get_width() // 2,
            200
        )
    )

    mouse_pos = pygame.mouse.get_pos()

    #Play Button
    play_text_surface = FONT.render("PLAY AGAIN", True, winner_color)
    play_padding_x = 40
    play_padding_y = 20

    play_again_rect = pygame.Rect(
        WIDTH // 2 - (play_text_surface.get_width() + play_padding_x) // 2,
        320,
        play_text_surface.get_width() + play_padding_x,
        62 + play_padding_y
    )

    menu_rect = pygame.Rect(
        WIDTH // 2 - 120, 
        420,
        240,
        70
    )


    mouse_pos = pygame.mouse.get_pos()
    play_hover = play_again_rect.collidepoint(mouse_pos)

    #Hover BG color (neutral, readable)
    play_bg_color = (60, 60, 60) if play_hover else BLACK

    base_rect = play_again_rect.copy()

    if play_hover:
        play_again_rect = base_rect.inflate(6, 6)


    pygame.draw.rect(
        screen,
        play_bg_color,
        play_again_rect, 
        width = 2,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        winner_color,
        play_again_rect,
        width=2,
        border_radius=12
    )
    
    screen.blit(
        play_text_surface,
        (
            play_again_rect.centerx - play_text_surface.get_width() // 2,
            play_again_rect.centery - play_text_surface.get_height() // 2
        )
    )


    #MENU BUTTON
    menu_text_surface = FONT.render("BACK TO MENU", True, winner_color)
    menu_base_rect = pygame.Rect(
        WIDTH // 2 - MENU_WIDTH // 2 + MENU_X_OFFSET,
        MENU_Y,
        MENU_WIDTH,
        MENU_HEIGHT
    )

    menu_hover = menu_base_rect.collidepoint(mouse_pos)
    menu_rect = menu_base_rect.inflate(8, 8) if menu_hover else menu_base_rect
    

    pygame.draw.rect(screen, BLACK, menu_rect, border_radius=12)

    border_width = 3 if menu_hover else 2

    pygame.draw.rect(
        screen,
        winner_color,
        menu_rect,
        width=border_width,
        border_radius=12
    )

    menu_text_rect = menu_text_surface.get_rect(center = menu_rect.center)
    screen.blit(menu_text_surface, menu_text_rect)
    
    pygame.display.update()
    return play_again_rect, menu_base_rect


# def game_over_click(pos):
#     play_again_rect = pygame.Rect(WIDTH // 2 - 150, 320, 300, 70)
#     menu_rect = pygame.Rect(WIDTH // 2 - 150, 420, 300, 70)

#     if play_again_rect.collidepoint(pos):
#         return "play again"
#     if menu_rect.collidepoint(pos):
#         return "menu"
    
#     return None
