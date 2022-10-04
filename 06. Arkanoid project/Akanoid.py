# 1. import packages
import pygame
from pygame.locals import *
import sys  #used for quitting our program
from pathlib import Path


# 2. Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BASE_PATH = Path(__file__).resolve().parent


# 3. Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # creating the window
clock = pygame.time.Clock()

# 4. Load assets: image(s), sound(s), etc.
ball_image = pygame.image.load('Images/64-Breakout-Tiles.png')

# 5. Initialize variables

# 6. Endless loop

while True:

    # 7. Check for and handle events
    for event in pygame.event.get():

        # If the CLOSE button was clicked quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8. Do any "per frame" actions

    # 9. Clear the window
    window.fill(BLACK)

    # 10. Draw all window elements
    # draw ball at position 100 across (x) and 200 down(y)
    window.blit(ball_image, (320, 440))
    # 11. Update the window
    pygame.display.update()

    # 12. Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
