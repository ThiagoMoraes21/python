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

def update_snake_direction():
    global snake_direction
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_UP]:
        snake_direction = (0, -pixel_width)
    if key_pressed[pygame.K_DOWN]:
        snake_direction = (0, pixel_width)
    if key_pressed[pygame.K_RIGHT]:
        snake_direction = (pixel_width, 0)
    if key_pressed[pygame.K_LEFT]:
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

def move_snake():
    global snake, snake_pixel
    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]

def snake_eat():
    global target, snake_length, snake
    if snake_pixel.colliderect(target):
        target.center = generate_starting_position()
        snake_length += 1

def is_out_of_bounds():
    return (snake_pixel.bottom > screen_height) or \
            (snake_pixel.top < 0) or \
            (snake_pixel.right > screen_width) or \
            (snake_pixel.left < 0)

def game_over():
    global snake_length, target, snake_pixel, snake
    snake_length = 1 
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    snake = [snake_pixel.copy()]

# playground
pixel_width = 50

# snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

# target
target = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
target.center = generate_starting_position()



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # reset game if snake goes out of boundaries
    if is_out_of_bounds():
        game_over()

    # increase snake body and generate a random start point for the target
    snake_eat()

    # identify the key being pressed to update the snake direction
    update_snake_direction()

    # Check if the snake hits the screen boundaries
    set_snake_boundaries()

    # move the snake
    move_snake()

    for snake_part in snake:
        pygame.draw.rect(screen, "purple", snake_part)

    pygame.draw.rect(screen, "green", target)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(10)  # limits FPS to 60

pygame.quit()
