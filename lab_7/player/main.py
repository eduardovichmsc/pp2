import pygame
import os

pygame.init()

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Аудио Плеер')

pygame.mixer.init()

ASSETS_PATH = r"C:\Users\Darzhan Eduardovich\Desktop\github\pp2\lab_7\player"
AUDIO_FOLDER = os.path.join(ASSETS_PATH, "music")
BUTTONS_FOLDER = os.path.join(ASSETS_PATH, "buttons")
audio_files = [
    os.path.join(AUDIO_FOLDER, "Boulevard Depo, SP4K - Нонграта.mp3"),
    os.path.join(AUDIO_FOLDER, "Men I Trust - Break for lovers.mp3")
]
current_track = 0

pygame.mixer.music.load(audio_files[current_track])


prev_button = pygame.image.load(os.path.join(BUTTONS_FOLDER, "prev.png"))
play_button = pygame.image.load(os.path.join(BUTTONS_FOLDER, "play.png"))
pause_button = pygame.image.load(os.path.join(BUTTONS_FOLDER, "pause.png"))
next_button = pygame.image.load(os.path.join(BUTTONS_FOLDER, "next.png"))

prev_button = pygame.transform.scale(prev_button, (60, 30))
play_button = pygame.transform.scale(play_button, (60, 30))
pause_button = pygame.transform.scale(pause_button, (60, 30))
next_button = pygame.transform.scale(next_button, (60, 30))

prev_button_pos = (50, 150)
play_button_pos = (120, 150)
pause_button_pos = (190, 150)
next_button_pos = (270, 150)

is_paused = False

while True:
    screen.fill((255, 255, 255))

    screen.blit(prev_button, prev_button_pos)
    screen.blit(play_button, play_button_pos)
    screen.blit(pause_button, pause_button_pos)
    screen.blit(next_button, next_button_pos)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if prev_button_pos[0] <= x <= prev_button_pos[0] + 60 and prev_button_pos[1] <= y <= prev_button_pos[1] + 30:
                current_track = (current_track - 1) % len(audio_files)
                pygame.mixer.music.load(audio_files[current_track])
                pygame.mixer.music.play()
            elif play_button_pos[0] <= x <= play_button_pos[0] + 60 and play_button_pos[1] <= y <= play_button_pos[1] + 30:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.play()
            elif pause_button_pos[0] <= x <= pause_button_pos[0] + 60 and pause_button_pos[1] <= y <= pause_button_pos[1] + 30:
                pygame.mixer.music.pause()
                is_paused = True
            elif next_button_pos[0] <= x <= next_button_pos[0] + 60 and next_button_pos[1] <= y <= next_button_pos[1] + 30:
                current_track = (current_track + 1) % len(audio_files)
                pygame.mixer.music.load(audio_files[current_track])
                pygame.mixer.music.play()

pygame.quit()
