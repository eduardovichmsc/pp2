import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'black': (0, 0, 0)}

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

tool = 'brush'  # Default tool
color = COLORS['blue']
radius = 15
start_pos = None
drawing = False

drawings = []  # Store shapes

# UI Buttons
buttons = {
    'brush': pygame.Rect(10, 10, 80, 30),
    'eraser': pygame.Rect(100, 10, 80, 30),
    'rectangle': pygame.Rect(190, 10, 100, 30),
    'circle': pygame.Rect(300, 10, 80, 30),
    'red': pygame.Rect(390, 10, 50, 30),
    'green': pygame.Rect(450, 10, 50, 30),
    'blue': pygame.Rect(510, 10, 50, 30)
}

def draw_ui():
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, 50))  # Background for UI
    pygame.draw.line(screen, BLACK, (0, 50), (SCREEN_WIDTH, 50), 2)  # Line separator
    
    for btn, rect in buttons.items():
        pygame.draw.rect(screen, COLORS.get(btn, BLACK), rect, 2)
        text = pygame.font.SysFont(None, 24).render(btn.capitalize(), True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 5))

def main():
    global tool, color, radius, start_pos, drawing
    screen.fill(WHITE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click
                    for btn, rect in buttons.items():
                        if rect.collidepoint(event.pos):
                            if btn in COLORS:
                                color = COLORS[btn]
                            else:
                                tool = btn
                    start_pos = event.pos
                    drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and start_pos:
                    end_pos = event.pos
                    if tool == 'rectangle':
                        drawings.append(('rectangle', start_pos, end_pos, color))
                    elif tool == 'circle':
                        radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                        drawings.append(('circle', start_pos, radius, color))
                    drawing = False
                    start_pos = None
            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == 'brush':
                    pygame.draw.circle(screen, color, event.pos, radius)
                    drawings.append(('brush', event.pos, radius, color))
                elif tool == 'eraser':
                    pygame.draw.circle(screen, WHITE, event.pos, radius)
                    drawings.append(('eraser', event.pos, radius, WHITE))
        
        screen.fill(WHITE)
        draw_ui()
        
        for shape in drawings:
            if shape[0] == 'brush' or shape[0] == 'eraser':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'rectangle':
                pygame.draw.rect(screen, shape[3], (*shape[1], shape[2][0] - shape[1][0], shape[2][1] - shape[1][1]), 2)
            elif shape[0] == 'circle':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2], 2)
        
        pygame.display.flip()
        clock.tick(60)

main()