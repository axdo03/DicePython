import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller 🎲")

# Fonts
font = pygame.font.SysFont(None, 60)
small_font = pygame.font.SysFont(None, 30)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)

# Button setup
button_rect = pygame.Rect(WIDTH//2 - 60, HEIGHT//2 + 40, 120, 40)

# Dice state
dice1 = 1
dice2 = 1
total = 2

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Roll dice
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                total = dice1 + dice2

    # Draw dice results
    dice_text = font.render(f"{dice1} + {dice2} = {total}", True, BLACK)
    screen.blit(dice_text, (WIDTH//2 - dice_text.get_width()//2, HEIGHT//2 - 40))

    # Draw button
    pygame.draw.rect(screen, BLUE, button_rect)
    button_text = small_font.render("Roll Dice", True, WHITE)
    screen.blit(button_text, (button_rect.x + 15, button_rect.y + 8))

    pygame.display.flip()
