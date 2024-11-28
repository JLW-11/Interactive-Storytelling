import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1900, 1200))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (229, 221, 116)
RED = (212, 34, 34)
GREEN = (59, 223, 26)

filename = "heaven.jpg"

def prepare_backround(file_name):
    backround_image = pygame.image.load(file_name)
    backround_image = pygame.transform.scale(backround_image, (screen_width, screen_height))
    screen.blit(backroundimage, (0, 0))

# Story state
scene = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                scene = 1
            elif event.key == pygame.K_2:
                scene = 2
            elif event.key == pygame.K_3:
                scene = 3 
            elif event.key == pygame.K_4:
                scene = 4

    # Fill the screen with white
    screen.fill(WHITE)

    # Render text based on the scene
    if scene == 1:
        text = font.render("You are in Heaven. Press 2 to go to Hell.", True, YELLOW)
    elif scene == 2:
        text = font.render("You are now in Hell. Press 1 to go back to Heaven.", True, RED)
    elif scene == 3: 
        text = font.render("You are now underground in a cave.", True, BLACK)
    elif scene == 4:
        text = font.render("you are now on a floating island", True, GREEN)


    screen.blit(text, (100, 250))

    # Update the display
    pygame.display.flip()

pygame.quit()