import pygame
import sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((1360, 706))

circle_pos = (1360/2, 706/2)
circle_col = "blue"

screen_col = 'darkorange'

def circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()
    
    if math.sqrt((mouse_pos[0] - circle_pos[0])**2 + (mouse_pos[1] - circle_pos[1])**2) <50:
        return True
    return False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #left click
                if circle_collision():
                    screen_col = pygame.Color(random.randint(0, 255),(random.randint(0, 255)),(random.randint(0, 255)))
                    circle_pos = (random.randint(0, 1360), random.randint(0, 706))
                    circle_col = pygame.Color(random.randint(0, 255),(random.randint(0, 255)),(random.randint(0, 255)))
            
    screen.fill(screen_col)
    pygame.draw.circle(screen, circle_col, circle_pos, 50)
    
    pygame.display.update()
    