# Initialize Pygame
import pygame

pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 400

# Set colors
red = (255, 0, 0)
blue = (0, 0, 255)

# Set initial color sizes
red_size = screen_width // 2
blue_size = screen_width // 2

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color Pusher")

# Load images
albania_img = pygame.image.load('albania.png')
serbia_img = pygame.image.load('serbia.png')

# Scale down images
flag_width = red_size
albania_img = pygame.transform.scale(albania_img, (flag_width, flag_width))
serbia_img = pygame.transform.scale(serbia_img, (flag_width, flag_width))

# Game loop
running = True
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Determine which color to grow and which color to shrink based on click position
            if pygame.mouse.get_pos()[0] < screen_width // 2:
                red_size -= 10
                if red_size < 0:
                    red_size = 0
                blue_size += 10
            else:
                blue_size -= 10
                if blue_size < 0:
                    blue_size = 0
                red_size += 10

    # Check if one color has completely overlapped the other
    if red_size >= screen_width and blue_size < screen_width:
        print("Red wins!")
        running = False
    elif blue_size >= screen_width and red_size < screen_width:
        print("Blue wins!")
        running = False

    # Draw colors
    blue_rect = pygame.Rect(0, 0, blue_size, screen_height)
    red_rect = pygame.Rect(screen_width - red_size, 0, red_size, screen_height)
    pygame.draw.rect(screen, blue, blue_rect)
    pygame.draw.rect(screen, red, red_rect)

    # Blit images on top of colors
    screen.blit(albania_img, (screen_width - red_size, 0))
    screen.blit(serbia_img, (blue_size - flag_width, 0))

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
