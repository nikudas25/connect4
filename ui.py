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
        
        