# 1. import packages
import pygame
from pygame.locals import *
import sys  #used for quitting our program
from pathlib import Path
import random

# 2. Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent

BALL_WIDTH_HEIGHT = 20
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

PLATFORM_WIDTH = 60
PLATFORM_HEIGHT = 20
PLATFORM_MAX_WIDTH = WINDOW_WIDTH - PLATFORM_WIDTH
PLATFORM_MAX_HEIGHT = WINDOW_HEIGHT - PLATFORM_HEIGHT
N_PIXELS_TO_MOVE = 5

# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # creating the window
clock = pygame.time.Clock()

# 4. Load assets: image(s), sound(s), etc.
ball_image = pygame.image.load('Images/64-Breakout-Tiles.png')
platform_image = pygame.image.load('Images/49-Breakout-Tiles.png').convert_alpha()
platform_image = pygame.transform.scale(platform_image, (60, 20))

# 5. Initialize variables
ball_x = 360
ball_y = BALL_WIDTH_HEIGHT
ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

platform_x = 320
platform_y = 460
platform_rect = pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

collision = False
# 6. Endless loop

while True:

    # 7. Check for and handle events
    for event in pygame.event.get():

        # If the CLOSE button was clicked quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # See if user pressed a key
    key_pressed_tuple = pygame.key.get_pressed()

    if key_pressed_tuple[pygame.K_LEFT]:
        platform_x -= N_PIXELS_TO_MOVE
    if key_pressed_tuple[pygame.K_RIGHT]:
        platform_x += N_PIXELS_TO_MOVE

    # 8. Do any "per frame" actions
    platform_rect = pygame.Rect(platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

    # Check if the ball is colliding with the platform
    if ball_rect.colliderect(platform_rect):
        collision = True
    elif ball_y == 0:
        collision = False

    if collision:
        ball_y -= N_PIXELS_TO_MOVE
    else:
        ball_y += N_PIXELS_TO_MOVE
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    # draw ball at position 100 across (x) and 200 down(y)
    window.blit(ball_image, (ball_x, ball_y))
    window.blit(platform_image, (platform_x, platform_y))

    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
