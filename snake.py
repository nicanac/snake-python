import pygame
import random

# Set the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the initial position and size of the snake
snake_pos = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
snake_body = [[SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2], [SCREEN_WIDTH / 2 - 10, SCREEN_HEIGHT / 2], [SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2]]

# Set the initial position of the food
food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
food_spawn = True

# Set the initial direction of the snake
direction = 'RIGHT'
changeto = direction

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption('Snake Game')

# Create a font for displaying the score
font = pygame.font.SysFont('times new roman', 30)

# Set the initial score
score = 0

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        # Check if the user has closed the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check if a key has been pressed
        if event.type == pygame.KEYDOWN:
            # Check if the left or right arrow key has been pressed
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'

    # Check if the direction of the snake needs to be changed
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    # Move the snake in the chosen direction
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'UP':
        snake_pos[1] -=10
    if direction == 'DOWN':
        snake_pos[1] += 10

    # Add the new position of the snake to the snake body
    snake_body.insert(0, list(snake_pos))

    # Check if the snake has eaten the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn a new food if the old one has been eaten
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
    food_spawn = True

    # Draw the background
    screen.fill((0, 0, 0))

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw the score
    score_text = font.render('Score: {}'.format(score), True, (255, 255, 255))
    screen.blit(score_text, (15, 15))

    # Update the screen
    pygame.display.update()

    # Check if the snake has collided with the edge of the screen
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - 10:
        game_over()

    # Check if the snake has collided with itself
    for body in snake_body[1:]:
        if snake_pos[0] == body[0] and snake_pos[1] == body[1]:
            game_over()
