import pygame
pygame.init()
display = pygame.display.set_mode((800, 600))
x, y = 30, 30
radius = 25
speed = 10
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x + radius + speed <= 800:
        x += speed
    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= 600:
        y += speed
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed

    display.fill((255, 255, 255))
    pygame.draw.circle(display, (0, 0, 0), (x, y), radius)
    pygame.display.flip()
    clock.tick(165)
pygame.quit()
