import pygame
import time
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("miki-rurk")
clock = pygame.time.Clock()

base_path = r"C:\Users\Darzhan Eduardovich\Desktop\pp2\Lab7\task1"
image_miki = pygame.image.load(os.path.join(base_path, "assets/clock.png"))
image_min = pygame.image.load(os.path.join(base_path, "assets/min.png"))
image_sec = pygame.image.load(os.path.join(base_path, "assets/sec.png"))

center_pos = (WIDTH // 2, HEIGHT // 2)
sec_angle = 60
min_angle = -49.5

def translateImageDegree(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=center)
    return rotated_image, rotated_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    rotated_sec, sec_rect = translateImageDegree(image_sec, sec_angle, center_pos)
    rotated_min, min_rect = translateImageDegree(image_min, min_angle, center_pos)

    display.fill((0, 0, 0))
    display.blit(image_miki, (0, 0))
    display.blit(rotated_sec, sec_rect.topleft)
    display.blit(rotated_min, min_rect.topleft)

    sec_angle -= 6
    min_angle -= 0.5

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
