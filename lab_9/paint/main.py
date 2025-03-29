import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'black': (0, 0, 0)}

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

tool = 'brush'  # Default tool is 'brush'
color = COLORS['blue']  # Default color is blue
radius = 15  # Default radius for brush
start_pos = None
drawing = False

drawings = []  # List to store all drawn shapes

# UI Buttons (for different tools and colors)
buttons = {
    'brush': pygame.Rect(10, 10, 80, 30),
    'eraser': pygame.Rect(100, 10, 80, 30),
    'rectangle': pygame.Rect(190, 10, 100, 30),
    'circle': pygame.Rect(300, 10, 80, 30),
    'square': pygame.Rect(390, 10, 80, 30),  # New button for square
    'triangle': pygame.Rect(480, 10, 80, 30),  # New button for right triangle
    'equilateral_triangle': pygame.Rect(570, 10, 120, 30),  # New button for equilateral triangle
    'rhombus': pygame.Rect(700, 10, 80, 30),  # New button for rhombus
    'red': pygame.Rect(790, 10, 50, 30),
    'green': pygame.Rect(850, 10, 50, 30),
    'blue': pygame.Rect(910, 10, 50, 30)
}

def draw_ui():
    """
    Draws the user interface at the top of the screen, including tool buttons and color selectors.
    """
    pygame.draw.rect(screen, WHITE, (0, 0, SCREEN_WIDTH, 50))  # Background for UI
    pygame.draw.line(screen, BLACK, (0, 50), (SCREEN_WIDTH, 50), 2)  # Line separator
    
    # Draw all the buttons
    for btn, rect in buttons.items():
        pygame.draw.rect(screen, COLORS.get(btn, BLACK), rect, 2)
        text = pygame.font.SysFont(None, 24).render(btn.replace('_', ' ').capitalize(), True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 5))

def main():
    """
    Main game loop: Handles events, drawing, and user interactions.
    """
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
                            if btn in COLORS:  # Color change
                                color = COLORS[btn]
                            else:  # Tool change
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
                    elif tool == 'square':  # Draw square
                        side_length = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                        drawings.append(('square', start_pos, side_length, color))
                    elif tool == 'triangle':  # Draw right triangle
                        drawings.append(('triangle', start_pos, end_pos, color))
                    elif tool == 'equilateral_triangle':  # Draw equilateral triangle
                        length = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                        drawings.append(('equilateral_triangle', start_pos, length, color))
                    elif tool == 'rhombus':  # Draw rhombus
                        drawings.append(('rhombus', start_pos, end_pos, color))
                    drawing = False
                    start_pos = None
            if event.type == pygame.MOUSEMOTION and drawing:
                if tool == 'brush':
                    pygame.draw.circle(screen, color, event.pos, radius)
                    drawings.append(('brush', event.pos, radius, color))
                elif tool == 'eraser':
                    pygame.draw.circle(screen, WHITE, event.pos, radius)
                    drawings.append(('eraser', event.pos, radius, WHITE))
        
        screen.fill(WHITE)  # Clear the screen
        draw_ui()  # Draw the user interface
        
        # Redraw all shapes from the `drawings` list
        for shape in drawings:
            if shape[0] == 'brush' or shape[0] == 'eraser':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'rectangle':
                pygame.draw.rect(screen, shape[3], (*shape[1], shape[2][0] - shape[1][0], shape[2][1] - shape[1][1]), 2)
            elif shape[0] == 'circle':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2], 2)
            elif shape[0] == 'square':  # Drawing square
                pygame.draw.rect(screen, shape[3], (*shape[1], shape[2], shape[2]), 2)
            elif shape[0] == 'triangle':  # Drawing right triangle
                pygame.draw.polygon(screen, shape[3], [shape[1], (shape[1][0], shape[2][1]), shape[2]])
            elif shape[0] == 'equilateral_triangle':  # Drawing equilateral triangle
                height = int(shape[2] * (3 ** 0.5) / 2)
                points = [shape[1], (shape[1][0] - shape[2] // 2, shape[1][1] + height), 
                          (shape[1][0] + shape[2] // 2, shape[1][1] + height)]
                pygame.draw.polygon(screen, shape[3], points, 2)
            elif shape[0] == 'rhombus':  # Drawing rhombus
                p1 = shape[1]
                p3 = shape[2]
                
                # Midpoint between p1 and p3 (center of the rhombus)
                mid_x = (p1[0] + p3[0]) // 2
                mid_y = (p1[1] + p3[1]) // 2
                
                # Calculate the length of the diagonals
                d1 = abs(p1[0] - p3[0])
                d2 = abs(p1[1] - p3[1])
                
                # Calculate the two other points (p2 and p4)
                p2 = (mid_x - d2 // 2, mid_y - d1 // 2)  # First diagonal point
                p4 = (mid_x + d2 // 2, mid_y + d1 // 2)  # Second diagonal point
                
                # Draw the rhombus using the 4 points
                pygame.draw.polygon(screen, shape[3], [p1, p2, p3, p4], 2)
        
        pygame.display.flip()  # Update the screen
        clock.tick(60)  # Set the frame rate

main()
