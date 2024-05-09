import pygame
import random

# Initialize pygame
pygame.init()

# Set up some constants
CELL_SIZE = 20
WIDTH, HEIGHT = 640, 480
BOARD_WIDTH, BOARD_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE

# Define colors for the game elements
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

class Snake:
    # Initialize snake properties
    def __init__(self):
        self.length = 1
        self.positions = [0] * self.length
        self.positions[0] = (random.randint(0, BOARD_WIDTH), random.randint(0, BOARD_HEIGHT))

# Create the game board and initialize it with zeros
board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# Initialize the snake and food objects
snake = Snake()
food = (random.randint(0, BOARD_WIDTH - 1), random.randint(0, BOARD_HEIGHT - 1))

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
running = True

while running:
    for event in pygame.event_loop:
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    screen.fill((0, 0, 0))

    # Draw the board and snake
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[y][x] == 1:
                pygame.draw.rect(screen, SNAKE_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

# Quit the game when done
pygame.quit()
