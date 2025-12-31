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

    start_y = SQUARE_SIZE // 2
    end_y = (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2

    for y in range(start_y, end_y, 20):
        draw_board(screen, board)

        pygame.draw.circle(
            screen,
            color,
            (col * SQUARE_SIZE + SQUARE_SIZE // 2, y),
            RADIUS
        )

        pygame.display.update()
        pygame.time.delay(20)
        
        
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
