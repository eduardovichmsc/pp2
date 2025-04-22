import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# Define colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions and speeds
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ENEMY_SPEED = 7
GG_SPEED = 7
SCORE = 0

COIN_SIZE = (64, 64)
COINS_COLLECTED = 0

# Load fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load images
BG_IMG = pygame.image.load("assets/AnimatedStreet.png")

# Create game window
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display.fill(WHITE)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-GG_SPEED, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(GG_SPEED, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Coin.png")
        self.image = pygame.transform.scale(self.image, COIN_SIZE) 
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 200))

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(40, SCREEN_HEIGHT - 200))

# Instantiate game objects
P1 = Player()
E1 = Enemy()
coin = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
coins = pygame.sprite.Group()
coins.add(coin)

# Increase speed event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            ENEMY_SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    display.blit(BG_IMG, (0, 0))
    
    # Display scores
    score_text = font_small.render(str(SCORE), True, BLACK)
    display.blit(score_text, (10, 10))
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    display.blit(coins_text, (300, 10))

    # Update and redraw all sprites
    for entity in all_sprites:
        display.blit(entity.image, entity.rect)
        entity.move()

    # Draw the coin
    display.blit(coin.image, coin.rect)

    # Collision detection between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        display.fill(RED)
        display.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision detection between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        coin.reset_position()

    pygame.display.update()
    pygame.time.Clock().tick(165)
