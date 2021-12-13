import pygame
import pygame.time
from object import *


FPS = 60
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# Define your things up here
Ball = object(10, 10, (255, 255, 255), 0, 9.8)
print(Ball.math)

def main(): 
    clock = pygame.time.Clock()
    run = True

    while run: 
        clock.tick(FPS)
    pygame.quit()