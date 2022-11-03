import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255,255,255), (0,0,400,400))

circle(screen, (255, 255, 0), (200,200), 100, 0)
circle(screen, (0,0,0), (200,200), 100, 3)

circle(screen, (255,0,0), (240,170), 15, 0)
circle(screen, (0,0,0), (240,170), 15, 1)
circle(screen, (0,0,0), (240,170), 7, 0)

circle(screen, (255,0,0), (160,170), 12, 0)
circle(screen, (0,0,0), (160,170), 12, 1)
circle(screen, (0,0,0), (160,170), 5, 0)

rect(screen, (0,0,0), (140, 240, 120, 20))

line(screen, (0,0,0), (120,165), (190, 145), 10)

line(screen, (0,0,0), (220,142), (270,162), 12)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()