# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def generate_starting_position():
    x_range = (pixel_width // 2, screen_width - pixel_width // 2 - 2, pixel_width)
    y_range = (pixel_width // 2, screen_height - pixel_width // 2 - 2, pixel_width)
    return [random.randrange(*x_range), random.randrange(*y_range)]

# playground
pixel_width = 50


# snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)


# target
target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])

# generate random starting position for target
target.center = generate_starting_position()

def update_snake_direction():
    global snake_direction
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_UP]:# and snake_direction != (0, pixel_width):
        snake_direction = (0, -pixel_width)
    if key_pressed[pygame.K_DOWN]:# and snake_direction != (0, -pixel_width):
        snake_direction = (0, pixel_width)
    if key_pressed[pygame.K_RIGHT]:# and snake_direction != (-pixel_width, 0):
        snake_direction = (pixel_width, 0)
    if key_pressed[pygame.K_LEFT]:# and snake_direction != (pixel_width, 0):
        snake_direction = (-pixel_width, 0)

def set_snake_boundaries():
    global snake_pixel
    if snake_pixel.left < 0:
        snake_pixel.left = pixel_width
    if snake_pixel.right > screen_width:
        snake_pixel.right = screen_width - pixel_width
    if snake_pixel.top < 0:
        snake_pixel.top = pixel_width
    if snake_pixel.bottom > screen_height:
        snake_pixel.bottom = screen_height - pixel_width



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE


    # identify the key being pressed to update the snake direction
    update_snake_direction()

    # Check if the snake hits the screen boundaries
    set_snake_boundaries()

    # move the snake
    snake_pixel.move_ip(snake_direction)

    for snake_part in snake:
        pygame.draw.rect(screen, "purple", snake_pixel)

    pygame.draw.rect(screen, "green", target)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
