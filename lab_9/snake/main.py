import pygame, sys, random
import time

# Game settings
speed = 4
frame_size_x = 1380
frame_size_y = 840

# Initialize pygame and mixer for sounds
pygame.init()
pygame.mixer.init()

# Game window settings
pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Color settings
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# FPS settings
fps_controller = pygame.time.Clock()
square_size = 60

# Initialize game variables
def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction, food_weight, food_timer
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_body = [[120, 60]]
    food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                random.randrange(1, (frame_size_y // square_size)) * square_size]
    food_weight = random.randint(1, 5)  # Random weight between 1 and 5
    food_spawn = True
    score = 0
    food_timer = time.time()  # Timer for the food to disappear

init_vars()

# Function to show the score on the screen
def show_score(choice, color, font, size):
    global speed, score
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score) + " " + "Speed " + str(speed), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)

    game_window.blit(score_surface, score_rect)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord("w")) and direction != "DOWN":
                direction = "UP"
            elif (event.key == pygame.K_DOWN or event.key == ord("s")) and direction != "UP":
                direction = "DOWN"
            elif (event.key == pygame.K_LEFT or event.key == ord("a")) and direction != "RIGHT":
                direction = "LEFT"
            elif (event.key == pygame.K_RIGHT or event.key == ord("d")) and direction != "LEFT":
                direction = "RIGHT"

    # Move the head of the snake based on direction
    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size
    else:
        head_pos[0] += square_size

    # Handle screen wrapping
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    # Insert the new head position at the front of the snake
    snake_body.insert(0, list(head_pos))

    # Check if snake eats food
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += food_weight  # Increase score based on food weight
        speed += 1  # Increase speed with every food eaten
        food_spawn = False
    else:
        snake_body.pop()

    # If the food has been eaten or timed out, spawn a new food
    if not food_spawn or (time.time() - food_timer > 5):  # If food exists for more than 5 seconds, remove it
        food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                    random.randrange(1, (frame_size_y // square_size)) * square_size]
        food_weight = random.randint(1, 5)  # Assign random weight to new food
        food_spawn = True
        food_timer = time.time()  # Reset timer for new food

    # Fill the game window with black
    game_window.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(
            pos[0] + 2, pos[1] + 2,
            square_size - 2, square_size - 2))

    # Draw the food
    pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0],
                                                   food_pos[1], square_size, square_size))

    # Check if snake collides with itself
    for block in snake_body[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            init_vars()

    # Show the score and speed
    show_score(1, white, 'courier', 20)

    # Update the game display
    pygame.display.update()

    # Control the game speed using the frame rate controller
    fps_controller.tick(speed)
